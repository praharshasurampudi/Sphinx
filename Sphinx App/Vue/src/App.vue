<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import NavCommonVue from "./components/NavCommon.vue";
</script>

<template>
  <NavCommonVue />
  <RouterView />
</template>

<style scoped></style>
