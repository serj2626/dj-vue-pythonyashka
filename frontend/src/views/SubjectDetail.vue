<script setup>
import { ref, onMounted, watchEffect } from "vue";
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
        console.log(response.data);
        lessons.value = response.data.lessons;
        subject.value = response.data.title

    } catch {
        console.log("error");
    }

};

onMounted(getSubject);


</script>

<template>
    <div class="row">
        <div class="text-center my-5" role="alert">
            <span class="fs-4">{{ subject }}</span>
        </div>
    </div>
    <div class="row">
        <ol class="grid">
            <li v-for="lesson in lessons" :key="lesson.id">

                <RouterLink 
                :to="{ name: 'lesson', params: { slug: lesson.slug } }"
                class="link-subject">
                    {{ lesson.title }}
                </RouterLink>
            </li>
        </ol>
    </div>

</template>
