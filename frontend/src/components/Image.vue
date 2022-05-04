<template>
  <div class="flex flex-col p-4 cursor-pointer border-1 border-gray-400 rounded-lg" @click="openImg">
    <div class="w-64 h-64 relative overflow-hidden">
      <img :src="url" class="absolute w-full h-full bg-gray-400 object-cover" />
    </div>
    <span>{{ name }}</span>
  </div>
</template>

<script setup>
import { defineProps, onMounted, ref } from 'vue';

const props = defineProps({
  name: String,
  url: String,
});

const imgUrl = ref('/loading.gif');

function openImg() {
  window.open(props.url, '_blank');
}

onMounted(async () => {
  // try to load file which will be blocked if the image need to be generated first
  await fetch(props.url);

  // update url to use generated image
  imgUrl.value = props.url;
});
</script>
