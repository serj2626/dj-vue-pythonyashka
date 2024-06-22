<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useToast } from "vue-toastification";

const tags = ref([]);
const toast = useToast();

const getTags = async () => {
  try {
    const res = await axios.get("/api/posts/tags");
    tags.value = res.data;
  } catch {
    toast.error("Ошибка при получении тегов");
  }
};

onMounted(getTags);
</script>

<template>
  <div class="row">
    <div class="alert alert-warning" role="alert">Главная страница</div>

    <div>
      <h1 class="text-center">Полезные статьи</h1>
    </div>
  </div>
  <div class="row">
    <div class="col-md-2 mt-3" v-for="tag in tags" :key="tag">
      <button class="btn btn-primary btn-tag">{{ tag.title }}</button>
    </div>
  </div>
</template>
<style scoped>
.btn-tag {
  padding: 10px 20px;
  font-size: 18px;
}
</style>
