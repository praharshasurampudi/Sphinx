<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4 card form-card">
        <div class="card-title text-center">
          <h3>Registration</h3>
        </div>
        <form class="card-body">
          <div class="form-group">
            <label for="exampleInputEmail1">Username</label>
            <input
              type="text"
              name="username"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              placeholder="Enter Username"
              v-model="userName"
            />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group">
            <label for="exampleInputPassword1">Create Password</label>
            <input type="password" name="password" v-model="password" class="form-control" id="exampleInputPassword1" placeholder="Enter Password" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group">
            <label for="exampleInputPassword1">Re-Enter Your Passsword</label>
            <input
              type="password"
              name="confirm_password"
              v-model="rePassWord"
              class="form-control"
              id="exampleInputPassword1"
              placeholder="Enter Password"
            />
          </div>
          <div style="height: 25px;"></div>
          <p class="text-danger">{{ errorText }}</p>
          <div class="text-center">
            <button type="submit" class="btn btn-light text-black login-frm-btn" @click="handleRegister">Register</button>
          </div>
        </form>
      </div>
      <div class="col-md-4"></div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      userName: "",
      password: "",
      rePassWord: "",
      showError: "",
      errorText: "",
    };
  },
  methods: {
    handleRegister($event) {
      $event.preventDefault();
      if (!this.userName || !this.password || !this.rePassWord) {
        this.showError = true;
        this.errorText = "Invalid Credentials";
      }
      if (this.password != this.rePassWord) {
        this.showError = true;
        this.errorText = "Passwords Not matching ....";
      }
      if (this.userName && this.password == this.rePassWord) {
        var self = this;
        $event.preventDefault();
        if (!this.userName || !this.password) {
          this.showError = true;
          this.errorText = "Invalid data";
        } else {
          axios
            .post("http://127.0.0.1:5000/registration", {
              username: this.userName,
              password: this.password,
            })
            .then(function (response) {
              self.$router.push("/userlogin");
            })
            .catch(function (error) {
                self.showError = true;
                self.errorText = response.data.msg;
            });
        }
      }
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

/* Body Styles */
body {
  background-image: url(./pxfuel.jpg);
  color: #fff;
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  font-family: Helvetica, sans-serif;
}

/* Component Styles */
.centered-banner-text {
  height: 25rem;
  position: relative;
}

.centered-banner-text p {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
}

.form-card {
  border-radius: 20px;
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.35);
  background-color: #222;
  backdrop-filter: blur(50px);
  padding: 3rem 2rem;
  margin-top: 4rem;
  color: #fff;
}

.btn-font-bold {
  font-size: 1.2rem;
  font-weight: 500;
}

</style>