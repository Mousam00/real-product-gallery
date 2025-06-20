<script setup>
import NavBar from './components/layout/NavBar.vue';
import HomePage from './views/HomePage.vue';
import { RouterView } from 'vue-router';
import Footer from './components/layout/Footer.vue';
</script>

<template>
  <NavBar />
  <RouterView />
  <Footer></Footer>


</template>

<style scoped>


</style>
