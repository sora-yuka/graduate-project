<template>
    <section class="all-course-section">
        <div class="container">
            <div class="courses"
                v-for="course in allCourse"
                v-bind:key="course.id"
            >

                <p>{{ course.title }}</p>
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
            allCourse: []
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
                this.allCourse = response.data
                console.log("CoursesView response: ", response.data)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        }
    }
}
</script>