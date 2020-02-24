<template>
  <div class="bar">
    <nav class="nav">
      <ul class="nav-links">
        <li><router-link to="/"><span class="nav-link-home">coworking</span></router-link></li>
        <li><router-link to="/workspaces">workspaces</router-link></li>
        <li><router-link to="/about">about</router-link></li>
      </ul>
    </nav>
  </div>
</template>
<style scoped lang=scss>
  @import '../styles/vars';

  $nav-height: 3em;

  .bar {
    position: fixed;
    z-index: 1001; // above .leaflet-top
    display: block;
    top: 0;
    width: 100%;
    height: $nav-height;
    background: $theme2;
    text-align: center;
  }

  .nav {
    display: block;
    width: $app-width;
    height: 100%;
    margin: 0 auto;
  }

  .nav-links {
    list-style: none;
    margin: 0;
    padding: 0;

    li {
      display: inline-block;
      float: left;
      height: 100%; 
    }

    a {
      display: inline-block;
      height: 100%; 
      line-height: $nav-height;
      color: #eee;
      font-variant: small-caps;
      padding: 0 $nav-height / 2;
      text-decoration: none;
    }

    a:hover {
      background-color: $theme3
    }
  }

  .nav-link-home {
    font-weight: bold;
  }

</style>
<script>
  
</script>