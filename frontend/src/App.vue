<template>
  <div>
    <div class="topbar">
      <div>
        <FileUpload />
      </div>
      <div>
        <button
          @click="runBatchjob"
          class="mdc-button mdc-button--unelevated !bg-green-500"
          :disabled="triggerDisabled"
        >Trigger DF-Calcuation Batchjob</button>
      </div>
    </div>

    <div class="flex flex-col m-4 justify-center content-start">
      <div class="mb-4 flex justify-center">
        <Image name="Aggregated Wordcloud" url="/api/cumulative-wordcloud" />
      </div>

      <div class="flex flex-wrap gap-4 justify-center">
        <Image
          v-for="(name, index) in files"
          :key="index"
          :name="name"
          :url="`/api/wordcloud/${name}`"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import FileUpload from '~/components/FileUpload.vue';
import Image from '~/components/Image.vue';

import { onMounted, ref } from 'vue';

const triggerDisabled = ref(false);

async function runBatchjob() {
  triggerDisabled.value = true;
  await fetch('/api/wordcount-trigger');
  location.reload();
}

const files = ref([]);

onMounted(async () => {
  const res = await fetch('/api/filenames');
  files.value = await res.json();
});
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
