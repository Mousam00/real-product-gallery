<script setup>
import { ref, defineProps, defineEmits } from 'vue'
import { Star, Upload, X, Camera } from 'lucide-vue-next'
import api from '@/axios'

const props = defineProps({
  isOpen: Boolean
})
const emit = defineEmits(['close', 'submit'])

const productTitle = ref('')
const productUrl = ref('')
const productDescription = ref('')
const reviewCaption = ref('')
const rating = ref(0)
const images = ref([])
const isSubmitting = ref(false)

const imageInput = ref(null)

const handleImageUpload = (e) => {
  const files = e.target.files;
  if (files) {
    Array.from(files).forEach(f => {
      images.value.push({
        file: f,
        preview: URL.createObjectURL(f)
      });
    });
  }
}

const removeImage = (index) => {
  images.value.splice(index, 1)
}

const resetForm = () => {
  productTitle.value = ''
  productUrl.value = ''
  productDescription.value = ''
  reviewCaption.value = ''
  rating.value = 0
  images.value = []
  isSubmitting.value = false
}

const handleClose = () => {
  resetForm()
  emit('close')
}

const handleSubmit = async () => {
  if (!productTitle.value || !reviewCaption.value || rating.value === 0) {
    alert('Please fill all required fields and rating')
    return
  }

  const formData = new FormData();
  formData.append('product_title', productTitle.value);
  formData.append('product_url', productUrl.value);
  formData.append('product_description', productDescription.value);
  formData.append('caption', reviewCaption.value);
  formData.append('rating', rating.value);

  images.value.forEach(imgObj => {
    formData.append('uploaded_images', imgObj.file);
  });

  try {
    const response = await api.post('review/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    console.log(response.data);
  } catch (error) {
    console.log(error);
  }

  isSubmitting.value = true
  await new Promise(resolve => setTimeout(resolve, 1500))

  emit('submit', {
    product: {
      title: productTitle.value,
      url: productUrl.value,
      description: productDescription.value
    },
    review: {
      caption: reviewCaption.value,
      rating: rating.value,
      images: images.value
    }
  })

  isSubmitting.value = false
  handleClose()
}
</script>


<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 bg-black/50 flex items-center justify-center">
    <div class="bg-white rounded-lg shadow-lg p-6 w-full max-w-2xl overflow-y-auto max-h-[90vh] relative">
      <button @click="handleClose"
        class="absolute top-3 right-3 text-gray-500 text-2xl hover:text-gray-800">&times;</button>

      <h2
        class="text-2xl font-bold text-center mb-1 bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
        Submit Product & Review</h2>
      <p class="text-gray-600 text-center mb-4">Add a product with your review for approval</p>

      <!-- Product Info -->
      <div class="space-y-4 p-4 bg-gray-50 rounded-lg mb-6">
        <h3 class="font-semibold text-gray-900">Product Information</h3>
        <label for="product-title" class="block mb-2 font-medium text-gray-700">Product Title *</label>
        <input v-model="productTitle" id="product-title" placeholder="Product Title *"
          class="w-full border border-gray-300 bg-white rounded-md p-2" />
        <label for="product-url" class="block mb-2 font-medium text-gray-700">Product URL *</label>
        <input v-model="productUrl" type="url" placeholder="https://example.com/product/"
          class="w-full border  border-gray-300 bg-white rounded-md p-2" />
        <label for="product-description" class="block mb-2 font-medium text-gray-700">Product Description *</label>
        <textarea v-model="productDescription" id="product-description" rows="3" placeholder="Product Description"
          class="w-full border border-gray-300 bg-white rounded-md p-2"></textarea>
      </div>

      <!-- Review Info -->
      <div class="space-y-4 p-4 bg-indigo-50 rounded-lg">
        <h3 class="font-semibold text-gray-900">Your Review</h3>

        <!-- Rating -->
        <h3>Rating *</h3>
        <div class="flex items-center space-x-1">
          <button v-for="star in 5" :key="star" type="button" @click="rating = star">
            <Star :class="['w-7 h-7 transition', star <= rating ? 'text-yellow-400 fill-current' : 'text-gray-300']" />
          </button>
          <span v-if="rating" class="ml-2 text-sm text-gray-600">{{ rating }} star{{ rating !== 1 ? 's' : '' }}</span>
        </div>

        <!-- Caption -->
        <h3>Review Caption *</h3>
        <textarea v-model="reviewCaption" rows="4" placeholder="Your review caption *"
          class="w-full border border-gray-300 bg-white rounded-md p-2"></textarea>

        <!-- Image Upload -->
        <div>
          <label for="image-upload" class="block mb-2 font-medium text-gray-700">Review Images</label>
          <div
            class="flex flex-col items-center justify-center w-full h-32 border-2 border-indigo-300 border-dashed rounded-lg cursor-pointer bg-indigo-50 hover:bg-indigo-100 transition"
            @click="imageInput && imageInput.click()">
            <Camera class="w-8 h-8 text-indigo-500" />
            <p class="text-sm text-indigo-600">Click to upload or drag & drop</p>
            <input id="image-upload" type="file" multiple accept="image/*" class="hidden" @change="handleImageUpload"
              ref="imageInput" />
          </div>

          <div v-if="images.length" class="grid grid-cols-3 gap-3 mt-3">
            <div v-for="(img, i) in images" :key="i" class="relative group">
              <img :src="img.preview" class="w-full h-24 object-cover rounded-lg" />
              <button @click="removeImage(i)"
                class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full p-1 opacity-0 group-hover:opacity-100 transition-opacity">
                <X class="h-4 w-4" />
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Actions -->
      <div class="flex space-x-3 pt-6">
        <button @click="handleClose" :disabled="isSubmitting"
          class="flex-1 border border-gray-300 text-gray-700 py-2 rounded hover:bg-gray-50">Cancel</button>
        <button @click="handleSubmit" :disabled="isSubmitting"
          class="flex-1 bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-2 rounded flex justify-center items-center hover:scale-105 transition">
          <span v-if="isSubmitting" class="animate-spin h-4 w-4 border-b-2 border-white rounded-full mr-2"></span>
          <Upload class="h-4 w-4 mr-2" />
          {{ isSubmitting ? 'Submitting...' : 'Submit' }}
        </button>
      </div>

      <div class="text-sm text-gray-500 bg-yellow-50 p-3 rounded-lg mt-4">
        <strong>Note:</strong> Product submissions require admin approval before public listing.
      </div>
    </div>
  </div>
</template>