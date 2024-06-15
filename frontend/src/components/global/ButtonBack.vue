<script setup>
import { RouterLink, useRouter } from "vue-router";


const router = useRouter();
</script>


<template>
    <button><RouterLink :to="{ name: 'home' }">Назад</RouterLink></button>
</template>