/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

import { createApp } from 'vue'
import App from './App.vue'
import store from './store';

// Vuetify
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi' 
import { md3 } from 'vuetify/blueprints'
import router from './router'
import { VBottomSheet } from 'vuetify/labs/VBottomSheet'
import { VDatePicker } from 'vuetify/labs/VDatePicker'
import { pl, zhHans } from 'vuetify/locale'

const vuetify = createVuetify({
  components: {
    VDatePicker,
    VBottomSheet,
  },
  locale: {
    locale: 'zhHans',
    fallback: 'sv',
    messages: { zhHans, pl},
  },
  directives,
  blueprint: md3,
  icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
        mdi,
        },
    }
})

const app = createApp(App)
app.use(vuetify)
app.use(router)
app.use(store)
app.mount('#app')

