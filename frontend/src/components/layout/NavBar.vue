<script setup>
import { RouterLink} from 'vue-router'
import { Upload, Heart, LogOut, Shield, User } from 'lucide-vue-next'
import {ref} from 'vue'
import AuthModal from '../AuthModal.vue'
import { useAuthStore } from '@/stores/auth'
import ReviewModel from '@/views/ReviewModel.vue'
// import AuthModal from './AuthModal.vue'
// import ProductSubmissionModal from './ProductSubmissionModal.vue'
const showModal = ref(false)
const authMode = ref('login')
const openModal = (mode) =>{
  authMode.value = mode
  showModal.value = true
}
const closeModal = () => {
  showModal.value = false
}
const authStore = useAuthStore()

</script>

<template>
  <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <RouterLink to="/" class="flex items-center space-x-2">
          <Heart class="h-8 w-8 text-indigo-600" />
          <span class="text-xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
            ReviewGallery
          </span>
        </RouterLink>

        <!-- Nav links -->
        <div class="hidden md:flex items-center space-x-8">
          <RouterLink
            to="/"
            class="text-sm font-medium transition-colors hover:text-indigo-600"
          >
            Home
          </RouterLink>

          <RouterLink
            to="/gallery"
            class="text-sm font-medium transition-colors hover:text-indigo-600"
          >
            Gallery
          </RouterLink>

          <RouterLink
          v-if="authStore.isAdmin"
            to="/admin-panel"
            class="text-sm font-medium transition-colors hover:text-indigo-600"
          >
            Admin
          </RouterLink>
        </div>

        <!-- Action buttons -->
        <div class="flex items-center space-x-4">
          <!-- Authenticated User Display -->
           <div v-if="authStore.isAuthenticated" class="flex space-x-4 items-center">
          <span class="text-sm text-gray-600 hidden sm:block">
            Welcome, <strong>User</strong>!
            <Shield class="h-4 w-4 text-amber-500 inline-flex items-center ml-1" title="Admin" />
          </span>

          <!-- Submit Product Button -->
          <button
          @click="openModal('submit')"
            class="px-3 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white font-medium rounded text-sm flex items-center"
          >
            <Upload class="h-4 w-4 mr-2" />
            <span class="hidden sm:inline">Submit Product</span>
            <span class="sm:hidden">Submit</span>
          </button>

          <!-- Logout Button -->
          <button
          @click="authStore.logout"
            class="text-gray-700 hover:text-red-600 text-sm font-medium flex items-center"
          >
            <LogOut class="h-4 w-4 mr-2" />
            <span class="hidden sm:inline">Logout</span>
          </button>
        </div>
          <!-- Login Button -->
           <div v-else class="flex space-x-4">
          <button
          @click="openModal('login')"
            class="text-gray-700 hover:text-indigo-600 text-sm flex items-center hover:bg-gray-100 p-2 rounded"
          >
            <User class="h-4 w-4 mr-2" />
            Login
          </button>

          <!-- Sign Up Button -->
          <button
          @click="openModal('register')"
            class="px-3 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white rounded text-sm flex items-center"
          >
            <Upload class="h-4 w-4 mr-2" />
            Sign Up
          </button>
          </div>
        </div>
      </div>
    </div>
  </nav>

  <!-- Modals -->
  <!-- <AuthModal />
  <ProductSubmissionModal /> -->
  <ReviewModel v-if="authStore.isAuthenticated" :is-open="showModal" @close="closeModal" />

  <AuthModal
  v-else
  :is-open="showModal"
  :mode="authMode"
  @close="showModal = false"
  @mode-change="val => authMode = val"
/>

</template>
