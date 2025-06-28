<template>
  <section class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
          Featured Products
        </h2>
        <p class="text-lg text-gray-600 max-w-2xl mx-auto">
          Discover the most popular products with authentic reviews from our community
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div
          v-for="product in featuredProducts"
          :key="product.id"
          class="group hover:shadow-xl transition-all duration-300 transform hover:-translate-y-2 border-0 shadow-lg bg-white/80 backdrop-blur-sm rounded-lg overflow-hidden"
        >
          <div class="relative overflow-hidden">
            <img
              :src="getImageUrl(product)"
              :alt="product.title"
              class="w-full h-48 object-cover transition-transform duration-300 group-hover:scale-110"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ product.title }}</h3>
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-1">
                <Star
                  v-for="i in 5"
                  :key="i"
                  class="h-4 w-4"
                  :class="i <= Math.floor(product.average_rating) ? 'text-yellow-400 fill-current' : 'text-gray-300'"
                />
                <span class="text-sm text-gray-600 ml-2">
                  {{ product.rating }} ({{ product.reviewCount }} reviews)
                </span>
              </div>
            </div>
            <RouterLink :to="`/product/${product.id}`">
              <button class="w-full mt-4 bg-gradient-to-r from-sky-400 to-indigo-500 hover:from-sky-500 hover:to-indigo-600 text-white px-4 py-2 rounded transition-all duration-200">
                View Details
              </button>
            </RouterLink>
          </div>
        </div>
      </div>

      <div class="text-center mt-12">
        <RouterLink to="/gallery">
          <button class="border border-indigo-200 text-indigo-600 hover:bg-indigo-50 px-8 py-3 text-lg rounded">
            View All Products
          </button>
        </RouterLink>
      </div>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { Star } from 'lucide-vue-next'
import { ref } from 'vue';
import api from '@/axios';
import { onMounted } from 'vue';

// Dummy product array — replace this later with props or API call
const featuredProducts = ref([])

// const MyProducts= []
const handleClick = async (params) => {
  try {
    
  } catch (error) {
    console.log(error);
    
    
  }
}

const fetchProduct = async() =>{

  try {
    const response = await api.get('featured/');
    console.log(response.data);
    
    
    featuredProducts.value = response.data
    // console.log(featuredProducts);
    
  } catch (error) {
    console.log(error);
    
  }
}


const apiBaseURL = 'http://127.0.0.1:8000'

function getImageUrl(product) {
  return product.featured_image
    ? apiBaseURL + product.featured_image
    : 'https://via.placeholder.com/400x300?text=No+Image'
}

onMounted(() => {
  fetchProduct()
})
</script>
