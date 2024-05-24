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
                    <p class="course-author">Author: {{ course.owner }}</p>
                    <p class="course-tags">Tag: {{ category.category }}</p>
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
            <div class="recommendation">
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
                        <p class="level"> {{ recommandation.level }} </p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


<script>
import axios from 'axios'

export default {
    name: "DetailedView",
    data() {
        return {
            course: {},
            category: {},
            recommendedCourse: [],
        }
    },
    mounted() {
        this.getDetailedCourse()
        document.title = "Detail"
    },
    methods: {
        getDetailedCourse() {
            const courseId = this.$route.params.id

            axios
            .get(`/api/v1/courses/page/${courseId}/`)
            .then(response => {
                this.course = response.data
                this.category = response.data.category
                this.recommendedCourse = response.data.recommendation
                
                console.log("Detail data: ", response.data)
                console.log("Recommendation: ", response.data.recommendation)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        },
        redirectToDetail(courseId) {
            window.location.href = courseId
        },
        previous() {
            this.$router.go(-1)
        },
    }
}
</script>