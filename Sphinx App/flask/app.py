from flask import Flask, render_template, request, redirect, url_for, flash, session,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os
from flask import json
from flask import jsonify, make_response
from flask_cors import CORS


app = Flask(__name__,static_url_path='/static/styles.css')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SECRET_KEY'] = '22f1001433'
app.config['UPLOAD_FOLDER'] = 'uploads'
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __rep__(self):
        return f"username : (self.username)"
   
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(100), nullable=False)
    album_title = db.Column(db.String(100), nullable=False)
    music_producer = db.Column(db.String(20))
    singer = db.Column(db.String(20))
    lyricist = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    lyrics = db.Column(db.String(500))
    audiofile = db.Column(db.String(255))

    def __rep__(self):
        return f"title : (self.song_title)"

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists', lazy=True)

playlist_songs = db.Table('playlist_songs',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id'), primary_key=True),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True)
)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/registration', methods=['GET'])
def user_register():
    return render_template('registration.html')

@app.route('/registration', methods=["POST"])
def registration():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username is already taken. Please choose another.", "status" : 400})

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully.","status": 201})

@app.route('/userlogin', methods=['GET'])
def ulogin():
    return render_template('userlogin.html')

@app.route('/userlogin', methods=['POST'])
def user_login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = User.query.filter_by(username=username).first()
   
    if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return jsonify({"status": 200, "msg": 'okay'});

    else:
         return jsonify({"status": 501, "msg": 'No user found'});

@app.route('/userdashboard', methods=['GET', 'POST'])
def user_dashboard():
    songs = Song.query.all()
    playlists = Playlist.query.all()

    if request.method == 'POST':
        search_query = request.json.get('search_button', "").lower()
        search_query_playlist = request.json.get('search_playlist_button', "").lower()

        if search_query:
            songs = [song for song in songs if search_query.lower() in song.song_title.lower()]
        if search_query_playlist:
            playlists = [playlist for playlist in playlists if search_query_playlist.lower() in playlist.title.lower()]

    response_data = {
        'songs': [{'id': song.id, 'title': song.song_title} for song in songs],
        'playlists': [{'id': playlist.id, 'title': playlist.title} for playlist in playlists]
    }
    return jsonify(response_data)
    
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'adminkey'

@app.route('/adminlogin', methods=['GET'])
def alogin():
    return render_template('adminlogin.html')

@app.route('/adminlogin', methods=['POST'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print('admin login success')
        return redirect(url_for('admin_dashboard'))
    else:
        flash('Invalid admin credentials. Please try again.', 'danger')
    return render_template('adminlogin.html')


@app.route('/admindashboard', methods=['GET','POST'])
def admin_dashboard():
    songs = Song.query.all()
    user_count = User.query.count()
    song_count = Song.query.count()
    playlist_count = Playlist.query.count()
    print(playlist_count)
    unique_albums = set(song.album_title for song in songs)
    unique_creators = set(song.music_producer for song in songs)
    unique_singers = set(song.singer for song in songs)
    unique_lyricists = set(song.lyricist for song in songs)
    album_count = len(unique_albums)
    creator_count = len(unique_creators)
    singer_count = len(unique_singers)
    lyricist_count = len(unique_lyricists)
    if request.method == 'POST':
            search_query = request.form.get('search_button')
            songs = [song for song in songs if search_query.lower() in song.song_title.lower()]  

    response_data = {
                   "user_count": user_count,
                    "song_count": song_count,
                    "album_count": album_count,
                    "creator_count": creator_count,
                    'songs': [{'id': song.id, 'title': song.song_title} for song in songs],
                      "singer_count": singer_count,
                      "lyricist_count": lyricist_count,
                      "playlist_count": playlist_count
                    }
    return jsonify(response_data)
    # return render_template('admindashboard.html',user_count=user_count,song_count=song_count,album_count=album_count,creator_count=creator_count,songs=songs,singer_count=singer_count,lyricist_count=lyricist_count,playlist_count=playlist_count)


@app.route('/creatordashboard', methods=['GET', 'POST'])
def creator_dashboard():
    songs = Song.query.all()
    song_count = len(songs)
    unique_albums = set(song.album_title for song in songs)
    album_count = len(unique_albums)

    if request.method == 'POST':
        search_query = request.json.get('search_button', "").lower()
        if search_query:
            songs = [song for song in songs if search_query.lower() in song.song_title.lower()]

    response_data = {
        'song_count': song_count,
        'album_count': album_count,
        'songs': [{'id': song.id, 'title': song.song_title} for song in songs],
    }
    return jsonify(response_data)  
    # return render_template('creatordashboard.html',song_count=song_count,album_count = album_count, songs=songs)

@app.route('/song', methods=['GET'])
def song():
    songs = Song.query.all()
    song = Song.query.first()
    song_id = request.args.get('song_id', None)
    if song_id:
        songid = Song.query.get(song_id)
    selected_song = next((song for song in songs if str(song.id) == str(song_id)), None)
    song_title = song.song_title if song else ""
    album_title = song.album_title if song else ""
    music_producer = song.music_producer if song else ""
    singer = song.singer if song else ""
    lyricist = song.lyricist if song else ""
    lyrics = song.lyrics if song else ""
    date = song.date if song else ""
    response_data= {
        'song': [
                    {'id': song.id, 
                    'title': song.song_title, 
                    'album_title': song.album_title, 
                    "music_producer": song.music_producer, 
                    "singer": song.singer, 
                    "lyrics": song.lyrics, 
                    "lyricist": song.lyricist, 
                    "date": song.date,
                    "path": song.audiofile
                    } 
                    for song in songs]
        }
    return jsonify(response_data)
    # return render_template('song.html',songs=songs,selected_song=selected_song,songid=songid,song_title=song_title,album_title=album_title,music_producer=music_producer,singer=singer,lyricist=lyricist,lyrics=lyrics,date=date)

@app.route('/song/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404

    db.session.delete(song)
    db.session.commit()

    return jsonify({'message': 'Song deleted successfully'}), 200

@app.route('/uploadsongs', methods=['GET'])
def usongs():
    return render_template('userdashboard.html')

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}

@app.route('/uploadsongs', methods=['POST'])
def upload_songs():
    song_title = request.form.get('song_title')
    album_title = request.form.get('album_title')
    music_producer = request.form.get('music_producer')
    singer = request.form.get('singer')
    lyricist = request.form.get('lyricist')
    date = request.form.get('date')
    lyrics = request.form.get('lyrics')
    audiofile = request.files.get('audiofile')

    if not all([song_title, album_title, music_producer, singer, lyricist, date, lyrics, audiofile]):
        return jsonify({'error': 'Please provide all required fields.'}), 400

    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD.'}), 400

    if audiofile and '.' in audiofile.filename and audiofile.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        filename = audiofile.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_paths = f'static/{file_path}'
        audiofile.save(file_paths)

        new_song = Song(
            song_title=song_title,
            album_title=album_title,
            music_producer=music_producer,
            singer=singer,
            lyricist=lyricist,
            date=date_obj,
            lyrics=lyrics,
            audiofile=file_paths
        )
        db.session.add(new_song)
        db.session.commit()

        return jsonify({'message': 'Song uploaded successfully.', 'file_path': file_paths}), 201
    else:
        return jsonify({'error': 'Unsupported audio file format.'}), 415
    return jsonify({'error': 'Failed to upload song.'}), 500

@app.route('/static/uploads/<filename>')
def serve_song(filename):
    return send_from_directory('static/uploads', filename)

@app.route('/newplaylist', methods=['GET'])
def get_new_playlist():
    songs = Song.query.all()
    return render_template('newplaylist.html', songs=songs)

@app.route('/newplaylist', methods=['POST'])
def create_new_playlist():
    playlist_title = request.json.get('playlist_title')
    song_ids = request.json.get('song_ids')

    if not playlist_title or not song_ids:
        return jsonify({'message': 'Missing required fields: playlist_title and song_ids'}), 400

    try:
        song_ids = [int(id) for id in song_ids.split(',')]
    except ValueError:
        return jsonify({'message': 'Invalid song ID format: Must be comma-separated integers'}), 400

    existing_songs = Song.query.filter(Song.id.in_(song_ids)).all()
    if len(existing_songs) != len(song_ids):
        return jsonify({'message': 'Some song IDs may not exist'}), 400

    new_playlist = Playlist(title=playlist_title)
    new_playlist.songs.extend(existing_songs)

    db.session.add(new_playlist)
    db.session.commit()

    return jsonify({'message': 'Playlist created successfully'})


@app.route('/playlist/<int:playlist_id>', methods=['GET'])
def playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return render_template('error.html', error_message='Playlist not found')
    response_data = {
        'playlist': {
            'id': playlist.id,
            'title': playlist.title
        },
        'songs': [{'id': song.id, 'title': song.song_title} for song in playlist.songs]
    }
    return jsonify(response_data)

@app.route('/playlist/<int:playlist_id>/songs', methods=['GET'])
def playlist_songs(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify([]), 404
    return jsonify([
        {'id': song.id, 'title': song.title} for song in playlist.songs
    ])
    # return render_template('playlist.html',playlist=playlist)

@app.route('/playlist/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404
    
    db.session.delete(playlist)
    db.session.commit()
    
    return jsonify({'message': 'Playlist deleted successfully'}), 200

def remove_song_from_playlist(playlist_id, song_id):
    s = playlist_songs.query.filter_by(playlistId=playlist_id,songId=song_id).first()
    if not s:
        return jsonify({"error": "song does not exist in the playlist"}), 404

    s.playlist_songs.remove(song)
    db.session.commit()
    
    return jsonify({"message":f"The {song.title} has been removed from the playlist."})

@app.route('/kickstart', methods=['GET'])
def kickstart():
    return render_template('kickstart.html')

@app.route('/alltracks', methods=['GET','POST'])
def all_tracks():
    songs = Song.query.all()
    albums = {}
    album_title = set([song.album_title for song in songs])
    if request.method == 'POST':
        search_query = request.json.get('search_button', "").lower()
        songs = [song for song in songs if search_query in song.song_title.lower() or search_query in song.album_title.lower()]

        for album_title in album_title:
            albums[album_title] = [song for song in songs if song.album_title == album_title]
    response_data = {
        'songs': [{'id': song.id, 'title': song.song_title, 'album_title': song.album_title} for song in songs]
    }
    return jsonify(response_data)  
    # return render_template('alltracks.html',songs=songs,albums = albums, album_title=album_title)


import requests
import schedule

def trigger_google_chat_notification(text, webhook_url):
    payload = {'text': text}
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(webhook_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print('Notification sent successfully!')
    else:
        print('Failed to send notification.')

webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAFUOmPGc/messages?key=YOUR_API_KEY&token=YOUR_TOKEN'
text = 'Hi there! This is a test message from the SPHINX music app to notify that a new track has been added.'
def job():
    schedule.every().day.at("18:00").do(job)
trigger_google_chat_notification(text, webhook_url)


if __name__ == '__main__':
    app.debug=False
    app.run()