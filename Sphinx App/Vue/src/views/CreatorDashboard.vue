<template>
  <div class="container-fluid">
    <div class="col-md-12 card ds" style="margin-top:3rem ;padding: 2rem;border-radius: 60px;box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;">
      <div class="row">
        <div class="col-md-12 text-center">
          <h4>Creator Dashboard</h4>
        </div>
      </div>
    </div>
    <div class="row user_dashboard_main_row">
      <div class="col-md-12 user_dashboard_card_main ds">
        <div class="row">
          <div style="height: 25px;"></div>
          <h4 class="col-md-10">Dashboard</h4>
          <div class="col-md-2 d-flex align-items-center justify-content-end">
            <button class="btn btn-light" @click="$router.push('/userdashboard')">User Dashboard</button>
          </div>
        </div>
        <div style="height: 25px;"></div>
        <br />
        <div class="row">
          <div style="width: 50px;"></div>
          <div class="col-md-5 card dashboard_card_inner">
            <div class="card-body d-flex flex-column align-items-center">
              <h5 style="margin-top: 50px">Total Songs</h5>
              <h3>{{ songCount }} Songs</h3>
            </div>
          </div>
          <div class="col-md-1"></div>
          <div class="col-md-5 card dashboard_card_inner">
            <div class="card-body d-flex flex-column align-items-center">
              <h5 style="margin-top: 50px">Total Albums</h5>
              <h3>{{ albumCount }} Albums</h3>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row user_dashboard_main_row">
      <div class="col-md-12 user_dashboard_card_main" style="background-color: #222;">
          <div class="card-body ds">
            <div style="height: 25px;"></div>
            <div class="row ds">
                <form class="col-md-8" action="/creatordashboard" method="post">
                  <h4>Songs</h4>
                </form>
                <div class="col-md-1 d-flex align-items-center justify-content-end">
                    <button class="btn btn-light" @click="$router.push('/uploadsongs')">Upload</button>
                </div>
                <div class="col-md-3 d-flex justify-content-end align-items-center">
                  <input type="text" v-model="searchQuery" class="form-control mr-1 search_tracks_input" id="searchTracks" placeholder="Search Tracks" @keyup.enter="searchTracks" />
                  <div style="width: 15px;"></div>
                  <button class="btn btn-light" @click="searchTracks">🔍</button>
                </div>
            </div>
            <br />
              <div class="col-md-12 card dashboard_card_inner2 ds" v-for="(song, index) in songs" :key="index">
                  <div class="row" style="margin-top: 15px;">
                    <div class="col-md-6">
                      <h5 >{{ song.title }}</h5>
                    </div>
                    <div class="col-md-6 d-flex justify-content-end">
                      <button class="btn btn-light text-right text-black" style="float: right;margin-right: 10px;" @click="$router.push('/song/' + song.id)">Play Song</button>
                      <button class="btn btn-danger text-right text-black" style="float: right; margin-right: 10px;" @click="deleteSong(song.id)">Delete Song</button>
                      <!-- <button class="btn btn-secondary text-right text-black" style="float: right; margin-right: 10px;" @click="$router.push('/song/'+song.id)">Edit Song</button> -->
                    </div>
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
      songCount: "",
      albumCount: "",
      songs: [],
    };
  },
  mounted() {
    this.fetchDashboardData();
  },
  methods: {
    fetchDashboardData() {
      axios.get("http://127.0.0.1:5000/creatordashboard")
        .then((result) => {
          this.songCount = result.data.song_count;
          this.albumCount = result.data.album_count;
          this.songs = result.data.songs;
        })
        .catch((error) => {
          console.error('Error fetching dashboard data:', error);
        });
    },
    searchTracks() {
      axios.post("http://127.0.0.1:5000/creatordashboard", { search_button: this.searchQuery })
        .then((result) => {
          this.songs = result.data.songs;
        })
        .catch((error) => {
          console.error('Error searching tracks:', error);
        });
    },
    deleteSong(songId) {
      axios.delete(`http://127.0.0.1:5000/song/${songId}`)
        .then(response => {
          // Remove the deleted song from the songs array
          this.songs = this.songs.filter(song => song.id !== songId);
          // Optionally, show a success message or perform any other necessary actions
        })
        .catch(error => {
          // Handle error, show error message or perform any other necessary actions
          console.error('Error deleting song:', error);
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
</style>