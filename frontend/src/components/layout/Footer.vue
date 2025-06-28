<template>
  <footer class="bg-gray-900 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        
        <!-- Brand -->
        <div class="md:col-span-1">
          <div class="flex items-center space-x-2 mb-4">
            <Heart class="h-8 w-8 text-indigo-400" />
            <span class="text-xl font-bold">ReviewGallery</span>
          </div>
          <p class="text-gray-400 text-sm">
            Discover amazing products through honest reviews from our community.
          </p>
        </div>

        <!-- Quick Links -->
        <div>
          <h3 class="font-semibold mb-4">Quick Links</h3>
          <ul class="space-y-2 text-sm">
            <li>
              <RouterLink to="/" class="text-gray-400 hover:text-white transition-colors">
                Home
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/gallery" class="text-gray-400 hover:text-white transition-colors">
                Gallery
              </RouterLink>
            </li>
          </ul>
        </div>

        <!-- Legal -->
        <div>
          <h3 class="font-semibold mb-4">Legal</h3>
          <ul class="space-y-2 text-sm">
            <li>
              <RouterLink to="/legal/terms" class="text-gray-400 hover:text-white transition-colors">
                Terms of Service
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/legal/privacy" class="text-gray-400 hover:text-white transition-colors">
                Privacy Policy
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/legal/guidelines" class="text-gray-400 hover:text-white transition-colors">
                Comment Guidelines
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/legal/dmca" class="text-gray-400 hover:text-white transition-colors">
                DMCA Policy
              </RouterLink>
            </li>
          </ul>
        </div>

        <!-- Contact -->
        <div>
          <h3 class="font-semibold mb-4">Contact</h3>
          <ul class="space-y-2 text-sm text-gray-400">
            <li>support@reviewgallery.com</li>
            <li>privacy@reviewgallery.com</li>
            <li>dmca@reviewgallery.com</li>
          </ul>
        </div>

      </div>

      <div class="border-t border-gray-800 mt-8 pt-8 text-center text-sm text-gray-400">
        <p>&copy; 2025 ReviewGallery. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { Heart } from 'lucide-vue-next'
</script>
