<template>
    <section class="update-course-item__section">
        <div class="container">
            <form class="course-item__form" @submit.prevent="submitForm">
                <h3 class="course-item__header">
                    Uploading your lessons
                </h3>
                <div class="form-container">
                    <div class="label-container">
                        <div class="title-container">
                        <label class="course-item__label">
                            Lesson's title <br>
                            <input class="course-item__input" type="text" v-model="title" placeholder="Write lesson title">
                        </label>
                        </div>
                        <div class="desc-container">
                            <label class="course-item__label">
                                Description <br>
                                <textarea v-model="description" placeholder="Write some description"></textarea>
                            </label>
                        </div>
                        <div class="upload-container">
                            <p>Lesson's video</p>
                            <label class="course-item__label-upload">
                                Upload video
                                <input class="course-item__upload" type="file" @change="handleVideo" accept="video/mp4">
                            </label>
                        </div>
                    </div>
                    <div class="course-container">
                        <div class="short-info">
                            <img class="photo" :src="course.preview_image" alt="">
                            <p class="accent">Title: <span class="value">"{{ course.title }}"</span></p>
                            <p class="accent">Level: <span class="value">{{ course.level }}</span></p>
                            <p class="accent">Tag: <span class="value">{{ courseCategory.category }}</span></p>

                        </div>
                    </div>
                </div>
                <div class="button-container">
                    <button class="course-item__button" @click="cancel">Cancel</button>
                    <button class="course-item__button" type="confirm">Publish</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import axios from "axios"
import { useToast } from "vue-toast-notification"

export default {
    name: "UpdateCourseItemView",
    data() {
        return {
            title: "",
            description: "",
            video: null,
            course: {},
            courseCategory: "",
            errors: []
        }
    },
    mounted() {
        this.getCourseInfo()
        this.$toast = useToast()
        document.title = "K.Hub | upload lesson"
    },
    methods: {
        getCourseInfo() {
            const courseId = this.$route.params.id
            
            axios
            .get(`api/v1/courses/page/${courseId}`)
            .then(response => {
                this.course = response.data
                this.courseCategory = response.data.category
                console.log("Getting course data for lesson uploading: ", response.data)
            })
            .catch(error => {
                console.log("An error occured while getting course data: ", error)
            })
        },
        handleVideo(event) {
            this.video = event.target.files[0]
        },
        cancel() {
            this.$router.go(-1)
        },
        submitForm() {
            let courseId = this.$route.params.id
            this.errors = []

            if (this.title === "") {
                this.errors.push("Title is missing")
                this.$toast.open({
                    message: "Title is missing", type: "warning", duration: 3000
                })
            }

            if (this.description === "") {
                this.errors.push("Description is missing")
                this.$toast.open({
                    message: "Description is missing", type: "warning", duration: 3000
                })
            }

            if (this.video === null) {
                this.errors.push ("Video is missing")
                this.$toast.open({
                    message: "Video is missing", type: "warning", duration: 3000
                })
            }

            if (!this.errors.length) {
                const formData = {
                    name: this.title,
                    description: this.description,
                    course_file: this.video,
                    course: this.$route.params.id
                }

                axios
                .post(`api/v1/courses/page/${courseId}/item/`, formData, {
                    headers: {
                        "Content-type": "multipart/form-data"
                    }
                })
                .then(response => {
                    console.log("Server response for creating items: ", response.data)
                    this.$toast.open({
                        message: "Lesson published successfully", type: "success", duration: 3000
                    })
                    setTimeout(() => {
                        this.$router.go(-1)
                    }, 2000)
                })
                .catch(error => {
                    console.log("An error occured while posting lessons: ", error)
                })
            }
        }
    }
}
</script>