import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import VacationPlan from '../components/VacationPlan.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/vacation-plan',
      name: 'vacation-plan',
      component: VacationPlan
    }
  ]
})

export default router
