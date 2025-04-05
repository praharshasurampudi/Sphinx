<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4 card form-card text-center" id="playliscard" style="padding: 1rem;">
        <div class="card-title text-center" style="margin: 2rem 2rem">
          <h3 style="font-size: 2rem; color: #fff;">{{ playlist.title }}</h3>
        </div>
      </div>
      <div class="col-md-4"></div>
    </div>
    <br />
    <div class="row">
      <div class="col-md-3"></div>
      <div class="col-md-6">
        <div class="row">
          <div class="col-md-12 card dashboard_card_inner2" v-for="(song, index) in songs" :key="index">
            <div class="card-body">
              <div class="row">
                {{ playlist.id }}
                <div class="col-md-12">
                  <div class="row" style="padding-bottom:-5px;">
                    <h5 class="col-md-6"style="color: white;">{{ song.title }}</h5>
                    <div class="col-md-6 d-flex justify-content-end">
                      <p>
                        <button class="text-right text-black btn btn-light" @click="$router.push('/song/' + song.id)">Play Song</button>
                      </p>
                      <div style="width: 15px;"></div>
                      <!-- <p>
                        <button class="text-right text-black btn btn-danger btn btn-danger"
                           @click="deleteSong(playlist.id,song.id)">Remove Song</button>
                      </p> -->
                    </div>
                  </div>
                </div>
              </div>   
            </div>
          </div>
        </div>
        <div class="col-md-3"></div>
      </div>
    </div>
  </div>
  <div style="height: 25px;"></div>
  <button class="text-center mx-auto d-block text-black btn btn-danger" @click="deletePlaylist(playlist.id)">Delete Playlist</button>
  <div style="height: 50px;"></div>
</template>

<script>
import axios from "axios";
import { SERVER_URL } from "../consts";
export default {
  data() {
    return {
      songs: [],
      playlist: {
        title: '',
        songs: []
      },
      url: 'http://localhost:5000',
      serverUrl: SERVER_URL,
      playlistId: this.$router.currentRoute.value.params.id,
    };
  },
  mounted() {
    const playlistId = this.$router.currentRoute.value.params.id;
      axios.get(`http://localhost:5000/playlist/${playlistId}`).then((result) => {
        this.playlist = result.data.playlist;
        this.songs = result.data.songs;
        console.log(result.data.playlist);
      });
    axios.get(`http://127.0.0.1:5000/song?song_id=${playlistId}`).then((response) => {
      this.songs1 = response.data.song;
      console.log(response.data.song);
    });
  },
  methods: {
    deletePlaylist(playlistId) {
      axios.delete(`http://127.0.0.1:5000/playlist/${playlistId}`)
        .then(response => {
          // Remove the deleted playlist from the playlists array
          this.playlists = this.playlists.filter(playlist => playlist.id !== playlistId);
          this.$router.push({path:'/userdashboard', replace: true});
        })
        .catch(error => {
          // Handle error, show error message or perform any other necessary actions
          console.error('Error deleting playlist:', error);
        });
    },
    deleteSong(playlistId,songId) {
        axios.delete(`http://127.0.0.1:5000/removesong?playlist_id=${playlistId}/${songId}`)
          .then(res => {
            // Remove the deleted playlist from the playlists array
            this.song = this.playlist_songs.filter(song => song.song_id !== songId && song.playlist_id === playlistId);
            })
          .catch(error => {
            // Handle error, show error message or perform any other necessary actions
            console.error('Error deleting playlist:', error);
          });

      }
  }
}

</script>


<style scoped>
  **{
    margin: 0;
    padding: 0;
  }
  .centered-banner-text p {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
}
  .form-card{
    border-radius: 20px;
    box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
    background-color: #222;
    backdrop-filter: blur(50px);
    padding: 3rem 2rem 3rem 2rem;
    margin-top: 4rem;
    font-size: 1rem;
  }
  .login-frm-btn{
      padding: 1rem 10rem 1rem 10rem;
      margin-top: 3rem;
      font-weight: 200;
  }
  .text-black{
    color: #000 !important;
  }
  .user_dashboard_card_main{
    border-radius: 10px;
    box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
    background-color: #222;
    padding: 1rem 2rem 3rem 2rem;
    margin-top: 1rem;
    color: #fff;
    font-size: 1rem;
  }
  .user_dashboard_main_row{
    padding: 2rem;
    font-size: 1rem;
    color: #000;
  }
  .dashboard_card_inner{
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  height: 15rem;
  margin : 0px;
  border-radius: 1rem;
  color: #fff;
  font-size: 1rem;
  padding-bottom: 0rem;
}
.dashboard_card_inner2 {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-color: #222;
  height: auto;
  margin: 0px;
  border-radius: 1rem;
  margin-top: 0.5rem;
  padding: 0rem;
}
.dashboard_card_inner3{
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-color: #222;
  height: auto;
  margin : 0px;
  border-radius: 1rem;
  margin-top: 3rem;
  padding: 2rem;
  color: #fff;
  font-size: 1rem;
}
.ds{
  color: #fff;
  background-color: #222;
  font-size: 1rem;
}
.login-frm-btn{
      padding: 1rem 10rem 1rem 10rem;
      margin-top: 3rem;
      font-weight: 700;
}
#playliscard{
    box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
    background-image: url(/src/assets/pxfuel.jpg);
    background-position: center;
    background-size: cover;

}
</style>