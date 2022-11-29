import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import '@/jquery'
import 'semantic-ui-css/semantic.min.css'
import 'semantic-ui-css/semantic'

const app = createApp(App)
app.use(router)
app.mount('#app')

