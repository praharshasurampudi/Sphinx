<template>
  <div class="container-fluid">
    <div class="col-md-12 card ds" style="margin-top:3rem ;padding: 2rem;border-radius: 60px;box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;">
      <div class="row">
        <div class="col-md-12 text-center">
          <h4>Admin Dashboard</h4>
        </div>
      </div>
    </div>
    <div class="row user_dashboard_main_row">
      <div class="col-md-12 user_dashboard_card_main card">
        <div class="card-body">
          <div class="row">
            <h4 class="col-md-10">Patron</h4>
            <div class="col-md-2  d-flex justify-content-end">
              <button class="btn btn-light" @click="$router.push('/userdashboard')">User Dashboard</button>
            </div>
          </div>
          <div style="height: 15px;"></div>
          <br />
          <div class="row text-center">
            <div style="width: 50px;"></div>
            <div class="col-md-5 card  dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Users</h5>
                <h3>{{ response.user_count }}</h3>
              </div>
            </div>
            <div style="width: 100px;"></div>
            <div class="col-md-5 card dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Artists</h5>
                <h3>{{ response.creator_count }}</h3>
              </div>
            </div>
          </div>
          <br />
          <br />
          <div class="row text-center">
            <div style="width: 50px;"></div>
            <div class="col-md-5 card dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Singers</h5>
                <h3>{{ response.singer_count }}</h3>
              </div>
            </div>
            <div style="width: 100px;"></div>
            <div class="col-md-5 float-right card dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Lyricists</h5>
                <h3>{{ response.lyricist_count }}</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="height: 15px;"></div>
      <div class="col-md-12 user_dashboard_card_main card">
        <div class="card-body">
          <div class="row">
            <div class="col-md-10">
              <h4>Performance</h4>
            </div>
            <div class="col-md-2  d-flex justify-content-end">
              <button class="btn btn-light" @click="$router.push('/alltracks')">Manage Tracks</button>
            </div>
          </div>
          <div style="height: 15px;"></div>
          <br />
          <div class="row text-center">
            <div style="width: 50px;"></div>
            <div class="col-md-3 card dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Total Songs</h5>
                <h3>{{ response.song_count }} Songs</h3>
              </div>
            </div>
            <div class="col-md-1"></div>
            <div class="col-md-3 card dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Total Playlists</h5>
                <h3>{{ response.playlist_count }} Playlists</h3>
              </div>
            </div>
            <div class="col-md-1"></div>
            <div class="col-md-3 card dashboard_card_inner">
              <div class="card-body">
                <h5 style="margin-top: 50px">Total Albums</h5>
                <h3>{{ response.album_count }} Albums</h3>
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
      response: [],
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:5000/admindashboard").then((result) => {
      this.response = result.data;
    });
  },
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
  height: 12rem;
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