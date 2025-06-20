import { defineStore } from "pinia";
import { ref,computed } from "vue";

export const useAuthStore = defineStore('auth', () => {
const token = ref(localStorage.getItem("access_token"))
const refreshToken = ref(localStorage.getItem("refresh_token"))
const user = ref(JSON.parse(localStorage.getItem("user")) || null)

const isAuthenticated = computed(() => token.value)
const isAdmin = computed(() => user.value?.isAdmin || false)

const login = (access,refresh,userData) => {
    localStorage.setItem("access_token", access)
    localStorage.setItem("refresh_token", refresh)
    localStorage.setItem("user",JSON.stringify(userData))
    token.value = access;
    refreshToken.value = refresh;
    user.value = userData;
}
const logout = () => {
    localStorage.removeItem("access_token")
    localStorage.removeItem("refresh_token")
    localStorage.removeItem("user")
    token.value = null
    refreshToken.value=null
    user.value =null
}

return {token, isAuthenticated, login, logout, user, isAdmin}
})