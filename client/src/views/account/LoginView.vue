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
import axios from 'axios'
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
        document.title = "Login"
    },
    methods: {
        submitForm() {
            const formData = {
                email: this.email,
                password: this.password
            }

            axios
            .post("api/v1/user/login/", formData)
            .then(response => {
                console.log(response.data), 
                this.$toast.success("Loged successfully!")}
            )
            .catch(errors => {
                console.log(errors),
                this.$toast.open({
                    message: "Unregistered user or incorrect credentials. Please check email or password.",
                    type: "warning", duration: 6000
                })
            })
        }
    }
}
</script>