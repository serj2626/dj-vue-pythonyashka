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
      path: '/subjects/:subject_slug',
      name: 'subject',
      component: () => import('../views/SubjectDetail.vue')
    },
    {
      path: '/lessons/:slug',
      name: 'lesson',
      component: () => import('../views/LessonDetail.vue')
    },
    {
      path: '/posts',
      name: 'posts',
      component: () => import('../views/PostListView.vue')
    },
    {
      path: '/tags',
      name: 'tags',
      component: () => import('../views/TagListView.vue')
    },
    {
      path: '/tags/:slug',
      name: 'tag',
      component: () => import('../views/TagDetailView.vue')
    },

  ]
})

export default router
