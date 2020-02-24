<template>
  <div class="pure-g">
    <div class="pure-u-1-2">
      <table class="ws-tbl pure-table pure-table-horizontal pure-table-striped">
        <tr>
          <th>#</th>
          <th>Workspace</th>
          <th>Address</th>
          <th>Actions</th>
        </tr>
        <tr v-for="(workspace, index) in workspaces"
            v-bind:key="workspace.id"
            v-bind:class="{ selected: selectedWorkspaceIndex == index }"
            v-on:mouseover="selectedWorkspaceIndex = index">
          <td>{{index + 1}}</td>
          <td>{{workspace.name}}</td>
          <td>{{workspace.address}}</td>
          <td><router-link :to="'/workspaces/' + workspace.id">manage</router-link></td>
        </tr>
      </table>
    </div>
    <div class="pure-u-1-2">
      <div class="ws-map" ref="map"></div>
    </div>
  </div>
</template>

<style scoped lang="scss">
  @import "~leaflet/dist/leaflet.css";
  @import "../styles/vars";

  .ws-tbl {
    width: 95%;

    tr.selected td { background: $highlight5 }

    td {
      cursor: pointer;
      font-size: 12px;
      padding: (16/12)*0.5em (16/12)*1em;
    }

    th {
      text-align: left;
      background: $theme3;
      color: #eee;
      font-weight: 500;
      font-variant: small-caps;
      text-transform: lowercase;
    }

    th:nth-child(1),
    td:nth-child(1) {
      text-align: right;
    }
  }

  .ws-map {
    border: 1px dashed $theme1;
    display: block;
    width: 100%;
    height: 100%;
  }
</style>  

<script>

import L from 'leaflet'
import axios from 'axios'
import { leafletOptions } from '../config'

/** @type {L.Icon} default marker */
const defaultIcon = new L.Icon.Default()
/** @type {L.Icon} highlighted/selected marker */
const selectedIcon = new (L.Icon.Default.extend({
  options: {
    iconUrl: 'marker-icon-selected.png'
  }
}))

export default {
  name: 'workspaces',

  data () {
    return {
      workspaces: [],
      selectedWorkspaceIndex: -1
    }
  },

  beforeCreate () {
    /** @type {L.Map} leaflet map instance */
    this.$map = null
    /** @type {Array<L.Marker>} one marker for each workspace */
    this.$markers = []
  },

  mounted () {
    this.$map = L.map(this.$refs.map)
      .setView(leafletOptions.position, leafletOptions.zoom)
      .addLayer(L.tileLayer(
        leafletOptions.tileSource,
        { attribution: leafletOptions.attribution }
      ))

    axios.get('/api/0.1.0/workspaces')
      .then(response => this.workspaces = response.data.results)
  },

  beforeDestroy () {
    this.$map.remove()
  },

  watch: {
    workspaces (workspaces) {
      this.$markers.forEach(m => m.remove())
      this.$markers = workspaces.map(({ latitude, longitude }, index) =>
        L.marker([latitude, longitude])
          .on('mouseover', () => this.selectedWorkspaceIndex = index)
          .addTo(this.$map)
      )
    },
    selectedWorkspaceIndex (newIndex, oldIndex) {
      if (oldIndex > -1) this.$markers[oldIndex].setIcon(defaultIcon)
      this.$markers[newIndex].setIcon(selectedIcon)
    }
  }
}
</script>
