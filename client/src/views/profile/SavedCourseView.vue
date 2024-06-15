<template>
    <section class="saved-section">
        <div class="container">
            <div class="saved">
                <h2 class="saved-header">
                    Your saves
                </h2>
                <div class="saved-list">
                    <div class="saved-box"
                    v-for="save in savedCollection"
                    v-bind:key="save.id"
                    >
                        <img :src="save.preview_image" alt="">
                        <p class="course-name" @click="redirectToDetail(save.course.id)">{{ save.course.name }}</p>
                    </div>
                </div>
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
        document.title = "K.Hub | saved"
    },
    methods: {
        getSavedCollection() {
            axios
            .get("api/v1/courses/saves/")
            .then(response => {
                this.savedCollection = response.data
                console.log("Saved data: ", response.data)
                this.getInfo()
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        },
        redirectToDetail(courseId) {
            this.$router.push(`/course/${courseId}`)
        },
    }
}
</script>