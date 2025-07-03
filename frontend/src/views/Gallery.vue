<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
          Product
          <span class="block bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
            Gallery
          </span>
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto">
          Discover amazing products through honest reviews from our community
        </p>
      </div>

      <!-- Products Grid -->
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="product in products"
          :key="product.id"
          class="hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 cursor-pointer h-full"
        >
          <div class="p-0 bg-white rounded-lg shadow">
            <!-- Product Image -->
            <div v-if="product" class="aspect-video w-full overflow-hidden rounded-t-lg">
              <img
                :src="getImageUrl(product)"
                :alt="product.title"
                class="w-full h-full object-cover"
              />
            </div>

            <div class="p-6">
              <!-- Product Title -->
              <h3 class="text-xl font-bold text-gray-900 mb-3 line-clamp-2">
                {{ product.title }}
              </h3>

              <!-- Rating -->
              <div class="flex items-center space-x-2 mb-3">
                <div class="flex items-center space-x-1">
                  <svg
                    v-for="star in 5"
                    :key="star"
                    :class="[
                      'h-4 w-4',
                      star <= product.average_rating ? 'text-yellow-400 fill-current' : 'text-gray-300',
                    ]"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path
                      d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.262 3.877a1 1 0 00.95.69h4.073c.969 0 1.371 1.24.588 1.81l-3.296 2.398a1 1 0 00-.364 1.118l1.262 3.877c.3.921-.755 1.688-1.538 1.118L10 13.347l-3.296 2.398c-.783.57-1.838-.197-1.538-1.118l1.262-3.877a1 1 0 00-.364-1.118L2.768 9.304c-.783-.57-.38-1.81.588-1.81h4.073a1 1 0 00.95-.69l1.262-3.877z"
                    />
                  </svg>
                </div>
                <span class="text-sm font-medium text-gray-900">{{product.average_rating}}</span>
                <span class="text-sm text-gray-600">({{product.all_reviews.length}})</span>
              </div>

              <!-- Description -->
              <p class="text-gray-600 text-sm mb-4 line-clamp-3">
                {{product.description}}
              </p>

              <!-- Initial Review Preview -->
              <div class="bg-gray-50 p-3 rounded-lg mb-4">
                <div class="flex items-center space-x-2 mb-2">
                  <span class="text-xs font-medium text-gray-700">{{ product.submited_by }}</span>
                  <span class="text-xs text-blue-600 border-blue-200 border px-2 py-0.5 rounded">
                    Initial Review
                  </span>
                </div>
                <p class="text-xs text-gray-600 line-clamp-2">{{product.initialReview.caption}}</p>
              </div>

              <!-- Metadata -->
              <div class="flex items-center justify-between text-xs text-gray-500">
                <div class="flex items-center space-x-1">
                  <span>{{product.initialReview.created_at}}</span>
                </div>
                <span class="text-green-600 border border-green-200 px-2 py-0.5 rounded">Approved</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import api from '@/axios';
import { onMounted } from 'vue';
import { ref } from 'vue';
// Example static product list — replace later with API or Pinia store
const products = ref([])

const featchProducts = async () => {
  try {
    const response = await api.get('api/gallery/');
    products.value = response.data;
    console.log("kjlj",response.data);
    
  } catch (error) {
    console.error('Error fetching products:', error);
  }
}

const apiBaseURL = import.meta.env.VITE_BACKEND_BASE_URL;

function getImageUrl(product) {
  return product.first_image
    ? apiBaseURL + product.first_image
    : 'https://via.placeholder.com/400x300?text=No+Image'
}
onMounted(() => {
  featchProducts()
})

</script>
