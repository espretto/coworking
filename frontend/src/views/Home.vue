<template>
  <div class="home">
    <schedule msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Schedule from '@/components/schedule.vue'

export default {
  name: 'Home',
  components: {
    Schedule
  }
}
</script>
