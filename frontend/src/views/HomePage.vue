<script setup>
import { ref } from 'vue';
import FeturedProduct from './FeturedProduct.vue';
import { RouterLink } from 'vue-router'
import { Search, Upload, Users, Camera, Star } from 'lucide-vue-next'
import ReviewModal from './ReviewModel.vue';
import { useAuthStore } from '@/stores/auth';
import AuthModal from '@/components/AuthModal.vue';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
const auth = useAuthStore();
const route =useRoute()

const isModalOpen = ref(false)

const openModal = () => {
  isModalOpen.value = true
}
const closeModal = () => {
  isModalOpen.value = false
}


const authMode =ref('register')



</script>

<template>
  <section class="relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-r from-indigo-600/10 to-purple-600/10"></div>
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
      <div class="text-center space-y-8">
        <div class="space-y-4">
          <h1 class="text-4xl md:text-6xl font-bold text-gray-900 leading-tight">
            Discover Products Through
            <span class="block bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Real User Reviews
            </span>
          </h1>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Share your experiences, upload photos, and help others make better purchasing decisions.
            Join our community of honest reviewers.
          </p>
        </div>

        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <RouterLink to="/gallery">
            <button class="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white px-8 py-3 text-lg rounded transition-all duration-200 transform hover:scale-105 flex items-center">
              <Search class="h-5 w-5 mr-2" />
              Explore Gallery
            </button>
          </RouterLink>

          <button
          v-if="auth.isAuthenticated"
          @click="openModal"
            class="border border-indigo-200 text-indigo-600 hover:bg-indigo-50 px-8 py-3 text-lg rounded transition-all duration-200 flex items-center"
          >
            <Upload class="h-5 w-5 mr-2" />
            Upload Review
          </button>

          <button
          v-else
          @click="openModal"
            class="border border-indigo-200 text-indigo-600 hover:bg-indigo-50 px-8 py-3 text-lg rounded transition-all duration-200 flex items-center"
          >
            <Upload class="h-5 w-5 mr-2" />
            Upload Review
          </button>
        </div>

        <div class="flex justify-center items-center space-x-8 text-sm text-gray-500">
          <div class="flex items-center">
            <Users class="h-5 w-5 mr-2 text-indigo-500" />
            <span>50K+ Users</span>
          </div>
          <div class="flex items-center">
            <Camera class="h-5 w-5 mr-2 text-purple-500" />
            <span>100K+ Photos</span>
          </div>
          <div class="flex items-center">
            <Star class="h-5 w-5 mr-2 text-yellow-500" />
            <span>25K+ Reviews</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <ReviewModal v-if="auth.isAuthenticated" :is-open="isModalOpen" @close="closeModal" />
  <AuthModal v-else :is-open="isModalOpen"
  :mode="authMode"
  @close="closeModal"
  @mode-change="val => authMode = val"
/>
  <FeturedProduct />

</template>
