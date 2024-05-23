<template>
    <section class="verification-section">
        <div class="container">
            <form action="" @submit.prevent="submitForm">
                <input type="text" v-model="username">
                <button type="submit" class="submit">confirm</button>
            </form>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
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