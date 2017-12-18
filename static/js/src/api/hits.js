function getHits() {
  return fetch('api/hits').then(data => data.json)
}