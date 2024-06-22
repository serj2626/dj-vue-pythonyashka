<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";

const route = useRoute();
const subject = ref('')
const lessons = ref([]);

const getSubject = async () => {
    try {
        const response = await axios.get(
            `/api/subjects/${route.params.subject_slug}`
        );
        lessons.value = response.data.lessons;
        subject.value = response.data.title

    } catch {
        console.log("error");
    }

};

onMounted(getSubject);


</script>

<template>
    <div class="alert alert-warning" role="alert">
        {{ subject }}
    </div>


    <div class="row">
        <ol class="grid">
            <li v-for="lesson in lessons" :key="lesson.id">

                <RouterLink :to="{ name: 'lesson', params: { slug: lesson.slug } }" class="link-subject">
                    {{ lesson.title }}
                </RouterLink>
            </li>
        </ol>
    </div>

</template>

<style scoped>
.link-subject {
    text-decoration: none;

    &:hover {
        color: red;
    }
}
</style>