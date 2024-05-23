<template>
    <section class="all-course-section">
        <div class="container">
            <div class="results">
                <p class="results-value">{{ courseCount }} results</p>
            </div>
            <div class="main-page">
                <div class="filters">
                    <ul class="filter-list">
                        <li class="list__item">Some filter</li>
                        <li class="list__item">Some filter</li>
                        <li class="list__item">Some filter</li>
                    </ul>
                </div>
                <div class="course-cards">
                    <div class="box"
                    v-for="course in allCourse"
                    v-bind.key="course.id"
                    >
                    <img v-bind:src="course.preview_image" alt="" class="course-image">
                    <p class="author">Author: {{ course.owner_profile.profile_username }}</p>
                    <p class="title">{{ course.title }}</p>
                    <p class="tag">Tag: {{ course.category.category }}</p>
                    <p class="level">{{ course.level }}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    name: "CourseView",
    data() {
        return {
            allCourse: [],
            courseCount: '',
        }
    },
    mounted() {
        this.getDetailCourse()
        document.title = "VIEW"
    },
    methods: {
        getDetailCourse() {

            axios
            .get("api/v1/courses/")
            .then(response => {
                this.allCourse = response.data.results
                this.courseCount = response.data.count
                console.log("CoursesView response: ", response.data)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        }
    }
}
</script>