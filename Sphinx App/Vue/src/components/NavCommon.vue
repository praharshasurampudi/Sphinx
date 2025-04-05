<template>
  <nav class="navbar navbar-inverse">
    <div class="container-fluid">
      <div class="navbar-header">
        <p class="navbar-brand route-link" style="color: #fff" @click="$router.push('/')">✩ SPHINX</p>
      </div>
      <p
        v-if="['/userdashboard', '/creatordashboard'].includes(currentRoute)"
        class="navbar-brand route-link"
        style="color: #fff"
        @click="$router.push('/kickstart')"
      >
      ♫ Upload
      </p>
      <div v-if="currentRoute">
        <p
          v-if="this.$router.currentRoute.value.href == '/userlogin' || currentRoute == '/'"
          class="navbar-brand route-link"
          style="color: #fff"
          @click="$router.push('/adminlogin')"
        >
        ♛ Admin Login
        </p>
        <p
          v-if="currentRoute == '/registration' || currentRoute == '/adminlogin'"
          class="navbar-brand route-link"
          style="color: #fff"
          @click="$router.push('/userlogin')"
        >
        ♕ User Login
        </p>
        <p
          v-if=" currentRoute == '/uploadsongs'"
          class="navbar-brand route-link"
          style="color: #fff"
          @click="$router.push('/userdashboard')"
        >
        ♕ User Dashboard
        </p>

        <p
          v-if="currentRoute === '/userdashboard' || currentRoute === '/creatordashboard' || currentRoute === '/admindashboard' || currentRoute === '/alltracks' || currentRoute === '/kickstart' || currentRoute === '/playlist/:id' || currentRoute === '/newplaylist'"
          class="navbar-brand route-link"
          style="color: #fff"
          @click="$router.push('/')"
        >
        » Logout
        </p>
      </div>
      <p v-if="currentRoute === '/playlist/1' || currentRoute === '/playlist/2'" class="navbar-brand route-link" style="color: #fff" @click="$router.push('/userdashboard')"> User Dashboard</p>

    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      currentRoute: "",
    };
  },
  mounted() {
    // setTimeout(() => {
    //   this.currentRoute = this.$router.currentRoute.value.href;
    //   console.log(this.currentRoute);
    // }, 1000);
  },
  watch: {
    $route(to, from) {
      // Put your logic here...
      console.log(to, from);
      this.currentRoute = to.fullPath;
    },
  },
  created() {},
};
</script>
<style scoped>
/* Reset */
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
.route-link {
  cursor: pointer;
}

.navbar {
  background-color: #191919;
  padding: 0.5rem;
  border-radius: 20px;

}

.navbar-brand {
  color: #ccc !important;
  font-size:20px;
}

.navbar-brand:hover {
  color: #fff !important;
}

</style>
