
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000'
      },
      '/static': {
        target: 'http://localhost:8000'
      }
    }
  }
}
