import Vue from 'vue'
import App from '@/components/app.vue'
import router from './router.js'

Vue.config.productionTip = false

new Vue({ router, render: h => h(App) }).$mount('#app')
