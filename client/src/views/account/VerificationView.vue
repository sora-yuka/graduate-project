<template>
    <section class="verification-section" v-if="!isAuthenticated">
        <div class="container">
            <div class="photo"></div>
            <form action="" @submit.prevent="submitForm" class="verification-form">
                <ul class="form-list">
                    <li class="form-list__item">
                        <input type="text" v-model="username"><br>
                        <label for="username">Username</label>
                    </li>
                </ul>
                <div class="form-button">
                    <button type="submit" class="confirm">confirm</button>
                </div>
            </form>
        </div>
    </section>
    <section class="verification-failed" v-else>
        <div class="container">
            <p class="info">
                You already have account in this platform
            </p>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import {useToast} from 'vue-toast-notification'

export default {
    name: "VerificationView",
    data() {
        return {
            username: "",
        }
    },
    mounted() {
        this.$toast = useToast()
        document.title = "Verify"
    },
    computed: {
        ...mapGetters({
            isAuthenticated: "isAuthenticated"
        })
    },
    methods: {
        submitForm() {
            const url = this.$route.params.verificationCode
            const formData = {
                username: this.username
            }

            axios
            .post(`api/v1/user/verify/${url}/`, formData)
            .then(response => {console.log(response.data)})
            .catch(errors => {
                console.log(errors)
            })
        }
    }
}
</script>