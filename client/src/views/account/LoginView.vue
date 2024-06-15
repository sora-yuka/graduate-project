<template>
    <section class="login-section">
        <div class="container">
            <div class="photo"></div>
            <form action="" @submit.prevent="submitForm" class="login-form">
                <ul class="form-list">
                    <li class="form-list__item">
                        <input type="text" v-model="email"><br>
                        <label for="email">Email</label>
                    </li>
                    <li class="form-list__item">
                        <input type="password" v-model="password"><br>
                        <label for="password">Password</label>
                    </li>
                </ul>
                <div class="form-button">
                    <button type="submit" class="confirm">confirm</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import AuthService from '@/service/authService'
import { useToast } from 'vue-toast-notification'

export default {
    name: "LoginView",
    data() {
        return {
            email: "",
            password: ""
        }
    },
    mounted() {
        this.$toast = useToast()
        document.title = "K.Hub | sign in"
    },
    methods: {
        submitForm() {
            const formData = {
                email: this.email,
                password: this.password
            }

            AuthService.login(formData)
            .then(response => {
                console.log(response.data)
                this.$toast.open({
                    message: "Logged in successfully!", 
                    type: "success", 
                    duration: 3000,
                })
                this.redirect()
            })
            .catch(errors => {
                console.log(errors),
                this.$toast.open({
                    message: "Unregistered user or incorrect credentials. Please check email or password.",
                    type: "warning", duration: 6000
                })
            })
        },
        redirect() {
            setTimeout(() => {
                window.location.href = "/"
            }, 1500)
        }
    }
}
</script>