
import L from 'leaflet'

export const apiVersion = '0.1.0'

export const leafletOptions = {
  zoom: 12,
  position: [47.21627, -1.54936],
  tileSource: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  imageBasePath: '/leaflet/'
}

// adjust image path to environment
L.Icon.Default.prototype.options.imagePath = leafletOptions.imageBasePath
