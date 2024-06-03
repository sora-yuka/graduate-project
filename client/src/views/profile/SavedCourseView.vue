<template>
    <section class="saved-section">
        <div class="container">
            <div class="saved">
                <h2 class="saved-header" @click="getUserProfile">
                    Saves
                </h2>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: "SavedCourseView",
    data() {
        return {
            savedCollection: []
        }
    },
    mounted() {
        this.getSavedCollection()
        document.title = "Saved"
    },
    methods: {
        getSavedCollection() {
            axios
            .get("api/v1/courses/saves/")
            .then(response => {
                this.savedCollection = response.data
                console.log("Saved data: ", response.data)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        },
        getUserProfile() {
            const token = JSON.parse(localStorage.getItem("token"));

            return axios.get("http://localhost:8000/api/v1/profiles/me/", {
                headers: {
                    "Authorization": "Bearer " + token.access
                }
            })
            .then(response => {
                localStorage.setItem("user", JSON.stringify(response.data))
                console.log("Profile data: ", response.data)
            })
        }
    }
}
</script>