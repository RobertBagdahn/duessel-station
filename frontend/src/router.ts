import { createRouter, createWebHistory } from 'vue-router'

import AppRouter from '@/modules/app/router'
import SensorDataRouter from '@/modules/sensorData/router'

const routes = [
  ...AppRouter,
  ...SensorDataRouter
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router