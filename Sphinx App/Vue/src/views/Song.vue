<template>
  <div class="container-fluid">
    <div style="height: 50px;"></div>
    <div class="col-md-3"></div>
    <div class="col-md-6 justify-content-center card_songpage_main mx-auto" style="padding: 3rem">
      <div class="row">
        <div class="col-md-12 text-center">
          <h3 style="color: white;">Song Page</h3>
          <br />
        </div>
        <div class="col-md-12 justify-content-center mx-auto text-center dashboard_card_inner3" id="pic">
          <div style="height: 20px;"></div>
          <h2>🎧</h2>
          <h2 style="color: white;">{{ response.title }}</h2>
          <br />
          <div class="container col-md-12" id="audio" style="align-self: center">
            <!-- <audio controls autoplay>
                <source :src="serverUrl + response.path" type="audio/mp3">
            </audio> -->
            <a :href="serverUrl +response.path" @click=playsong() class="btn btn-light" target="_blank">Play Song</a>
          </div>
        </div>
        <div class="container d-flex col-md-12" id="audio" style="align-self: center">
          <div class="row">
            <div class="col-md-12 text-center">
              <h4 style="color: white;">Song Details</h4>
              <br />
            </div>
            <div class="col-md-12 d-flex align-items-center justify-content-center card_songpage_inner" style="padding: 3rem; color: white;">
              <div class="card-body text-center">
                <div class="card-text"  style="padding-bottom: 20px;">Song Title: {{ response.title }}</div>
                <div class="card-text"  style="padding-bottom: 20px;">Album Title: {{ response.album_title }}</div>
                <div class="card-text"  style="padding-bottom: 20px;">Music Producer: {{ response.music_producer }}</div>
                <div class="card-text"  style="padding-bottom: 20px;">Singer: {{ response.singer }}</div>
                <div class="card-text"  style="padding-bottom: 20px;">Lyricist: {{ response.lyricist }}</div>
                <div class="card-text"  style="padding-bottom: 20px;">Release Date: {{ response.date }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12 text-center">
          <h4 style="color: white;">Lyric Sheet</h4>
          <br />
        </div>
      </div>
      <div class="row">
        <div class="col-md-12 card_songpage_main text-center" style="padding: 3rem;color: white;">
          <h6 style="font-size: 14px; font-weight: 300">
            {{ response.lyrics }}
          </h6>
        </div>
      </div>
      <!-- {% endif %} -->
    </div>
    <div class="col-md-3"></div>
  </div>
</template>
<script>
import axios from "axios";
import {SERVER_URL} from '../consts';
var showauido=false;
export default {
  data() {
    return {
      response: {},
      serverUrl: SERVER_URL

    };
  },
  mounted() {
    axios.get(`http://127.0.0.1:5000/song?song_id=${this.$router.currentRoute.value.params.id}`).then((result) => {
      let data = result.data.song.filter((s) => s.id == this.$router.currentRoute.value.params.id);
      data.forEach((el) => {
        if (el.id == this.$router.currentRoute.value.params.id) {
          this.response = el;
        }
      });
    });
  },
  methods: {
    playsong(){
      this.showauido=true;
    }
  }
};
</script>
<style scoped>
  body{
    color: #fff
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

  #audio {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 2rem;
    margin-bottom: 2rem;
  }

  #pic {
    box-shadow: rgb(255 255 255 / 35%) 0px 0px 5px;
    background-image: url(/src/assets/pxfuel.jpg);
    background-position: center;
    background-size: cover;
    height: 20rem;
    margin: 2px;
    border-radius: 1rem;
    margin-top: 2rem;
    padding: 2rem;
    width: 20rem;
    margin-left: 33%;
  }
</style>
