import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/components/home.vue'
import About from '@/components/about.vue'
import Workspace from '@/components/workspace.vue'
import Workspaces from '@/components/workspaces.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/workspaces/',
    name: 'workspaces',
    component: Workspaces,
  },
  {
    path: '/workspaces/:id',
    name: 'workspace',
    component: Workspace
  },
  {
    path: '/about/',
    name: 'about',
    component: About
  }
]

export default new VueRouter({ routes })
