#!/usr/bin/env node

var offices = JSON.parse(require('fs').readFileSync(`${__dirname}/../fixtures/13-offices.json`, { encoding: 'utf8' }))

/**
 * helpers
 */
function randomInteger (min, max) {
  return Math.round(min + Math.random() * (max - min))
}

function choose (choices) {
  var index = randomInteger(0, choices.length - 1)
  return choices[index]
}

function isOverlapping (a, b) {
  return a.begin < b.begin ? a.end > b.begin : a.begin < b.end
}

function count (array, predicate) {
  var len = array.length, i = -1, count = 0;
  while (++i < len) if (predicate(array[i], i, array)) count++
  return count
}

/**
 * main
 */
var reservations = []
var workspaceClientMap = {}

while (reservations.length < 1500) {

  var day = choose([
    17, 18, 19, 20, 21,
    24, 25, 26, 27, 28
  ])
  
  var [open, close] = choose([
    ['09:00', '12:30'],
    ['14:00', '18:00']
  ])

  var client_id = randomInteger(1, 100)
  var workspace_id = workspaceClientMap[client_id] || (workspaceClientMap[client_id] = randomInteger(1, 10))
  var workspaceOffices = offices.filter(o => o.fields.workspace_id === workspace_id)
  var office = choose(workspaceOffices)

  var reservation = {
    begin: new Date(`2020-02-${day}T${open}:00Z`),
    end: new Date(`2020-02-${day}T${close}:00Z`),
    office_id: office.pk,
    client_id: client_id
  }

  var overlapping = reservations.filter(r => isOverlapping(r, reservation))
  
  // see if client has the time
  if (overlapping.some(r => r.client_id === client_id)) {
    continue
  }

  if (count(overlapping, r => r.office_id === reservation.office_id) > office.fields.capacity) {
    continue
  }

  reservations.push(reservation)
}

/**
 * output
 */
var envelope = { model: 'coworking.reservation', pk: 0, fields: null }

console.log("[" + reservations
  .map((r, i) => {
    envelope.pk = i + 1
    envelope.fields = r
    return JSON.stringify(envelope)
  })
  .join(",\n") + "]")
