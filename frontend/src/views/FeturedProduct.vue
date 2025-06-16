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
              :src="product.image"
              :alt="product.name"
              class="w-full h-48 object-cover transition-transform duration-300 group-hover:scale-110"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </div>
          <div class="p-6">
            <h3 class="text-xl font-semibold text-gray-900 mb-2">{{ product.name }}</h3>
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-1">
                <Star
                  v-for="i in 5"
                  :key="i"
                  class="h-4 w-4"
                  :class="i <= Math.floor(product.rating) ? 'text-yellow-400 fill-current' : 'text-gray-300'"
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

// Dummy product array — replace this later with props or API call
const featuredProducts = [
  {
    id: 1,
    name: 'Product One',
    image: 'https://via.placeholder.com/300',
    rating: 4.5,
    reviewCount: 124
  },
  {
    id: 2,
    name: 'Product Two',
    image: 'https://via.placeholder.com/300',
    rating: 4.0,
    reviewCount: 98
  },
  {
    id: 3,
    name: 'Product Three',
    image: 'https://via.placeholder.com/300',
    rating: 5,
    reviewCount: 210
  }
]
</script>
