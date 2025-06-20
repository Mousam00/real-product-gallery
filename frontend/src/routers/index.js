import { createWebHistory, createRouter } from 'vue-router'

import HomePage from '@/views/HomePage.vue'
import Gallery from '@/views/Gallery.vue'
import AdminPanel from '@/views/AdminPanel.vue'
import { useAuthStore } from '@/stores/auth'

const routes = [
  { path: '/', component: HomePage },
  { path: '/gallery', component: Gallery },
  { path: '/admin-panel', component: AdminPanel, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const auths = useAuthStore()
  const path = to.path.replace(/\/$/, ''); //removing the slash from url 
  if (path === '/admin-panel' && !auths.isAdmin) {
    next('/')
  } else {
    next()
  }
})

export default router