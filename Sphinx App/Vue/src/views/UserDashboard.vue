<template>
  <div class="container-fluid">
    <div class="col-md-12 card ds" style="margin-top:3rem ;padding: 2rem;border-radius: 60px;box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;">
      <div class="row">
        <div class="col-md-12 text-center">
          <h4>User Dashboard</h4>
        </div>
      </div>
    </div>
    <div class="row user_dashboard_main_row">
      <div class="col-md-12 user_dashboard_card_main card">
        <div class="card-body">
          <div class="row">
            <div class="row" style="margin-top: 1rem;">
              <form class="col-md-7" action="/creatordashboard" method="post">
                <h4 style="color: white;">Tracks Library</h4>
              </form>
              <div class="col-md-2 d-flex justify-content-end align-items-center">
                <button class="btn btn-light" @click="$router.push('/creatordashboard')">Creator Dashboard</button>
              </div>
              <div class="col-md-3 d-flex justify-content-end align-items-center">
                <input type="text" v-model="searchQuery" class="form-control mr-1 search_tracks_input" id="searchTracks" placeholder="Search Tracks" @keyup.enter="searchTracks" />
                <div style="width: 15px;"></div>
                <button class="btn btn-light" @click="searchTracks">🔍</button>
              </div>
            </div>
          </div>
          <div class="row" style="padding: 2rem; display: flexbox; justify-content: center">
            <div class="col-md-12" v-if="songs.length > 0">
              <div class="row">
                <div class="col-md-3 dashboard_card_inner3" v-for="(song, index) in songs" :key="index">
                  <h2>🎧</h2>
                  <h3 class="text-center">{{ song.title }}</h3>
                  <button class="text-right btn btn-light btn-large"style="float: right; margin-top: 1rem" @click="$router.push('/song/' + song.id)">View Song</button>
                  <div style="width: 25px;"></div>
                </div>
                
              </div>
            </div>
            <div v-else class="col-md-3 dashboard_card_inner3">
              <div class="row">
                <h2>🎧</h2>
                <h3 class="text-center">No Song</h3>
                <button class="btn btn-light" style="float: right; margin-top: 1rem" @click="$router.push('/uploadsongs')">Upload Song</button>
              </div>
            </div>
            <br /><br />
          </div>
        </div>
      </div>
    </div>
    <hr />
    <div class="row user_dashboard_main_row">
      <div class="col-md-12 user_dashboard_card_main card">
        <div class="card-body">
          <div class="row">
            <div class="row" style="margin-top: 1rem;">
              <form class="col-md-7" action="/creatordashboard" method="post">
                <h4 style="color: white;">Your Playlists</h4>
              </form>
              <div class="col-md-2 d-flex align-items-center justify-content-end">
                <button class="btn btn-light" @click="$router.push('/newplaylist')">New Playlist</button>
              </div>
              <div class="col-md-3 d-flex justify-content-end align-items-center">
                <input type="text" v-model="searchPlaylistQuery" class="form-control mr-1 search_tracks_input" id="searchPlaylists" placeholder="Search Playlists" @keyup.enter="searchTracksp" />
                <div style="width: 15px;"></div>
                <button class="btn btn-light" @click="searchTracksp">🔍</button>
              </div>
            </div>
            <div class="row" style="padding: 2rem; display: flexbox; justify-content: center">
              <div class="col-md-12">
                <div class="row" v-if="playlists.length > 0">
                  <div class="col-md-3 dashboard_card_inner3 ds" v-for="(playlist, index) in playlists" :key="index">
                    <h2>♬</h2>
                      <h3 class="text-center">{{ playlist.title }}</h3>
                      <button class="text-right btn btn-light" style="float: right; margin-top: 1rem" @click="$router.push('/playlist/' + playlist.id)">View Playlist</button>
                  </div>
                </div>
                <div v-else class="col-md-3 dashboard_card_inner3 ds">
                  <div class="row ds">
                    <h2>🎵</h2>
                    <h3 class="text-center">No Playlists</h3>
                    <button class="btn btn-light btn-large" style="float: right; margin-top: 1rem" @click="$router.push('/newplaylist')">Create Playlist</button>
                  </div>
                </div>
              </div>
              <br /><br />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      searchQuery: "",
      searchPlaylistQuery: "",
      songs: [],
      playlists: [],
    };
  },
  mounted() {
    this.fetchDashboardData();
  },
  methods: {
    fetchDashboardData() {
      axios.get("http://127.0.0.1:5000/userdashboard")
        .then((result) => {
          this.songs = result.data.songs;
          this.playlists = result.data.playlists;
        })
        .catch((error) => {
          console.error('Error fetching dashboard data:', error);
        });
    },
    searchTracks() {
      axios.post("http://127.0.0.1:5000/userdashboard", { search_button: this.searchQuery })
        .then((result) => {
          this.songs = result.data.songs;
        })
        .catch((error) => {
          console.error('Error searching tracks:', error);
        });
    },
    searchTracksp() {
      axios.post("http://127.0.0.1:5000/userdashboard", { search_playlist_button: this.searchPlaylistQuery })
        .then((result) => {
          this.playlists = result.data.playlists;
        })
        .catch((error) => {
          console.error('Error searching playlists:', error);
        });
    }
  }
};
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
.dashboard_card_inner2{
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-color: #222;
  height: auto;
  margin : 0px;
  border-radius: 1rem;
  margin-top: 1rem;
  padding: 1rem 1rem 1rem 1rem;
  color: #fff;
  font-size: 1rem;
}
.dashboard_card_inner3{
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-color: #222;
  height: auto;
  margin-right : 0px;
  border-radius: 1rem;
  margin-top: 3rem;
  padding: 2rem;
  color: #fff;
  font-size: 1rem;
  margin-left: 75px;
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
</style>