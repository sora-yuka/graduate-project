import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import ToastPlugin from 'vue-toast-notification'

import 'vue-toast-notification/dist/theme-sugar.css'

import setupInterceptors from './service/authHeader'


axios.defaults.baseURL = 'http://127.0.0.1:8000'
setupInterceptors(store)

const app = createApp(App)

app.use(store)
app.use(router)
app.use(ToastPlugin)

app.config.globalProperties.$axios = axios

app.mount('#app')