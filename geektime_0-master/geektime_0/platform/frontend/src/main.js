import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import jQuery from 'jquery';
window.jQuery = jQuery;
require('semantic-ui-css/semantic.min.css');
require('semantic-ui-css/semantic');

const app = createApp(App)
app.use(router)
app.mount('#app')

