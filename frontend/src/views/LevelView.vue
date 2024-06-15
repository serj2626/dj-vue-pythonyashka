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

    <div class="row">
      <div class="text-center my-5" role="alert">
        <span class="fs-4">{{ level.title }}</span>
      </div>
    </div>
    <div class="row">
      <ol class="grid">
        <li v-for="subject in level.subjects" :key="subject.id">
            
            <RouterLink class="link-subject" 
         :to="{ name: 'subject', params: { subject_slug: subject.slug } }"
            >
               {{ subject.title }}
            </RouterLink>
        </li>
      </ol>
    </div>

</template>

<style scoped>
.list {
  margin: 10px;
}

.link-subject {
  text-decoration: none;
  font-size: 20px;

  &:hover {
    color: red;
  }
}


.grid{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
}
</style>
