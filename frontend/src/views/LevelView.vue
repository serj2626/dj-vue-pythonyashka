<script setup>
import { ref, onMounted, watchEffect } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();

const level = ref({});

const getLevel = async () => {
  const response = await axios.get(`/api/levels/${route.params.slug}`);
  level.value = response.data;
};

onMounted(getLevel);

watchEffect(() => {
  getLevel();
});


</script>

<template>
  <div class="container">
    <div class="row">
      <div class="alert alert-warning text-center" role="alert">
        {{ level.title }}
      </div>
      <div
        class="list col-2 mx-auto mt-5"
        v-for="subject in level.subjects"
        :key="subject.id"
      >
      <RouterLink class="link" to="{ name: 'home'}">
        {{ subject.title }}
      </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.list {
  margin: 10px;
}
</style>
