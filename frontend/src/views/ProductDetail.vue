<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">

    <!-- Error Message -->
    <div v-if="errorMessage" class="max-w-4xl mx-auto px-4 py-4 text-center text-red-600">
      {{ errorMessage }}
    </div>

    <!-- Product Not Found -->
    <div v-else-if="!product" class="max-w-4xl mx-auto px-4 py-16 text-center">
      <h1 class="text-2xl font-bold text-gray-900 mb-4">Product Not Found</h1>
      <p class="text-gray-600">The product you're looking for doesn't exist or hasn't been approved yet.</p>
    </div>

    <!-- Product Header -->
    <div v-else class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="bg-white rounded-2xl shadow p-8 mb-8">
        <div class="flex items-start justify-between mb-6">
          <div class="flex-1">
            <h1 class="text-3xl font-bold text-gray-900 mb-4" v-html="sanitize(product.title)"></h1>

            <div class="flex items-center space-x-6 mb-4">
              <div class="flex items-center space-x-2">
                <div class="flex items-center space-x-1">
                  <Star v-for="n in product.initialReview.rating" :key="n"
                    class="h-4 w-4 text-yellow-400 fill-current" />
                  <Star v-for="n in (5 - product.initialReview.rating)" :key="`empty-${n}`"
                    class="h-4 w-4 text-gray-300" />

                </div>
                <span class="text-lg font-medium text-gray-900">{{product.average_rating}}</span>
                <span class="text-gray-600">(1 review)</span>
              </div>

              <span class="border border-green-200 text-green-600 rounded px-2 py-1 text-sm">Approved Product</span>
            </div>

            <p class="text-gray-700 mb-6" v-html="sanitize(product.description)"></p>

            <div class="flex items-center space-x-2 mb-6">
              <ExternalLink class="h-5 w-5 text-indigo-600" />
              <a :href="product.url" target="_blank" rel="noopener noreferrer"
                class="text-indigo-600 hover:text-indigo-800 underline font-medium">View Product Page</a>
            </div>
          </div>

          <button
          @click="openModal()"
            class="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white px-4 py-2 rounded-lg font-medium flex items-center">
            <Plus class="h-4 w-4 mr-2" /> Add Review
          </button>
        </div>
      </div>

      <!-- Reviews Section -->
      <div class="space-y-6">
        <div class="flex items-center justify-between">
          <h2 class="text-2xl font-bold text-gray-900">Reviews</h2>
        </div>

        <div v-if="!product.initialReview" class="bg-white rounded-2xl shadow p-8 text-center">
          <Star class="h-12 w-12 text-gray-300 mx-auto mb-4" />
          <h3 class="text-lg font-semibold text-gray-900 mb-2">No reviews yet</h3>
          <p class="text-gray-600 mb-4">Be the first to share your experience with this product!</p>
          <button
            class="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white px-4 py-2 rounded-lg font-medium">
            Write First Review
          </button>
        </div>

        <div v-else class="bg-white rounded-2xl shadow p-6">
          <div class="flex items-start space-x-4">
            <div class="flex-1">
              <div class="flex items-center space-x-3 mb-3">
                <div class="flex items-center space-x-1">
                  <User class="h-4 w-4 text-gray-500" />
                  <span class="font-medium text-gray-900">{{ product.initialReview.user }}</span>
                </div>

                <div class="flex items-center space-x-1">
                  <Star v-for="n in product.initialReview.rating" :key="n"
                    class="h-4 w-4 text-yellow-400 fill-current" />
                  <Star v-for="n in (5 - product.initialReview.rating)" :key="`empty-${n}`"
                    class="h-4 w-4 text-gray-300" />
                </div>

                <div class="flex items-center space-x-1 text-sm text-gray-500">
                  <Calendar class="h-4 w-4" />
                  <span>{{ product.initialReview.created_at }}</span>
                </div>

                <span class="border border-blue-200 text-blue-600 text-xs rounded px-2 py-1">Initial Review</span>
              </div>

              <p class="text-gray-700 mb-4" v-html="sanitize(product.initialReview.caption)"></p>

              <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
                <img v-for="(img, i) in product.initialReview.images" :key="i" :src="img"
                  alt="Review image"
                  class="w-full h-24 object-cover rounded-lg hover:scale-105 transition-transform cursor-pointer"
                  @error="event => event.target.src = 'https://via.placeholder.com/400x300?text=No+Image'" />
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
  <ReviewModel :isOpen="showModal"  mode="only-review" :productId="selectedProductId" @close="closeModal" />

</template>

<script setup>
import api from '@/axios'
import { useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { Star, ExternalLink, User, Calendar, Plus, FastForward } from 'lucide-vue-next';
import DOMPurify from 'dompurify'
import ReviewModel from './ReviewModel.vue';

const route = useRoute();
const product = ref(null)
const errorMessage = ref('');

const showModal = ref(false)

const openModal = (mode) => {

  showModal.value = true
}
const closeModal = () => {
  showModal.value = false
}
const selectedProductId = ref(parseInt(route.params.id))

function sanitize(html) {
  return DOMPurify.sanitize(html)
}

const fetchDetails = async () => {
  try {
    const id = route.params.id
    const response = await api.get(`api/products/${id}`);
    console.log(response.data);
    
    product.value = response.data;
  } catch (error) {
    errorMessage.value = 'Failed to load product details. Please try again later.';
  }
}



onMounted(() => {
  fetchDetails()
})
</script>