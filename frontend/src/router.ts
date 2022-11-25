import { createRouter, createWebHistory } from 'vue-router'

import AppRouter from '@/modules/app/router'
import TemperaturRouter from '@/modules/temperatur/router'

const routes = [
  ...AppRouter,
  ...TemperaturRouter
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})



export default router
