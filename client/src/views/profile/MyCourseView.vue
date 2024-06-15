<template>
    <section class="my-course__section">
        <div class="container">
            <div class="users-courses">
                <div class="users-box"
                    v-for="course in courses"
                    v-bind:key="course.id"
                >
                    <img class="box-photo" :src="course.preview_image" alt="">

                    <div class="box-info">
                        <h3 class="box-header">Course title: {{ course.title }}</h3>
                        <p class="box-created">Published at: {{ course.created_at }}</p>

                        <div class="courses-button">
                            <button class="button-get" @click="getCourse(course.id)">Get</button>
                            <button class="button-edit">Edit</button>
                            <button class="button-delete" @click="deleteCourse(course.id)">Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { useToast } from 'vue-toast-notification'

export default {
    name: "MyCourseView",
    data() {
        return {
            courses: []
        }
    },
    mounted() {
        this.myCourses()
        this.$toast = useToast()
        document.title = "K.Hub | my courses"
    },
    methods: {
        myCourses() {
            axios
            .get("api/v1/courses/my-course/")
            .then(response => {
                this.courses = response.data
                console.log("My course: ", response.data)
            })
            .catch(error => {
                console.log("An error occured while getting users courses: ", error)
            })
        },
        getCourse(courseId) {
            this.$router.push(`course/${courseId}`)
        },
        deleteCourse(courseId) {
            axios
            .delete(`api/v1/courses/page/${courseId}`)
            .then(response => {
                console.log("Course deleted: ", response.data)
                this.$toast.open({
                    message: "Course deleted successfully", type: "success", duration: 2000
                })
                setTimeout(() => {
                    this.$router.go()
                }, 2000)
            })
            .catch(error => {
                console.log("An error occured while deleting course: ", error)
            })
        }
    }
}
</script>