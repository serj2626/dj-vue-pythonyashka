<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { onMounted, reactive } from 'vue';
const route = useRoute();

const level = reactive({
    title: '',
    slug: '',
});
const subject = reactive({
    title: '',
    slug: '',
});

const lesson = reactive({
    title: '',
    description: '',
    photo: '',
    slug: '',
});

const getLesson = async () => {
    try {
        const response = await axios.get(`/api/lessons/${route.params.slug}`);
        lesson.title = response.data.title
        lesson.description = response.data.description
        lesson.photo = response.data.photo
        lesson.slug = response.data.slug
        level.title = response.data.subject.level.title
        level.slug = response.data.subject.level.slug
        subject.title = response.data.subject.title
        subject.slug = response.data.subject.slug
        console.log(lesson);
    } catch {
        console.log('error');
    }
};
onMounted(getLesson);

</script>


<template>
    <div class="alert alert-warning" role="alert">
        Тема {{ subject.title }} ||  Уровень {{ level.title }}
    </div>
    <div class="row">
        <div class="text-center my-5" role="alert">
            <span class="fs-4">{{ lesson.title }}</span>
        </div>
    </div>
    <div class="row">
        <img :src="lesson.photo" :alt="lesson.title" width="300" height="auto" />
    </div>
    <div class="row">
        <p v-html="lesson.description"></p>
    </div>

</template>