<template>
  <div class="topbar">
    <div>
      <FileUpload />
    </div>
    <div>
      <button
        style="background-color: green"
        @click="runBatchjob"
        class="mdc-button mdc-button--unelevated"
        :disabled="triggerDisabled"
      >Trigger Batchjob</button>
    </div>
  </div>
  <div class="img">
    <ui-card
      class="img-card"
      outlined
      style="width: 300px; margin-right: 20px; margin-bottom: 20px"
    >
      <ui-image-item
        style="cursor: pointer"
        @click="openCumulativeWordCloudImg"
        alt="Aggregate Wordcloud"
        bg-image="/api/cumulative-wordcloud"
      >
        <ui-image-text>cumulative</ui-image-text>
      </ui-image-item>
    </ui-card>

    <div class="imgs">
      <WordcloudList />
    </div>
  </div>
</template>

<script>
import WordcloudList from "~/components/WordcloudList.vue";
import FileUpload from "~/components/FileUpload.vue";

import { ref } from 'vue'

export default {
  name: 'App',
  components: {
    FileUpload,
    WordcloudList,
  },
  setup() {
    const triggerDisabled = ref(false);

    async function runBatchjob() {
      triggerDisabled.value = true
      await fetch('/api/wordcount-trigger')
      location.reload()
    }

    function openCumulativeWordCloudImg() {
      window.open(`/api/cumulative-wordcloud`, '_blank');
    }

    return {
      runBatchjob,
      openCumulativeWordCloudImg,
      triggerDisabled
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

.topbar {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.img {
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: center;
}

.img-card {
  padding: 20px;
}

.imgs {
  display: flex;
  width: 100%;
}
</style>
