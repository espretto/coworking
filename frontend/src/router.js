import Vue from 'vue'
import VueRouter from 'vue-router'

import About from '@/components/about.vue'
import Workspace from '@/components/workspace.vue'
import Workspaces from '@/components/workspaces.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: { name: 'workspaces' }
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
