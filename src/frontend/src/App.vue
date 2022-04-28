<template>
  <div class="topbar">
    <div>
      <FileUpload></FileUpload>
    </div>
    <div>
      <button style="background-color: green" @click="runBatchjob()" class="mdc-button mdc-button--unelevated">Trigger Batchjob</button>
    </div>
  </div>
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
  },
  methods: {
    runBatchjob(){
      fetch('http://localhost:5000/api/wordcount/trigger')
    }
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

.topbar{
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
