<template>
    <section class="all-course-section">
        <div class="container">
            <div class="results">
                <p class="results-value">{{ courseCount }} results</p>
            </div>
            <div class="main-page">
                <div class="filters">
                    <ul class="filter-list">
                        <li class="list__item">
                            <input type="radio" id="Game" value="game" name="category">
                            <label for="Game" class="radio">Game</label><br>
                            <input type="radio" id="Code" value="code" name="category">
                            <label for="Code" class="radio">Code</label><br>
                            <input type="radio" id="General" value="general" name="category">
                            <label for="General" class="radio">General</label><br>
                            <input type="radio" id="Any" value="any" name="category">
                            <label for="Any" class="radio">Any</label>
                        </li>
                    </ul>
                </div>
                <div class="course-cards">
                    <div class="box"
                        v-for="course in allCourse"
                        v-bind.key="course.id"
                        @click="redirectToDetail(course.id)"
                    >
                    <img v-bind:src="course.preview_image" alt="" class="course-image">
                    <p class="author">Author: {{ course.owner_profile.profile_userid }}</p>
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
    id: "CourseView",
    data() {
        return {
            allCourse: [],
            courseCount: '',
        }
    },
    mounted() {
        this.getDetailCourse()
        document.title = "K.Hub | courses"
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
        },
        redirectToDetail(courseId) {
            this.$router.push(`/course/${courseId}`)
        }
    }
}
</script>