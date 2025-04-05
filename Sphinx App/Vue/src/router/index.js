import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserLogin from '../views/UserLogin.vue'
import Registration from '../views/Registration.vue'
import AdminLogin from '../views/AdminLogin.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import UserDashboard from '../views/UserDashboard.vue'
import UploadSongs from '../views/UploadSongs.vue'
import CreatorDashboard from '../views/CreatorDashboard.vue'
import AllTracks from '../views/AllTracks.vue'
import KickStart from '../views/KickStart.vue'
import NewPlaylist from '../views/NewPlaylist.vue'
import Song from '../views/Song.vue'
import PlayList from '../views/Playlist.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/userlogin',
      name: 'userlogin',
      component: UserLogin
    },
    {
      path: '/registration',
       name: 'Registration',
      component: Registration
    },
    {
      path: '/adminlogin',
       name: 'AdminLogin',
      component: AdminLogin
    },
    {
      path: '/admindashboard',
       name: 'AdminDashboard',
      component: AdminDashboard
    },
    {
      path: '/userdashboard',
       name: 'UserDashboard',
      component: UserDashboard
    },
    {
      path: '/uploadsongs',
       name: 'UploadSongs',
      component: UploadSongs
    },
    {
      path: '/creatordashboard',
       name: 'CreatorDashboard',
      component: CreatorDashboard
    },
    {
      path: '/alltracks',
       name: 'AllTracks',
      component: AllTracks
    },
    {
      path: '/kickstart',
       name: 'KickStart',
      component: KickStart
    },
    {
      path: '/newplaylist',
       name: 'NewPlaylist',
      component: NewPlaylist
    },
    {
      path: '/song/:id',
      name: 'Song',
      component: Song
    },
      {
      path: '/PlayList/:id',
      name: 'PlayList',
      component: PlayList
    },

  ]
})

export default router
