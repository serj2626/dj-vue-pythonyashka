<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
</script>

<template>


  <div class="app">
    <header>
      <Header />
    </header>
    <main class="container">
      <div>
        <RouterView />
      </div>

    </main>
    <footer>

    </footer>
  </div>

</template>

<style scoped>
.app {
    margin: 60px;
    background-color: rgb(238, 210, 221);
    min-height: 90vh;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 35px 25px 12px rgba(0, 0, 0, 0.5); 
} 
</style>
