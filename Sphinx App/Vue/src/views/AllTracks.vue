<template>
  <div class="container-fluid">
    <div class="col-md-12 card ds" style="margin-top:3rem ;padding: 2rem;border-radius: 60px;box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;">
      <div class="row">
        <div class="col-md-12 text-center">
          <h4>Track List</h4>
        </div>
      </div>
    </div>
    <div class="row user_dashboard_main_row">
      <div class="col-md-12 user_dashboard_card_main">
          <div class="card-body ds">
            <div class="row">
              <div class="col-md-8">
                  <h4 style="padding-top:2rem;">Sound Tracks</h4>
              </div>
              <div class="col-md-4 d-flex justify-content-end align-items-center" style="padding-top:2rem;">
                  <input type="text" v-model="searchQuery" class="form-control mr-2 search_tracks_input" id="searchTracks" placeholder="Search Tracks" />
                  <div style="width: 15px;"></div>
                  <button class="btn btn-light" @click="searchTracks">🔍</button>
              </div>
          </div>

            <br />
            <div class="row">
              <div class="col-md-12 card dashboard_card_inner2" v-for="(song, index) in response.songs" :key="index">
                <div class="card-body">
                  <div class="row">
                    <div class="col-md-8">
                      <h5>{{ song.title }}</h5>
                      <h5>Album: {{ song.album_title }}</h5>
                    </div>
                    <div class="col-md-4">
                      <button class="btn btn-danger text-right text-black" style="float: right; margin-right: 10px;" @click="deleteSong(song.id)">Delete Song</button>
                      <button v-if="!song.flagged" class="btn btn-warning text-right text-black" style="float: right; margin-right: 10px;" @click="toggleFlag(song)">Flag Song</button>
                        <button v-else class="btn btn-secondary text-right text-black" style="float: right; margin-right: 10px;" @click="toggleFlag(song)">Song Flagged</button>
                      <button class="btn btn-light text-right text-black" style="float: right;margin-right: 10px;" @click="$router.push('/song/' + song.id)">Play Song</button>
                    </div>
                  </div>
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
      response: [],
    };
  },
  mounted() {
    this.fetchTracks();
  },
  methods: {
    fetchTracks() {
      axios.get("http://127.0.0.1:5000/alltracks")
        .then((result) => {
          this.response = result.data;
          this.loadFlaggedState();
        })
        .catch((error) => {
          console.error('Error fetching tracks:', error);
        });
    },
    searchTracks() {
      axios.post("http://127.0.0.1:5000/alltracks", { search_button: this.searchQuery })
        .then((result) => {
          this.response = result.data;
          this.loadFlaggedState();
        })
        .catch((error) => {
          console.error('Error searching tracks:', error);
        });
    },
    deleteSong(songId) {
      axios.delete(`http://127.0.0.1:5000/songs/${songId}`)
        .then(response => {
          this.response.songs = this.response.songs.filter(song => song.id !== songId);
        })
        .catch(error => {
          console.error('Error deleting song:', error);
        });
    },
    toggleFlag(song) {
      song.flagged = !song.flagged;
      localStorage.setItem(`song_${song.id}_flagged`, song.flagged);
    },
    loadFlaggedState() {
      this.response.songs.forEach(song => {
        const flagged = localStorage.getItem(`song_${song.id}_flagged`);
        if (flagged !== null) {
          song.flagged = JSON.parse(flagged);
        }
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