<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import { useToast } from "vue-toastification";

const toast = useToast();
const post = ref({});
const route = useRoute();
const { slug } = route.params;

const getPost = async () => {
  try {
    const res = await axios.get(`/api/posts/${slug}`);
    post.value = { ...res.data };
    console.log(post.value);
  } catch (err) {
    toast.error("Ошибка при получении поста");
    console.log(err);
  }
};

onMounted(getPost);
</script>

<template>
  <div class="row">
    <div class="alert alert-warning" role="alert">
      Пост на тему <span class="fs-4 text-danger">{{ post.title }}</span>
    </div>
  </div>
  <div class="row">
    <div class="">
      <p v-html="post.content"></p>
    </div>
  </div>

  <div
    class="d-flex justify-content-center"
    v-for="tag in post.tags"
    :key="tag"
  >
    <button class="btn btn-primary btn-tag">{{ tag.title }}</button>
  </div>
</template>
<style scoped>
.btn-tag {
  padding: 10px 20px;
  font-size: 18px;
  display: block;
}
</style>
