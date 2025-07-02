<template>
  <div v-if="isOpen" class="fixed inset-0 bg-black/50 z-50 flex items-center justify-center">

    <div class="bg-white w-full max-w-md rounded-lg shadow-lg p-6 space-y-6 relative">
      <h2 class="text-2xl font-bold text-center text-gray-900">
        {{ mode === 'login' ? 'Welcome Back' : 'Create Account' }}
      </h2>

      <!-- Error Message -->
      <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded relative text-sm">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div>
          <label class="block mb-1 text-sm font-medium text-gray-700">Email</label>
          <input v-model="formData.email" type="email" required placeholder="Enter your email"
            class="w-full border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-indigo-500" />
        </div>

        <div v-if="mode === 'register'">
          <label class="block mb-1 text-sm font-medium text-gray-700">Username</label>
          <input v-model="formData.username" type="text" required placeholder="Choose a username"
            class="w-full border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-indigo-500" />
        </div>

        <div>
          <label class="block mb-1 text-sm font-medium text-gray-700">Password</label>
          <div class="relative">
            <input v-model="formData.password" :type="showPassword ? 'text' : 'password'" required
              placeholder="Enter your password"
              class="w-full border border-gray-300 rounded px-3 py-2 pr-10 focus:ring-2 focus:ring-indigo-500" />
            <button type="button" @click="showPassword = !showPassword"
              class="absolute right-2 top-2 text-sm text-gray-500">
              {{ showPassword ? 'Hide' : 'Show' }}
            </button>
          </div>
        </div>

        <div v-if="mode === 'register'">
          <label class="block mb-1 text-sm font-medium text-gray-700">Confirm Password</label>
          <input v-model="formData.confirmPassword" type="password" required placeholder="Confirm your password"
            class="w-full border border-gray-300 rounded px-3 py-2 focus:ring-2 focus:ring-indigo-500" />
        </div>

        <div v-if="mode === 'register'" class="flex items-center space-x-2">
          <input v-model="formData.agreeToTerms" type="checkbox" id="terms" />
          <label for="terms" class="text-sm text-gray-600">I agree to the Terms & Conditions</label>
        </div>

        <button type="submit" :disabled="isLoading"
          class="w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-700 transition">
          {{ isLoading ? 'Processing...' : (mode === 'login' ? 'Sign In' : 'Create Account') }}
        </button>
        <p class="text-center">or</p>
        <!-- Google Login Button -->
        <button type="button" @click="loginWithGoogle"
          class="w-full flex items-center justify-center border border-gray-300 py-2 rounded hover:bg-gray-50 transition mt-2">
          <img src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="Google"
            class="w-5 h-5 mr-2" />
          <span>Continue with Google</span>
        </button>

      </form>

      <div class="text-center text-sm text-gray-600">
        <button @click="switchMode" class="text-indigo-600 hover:underline">
          {{ mode === 'login' ? "Don't have an account? Sign up" : 'Already have an account? Sign in' }}
        </button>
      </div>

      <button @click="closeModal"
        class="absolute top-3 right-3 text-gray-500 hover:text-gray-800 text-xl">&times;</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
import axios from 'axios'

const auth = useAuthStore()

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

const errorMessage = ref('')
const showPassword = ref(false)
const isLoading = ref(false)

const handleSubmit = async () => {
  isLoading.value = true
  errorMessage.value = ''  // clear previous error

  if (props.mode === 'register') {
    if (formData.value.password !== formData.value.confirmPassword) {
      errorMessage.value = 'Passwords do not match'
      isLoading.value = false
      return
    }
    if (!formData.value.agreeToTerms) {
      errorMessage.value = 'Please agree to the Terms & Conditions.'
      isLoading.value = false
      return
    }

    try {
      await axios.post('http://127.0.0.1:8000/api/auth/users/', {
        email: formData.value.email,
        username: formData.value.username,
        password: formData.value.password,
        confirm_password: formData.value.confirmPassword,
        accepted_terms: formData.value.agreeToTerms
      })

      errorMessage.value = 'Account created successfully! You can now log in.'
      emit('mode-change', 'login')
      resetForm()

    } catch (err) {
      if (err.response && err.response.data) {
        errorMessage.value = formatErrorResponse(err.response.data)
      } else {
        errorMessage.value = err.message
      }
    } finally {
      isLoading.value = false
    }
    return
  }

  // LOGIN logic
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', formData.value)
    const { access, refresh, user } = response.data
    auth.login(access, refresh, user)
    emit('close')

  } catch (err) {
    if (err.response && err.response.data) {
      errorMessage.value = formatErrorResponse(err.response.data)
    } else {
      errorMessage.value = err.message
    }
  } finally {
    isLoading.value = false
  }
}

const loginWithGoogle = () => {
  window.location.href = 'http://localhost:8000/auth/account/google/login/'
}

const formatErrorResponse = (data) => {
  if (typeof data === 'string') return data
  if (typeof data === 'object') {
    return Object.entries(data)
      .map(([key, val]) => `${key}: ${Array.isArray(val) ? val.join(' ') : val}`)
      .join('\n')
  }
  return 'An unknown error occurred.'
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
  errorMessage.value = ''
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
