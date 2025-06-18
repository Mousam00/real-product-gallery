<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center">
    
    <div class="bg-white w-full max-w-md rounded-lg shadow-lg p-6 space-y-6 relative">
      <h2 class="text-2xl font-bold text-center text-gray-900">
        {{ mode === 'login' ? 'Welcome Back' : 'Create Account' }}
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label class="block mb-1 text-sm font-medium text-gray-700">Email</label>
          <input
            v-model="formData.email"
            type="email"
            required
            placeholder="Enter your email"
            class="w-full border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <div v-if="mode === 'register'">
          <label class="block mb-1 text-sm font-medium text-gray-700">Username</label>
          <input
            v-model="formData.username"
            type="text"
            required
            placeholder="Choose a username"
            class="w-full border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <div>
          <label class="block mb-1 text-sm font-medium text-gray-700">Password</label>
          <div class="relative">
            <input
              v-model="formData.password"
              :type="showPassword ? 'text' : 'password'"
              required
              placeholder="Enter your password"
              class="w-full border border-gray-300 rounded px-3 py-2 pr-10 focus:ring-2 focus:ring-indigo-500"
            />
            <button type="button" @click="showPassword = !showPassword" class="absolute right-2 top-2 text-sm text-gray-500">
              {{ showPassword ? 'Hide' : 'Show' }}
            </button>
          </div>
        </div>

        <div v-if="mode === 'register'">
          <label class="block mb-1 text-sm font-medium text-gray-700">Confirm Password</label>
          <input
            v-model="formData.confirmPassword"
            type="password"
            required
            placeholder="Confirm your password"
            class="w-full border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <div v-if="mode === 'register'" class="flex items-center space-x-2">
          <input v-model="formData.agreeToTerms" type="checkbox" id="terms" />
          <label for="terms" class="text-sm text-gray-600">I agree to the Terms & Conditions</label>
        </div>

        <button
          type="submit"
          :disabled="isLoading"
          class="w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-700 transition"
        >
          {{ isLoading ? 'Processing...' : (mode === 'login' ? 'Sign In' : 'Create Account') }}
        </button>
      </form>

      <div class="text-center text-sm text-gray-600">
        <button @click="switchMode" class="text-indigo-600 hover:underline">
          {{ mode === 'login' ? "Don't have an account? Sign up" : 'Already have an account? Sign in' }}
        </button>
      </div>

      <button @click="closeModal" class="absolute top-3 right-3 text-gray-500 hover:text-gray-800 text-xl">&times;</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  isOpen: Boolean,
  mode: {
    type: String,
    default: 'login',
  },
})

const emit = defineEmits(['close', 'mode-change'])

const formData = ref({
  email: '',
  username: '',
  password: '',
  confirmPassword: '',
  agreeToTerms: false,
})

const showPassword = ref(false)
const isLoading = ref(false)

import { useAuthStore } from '@/stores/auth.js'
import axios from 'axios'

const handleSubmit = async () => {
  isLoading.value = true

  if (props.mode === 'register') {
    if (formData.value.password !== formData.value.confirmPassword) {
      alert('Passwords do not match')
      isLoading.value = false
      return
    }
    if (!formData.value.agreeToTerms) {
      alert('Please agree to the Terms & Conditions.')
      isLoading.value = false
      return
    }
    // Registration logic placeholder
    alert(`Registered with email: ${formData.value.email}`)
    resetForm()
    isLoading.value = false
    emit('close')
    return
  }

  // LOGIN LOGIC
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/',formData.value)
    useAuthStore().setToken(response.data.access,response.data.refresh)
    console.log(response);
    
    
  } catch (err) {
    alert(err.message)
  } finally {
    isLoading.value = false
  }
}

const switchMode = () => {
  emit('mode-change', props.mode === 'login' ? 'register' : 'login')
  resetForm()
}

const resetForm = () => {
  formData.value = {
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
    agreeToTerms: false,
  }
}

const closeModal = () => {
  emit('close')
}
</script>

<style scoped>
input[type='checkbox'] {
  width: 16px;
  height: 16px;
}
</style>