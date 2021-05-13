import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Panel from '../views/Panel.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/panel',
    name: 'Panel',
    component: Panel
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
