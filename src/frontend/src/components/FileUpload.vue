<template>
  <ui-file text="Add Files"  accept="text/plain" multiple @change="change"></ui-file>
  <div style="height: 50px;">
    <div style="height: 20px"></div>
    <p style="margin: 0px" v-if="showUploaded">Uploaded</p>
  </div>
</template>

<script>
import { useEvent } from 'balm-ui';

export default {
  name: 'FileUpload',
  data() {
    return {
      balmUI: useEvent(),
      files: [],
      showUploaded: false,
      postUrl: 'http://localhost:5000/api/uploads'
    };
  },
  methods: {
    async change(event){
      this.showUploaded = false
      this.balmUI.onChange('files', event)
      for(const file of this.files) { await this.upload(file)}
      this.showUploaded =  true
      window.location.reload()
    },
    async upload(file) {
      try {
        var data = new FormData()
        data.append('file', file.sourceFile)

        fetch(this.postUrl, {
          method: 'POST',
          body: data
        })
        file.uploaded = true;
        console.log(`${file.name} is uploaded`);
      } catch (e) {
        // your code
      }
    }
  }
};
</script>

<style scoped lang="scss">

.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(100%);
}
.list-leave-active {
  position: absolute;
}

.preview-list {
  display: flex;
  flex-wrap: wrap;
  padding: 1em 0 0 1em;
  position: relative;
& > .item {
    width: 12.5%;
    padding-right: 1em;
    margin-bottom: 1em;
    list-style: none;
    transition: all 1s;
.inner {
  width: 100%;
}
.preview {
  display: block;
  width: 100%;
  height: 0;
  padding-bottom: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  border: 1px solid #ddd;
  border-radius: 3px;
}
.name {
  display: block;
  width: 100%;
  line-height: 1.8em;
  text-align: center;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
}
}

/* extends demo2 */
.preview-list {
& > .item {
.actions {
  display: flex;
  align-items: center;
  justify-content: space-around;
  height: 48px;
}
&.add-btn {
.mdc-file {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 100%;
  border: 1px solid #ddd;
  border-radius: 3px;
  cursor: pointer;
  background-color: #fff;
}
.add-icon {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-size: 48px;
}
}
}
}

</style>