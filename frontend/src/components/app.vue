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
    font-size: 12px;
    font-family: Helvetica;

    width: $app-width;
    margin: 1em auto;
    padding: 1.5em 24px;
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
