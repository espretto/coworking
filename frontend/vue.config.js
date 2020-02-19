
var path = require('path')

/** TODO: sass does not rewrite image urls on @import, leaflet's images cannot be found */
const leafletAssetsPath = path.join(__dirname, 'node_modules/leaflet/dist')

module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000'
      },
      '/static': {
        target: 'http://localhost:8000'
      }
    }
  },
  css: {
    loaderOptions: {
      css: {
        url: false
      }
    }
  }
}
