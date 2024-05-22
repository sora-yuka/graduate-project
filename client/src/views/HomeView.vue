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

                <button class="explore">
                    Explore Programs 
                    <img src="../components/source/loupe.png" class="loupe" alt="">
                </button>
            </div>
        </div>
    </header>
    <main class="main">
        <div class="container">
            <div class="latest-block">
                <h2 class="latest-course__header">Get a head start on a degree today</h2>
                <p class="latest-course__description">
                    Explore our newest programs, focused on delivering in-demand skills.
                </p>
                <div class="latest-course__list">
                    <div class="box"
                        v-for="course in latestCourse"
                        v-bind:key="course.id"
                    >
                        <img v-bind:src="course.preview_image" alt="" class="course-image">
                        <p class="author">Author: {{ course.owner_profile.profile_username }}</p>
                        <p class="title">{{ course.title }}</p>
                        <p class="tag">Tag: {{ course.category.category }}</p>
                        <p class="level"> {{ course.level }} </p>
                    </div>
                </div>
                <router-link class="view-all" to="/all/">View all</router-link>
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
                console.log("HomeView response: ", response.data)
            })
            .catch(errors => {
                console.log("An error occurred: ", errors)
            })
        }
    }
}
</script>