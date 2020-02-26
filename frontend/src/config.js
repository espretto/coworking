
/**
 * coworking api config
 */
export const apiVersion = '0.1.0'

/**
 * leaflet config
 */
import L from 'leaflet'

export const leafletOptions = {
  zoom: 12,
  position: [47.21627, -1.54936],
  tileSource: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  imageBasePath: '/leaflet/'
}

// adjust image path to environment
L.Icon.Default.prototype.options.imagePath = leafletOptions.imageBasePath
L.Icon.Default.prototype.options.iconRetinaUrl = L.Icon.Default.prototype.options.iconUrl

/**
 * axios (ajax) config
 */
import axios from 'axios'

var ISO_8601 = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;

function dateReviver (key, value) {
  return typeof value === 'string' && ISO_8601.test(value) ? new Date(value) : value
}

axios.defaults.transformResponse = [function (data) {
  if (typeof data === 'string') {
    try {
      data = JSON.parse(data, dateReviver);
    } catch (e) { /* Ignore */ }
  }
  return data;
}]