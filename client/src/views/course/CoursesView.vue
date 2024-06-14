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
                    <div class="tags">
                        <p class="filters-tags">Tags</p>
                        <div class="label-container">
                            <label class="label">
                                <input type="radio" id="Code" value="code" name="category" @click="filterCourses(1, selectedLevel)"/>
                                Code
                            </label>
                            <label for="General" class="label">
                                <input type="radio" id="General" value="general" name="category" @click="filterCourses(2, selectedLevel)">
                                General
                            </label>
                            <label for="Game" class="label">
                                <input type="radio" id="Game" value="game" name="category" @click="filterCourses(3, selectedLevel)">
                                Game
                            </label>
                            <label for="Any" class="label">
                                <input type="radio" id="Any" value="any" name="category" @click="filterCourses(undefined, selectedLevel)">
                                Any
                            </label>
                        </div>
                    </div>

                    <div class="level">
                        <p class="filters-tags">Level</p>
                        <div class="label-container">
                            <label for="All" class="label">
                                <input type="radio" id="All" value="" name="level" @click="filterCourses(selectedCategory, '')">
                                All
                            </label>
                            <label for="Beginner" class="label">
                                <input type="radio" id="Beginner" value="beginner" name="level" @click="filterCourses(selectedCategory, 'Beginner')"/>
                                Beginner
                            </label>
                            <label for="Intermediate" class="label">
                                <input type="radio" id="Intermediate" value="intermediate" name="level" @click="filterCourses(selectedCategory, 'Intermediate')">
                                Intermediate
                            </label>
                            <label for="Advanced" class="label">
                                <input type="radio" id="Advanced" value="advanced" name="level" @click="filterCourses(selectedCategory, 'Advanced')">
                                Advanced
                            </label>
                            <label for="Any-level" class="label">
                                <input type="radio" id="Any-level" value="any" name="level" @click="filterCourses(selectedCategory, 'Any')">
                                Any
                            </label>
                        </div>
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
            </div>
            <div class="page-control">
                <button class="page-button" @click="handlePage(links.previous)">
                    previous
                </button>
                <p class="info">{{ currentPage }} of {{ pageNums }} pages</p>
                <button class="page-button" @click="handlePage(links.next)">
                    next
                </button>
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
            links: {
                previous: null,
                next: null,
            },
            pageNums: [],
            currentPage: '',
            selectedCategory: '',
            selectedLevel: ''
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
                    this.pageNums = response.data.total_pages
                    this.currentPage = response.data.current_page
                    this.links = response.data.links
                    console.log("CoursesView response: ", response.data);
                })
                .catch(errors => {
                    console.log("An error occured: ", errors)
                })
        },
        redirectToDetail(courseId) {
            this.$router.push(`/course/${courseId}`)
        },
        filterCourses(categoryId, levelId) {
            this.selectedCategory = categoryId;
            this.selectedLevel = levelId;

            let filterUrl = `/api/v1/courses/?`;

            if (this.selectedCategory !== undefined) {
                filterUrl += `category=${this.selectedCategory}`;
            }

            if (this.selectedLevel !== '') {
                if (this.selectedCategory !== undefined) {
                    filterUrl += `&level=${this.selectedLevel}`;
                } else {
                    filterUrl += `level=${this.selectedLevel}`;
                }
            }
                
            axios
            .get(filterUrl)
            .then(response => {
                this.allCourse = response.data.results
                this.courseCount = response.data.count
                this.currentPage = response.data.current_page
                this.pageNums = response.data.total_pages
                this.links = response.data.links
                console.log("Filter: ", response.data)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
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
        handlePage(link) {
            if (!link) return

            axios
            .get(link)
            .then(response => {
                this.allCourse = response.data.results
                this.courseCount = response.data.count
                this.currentPage = response.data.current_page
                this.pageNums = response.data.total_pages
                this.links = response.data.links
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        }
    }
}
</script>