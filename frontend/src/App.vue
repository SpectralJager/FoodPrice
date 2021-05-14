<template>
  <Header />
  <main>
    <router-view />
  </main>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  components: {
    Header,
  },
  
}
</script>


<style lang="scss">
*,
*::before,
*::after{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
a{
  color: inherit;
  text-decoration: none;
}
body{
  min-width: 360px;
}
</style>
