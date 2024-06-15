import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/:slug',
      name: 'level',
      component: () => import('../views/LevelView.vue')
    },
    {
      path: '/subject/:subject_slug',
      name: 'subject',
      component: () => import('../views/SubjectDetail.vue')
    },
    {
      path: '/posts',
      name: 'posts',
      component: () => import('../views/PostListView.vue')
    },

  ]
})

export default router
