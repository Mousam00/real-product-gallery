<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()

onMounted(() => {
  const query = route.query
  const access = query.access
  const refresh = query.refresh
  const username = query.username
  const email = query.email
  console.log("at the auth page frontend");
  
  if (access && refresh && username && email) {
    // Save tokens and user info in your auth store
    auth.login(access, refresh, { username, email })

    // Redirect to homepage or dashboard after successful login
    router.replace('/')
  } else {
    // If tokens or user info missing, redirect to login page
    router.replace('/')
  }
})
</script>

<template>
  <div class="flex justify-center items-center h-screen">
    <p class="text-lg">Logging you in...</p>
  </div>
</template>
