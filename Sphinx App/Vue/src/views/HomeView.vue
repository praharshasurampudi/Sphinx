<template>
  <div class="container-fluid">
    <div class="centered-banner-text">
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4 card form-card">
          <div class="card-title text-center">
            <h4>Welcome To</h4>
            <h1>SPHINX</h1>
            <br><br>
          </div>
          <form method="post" action="/userlogin" class="card-body">
            <div class="d-flex justify-content-center">
              <button class="btn btn-light btn-ref-no-href" @click="goTo('/userlogin')">Login</button>
              <div style="width: 10px;"></div>
              <button class="btn btn-light btn-ref-no-href" @click="goTo('/registration')">Register</button>
            </div>
          </form>
        </div>
        <div class="col-md-4"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    goTo(val) {
      this.$router.push(val);
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
