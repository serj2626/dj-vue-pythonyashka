import './assets/main.css'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"



axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app
    .use(createPinia())
    .use(Toast)
    .use(router, axios)
    .mount('#app')

