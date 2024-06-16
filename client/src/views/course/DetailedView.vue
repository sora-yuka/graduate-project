<template>
    <button class="previous" @click="previous">
        <img src="../../components/source/previous.png" alt="">
    </button>
    <section class="detailed-section">
        <div class="container">
            <div class="course">
                <div class="course-info">
                    <h2 class="course-name">{{ course.title }}</h2>
                    <p class="course-description">{{ course.description }}</p>
                    <p class="course-author">Author: {{ course.profile_username }}</p>
                    <p class="course-tags">Tag: {{ category.category }}</p>
                    <button class="save-button" v-if="isAuthenticated" @click="save">
                        {{ isSaved ? "unsave" : "save" }}
                    </button> <br>
                </div>
                <div class="image">
                    <img v-bind:src="course.preview_image" alt="" class="preview-image">
                </div>
            </div>
            <div class="additional-info">
                <div class="level">
                    <p class="value">{{ course.level }} level</p>
                    <p class="hint">Recommended experience</p>
                </div>
                <div class="splitter"></div>
                <div class="created_at">
                    <p class="value">{{ course.created_at }}</p>
                    <p class="hint">Published</p>
                </div>
                <div class="splitter"></div>
                <div class="updated_at">
                    <p class="value">{{ course.updated_at }}</p>
                    <p class="hint">Last updates</p>
                </div>
                <div class="splitter"></div>
                <div class="text">
                    <p class="value">Flexible schedule</p>
                    <div class="hint">Learn at your own pace</div>
                </div>
            </div>
            <div class="lessons">
                <div class="header-container">
                    <h3 class="lesson-header">Module</h3>

                    <button class="add-item" v-if="ownerData.owner_email === userData.email">
                        <router-link class="add-item-link" :to="'page/' + course.id">+ add lesson</router-link>
                    </button>
                </div>
                <div class="accordion" v-if="courseItem.length !== 0">
                    <div class="accordion-item"
                    v-for="(lesson, index) in courseItem"
                    v-bind:key="lesson.id"
                    >
                        <div class="button-container">
                            <button @click="toggleLesson(index)" class="accordion-button">
                                {{ lesson.name }}
                            </button>
                            
                            <div class="accordion-control" v-if="ownerData.owner_email === userData.email">
                                <button class="accordion-edit"
                                    @click="editItem(lesson)"
                                >
                                    Edit
                                </button>
                                <button class="accordion-delete" 
                                    @click="deleteItem(lesson)"
                                >
                                    Delete
                                </button>
                            </div>
                        </div>
                        <transition class="transition">
                            <div v-show="activeLesson === index">
                                <video width="1200" class="video" ref="video" controls="true">
                                    <source v-bind:src="lesson.course_file" type="video/mp4">
                                </video>
                                <p class="description">
                                    {{ lesson.description }}
                                </p>
                            </div>
                        </transition>
                    </div>
                </div>
                <div class="accordion" v-else>
                    <p class="accordion-empty">Empty for now</p>
                </div>
            </div>
            <div class="recommendation" v-if="recommendedCourse.length !== 0">
                <h3 class="recommendation-header">
                    Recommended if you're interested in "<span class="category">{{ category.category }}"</span>
                </h3>
                <div class="recommendation-list">
                    <div class="box"
                    v-for="recommandation in recommendedCourse"
                    v-bind:key="recommandation.id"
                    @click="redirectToDetail(recommandation.id)"
                    >
                        <img v-bind:src="recommandation.preview_image" alt="" class="course-image">
                        <p class="author">Author: {{ recommandation.owner }}</p>
                        <p class="title">{{ recommandation.title }}</p>
                        <p class="tag">Tag: {{ recommandation.category.category }}</p>
                        <p class="level">{{ recommandation.level }}</p>
                    </div>
                </div>
            </div>
            <div class="recommendation" v-else>
                <h3 class="recommendation-header">
                    Empty for now
                </h3>
            </div>
        </div>
    </section>
</template>


<script>
import axios from 'axios'
import { mapGetters } from 'vuex';
import { useToast } from 'vue-toast-notification';

export default {
    name: "DetailedView",
    data() {
        return {
            course: {},
            courseItem: [],
            category: {},
            activeLesson: null,
            recommendedCourse: [],
            savedCollection: [],
            isSaved: false,
            userData: {},
            ownerData: {}
        }
    },
    mounted() {
        this.getDetailedCourse()
        this.$toast = useToast()
    },
    computed: {
        videoElement() {
            return this.$refs.video
        },
        ...mapGetters({
            isAuthenticated: "isAuthenticated"
        })
    },
    methods: {
        getDetailedCourse() {
            const checkSaved = "api/v1/courses/saves/"
            const courseId = this.$route.params.id

            axios
            .get(`/api/v1/courses/page/${courseId}/`)
            .then(response => {
                this.course = response.data
                this.ownerData = response.data.owner
                this.courseItem = response.data.course_items
                this.category = response.data.category
                this.recommendedCourse = response.data.recommendation
                this.userData = JSON.parse(localStorage.getItem("user")).owner
                document.title = "K.Hub | " + this.course.title

                console.log("Detail data: ", response.data)
                console.log("Recommendation: ", response.data.recommendation)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })

            axios
            .get(checkSaved)
            .then(response => {
                const savedCourses = response.data;
                this.isSaved = savedCourses.some(savedCourse => savedCourse.course.id === parseInt(courseId));
            })
            .catch(errors => {
                console.log("An error occured while checking saved courses: ", errors)
            })
        },
        redirectToDetail(courseId) {
            window.location.href = courseId
        },
        previous() {
            this.$router.go(-1)
        },
        toggleLesson(index) {
            if (this.activeLesson === index) {
                this.activeLesson = null
            } else {
                this.activeLesson = index
            }
        },
        save() {
            this.isSaved = !this.isSaved
            const url = `api/v1/courses/page/${this.course.id}/save/`

            axios
            .post(url)
            .then(this.$toast.open({
                    "message": (!this.isSaved ? "Removed from saved" : "Added to saved"),
                    "duration": 6000,
                    "type": "info"
                })
            )
            .catch(errors => {
                console.log("An error occured, while saving course: ", errors)
            })
        },
        deleteItem(lesson) {
            let itemId = lesson.id
            
            axios
            .delete(`api/v1/courses/page/${this.course.id}/item/${itemId}/`)
            .then(response => {
                console.log("Server log due to deleting lesson: ", response.data)
                this.$toast.success("Lesson deleted successfully")
                setTimeout(() => {
                    this.$router.go()
                }, 1500)
            })
            .catch(error => {
                console.log("An error occured while deleting lesson: ", error)
            })
        },
        editItem(lesson) {
            this.$toast.default(lesson.name)
        }
    }
}
</script>