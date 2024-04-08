import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovieFormView from '../views/AddMovieFormView.vue';
import MoviesView from '../views/MoviesView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/movies',
      name: 'Movies',
      component: MoviesView
    }
    ,
  {
    path: '/movies/create', // Define the route for adding a movie
    name: 'AddMovie',
    component: AddMovieFormView
  }
  ]
})

export default router
