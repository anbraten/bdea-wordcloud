<template>
  <ui-file text="Add Files" accept="text/plain" multiple @change="change"></ui-file>
</template>

<script setup>
import { ref } from 'vue';
import { useEvent } from 'balm-ui';

const balmUI = useEvent();
const files = ref([]);

async function change(event) {
  balmUI.onChange('files', event);
  for await (const file of files.value) {
    await upload(file);
  }
  location.reload();
}

async function upload(file) {
  try {
    const data = new FormData();
    data.append('file', file.sourceFile);

    await fetch('/api/uploads', {
      method: 'POST',
      body: data,
    });

    console.log(`${file.name} has been uploaded`);
  } catch (e) {
    console.error(e);
  }
}
</script>
