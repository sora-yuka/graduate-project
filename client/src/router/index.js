import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import CoursesView from '../views/course/CoursesView.vue'
import RegisterView from '../views/account/RegisterView.vue'


const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
    {
        path: '/all',
        name: 'courses',
        component: CoursesView 
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterView
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
