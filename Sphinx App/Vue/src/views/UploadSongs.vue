<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4 card form-card">
        <div class="card-title text-center">
          <h3 style="font-size: 2rem; color: #fff;">Upload Song</h3>
        </div>
        <form class="card-body" @submit.prevent="submitForm" enctype="multipart/form-data">
          <div class="form-group" style="color: white;">
            <label for="song_title">Song Title</label>
            <input v-model="songTitle" type="text" name="song_title" class="form-control" placeholder="Song title" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="album_title">Album Title</label>
            <input v-model="albumTitle" type="text" name="album_title" class="form-control" placeholder="Album title" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="music_producer">Music Producer</label>
            <input v-model="musicProducer" type="text" name="music_producer" class="form-control" placeholder="Music Producer name" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="singer">Singer</label>
            <input v-model="singer" type="text" name="singer" class="form-control" placeholder="Singer name" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="lyricist">Lyricist</label>
            <input v-model="lyricist" type="text" name="lyricist" class="form-control" placeholder="Lyricist name" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="date">Release Date</label>
            <input v-model="releaseDate" type="date" name="date" class="form-control" placeholder="Date of Release" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="lyrics">Lyrics</label>
            <textarea v-model="lyrics" name="lyrics" style="width: 100%; border-radius: 1rem; color: black" id="" cols="20"
              rows="10"></textarea>
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group" style="color: white;">
            <label for="audiofile">Upload File</label>
            <input type="file" @change="handleFileUpload" accept=".mp3" required />
          </div>
          <div style="height: 15px;"></div>
          <div class="text-center">
            <button type="submit" class="btn btn-light text-black login-frm-btn">Upload</button>
          </div>
        </form>
      </div>
      <div class="col-md-4"></div>
    </div>
  </div>
  <div style="height: 25px;"></div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      songTitle: '',
      albumTitle: '',
      musicProducer: '',
      singer: '',
      lyricist: '',
      releaseDate: '',
      lyrics: '',
      audiofile: null
    };
  },
  methods: {
async submitForm() {
  try {
    const formData = new FormData();
    formData.append('song_title', this.songTitle);
    formData.append('album_title', this.albumTitle);
    formData.append('music_producer', this.musicProducer);
    formData.append('singer', this.singer);
    formData.append('lyricist', this.lyricist);
    formData.append('date', this.releaseDate);
    formData.append('lyrics', this.lyrics);
    formData.append('audiofile', this.audiofile);

    // Log FormData to check if it's correctly populated
    for (let pair of formData.entries()) {
      console.log(pair[0] + ', ' + pair[1]);
    }
    
    // Your Axios request remains unchanged
    await axios.post('http://127.0.0.1:5000/uploadsongs', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });

    this.$router.push('/userdashboard');
    // Handle successful submission (e.g., redirect to another page)
  } catch (error) {
    console.error('Error uploading song:', error);
    this.error = 'Error uploading song. Please try again.';
  }
},

    handleFileUpload(event) {
      this.audiofile = event.target.files[0];
    }
  }
};
</script>

<style scoped>
** {
  margin: 0;
  padding: 0;
}

body {
  background-image: url(./pxfuel.jpg);
  color: #fff;
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  font-family: Helvetica, sans-serif;
}

.form-card {
  border-radius: 20px;
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  backdrop-filter: blur(50px);
  padding: 3rem 2rem 3rem 2rem;
  margin-top: 4rem;
}

.login-frm-btn {
  padding: 1rem 10rem 1rem 10rem;
  margin-top: 3rem;
  font-weight: 700;
}

.text-black {
  color: #000 !important;
}
</style>

