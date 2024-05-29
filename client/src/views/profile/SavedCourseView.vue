<template>
    <section class="saved-section">
        <div class="container">
            <div class="saved">
                <h2 class="saved-header">
                    Saves
                </h2>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    name: "SavedCourseView",
    data() {
        return {
            savedCollection: []
        }
    },
    mounted() {
        this.getSavedCollection()
        document.title = "Saved"
    },
    methods: {
        getSavedCollection() {
            axios
            .get("api/v1/courses/saves/")
            .then(response => {
                this.savedCollection = response.data
                console.log("Saved data: ", response.data)
            })
            .catch(errors => {
                console.log("An error occured: ", errors)
            })
        }
    }
}
</script>