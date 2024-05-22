<template>
    <section class="register-section">
        <div class="container">
            <div class="register-form">
                <div class="preview-form">
                    <div class="preview-photo"></div>
                    <div class="preview-text">
                        <h1 class="register-header">registration</h1>
                        <p class="register-description">Register to our paltform</p>
                    </div>
                </div>
                <form @submit.prevent="submitForm">
                    <div class="form">
                        <div class="register-fields">
                            <input type="text" v-model="email">
                            <input type="password" v-model="password">
                            <input type="password" v-model="password_confirm">
                        </div>
                        <router-link>
                            <button class="submit" type="submit">sign up</button>
                        </router-link>
                        
                    </div>
                </form>
                <div class="fields-text">
                    <span class="email">Email</span>
                    <span class="password">Password</span>
                    <span class="confirm">Confirm</span>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    name: "RegisterView",
    data() {
        return {
            email: "",
            password: "",
            password_confirm: "",
            errors: []
        }
    },
    components: {

    },
    mounted() {
        document.title = "SIGN UP"
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.email === "") {
                this.errors.push("The email is missing")
            }

            if (this.password === "") {
                this.errors.push("The password is missing")
            }

            if (this.password_confirm !== this.password) {
                this.errors.push("The password does not match")
            }

            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password,
                    password_confirm: this.password_confirm
                }

                axios
                .post("api/v1/user/register/", formData)
                .then(response => {console.log(response.data)})
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
                })
            }
        }
    },
}
</script>