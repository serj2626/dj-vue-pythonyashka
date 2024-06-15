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

    </main>
    <footer>

    </footer>
  </div>

  <RouterView />
</template>

<style scoped>
.app {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100vh;
}
</style>
