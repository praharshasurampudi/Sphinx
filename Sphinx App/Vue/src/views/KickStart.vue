<template>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4 card form-card">
          <div class="card-title text-center">
            <h4 style="color: white;">Embrace your creator journey</h4>
            <h5 style="color: white;">Continue with uploading songs</h5>
          </div>
          <form class="card-body">
            <div class="text-center">
              <button type="submit" class="btn btn-light Registorascreator text-black login-frm-btn text-center" id="anchor_notext_decor" style="font-size: 3rem" @click="$router.push('/uploadsongs')">
              +
              </button>
            </div>
          </form>
        </div>
        <div class="col-md-4"></div>
      </div>
    </div>
</template>

<style scoped>
** {
  margin: 0;
  padding: 0;
}
.form-card {
  border-radius: 20px;
  box-shadow: rgb(255 255 255 / 35%) 0px 0px 20px;
  background-color: #222;
  backdrop-filter: blur(50px);
  padding: 3rem 2rem 3rem 2rem;
  margin-top: 4rem;

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
  border-radius: 100px;
  height: 8rem;
  width: 8rem;
}
</style>