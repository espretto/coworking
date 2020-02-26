<template>
  <main>
    <navbar/>
    <div class="content">
      <router-view/>
    </div>
  </main>
</template>

<style lang="scss">
  @import 'purecss';
  @import '../styles/reset';
  @import '../styles/vars';

  .content {
    font-size: 14px;
    font-family: Helvetica;

    width: $app-width;
    margin: 0 auto;
    padding: 1em 2em;
  }
</style>

<script>
  import navbar from '@/components/navbar.vue'

  export default {
    name: 'App',
    components: {
      navbar
    }
  }
</script>
