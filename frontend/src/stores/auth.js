import { defineStore } from "pinia";
import { ref,computed } from "vue";

export const useAuthStore = defineStore('auth', () => {
const token = ref(localStorage.getItem("access_token"))
const isAuthenticated = computed(() => token.value)
const login = (accessToken) => {
    localStorage.setItem("access_token", accessToken)
    token.value = accessToken
}
const logout = () => {
    localStorage.removeItem("access_token")
    localStorage.removeItem("refresh_token")
    token.value = null
}
const setToken = (accessToken, refreshToken) => {
    localStorage.setItem("access_token", accessToken)
    localStorage.setItem("refresh_token", refreshToken)
    token.value = accessToken
}
return {token, isAuthenticated, login, logout, setToken }
})