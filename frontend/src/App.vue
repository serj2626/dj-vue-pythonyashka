<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
</script>

<template>
  <div class="app container-fluid">
    <header>
      <Header />
    </header>
    <main>
      <RouterView />
    </main>
    <footer>

    </footer>
  </div>


</template>

<style scoped>
.app{
    min-height: 100vh;
}
</style>
