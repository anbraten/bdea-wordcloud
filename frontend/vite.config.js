import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'
import WindiCSS from 'vite-plugin-windicss'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), WindiCSS()],
  resolve: {
    alias: {
      '~/': `${path.resolve(__dirname, 'src')}/`,
      // vue: 'vue/dist/vue.esm-bundler.js',
      'balm-ui-plus': 'balm-ui/dist/balm-ui-plus.esm.js',
      'balm-ui-css': 'balm-ui/dist/balm-ui.css'
    }
  },
  server: {
    host: '0.0.0.0',
    proxy: {
      '/api': 'http://localhost:5000/'
    },
    hmr: {
      clientPort: process.env.GITPOD_HOST ? 443 : undefined,
    }
  }
})
