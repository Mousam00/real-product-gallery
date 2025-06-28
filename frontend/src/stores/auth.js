import { defineStore } from "pinia";
import { ref, computed } from "vue";
import axios from "axios";
import router from "@/routers";

export const useAuthStore = defineStore('auth', () => {
  // State
  const token = ref(localStorage.getItem("access_token"));
  const refreshToken = ref(localStorage.getItem("refresh_token"));
  const user = ref(JSON.parse(localStorage.getItem("user") || "null"));
  const isLoading = ref(false);
  const error = ref(null);

  // Getters
  const isAuthenticated = computed(() => !!token.value);
  const isAdmin = computed(() => user.value?.is_staff || false);

  // Actions
  const login = (access, refresh, userData) => {
    localStorage.setItem("access_token", access);
    localStorage.setItem("refresh_token", refresh);
    localStorage.setItem("user", JSON.stringify(userData));
    token.value = access;
    refreshToken.value = refresh;
    user.value = userData;
    setAxiosAuthHeader(access);
  };

  // New action: login using Google OAuth code
  const loginWithGoogleCode = async (code) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await axios.get('http://localhost:8000/auth/google/login/callback/', {
        params: { code }
      });
      
      const data = response.data;
      
      login(data.access, data.refresh, data.user); // store tokens and user
      
      isLoading.value = false;
      router.push('/'); // redirect to home or wherever
      return true;
    } catch (err) {
      console.error("Google login failed:", err);
      error.value = err.response?.data?.detail || "Login failed";
      isLoading.value = false;
      return false;
    }
  };

  const logout = () => {
    clearAuthData();
    router.push('/');
  };

  const clearAuthData = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user");
    token.value = null;
    refreshToken.value = null;
    user.value = null;
    delete axios.defaults.headers.common['Authorization'];
  };

  const setAxiosAuthHeader = (token) => {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  };

  const fetchCurrentUser = async () => {
    if (!token.value) {
      clearAuthData();
      return null;
    }

    try {
      const response = await axios.get('http://127.0.0.1:8000/api/accounts/user/');
      user.value = response.data;
      localStorage.setItem("user", JSON.stringify(response.data));
      return response.data;
    } catch (err) {
      if (err.response?.status === 401) {
        // Token expired, try to refresh
        return await refreshTokenAndRetry();
      }
      clearAuthData();
      return null;
    }
  };

  const refreshTokenAndRetry = async () => {
    if (!refreshToken.value) {
      clearAuthData();
      return null;
    }

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {
        refresh: refreshToken.value
      });
      
      token.value = response.data.access;
      localStorage.setItem("access_token", response.data.access);
      setAxiosAuthHeader(response.data.access);
      
      // Retry fetching user
      const userResponse = await axios.get('http://127.0.0.1:8000/api/accounts/user/');
      user.value = userResponse.data;
      localStorage.setItem("user", JSON.stringify(userResponse.data));
      return userResponse.data;
    } catch (err) {
      clearAuthData();
      return null;
    }
  };

  // Initialize axios header if token exists
  if (token.value) {
    setAxiosAuthHeader(token.value);
  }

  return {
    token,
    refreshToken,
    user,
    isLoading,
    error,
    isAuthenticated,
    isAdmin,
    login,
    loginWithGoogleCode,   // expose new action
    logout,
    fetchCurrentUser,
    refreshTokenAndRetry
  };
});
