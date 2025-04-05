<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4"></div>
      <div class="col-md-4 card form-card">
        <div class="card-title text-center">
          <h3>Administrator Login</h3>
        </div>
        <form class="card-body">
          <div class="form-group">
            <label for="exampleInputEmail1">Username</label>
            <input type="text" class="form-control" name="username" v-model="userName" id="exampleInputEmail1" placeholder="Enter Username" />
          </div>
          <div style="height: 15px;"></div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" class="form-control" name="password" v-model="passWord" id="exampleInputPassword1" placeholder="Enter Password" />
          </div>
          <div style="height: 25px;"></div>
          <p class="text-danger">{{ errorText }}</p>
          <div class="text-center">
            <button type="submit" class="btn btn-light text-black login-frm-btn" @click="handleLogin">Login</button>
          </div>
          <br />
          <p class="text-center">No Admin access, go to user login</p>
        </form>
      </div>
      <div class="col-md-4"></div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      userName: "",
      passWord: "",
      showError: "",
      errorText: "",
    };
  },
  mounted() {},
  methods: {
    handleLogin($event) {
      $event.preventDefault();
      if (!this.userName || !this.passWord) {
        this.showError = true;
        this.errorText = "Invalid Credentials";
      }
      if (this.userName == "admin" && this.passWord == "adminkey") {
        this.$router.push("/admindashboard");
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