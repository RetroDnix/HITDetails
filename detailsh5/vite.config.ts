// Plugins
import vue from '@vitejs/plugin-vue'
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

// Utilities
import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({ 
      template: { transformAssetUrls }
    }),
    // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vite-plugin
    vuetify({
      autoImport: true,
      styles: {
        configFile: 'src/styles/settings.scss',
      },
    }),
  ],
  build: {
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true,
      },
    },
  },
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
    extensions: [
      '.js',
      '.json',
      '.jsx',
      '.mjs',
      '.ts',
      '.tsx',
      '.vue',
    ],
  },
  server: {
    port: 3000,
    // cors: true, // 默认启用并允许任何源
    // open: true, // 在服务器启动时自动在浏览器中打开应用程序
    // //反向代理配置，注意rewrite写法，开始没看文档在这里踩了坑
    // proxy: {// 本地开发环境通过代理实现跨域，生产环境使用 nginx 转发
    //   '/Imageapi': {
    //     target: 'http://116.204.83.124:9003/api/v1', // 通过代理接口访问实际地址。这里是实际访问的地址。vue会通过代理服务器来代理请求
    //     changeOrigin: true,
    //     ws: true,  // 允许websocket代理
    //     rewrite: (path) => path.replace(/^\/Imageapi/, '') // 将api替换为空
    //   }
    // }
  }
})
