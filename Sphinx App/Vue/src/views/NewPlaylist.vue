<template>
  <div class="container-fluid">
    <form method="POST" action="/newplaylist" @submit.prevent="submitPlaylist">
        <div class="container">
            <div class="row">
                <div class="col-md-4"></div>
                <div class="col-md-4 card form-card text-center">
                <div class="card-title text-center" style="margin: 1rem 1rem">
                    <h2 style="color: white">New Playlist</h2>
                </div>
                <div class="form-group">
                    <input type="text" v-model="playlistTitle" name="playlist_title" class="form-control" placeholder="Enter playlist name" />
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
                        <div class="col-md-12">
                          <div class="row" style="padding-bottom:-5px;">
                            <h5 class="col-md-6" style="color: white;">{{ song.title }}</h5>
                            <div class="col-md-6 d-flex justify-content-end">
                              <div class="text-center" style="text-align: right; margin-right: 15px">
                                <input type="checkbox" v-model="selectedSongs" :value="song.id" name="song_ids" style="width: 2rem; height: 2rem" />
                              </div>
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

            <div style="height: 25px;"></div>
            <div class="row">
                <div class="col-md-12 text-center">
                <button type="submit" class="btn btn-light text-black">Create Playlist</button>
                </div>
            </div>
        </div>
    </form>
  </div>
  <div style="height: 25px;"></div>
</template>
<script>
import axios from "axios";
import { SERVER_URL } from "../consts";
export default {
  data() {
    return {
      songs: [],
      playlistTitle: "",
      selectedSongs: [],
      serverUrl: SERVER_URL,
      error: "",
    };
  },

  computed: {
    formattedSelectedSongs() {
      return this.selectedSongs.join(",");
    },
  },

  mounted() {
    axios.get(`http://127.0.0.1:5000/song?song_id=${this.$router.currentRoute.value.params.id}`).then((result) => {
      this.songs = result.data.song;
      console.log(result.data.song);
      this.formattedSelectedSongs = this.selectedSongs.join(",");
    });
  },
  methods: {
      computed: {
    formattedSelectedSongs() {
      return this.selectedSongs.join(',');
    }
  },

  async submitPlaylist() {
    try {
      // Validate user input (optional)
      if (!this.playlistTitle || !this.formattedSelectedSongs) {
        this.error = 'Please enter a playlist title and select songs.';
        return;
      }

      const formData = new FormData();
      formData.append('playlist_title', this.playlistTitle);
      formData.append('song_ids', this.formattedSelectedSongs);

      const config = {
        headers: {
          'Content-Type': 'application/json'
        }
      };

      const response = await axios.post('http://127.0.0.1:5000/newplaylist', formData, config);

      if (response.status === 200) {
        console.log('Playlist created successfully:', response.data);
        this.$router.push('/userdashboard');
      } else {
        console.error('Error creating playlist:', response.data);
        this.error = 'Error creating playlist. Please try again.';
      }
    } catch (error) {
      if (error.response) {
        console.error('Error creating playlist:', error.response.data);
        this.error = 'Error creating playlist. Please try again.';
      } else if (error.request) {
        console.error('Error creating playlist:', error.request);
        this.error = 'Error creating playlist. Please try again.';
      } else {
        console.error('Error creating playlist:', error.message);
        this.error = 'Error creating playlist. Please try again.';
      }
    }
  },
    fetchSongs() {
      axios.get(`http://127.0.0.1:5000/song?song_id=${this.$router.currentRoute.value.params.id}`)
        .then((result) => {
          this.songs = result.data;
        })
        .catch((error) => {
          console.error("Error fetching songs:", error);
        });
    },
  }
}
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

.centered_banner_text {
  height: 25rem;
  position: relative;
}

.centered_banner_text p {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  font-size: 3rem;
}

.btn-font-bold {
  font-size: 2rem;
  font-weight: 500;
}

#reg_btn_home {
  color: #fff !important;
  text-decoration: none !important;

}

#log_btn_home {
  color: #000 !important;
  text-decoration: none !important;
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

#anchor_notext_decor {
  color: #000 !important;
  text-decoration: none !important;
  font-family: Helvetica, sans-serif;
}

.Registorascreator {
  color: #fff;
  background-color: whitesmoke;
  border-color: rgb(255, 255, 255);
  border-radius: 120px;
  height: 24rem;
  width: 24rem;
}

.user_dashboard_card_main {
  border-radius: 10px;
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  padding: 1rem 3rem 5rem 3rem;
  margin-top: 5rem;
}

.user_dashboard_track_main {
  border-radius: 10px;
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  padding: 1rem 3rem 1rem 3rem;
  margin-top: 4rem;
}

.dashboard_card_inner {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  height: 15rem;
  margin: 0px;
  border-radius: 1rem;
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

.dashboard_card_inner3 {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-color: #222;
  height: auto;
  margin: 0px;
  border-radius: 1rem;
  margin-top: 3rem;
  padding: 2rem;
}

.user_dashboard_main_row {
  padding: 5rem;
}

.search_tracks_input {
  width: 35%;
  float: right;
  margin: 2rem;
}

.card_songpage_main {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  height: auto;
  margin: 0px;
  border-radius: 1rem;
}

.card_songpage_inner {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  justify-content: center;
  height: auto;
  margin-bottom: 2rem;
  border-radius: 1rem;
}

.percentage:after {
  content: "";
  display: block;
  background-color: #3d9970;
}

.percentage-20:after {
  width: 20%;
}

.percentage-30:after {
  width: 30%;
}

#audio {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
  margin-bottom: 2rem;
}

#pic {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-image: url(./pxfuel.jpg);
  background-position: center;
  background-size: cover;
  height: 35rem;
  margin: 2px;
  border-radius: 1rem;
  margin-top: 2rem;
  padding: 2rem;
  width: 35rem;
  margin-left: 24%;
}

#playliscard {
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
  background-image: url(./pxfuel.jpg);
  background-position: center;
  background-size: cover;

}
</style>
