<script setup>
import { RouterLink, useRouter } from "vue-router";


const router = useRouter();
</script>


<template>
    <button @click="router.go(-1)">Назад</button>
</template>

<style scoped>
button{
    padding: 15px 20px;
    font-size: 18px;
    border: none;
    color: white;
    border-radius: 20px;
    background-color: red;
}

</style>