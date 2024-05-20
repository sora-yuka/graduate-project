<template>
    <header class="header">
        <div class="container">
            <div class="preview-section">
                <h1 class="preview-header">
                    Lead with Excellence
                </h1>
                <p class="preview-description">
                    <i>"Advance your skills and achieve your professional goals with our comprehensive courses."</i>
                </p>

                <button class="explore">Explore Programs <span class="arrow">⟶</span></button>
            </div>
        </div>
    </header>
    <main class="main">
        <div class="container">
            <div class="latest-block">
                <h2 class="latest-course__header">Get a head start on a degree today</h2>
                <p class="latest-course__description">
                    With these programs, you can build valuable skills, earn career credentials, and make progress toward a degree before you even enroll.
                </p>
                <div class="latest-course__list">
                    <div class="box"
                        v-for="course in latestCourse"
                        v-bind:key="course.id"
                    >
                        <img v-bind:src="course.preview_image" alt="" class="course-image">
                        <p class="owner">Owner: {{ course.owner_profile.profile_username }}</p>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
import axios from 'axios'

export default {
    name: "HomeView",
    data() {
        return {
            latestCourse: []
        }
    },
    mounted() {
        this.getLatestCourse()
        document.title = "HOME"
    },
    methods: {
        getLatestCourse() {

            axios
            .get("api/v1/courses/latest/")
            .then(response => {
                this.latestCourse = response.data
                console.log("Response: ", response.data)
            })
            .catch(errors => {
                console.log("An error occurred: ", errors)
            })
        }
    }
}
</script>