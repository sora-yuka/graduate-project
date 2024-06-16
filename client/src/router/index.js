import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RegisterView from '@/views/account/RegisterView.vue'
import VerificationView from '@/views/account/VerificationView.vue'
import LoginView from '@/views/account/LoginView.vue'
import CoursesView from '@/views/course/CoursesView.vue'
import DetailedView from '@/views/course/DetailedView.vue'
import AddCourseView from '@/views/course/AddCourseView.vue'
import UpdateCourseView from '@/views/course/UpdateCourseView.vue'
import UpdateCourseItemView from '@/views/course/UpdateCourseItemView.vue'
import SavedCourseView from '@/views/profile/SavedCourseView.vue'
import MyCourseView from '@/views/profile/MyCourseView.vue'


const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
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
    },
    {
        path: '/saved',
        name: 'saved',
        component: SavedCourseView
    },
    {
        path: '/add',
        name: 'add',
        component: AddCourseView
    },
    {
        path: '/my-course',
        name: 'my-course',
        component: MyCourseView
    },
    {
        path: '/edit/:id',
        name: 'edit',
        component: UpdateCourseView
    },
    {
        path: '/course/page/:id',
        name: 'update-item',
        component: UpdateCourseItemView
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
