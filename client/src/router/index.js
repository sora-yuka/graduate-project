import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import RegisterView from '../views/account/RegisterView.vue'
import VerificationView from '../views/account/VerificationView.vue'
import LoginView from '../views/account/LoginView.vue'
import CoursesView from '../views/course/CoursesView.vue'
import DetailedView from '../views/course/DetailedView.vue'


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
    },
    {
        path: '/verify/:verificationCode',
        name: 'verify',
        component: VerificationView
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },
    {
        path: '/course/:id',
        name: 'detailed',
        component: DetailedView
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

router.beforeEach((to, from, next) => {
    window.scrollTo(0, 0)
    next()
})

export default router
