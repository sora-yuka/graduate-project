<template>
    <section class="register-section">
        <div class="container">
            <div class="register-form" v-if="!isSubmited">
                <div class="preview-form">
                    <div class="preview-photo"></div>
                    <div class="preview-text">
                        <h1 class="register-header">registration</h1>
                        <p class="register-description">Register to our paltform</p>
                    </div>
                </div>
                <form @submit.prevent="submitForm" class="register-form">
                    <ul class="form-list">
                        <li class="form-list__item">
                            <input type="text" v-model="email"><br>
                            <label for="email">Email</label>
                        </li>
                        <li class="form-list__item">
                            <input type="password" v-model="password"><br>
                            <label for="password">Password</label>
                        </li>
                        <li class="form-list__item">
                            <input type="password" v-model="password_confirm"><br>
                            <label for="password_confirm">Confirm</label>
                        </li>
                    </ul>
                    <button class="confirm" type="submit">sign up</button>
                </form>
            </div>
            <div class="registered-form" v-else>
                <p class="response">
                    You have successfully registered. Please check your email and confirm your account. <br>
                    You can close this page.
                </p>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { useToast } from 'vue-toast-notification'

export default {
    name: "RegisterView",
    data() {
        return {
            email: "",
            password: "",
            password_confirm: "",
            errors: [],
            isSubmited: false
        }
    },
    mounted() {
        document.title = "K.Hub | sign up"
        this.$toast = useToast()
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email === "") {
                this.errors.push("The email is missing")
                this.$toast.open({
                    message: "The 'email' field is empty", type: "warning", duration: 6000
                })
            }

            if (this.password === "") {
                this.errors.push("The password is missing")
                this.$toast.open({
                    message: "The 'password' fields is empty", type: "warning", duration: 6000
                })
            }

            if (this.password_confirm !== this.password) {
                this.errors.push("The password does not match")
                this.$toast.open({
                    message: "Password didn't match", type: "warning", duration: 6000
                })
            }

            if (this.password.length < 6) {
                this.errors.push("The password is too small")
                this.$toast.open({
                    message: "Password cannot be less then 6 characters", type: "warning", duration: 6000
                })
            }

            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password,
                    password_confirm: this.password_confirm
                }

                axios
                .post("api/v1/user/register/", formData)
                .then(response => {
                    this.isSubmited = true
                    this.$toast.success("Account registered successfully!")
                    console.log(response.data)
                })
                .catch(errors => {
                    if (errors.response) {
                        for (const property in errors.response.data) {
                            this.errors.push(`${property}: ${errors.response.data[property]}`)
                        }

                        console.log(JSON.stringify(errors.response.data))
                    } else if (errors.message) {
                        this.errors.push("Something went wrong, please try again")
                        console.log(JSON.stringify(errors))
                    }
                    this.$toast.error("The given email is already exist!")
                }) 
            } else {
                this.$toast.open({
                    message: "Registration failed", type: "error", duration: 5000
                })
            }
        }
    },
}
</script>