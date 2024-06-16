<template>
    <section class="update-course__section">
        <div class="container">
            <h3 class="update-course__header">Editing your course</h3>
            <p class="require-desc"><i>If you don't want to change the field, you can leave it blank</i></p>
            <form class="update-form" @submit.prevent="submitForm">
                <ul class="update-form__list">
                    <li class="update-form__item">
                        <label class="update-form__label">
                            Title <br>
                            <input type="text" v-model="title" :placeholder="courseData.title"
                        </label>
                    </li>
                    <li class="update-form__item">
                        <label class="update-form__label">
                            Description <br>
                            <input type="text" v-model="description" :placeholder="courseData.description">
                        </label>
                    </li>
                    <li class="update-form__item">
                        <label class="update-form__label">
                            Level <br>
                            <select class="update-form__select" v-model="level">
                                <option value="Any">Any</option>
                                <option value="Beginner">Beginner</option>
                                <option value="Intermediate">Intermediate</option>
                                <option value="Advanced">Advanced</option>
                            </select>
                        </label>
                    </li>
                    <li class="update-form__item">
                        <label class="update-form__label">
                            Tag <br>
                            <select class="update-form__select" v-model="tag">
                                <option :value="tags.id" v-for="tags in serverTags">{{ tags.category }}</option>
                            </select>
                        </label>
                    </li>
                    <span>Preview image</span>
                    <li class="update-form__upload">
                        <input type="file" id="file" accept="image/*" @change="handleImage">
                        <label class="update-form__label" for="file">
                            + Upload photo
                        </label>
                    </li>
                </ul>
                <div class="form-additional">
                    <img src="../../components/source/ll.png" alt="">
                    <i>With great power comes great responsibility</i>
                </div>
                <div class="update-button-container">
                    <button class="update-form__button" @click="redirect">Cancel</button>
                    <button class="update-form__button" type="confirm">Save changes</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { useToast } from 'vue-toast-notification'

export default {
    name: "UpdateCourseView",
    data() {
        return {
            title: null,
            description: null,
            level: null,
            tag: null,
            image: null,
            serverTags: [],
            courseData: {},
        }
    },
    mounted() {
        this.collectData()
        this.getTags()
        this.$toast = useToast()
        document.title = "K.Hub | edit"
    },
    methods: {
        getTags() {
            axios
            .get("api/v1/courses/category")
            .then(response => {
                this.serverTags = response.data
                console.log("Tags: ", response.data)
            })
        },
        collectData() {
            const courseId = this.$route.params.id

            axios
            .get(`api/v1/courses/page/${courseId}/`)
            .then(response => {
                this.courseData = response.data
                console.log("Getting data for editing course: ", response.data)
            })
            .catch(error => {
                console.log("An error occured while getting course data: ", error)
            })
        },
        handleImage(event) {
            this.image = event.target.files[0]
        },
        submitForm() {
            const courseId = this.$route.params.id

            const formData = {
                title: this.title,
                description: this.description,
                level: this.level,
                category: this.tag,
                preview_image: this.image,
            }

            axios
            .patch(`api/v1/courses/page/${courseId}/`, formData, {
                headers: {
                    "Content-type": "multipart/form-data"
                }
            })
            .then(response => {
                console.log("Server log: ", response.data)
                this.$toast.open({
                    message: "Changed successfully", type: "success", duration: 2000
                })
                setTimeout(() => {
                    this.redirect()
                }, 2000)
            })
            .catch(error => {
                this.$toast.open({
                    message: "Something went wrong!", type: "error", duration: 4000
                })
                console.log("An error occured, while changing course: ", error)
            })
        },
        redirect() {
            const courseId = this.$route.params.id
            this.$router.push(`/course/${courseId}`)
        },
    }
}
</script>