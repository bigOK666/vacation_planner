import { createRouter, createWebHistory } from 'vue-router'
import VacationPlan from '../components/VacationPlan.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/vacation-plan',
      name: 'vacation-plan',
      component: VacationPlan
    }
  ]
})

export default router
