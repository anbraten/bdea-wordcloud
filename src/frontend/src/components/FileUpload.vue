<template>
  <transition-group class="preview-list" name="list" tag="ul">
    <li v-for="(file, index) in files3" :key="file.tmpId" class="item">
      <div class="inner">
        <span class="preview" :style="setBg(file)"></span>
        <span class="actions">
        <ui-fab
            v-if="!file.uploaded"
            icon="publish"
            mini
            @click="upload(file)"
        ></ui-fab>
        <ui-fab icon="delete" mini @click="remove(index)"></ui-fab>
      </span>
      </div>
    </li>
    <li v-if="files3.length < limit" key="add" class="item add-btn">
      <div class="inner">
        <ui-file accept="text/plain" multiple preview @change="onChange">
          <ui-icon class="add-icon">add</ui-icon>
        </ui-file>
      </div>
    </li>
  </transition-group>
  <p>
    <ui-button raised @click="uploadAllFiles">
      <ui-icon>publish</ui-icon>
      Upload All
    </ui-button>
  </p>
</template>

<script>
import { useEvent } from 'balm-ui';

export default {
  name: 'FileUpload',
  data() {
    return {
      files: [],
      files3: [],
      limit: 5,
      postUrl: 'http://localhost:5000/api/uploads'
    };
  },
  methods: {
    setBg({ previewSrc }) {
      return previewSrc ? { backgroundImage: `url(${previewSrc})` } : {};
    },
    onChange(files) {
      if (files.length > this.limit - this.files3.length) {
        this.$toast(`Image Limit: ${this.limit}`);
      } else {
        files.forEach((file) => {
          file.uploaded = false;
          this.files3.push(file);
        });
      }
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
    },
    uploadAllFiles() {
      if (this.files3.length) {
        this.files3.forEach((file) => {
          this.upload(file);
        });
      } else {
        this.$toast('No files');
      }
    },
    remove(index) {
      this.files3.splice(index, 1);
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