import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/components/home.vue'
import About from '@/components/about.vue'
import Workspaces from '@/components/workspaces.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/workspaces/',
    name: 'Workspaces',
    component: Workspaces
  },
  {
    path: '/about/',
    name: 'About',
    component: About
  }
]

export default new VueRouter({ routes })
