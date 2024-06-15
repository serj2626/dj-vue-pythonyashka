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
      <div class="container">
        <RouterView />
      </div>

    </main>
    <footer>

    </footer>
  </div>

</template>

<style scoped>

.app {
  min-height: 100vh;
}

/* .app {
    margin: 50px;
    background-color: #ffffff;
    height: 90vh;
    border-radius: 15px;
} */
</style>
