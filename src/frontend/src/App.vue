<template>
  <form action="/api/uploads" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" />
    <input type="submit" />
  </form>
  <WordcloudList></WordcloudList>
</template>

<script>

import WordcloudList from "@/components/WordcloudList";
export default {
  name: 'App',
  components: {
    WordcloudList,
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
