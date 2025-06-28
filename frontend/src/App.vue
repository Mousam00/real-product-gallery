<script setup>
import NavBar from './components/layout/NavBar.vue';
import HomePage from './views/HomePage.vue';
import { RouterView } from 'vue-router';
import Footer from './components/layout/Footer.vue';

// const auth = useAuthStore()

// const fetchCurrentUser = async () => {
//   try {
//     const response = await axios.get('http://127.0.0.1:8000/api/accounts/user/', {
//       headers: {
//         Authorization: `Bearer ${auth.accessToken}`,
//       },
//     })
//     auth.login(auth.accessToken, auth.refreshToken, response.data)
//   } catch (error) {
//     auth.logout()
//   }
// }

// // Call this on app start
// fetchCurrentUser()

</script>

<template>
  <NavBar />
  <RouterView />
  <Footer></Footer>


</template>

<style scoped>


</style>
