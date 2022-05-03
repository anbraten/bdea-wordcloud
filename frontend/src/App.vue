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
      >Trigger Batchjob</button>
    </div>
  </div>
  <ui-image-list :text-protection="labelsType === 2" class="img-list">
    <ui-card
      class="img-card"
      outlined
      style="width: 300px; margin-right: 20px; margin-bottom: 20px"
    >
      <ui-image-item
        style="cursor: pointer"
        @click="openCumulativeWordCloudImg"
        alt="Aggregate Wordcloud"
        :bg-image="`/api/cumulative-wordcloud/`"
        class="cumulative-wordcloud"
      >
        <ui-image-text>cumulative</ui-image-text>
      </ui-image-item>
    </ui-card>
    <WordcloudList />
  </ui-image-list>
</template>

<script>
import WordcloudList from "~/components/WordcloudList.vue";
import FileUpload from "~/components/FileUpload.vue";

export default {
  name: 'App',
  components: {
    FileUpload,
    WordcloudList,
  },
  methods: {
    async runBatchjob() {
      await fetch('/api/wordcount/trigger')
      console.log('done')
      location.reload()
    },
    openCumulativeWordCloudImg() {
      window.open(`/api/cumulative-wordcloud`, '_blank');
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
</style>
