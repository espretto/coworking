<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <table>
      <tr>
        <th>Workspace</th>
        <th>Address</th>
        <th>Latitude</th>
        <th>Longitude</th>
      </tr>
      <tr v-for="ws in workspaces" v-bind:key="ws.id">
        <td>{{ws.name}}</td>
        <td>{{ws.address}}</td>
        <td>{{ws.latitude}}</td>
        <td>{{ws.longitude}}</td>
      </tr>
    </table>
    <div class="map" ref="map"></div>
  </div>
</template>

<script>
import axios from 'axios'
import L from 'leaflet'

L.Icon.Default.prototype.options.imagePath = '/leaflet/'

export default {
  name: 'schedule',

  props: {
    msg: String
  },

  data () {
    return {
      workspaces: []
    }
  },

  watch: {
    workspaces (workspaces) {
      this.$map.eachLayer(layer => {
        if (layer instanceof L.Marker) layer.remove()
      })
      workspaces.forEach(({ latitude, longitude }) => {
        this.$map.addLayer(L.marker([latitude, longitude], { riseOnHover: true }))
      })
    }
  },

  mounted () {
    axios.get('/api/0.1.0/workspaces')
      .then(r => (this.workspaces = r.data.results))

    this.$map = L.map(this.$refs.map).setView([47.21627, -1.54936], 13)
    this.$map.addLayer(L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }))
  },

  beforeDestroy () {
    this.$map.clearLayers()
    this.$map.remove()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

  .map {
    display: block;
    width: 600px;
    height: 400px;
  }
</style>
