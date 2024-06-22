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
    <div class="alert alert-warning my-5" role="alert">Главная страница</div>

    <div>
      <h1 class="text-center mt-2">Полезные статьи</h1>
    </div>
  </div>
  <div class="row mt-5">
    <div class="col-md-2 mt-3" v-for="tag in tags" :key="tag">
      <RouterLink
        :to="{
          name: 'tag',
          params: { slug: tag.slug },
        }"
      >
        <button class="btn btn-primary btn-tag">{{ tag.title }}</button>
      </RouterLink>
    </div>
  </div>
</template>
<style scoped>
.btn-tag {
  padding: 10px 20px;
  font-size: 18px;
  width: 100%;
}
</style>
