<script setup>
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";

const levels = ref([]);
onMounted(async () => {
  const response = await axios.get("/api/levels");
  levels.value = response.data;
});
</script>

<template>
  <div class="container mt-5 mx-auto">
    <div class="row">
      <div class="mx-auto text-center">
        <img src="@/assets/python.jpg" width="300" height="auto" />
      </div>
      <div class="d-flex mt-3">
        <div v-for="level in levels" :key="level.id">
          <button class="btn btn-primary py-3 px-2">{{ level.title }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
button {
  width: 222px;
  height: 90px;
  margin: 10px;
  font-size: 18px;
  background: linear-gradient(90deg, #ba4e55 0%, #ab09ec 100%);

}

button:hover {
  transition: all 0.6s ease;
  transform: scale(1.1);
}
</style>
