<script setup>
import { RouterLink } from 'vue-router'
import { Upload, Heart, LogOut, Shield, User, Menu, X } from 'lucide-vue-next'
import { ref } from 'vue'
import AuthModal from '../AuthModal.vue'
import { useAuthStore } from '@/stores/auth'
import ReviewModel from '@/views/ReviewModel.vue'

const showModal = ref(false)
const authMode = ref('login')
const isMobileMenuOpen = ref(false)

const openModal = (mode) => {
  authMode.value = mode
  showModal.value = true
}
const closeModal = () => {
  showModal.value = false
}
const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
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

        <!-- Desktop Nav links -->
        <div class="hidden md:flex items-center space-x-8">
          <RouterLink to="/" class="text-sm font-medium transition-colors hover:text-indigo-600">Home</RouterLink>
          <RouterLink to="/gallery" class="text-sm font-medium transition-colors hover:text-indigo-600">Gallery</RouterLink>
          <RouterLink v-if="authStore.isAdmin" to="/admin-panel" class="text-sm font-medium transition-colors hover:text-indigo-600">Admin</RouterLink>
        </div>

        <!-- Mobile menu button -->
        <button @click="toggleMobileMenu" class="md:hidden p-2 rounded hover:bg-gray-100 text-gray-700">
          <Menu v-if="!isMobileMenuOpen" class="h-6 w-6" />
          <X v-else class="h-6 w-6" />
        </button>

        <!-- Action buttons -->
        <div class="hidden md:flex items-center space-x-4">
          <div v-if="authStore.isAuthenticated" class="flex space-x-4 items-center">
            <span class="text-sm text-gray-600 hidden sm:block">
              Welcome, <strong>{{authStore.username}}</strong>!
              <Shield class="h-4 w-4 text-amber-500 inline-flex ml-1" title="Admin" />
            </span>

            <button @click="openModal('submit')" class="px-3 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white font-medium rounded text-sm flex items-center">
              <Upload class="h-4 w-4 mr-2" />
              <span class="hidden sm:inline">Submit Product</span>
              <span class="sm:hidden">Submit</span>
            </button>

            <button @click="authStore.logout" class="text-gray-700 hover:text-red-600 text-sm font-medium flex items-center">
              <LogOut class="h-4 w-4 mr-2" />
              <span class="hidden sm:inline">Logout</span>
            </button>
          </div>

          <div v-else class="flex space-x-4">
            <button @click="openModal('login')" class="text-gray-700 hover:text-indigo-600 text-sm flex items-center hover:bg-gray-100 p-2 rounded">
              <User class="h-4 w-4 mr-2" />Login
            </button>

            <button @click="openModal('register')" class="px-3 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white rounded text-sm flex items-center">
              <Upload class="h-4 w-4 mr-2" />Sign Up
            </button>
          </div>
        </div>
      </div>
    </div>

    
    <!-- Mobile Menu Panel -->
<div v-if="isMobileMenuOpen" class="md:hidden border-t border-gray-200">
  <div class="px-4 py-4 space-y-2">
    <RouterLink to="/" class="block text-sm font-medium hover:text-indigo-600">Home</RouterLink>
    <RouterLink to="/gallery" class="block text-sm font-medium hover:text-indigo-600">Gallery</RouterLink>

    <!-- Show Admin only if authenticated and isAdmin -->
    <RouterLink
      v-if="authStore.isAuthenticated && authStore.isAdmin"
      to="/admin-panel"
      class="block text-sm font-medium hover:text-indigo-600"
    >
      Admin
    </RouterLink>

    <div class="pt-2 border-t border-gray-200 space-y-2">
      <div v-if="authStore.isAuthenticated" class="space-y-2">
        <button
          @click="openModal('submit')"
          class="w-full text-left px-3 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded text-sm"
        >
          Submit Product
        </button>
        <button
          @click="authStore.logout"
          class="w-full text-left text-sm text-red-600 hover:bg-gray-100 p-2 rounded"
        >
          Logout
        </button>
      </div>
      <div v-else class="space-y-2">
        <button
          @click="openModal('login')"
          class="w-full text-left text-sm hover:text-indigo-600 p-2 rounded hover:bg-gray-100"
        >
          Login
        </button>
        <button
          @click="openModal('register')"
          class="w-full text-left px-3 py-2 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded text-sm"
        >
          Sign Up
        </button>
      </div>
    </div>
  </div>
</div>

  </nav>

  <!-- Modals -->
  <!-- <ReviewModel v-if="authStore.isAuthenticated" :is-open="showModal" @close="closeModal" /> -->
  <ReviewModel v-if="authStore.isAuthenticated" :isOpen="showModal" mode="product-review" @close="closeModal" />

  <AuthModal v-else :is-open="showModal" :mode="authMode" @close="showModal = false" @mode-change="val => authMode = val" />
</template>
