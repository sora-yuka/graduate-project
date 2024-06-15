<template>
    <section class="add-course__section">
        <div class="container">
            <h3 class="add-course__header">Create a new course</h3>
            <p class="require-desc"><i>Required fields are marked with an asterisk (*).</i></p>
            <form class="create-form" @submit.prevent="submitForm">
                <ul class="create-form__list">
                    <li class="create-form__item">
                        <label class="create-form__label">
                            Title* <br>
                            <input type="text" v-model="title">
                        </label>
                    </li>
                    <li class="create-form__item">
                        <label class="create-form__label">
                            Description* <br>
                            <input type="text" v-model="description">
                        </label>
                    </li>
                    <li class="create-form__item">
                        <label class="create-form__label">
                            Level* <br>
                            <select class="create-form__select" v-model="level">
                                <option value="" disabled selected>select level...</option>
                                <option value="Any">Any</option>
                                <option value="Beginner">Beginner</option>
                                <option value="Intermediate">Intermediate</option>
                                <option value="Advanced">Advanced</option>
                            </select>
                        </label>
                    </li>
                    <li class="create-form__item">
                        <label class="create-form__label">
                            Tag* <br>
                            <select class="create-form__select" v-model="tag">
                                <option value="" disabled selected>select tag...</option>
                                <option :value="tags.id" v-for="tags in serverTags">{{ tags.category }}</option>
                            </select>
                        </label>
                    </li>
                    <span>Preview image*</span>
                    <li class="create-form__upload">
                        <input type="file" id="file" accept="image/*" @change="handleImage">
                        <label class="create-form__label" for="file">
                            + Upload photo
                        </label>
                    </li>
                </ul>
                <div class="form-additional">
                    <img src="../../components/source/ll.png" alt="">
                    <i>You are creating a public course in your personal account</i>
                </div>
                <div class="create-button-container">
                    <button class="create-form__button" type="confirm">Create course</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { useToast } from 'vue-toast-notification'

export default {
    name: "AddCourseView",
    data() {
        return {
            title: "",
            description: "",
            level: "",
            tag: "",
            image: null,
            serverTags: [],
            errors: []
        }
    },
    mounted() {
        this.getTags()
        this.$toast = useToast()
        document.title = "K.Hub | add course"
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
        handleImage(event) {
            this.image = event.target.files[0]
        },
        submitForm() {
            this.errors = []

            if (this.title === "") {
                this.errors.push("Title is missing")
                this.$toast.open({
                    message: "Title is missing", type: "warning", duration: 4000
                })
            }

            if (this.description === "") {
                this.errors.push("Description is missing")
                this.$toast.open({
                    message: "Description is missing", type: "warning", duration: 4000
                })
            }

            if (this.level === "") {
                this.errors.push("Level is missing")
                this.$toast.open({
                    message: "Level not choosen", type: "warning", duration: 4000
                })
            }

            if (this.tag === "") {
                this.errors.push("Tag is missing")
                this.$toast.open({
                    message: "Tag not choosen", type: "warning", duration: 4000
                })
            }

            if (this.image === null) {
                this.errors.push("Image is missing")
                this.$toast.open({
                    message: "Image is missing", type: "warning", duration: 4000
                })
            }

            if (!this.errors.length) {
                const formData = {
                    title: this.title,
                    description: this.description,
                    level: this.level,
                    category: this.tag,
                    preview_image: this.image,
                }

                axios
                .post("api/v1/courses/page/", formData, {
                    headers: {
                        "Content-type": "multipart/form-data"
                    }
                })
                .then(response => {
                    this.$toast.open({
                        message: "Published successfully", type: "success", // duration: 2000
                    })
                    this.redirect()
                })
                .catch(error => {
                    this.$toast.open({
                        message: "Something went wrong!", type: "error", duration: 4000
                    })
                    console.log("An error occured, while publishing course: ", error)
                })
            }
        },
        redirect() {
            setTimeout(() => {
                window.location.href = "/all"
            }, 1500)
        }
    }
}
</script>