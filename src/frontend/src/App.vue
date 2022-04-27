<template>
  <FileUpload></FileUpload>
  <WordcloudList></WordcloudList>
</template>

<script>

import WordcloudList from "@/components/WordcloudList";
import FileUpload from "@/components/FileUpload";
export default {
  name: 'App',
  components: {
    FileUpload,
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
