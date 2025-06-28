import { createWebHistory, createRouter } from 'vue-router'

import HomePage from '@/views/HomePage.vue'
import Gallery from '@/views/Gallery.vue'
import AdminPanel from '@/views/AdminPanel.vue'
import ProductDetail from '@/views/ProductDetail.vue'
import Guidelines from '@/views/legal/Guidelines.vue'
import privacypolicy from '@/views/legal/Privacypolicy.vue'
import TermsOfService from '@/views/legal/TermsOfService.vue'
import Dmca from '@/views/legal/Dmca.vue'
import GoogleCallback from '@/views/GoogleCallback.vue'  // 👈 import your callback component
import { useAuthStore } from '@/stores/auth'

const routes = [
  { path: '/', component: HomePage },
  { path: '/gallery', component: Gallery },
  { path: '/product/:id', component: ProductDetail },
  { path: '/admin-panel', component: AdminPanel, meta: { requiresAuth: true } },
  { path: '/legal/guidelines', component: Guidelines },
  { path: '/legal/privacy', component: privacypolicy },
  { path: '/legal/terms', component: TermsOfService },
  { path: '/legal/dmca', component: Dmca },
  
  // 👇 Google OAuth callback route
  { path: '/auth/google/callback', component: GoogleCallback },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auths = useAuthStore()
  const path = to.path.replace(/\/$/, '')  // Normalize trailing slash

  if (path === '/admin-panel' && !auths.isAdmin) {
    next('/')
  } else {
    next()
  }
})

export default router
