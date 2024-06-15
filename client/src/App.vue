<template>
    <div class="app">
        <nav class="nav">
        <div class="container">
            <router-link to="/"><span class="home-button">KnowledgeHub</span></router-link>
            <ul class="nav-bar" v-if="this.$route.path !== '/register' && this.$route.path !== '/login'">
                <ul class="sign-in" v-if="!isAuthenticated">
                    <li class="sign-in__item">
                        <router-link to="/login" class="sign-in__button">Log In</router-link>
                    </li>
                    <li class="sign-in__item">
                        <router-link to="/register" class="sign-in__button">Register</router-link>
                    </li>
                </ul>
                <ul class="control" v-else>
                    <ul class="user-func">
                        <li class="user-func__item">
                            <router-link to="/my-course" class="user-func__button">My courses</router-link>
                        </li>
                        <li class="user-func__item">
                            <router-link to="/add" class="user-func__button">Add course</router-link>
                        </li>
                        <li class="user-func__item">
                            <router-link to="/saved" class="user-func__button">Saved</router-link>
                        </li>
                    </ul>
                    <li class="control__item">
                        <router-link to="/" class="control__button" @click="logout">Log Out</router-link>
                    </li>
                </ul>
            </ul>
        </div>
        </nav>
        <section class="content">
            <router-view/>
        </section>
        <footer class="footer">
            <div class="container">
                <ul class="footer-links">
                    <li class="footer-links__item">
                        <a href="https://github.com/sora-yuka/graduate-project" target="_blank">
                            <img src="./components/source/social-links/github.png" alt="github.png">
                        </a>
                    </li>
                    <li class="footer-links__item">
                        <a href="#!" target="_blank">
                            <img src="./components/source/social-links/instagram.png" alt="instagram.png">
                        </a>
                    </li>
                    <li class="footer-links__item">
                        <a href="#!" target="_blank">
                            <img src="./components/source/social-links/linkedin.png" alt="linked-in.png">
                        </a>
                    </li>
                    <li class="footer-links__item">
                        <a href="#!" target="_blank">
                            <img src="./components/source/social-links/vk.png" alt="vk.png">
                        </a>
                    </li>
                </ul>
                <p class="policy">@2024. Дипломный проект Сабыркулов Н.Н.</p>
            </div>
        </footer>
    </div>
</template>

<style>
@import "./components/css/main.css";
</style>

<script>
import { mapGetters } from 'vuex'
import { useToast } from 'vue-toast-notification'

export default {
    mounted() {
        this.$toast = useToast()
    },
    computed: {
        ...mapGetters({
            isAuthenticated: "isAuthenticated"
        })
    },
    methods: {
        logout() {
            this.$store.dispatch("logout")
            this.$toast.open({
                message: "You've successfully logged out.", type: "success", duration: 2000
            })
        }
    }
}
</script>