<template>
    <div class=" max-w-6xl m-auto rounded-lg px-16 py-6 mt-8">
  <div class="space-y-6">
    <div class="text-center mb-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-2">Admin Panel</h1>
      <p class="text-gray-600">Review and approve product submissions</p>
    </div>

    <div v-if="!auth.isAdmin" class="text-center py-12">
      <p class="text-gray-500">Access denied. Admin privileges required.</p>
    </div>

    <div v-else>
      <div v-if="pendingProducts.length === 0">
        <div class="border p-8 rounded text-center">
          <svg class="h-12 w-12 text-green-500 mx-auto mb-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M16.707 5.293a1 1 0 00-1.414 0L8 12.586 4.707 9.293a1 1 0 10-1.414 1.414l4 4a1 1 0 001.414 0l8-8a1 1 0 000-1.414z"/>
          </svg>
          <h3 class="text-lg font-semibold text-gray-900 mb-2">All caught up!</h3>
          <p class="text-gray-600">No pending product submissions to review.</p>
        </div>
      </div>

      <div v-else class="space-y-6">
        <div class="flex items-center space-x-2">
          <svg class="h-5 w-5 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <h2 class="text-xl font-semibold text-gray-900">
            Pending Submissions ({{ pendingProducts.length }})
          </h2>
        </div>

        <div v-for="product in pendingProducts" :key="product.id" class="border border-amber-500 p-6 rounded-md">
          <div class="flex justify-between mb-4">
            <div>
              <h3 class="text-lg font-semibold text-gray-900">{{ product.title }}</h3>
              <div class="text-sm text-gray-600 flex space-x-4 mt-2">
                <span>Submitted by: {{ product.submited_by }}</span>
                <span>{{ product.submittedAt }}</span>
              </div>
              <span class="text-xs text-orange-600 border border-orange-200 px-2 py-0.5 rounded mt-2 inline-block">
                Pending Approval
              </span>
            </div>
          </div>

          <div class="space-y-2">
            <h4 class="font-medium text-gray-900">Product Description:</h4>
            <p class="text-gray-600">{{ product.description || 'No description provided' }}</p>
            <div v-if="product.url" class="flex items-center space-x-2">
              <a :href="product.url" target="_blank" class="text-indigo-600 hover:underline">Product URL</a>
            </div>
          </div>

          <div v-if="product.initialReview" class="bg-gray-50 p-4 rounded-lg mt-4">
            <h4 class="font-medium text-gray-900 mb-2">Initial Review:</h4>
            <div class="flex items-center space-x-1 mb-2">
              <span v-for="star in 5" :key="star" :class="['h-4 w-4', star <= product.initialReview.rating ? 'text-yellow-400' : 'text-gray-300']">
                ★
              </span>
              <span class="text-sm text-gray-600">{{ product.initialReview.rating }} stars</span>
            </div>
            <p class="text-gray-700">{{ product.initialReview.caption }}</p>

            <div v-if="product.initialReview.images.length" class="grid grid-cols-4 gap-2 mt-3">
              <img v-for="(image, index) in product.initialReview.images" :key="index" :src="image" class="w-full h-16 object-cover rounded" />
            </div>
          </div>

          <div class="flex space-x-3 pt-4 border-t mt-4">
            <button @click="handleClick(product.id,'approved')" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded flex items-center">
              ✅ Approve Product
            </button>
            <button @click="handleClick(product.id,'rejected')" class="border border-red-200 text-red-600 px-4 py-2 rounded hover:bg-red-50">
              Reject
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
import api from '@/axios'
import { onMounted } from 'vue'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
// Mock data and props for now
console.log(auth.isAdmin);

const pendingProducts = ref([])

const handleClick = async (id, status) => {
  try {
    if(status === 'approved') {
    const response = await api.post(`api/admin/${id}/approve/`)
    featchProducts()
    console.log(response.data)
    } else if(status === 'rejected') {
      const response = await api.post(`api/admin/${id}/reject/`)
      console.log(response.data)
      featchProducts()
    } else {
      console.log('Invalid status');
      return;
    }
  } catch (error) {
    console.log(error);
  }
}
const featchProducts = async () => {
  try {
    const response = await api.get('api/admin/')
    pendingProducts.value = response.data
    console.log(response.data)
  } catch (error) {
    console.log(error);
    
  }
}
const apiBaseURL = import.meta.env.VITE_BACKEND_BASE_URL;

function getImageUrl(product) {
  return product
    ? apiBaseURL + product
    : 'https://via.placeholder.com/400x300?text=No+Image'
}
onMounted(() => {
  featchProducts()
})
</script>
