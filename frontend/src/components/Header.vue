<script setup>
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";
import ButtonBack from "./global/ButtonBack.vue";

const levels = ref([]);
onMounted(async () => {
  const response = await axios.get("/api/levels");
  levels.value = response.data;
});
</script>

<template>
  <div class="container mt-3 mx-auto">
    <ButtonBack class="back" />
    <div class="row mx-auto">
      <div class="text-center">
        <RouterLink :to="{ name: 'home' }">
          <img
            src="@/assets/python.png"
            title="Домой"
            width="300"
            height="auto"
          />
        </RouterLink>
      </div>
      <div class="text-center mt-2">
        <p class="header-title">Программирование на Python</p>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <div v-for="level in levels" :key="level.id">
          <RouterLink
            class="btn-link btn"
            :to="{ name: 'level', params: { slug: level.slug } }"
          >
            {{ level.title }}
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.back {
  position: absolute;
  top: 80px;
  left: 90%;
}
.btn-link {
  text-align: center;
  text-decoration: none;
  padding: 20px 20px;
  color: white;
  font-size: 18px;
  margin: 15px;
  width: 260px;
  height: 100px;
  font-weight: 600;
  display: inline-flex;
  transition: all 1s ease;
  justify-content: center;
  align-items: center;

  background: linear-gradient(90deg, #ba4e55 0%, #ab09ec 100%);

  &:hover {
    transform: scale(1.1);
    color: yellow;
  }
}

.header-title {
  font-size: 26px;
  font-weight: 700;
  color: #ba4e55;
}
.router-link-exact-active {
  color: rgb(238, 238, 8);
}

img {
  transition: all 0.5s ease-in;
}

img:hover {
  transform: scale(1.1);
  filter: brightness(110%);
}
</style>
