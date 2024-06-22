<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useToast } from 'vue-toastification';
import { useRoute,useRouter } from 'vue-router';


const route = useRoute();
const router = useRouter();
const { slug } = route.params

const toast = useToast();
const tag = ref('')
const posts = ref([]);

const getTagWithPosts = async () => {
    try {
        const res = await axios.get(`/api/posts/tags/${slug}`);
        console.log(res.data);
        posts.value = res.data.posts;
        tag.value = res.data.title
    } catch (err) {
        toast.error("Ошибка при получении постов");
        console.log(err);
    }
}

onMounted(getTagWithPosts);
</script>


<template>
    <div class="row">
        <div class="alert alert-warning" role="alert">
            Тема {{ tag }} || Количество постов: {{ posts.length }}
        </div>
    </div>
    <div class="row">
        <div class="col-md-4" v-for="post in posts" :key="post.id">
            <div 
            @click="$router.push({ name: 'post', 
            params: { slug: post.slug } })"
            class="post" role="alert">
                {{ post.title }}
            </div>
        </div>
    </div>
</template>

<style scoped>
.post {
    margin: 10px;
    padding: 10px;
    background: linear-gradient(90deg, #3099df 0%, #0c7f83 100%);
    color: white;
    font-size: 22px;
    height: 100px;
    border-radius: 10px;
    box-shadow: 20px 15px 5px rgba(0, 0, 0, 0.5);
}

.post:hover {
    cursor: pointer;
    transition-duration: 0.8s;
    transform: scale(1.1);
    color: yellow;
}
</style>