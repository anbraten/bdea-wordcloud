<template>
  <ui-image-list :text-protection="labelsType === 2" class="img-list">
    <ui-card
      class="img-card"
      v-for="(name, index) in files"
      :key="index"
      outlined
      style="width: 300px; margin-right: 20px; margin-bottom: 20px"
    >
      <ui-image-item
        style="cursor: pointer"
        @click="openImg(name)"
        :bg-image="`/api/wordcloud/${name}`"
      >
        <ui-image-text v-if="labelsType">{{ name }}</ui-image-text>
      </ui-image-item>
    </ui-card>
  </ui-image-list>
</template>

<script>
export default {
  async created() {
    const res = await fetch('/api/filenames')
    this.files = await res.json()
  },
  name: "WordcloudList",
  data() {
    return {
      labelsType: 1,
      files: []
    };
  },
  methods: {
    openImg(name) {
      window.open(`/api/wordcloud/${name}`, '_blank');
    }
  },
}
</script>

<style scoped>
.img-card {
  padding: 20px;
}
</style>