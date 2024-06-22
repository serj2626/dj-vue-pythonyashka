<script setup>
import { RouterLink, useRouter } from "vue-router";


const router = useRouter();
</script>


<template>
    <button @click="router.go(-1)">Назад</button>
</template>