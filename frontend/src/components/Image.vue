<template>
  <div class="flex flex-col p-4 cursor-pointer border-1 border-gray-400 rounded-lg" @click="openImg">
    <div class="w-64 h-64 relative overflow-hidden">
      <img :src="url" class="absolute w-full h-full bg-gray-400 object-cover" />
    </div>
    <span>{{ name }}</span>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  name: String,
  url: String,
});

function openImg() {
  window.open(props.url, '_blank');
}
</script>
