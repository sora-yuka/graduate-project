<template>
    <section class="all-course-section">
        <div class="container">
            <div class="results">
                <p class="results-value">{{ courseCount }} results</p>
            </div>
            <div class="search" ref="searchContainer">
                <form @submit.prevent="searchCourses">
                    <input type="text" class="search-bar" placeholder="Search..." v-model="searchQuery" @input="filterSuggestions">
                    <button type="submit" class="search-button"><img src="../../components/source/magnifier.png" alt=""> find</button>
                </form>
                <ul class="suggestions" v-if="showSuggestions">
                    <li v-for="(suggestion, index) in filteredSuggestions.slice(0, suggestionsLimit)" :key="suggestion.id" @click="selectSuggestion(suggestion.title)">
                        <img src="../../components/source/magnifier.png" alt=""> {{ suggestion.title }}
                    </li>
                    <li v-if="filteredSuggestions.length > suggestionsLimit" class="suggestions-more"><i>More...</i></li>
                </ul>
            </div>
            <div class="main-page">
                <div class="filters">
                    <p class="filters-tags">Tags</p>
                    <div class="label-container">

                        <label class="label">
                            <input type="radio" id="Code" value="code" name="category" @click="filterCoursesByCategory(1)"/>
                            Code
                            </label>
                        <label for="General" class="label">
                            <input type="radio" id="General" value="general" name="category" @click="filterCoursesByCategory(2)">
                            General
                            </label>
                            <label for="Game" class="label">
                            <input type="radio" id="Game" value="game" name="category" @click="filterCoursesByCategory(3)">
                            Game
                        </label>
                        <label for="Any" class="label">
                            <input type="radio" id="Any" value="any" name="category" @click="filterCoursesByCategory()">
                            Any
                        </label>
                    </div>
                </div>
                <div class="course-cards">
                    <div class="box"
                        v-for="course in allCourse"
                        v-bind:key="course.id"
                        @click="redirectToDetail(course.id)"
                    >
                    <img v-bind:src="course.preview_image" alt="" class="course-image">
                    <p class="author">Author: {{ course.owner_profile.profile_userid }}</p>
                    <p class="title">{{ course.title }}</p>
                    <p class="tag">Tag: {{ course.category.category }}</p>
                    <p class="level">{{ course.level }}</p>
                    </div>
                </div>
                <!-- <div class="page-control">
                    
                </div> -->
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
            searchQuery: '',
            filteredSuggestions: [],
            showSuggestions: false,
            suggestionsLimit: 8,
        }
    },
    mounted() {
        this.getDetailCourse();
        document.title = "K.Hub | courses"
        document.addEventListener('click', this.handleClickOutside)
        document.addEventListener('keydown', this.handleEscKey)
    },
    destroyed() {
        document.removeEventListener('click', this.handleClickOutside)
        document.removeEventListener('keydown', this.handleEscKey)
    },
    methods: {
        getDetailCourse() {
            axios
                .get("api/v1/courses/?category=&level=&page=")
                .then(response => {
                    this.allCourse = response.data.results
                    this.courseCount = response.data.count
                    console.log("CoursesView response: ", response.data);
                })
                .catch(errors => {
                    console.log("An error occured: ", errors)
                })
        },
        redirectToDetail(courseId) {
            this.$router.push(`/course/${courseId}`)
        },
        filterCoursesByCategory(categoryId) {
            if (categoryId !== undefined) {
                const filterUrl = `/api/v1/courses/?category=${categoryId}`
                axios
                    .get(filterUrl)
                    .then(response => {
                        this.allCourse = response.data.results
                        this.courseCount = response.data.count
                    })
                    .catch(errors => {
                        console.log("An error occured: ", errors)
                    })
            } else {
                this.getDetailCourse();
            }
        },
        filterSuggestions() {
            const query = this.searchQuery.toLowerCase()
            this.filteredSuggestions = this.allCourse.filter(course => 
                course.title.toLowerCase().includes(query)
            )
            if (this.filteredSuggestions.length > this.suggestionsLimit) {
                this.filteredSuggestions.push({id: "more", title: "..."})
            }
            this.showSuggestions = true
        },
        selectSuggestion(title) {
            this.searchQuery = title
            this.filteredSuggestions = []
            this.showSuggestions = false
        },
        searchCourses() {
            let searchRequest = this.searchQuery.replace(/ /g, "+")
            console.log(`Searching for: ${this.searchQuery}`)

            axios
            .get(`api/v1/courses/?search=${searchRequest}`)
            .then(response => {
                this.courseCount = response.data.count
                this.allCourse = response.data.results
            })
        },
        handleClickOutside(event) {
            if (this.$refs.searchContainer && !this.$refs.searchContainer.contains(event.target)) {
                this.showSuggestions = false
            }
        },
        handleEscKey(event) {
            if (event.key === 'Escape' || event.key === "Enter") {
                this.showSuggestions = false
            }
        },

    }
}
</script>