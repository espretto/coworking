#!/usr/bin/env node

var fs = require('fs')
var path = require('path')
var moment = require('moment')

/* -----------------------------------------------------------------------------
 * general purpose helpers
 */
function relative (filepath) {
  return path.join(__dirname, filepath)
}

function readJson (path) {
  return JSON.parse(fs.readFileSync(path, { encoding: 'utf8' }))
}

function randFloat (min, max) {
  return min + Math.random() * (max - min)
}

function randChoice (choices) {
  return choices[Math.floor(randFloat(0, choices.length-1))]
}

function nearest (num, step) {
  return (num % step > step/2 ? Math.ceil : Math.floor)(num / step) * step
}

function isOverlapping (a, b) {
  return a.begin < b.begin ? a.end > b.begin : a.begin < b.end
}

function count (array, predicate) {
  var len = array.length, i = -1, count = 0;
  while (++i < len) if (predicate(array[i], i, array)) count++
  return count
}

/* -----------------------------------------------------------------------------
 * domain specific helpers
 */

var clientWorkspaceMap = {}
function getClientWorkspace (client, workspaces) {
  // clients usually stay at the same workspace
  if (Math.random() < 0.95) {
    return clientWorkspaceMap[client.pk] || (clientWorkspaceMap[client.pk] = randChoice(workspaces))
  }
  else {
    return randChoice(workspaces)
  }
}

function getClientOffice(workspace, offices) {
  const workspaceOffices = offices.filter(office => office.fields.workspace_id === workspace.pk)
  return randChoice(workspaceOffices)
}

/* -----------------------------------------------------------------------------
 * main
 */
function main () {
  var clients = readJson(relative('../../backend/apps/coworking/fixtures/11-clients.json'))
  var offices = readJson(relative('../../backend/apps/coworking/fixtures/13-offices.json'))
  var workspaces = readJson(relative('../../backend/apps/coworking/fixtures/12-workspaces.json'))
  var reservations = []

  // prep
  var base = moment([2020, 1, 24, 12, 0, 0, 0])
  var offsets = [
    0, 1, 2,  3,  4, // this week
    7, 8, 9, 10, 11  // next week
  ]

  while (reservations.length < 5000) {

    // reservation start time
    var begin = randFloat(9, 16)
    var beginHours = Math.floor(begin)
    var beginMinutes = nearest((begin - beginHours) * 60, 15)
    
    // reservation end time
    var end = randFloat(begin + 1, 18)
    var endHours = Math.floor(end)
    var endMinutes = nearest((end - endHours) * 60, 15)

    // reservation date
    var localBase = base.clone().add(randChoice(offsets), 'days')

    // one client always stays within the same workspace
    var client = randChoice(clients)
    var workspace = getClientWorkspace(client, workspaces)
    var office = getClientOffice(workspace, offices)

    // composition
    var reservation = {
      begin: localBase.hours(beginHours).minutes(beginMinutes).toISOString(),
      end: localBase.hours(endHours).minutes(endMinutes).toISOString(),
      office_id: office.pk,
      client_id: client.pk
    }

    // validation
    var overlapping = reservations.filter(r => isOverlapping(r, reservation))
  
    // does the client have other engagements at the same time ?
    if (overlapping.some(r => r.client_id === client.pk)) {
      continue
    }
    // does the office have the capacity at the given time ?
    if (count(overlapping, r => r.office_id === reservation.office_id) >= office.fields.capacity) {
      continue
    }
    
    reservations.push(reservation)
  }

  outputReservations(reservations)  
}

/* -----------------------------------------------------------------------------
 * interfacing
 */

function outputReservations (reservations, file=process.stdout) {
  var envelope = { model: 'coworking.reservation', pk: 0, fields: null }
  
  file.write('[')
  
  reservations.forEach((r, i) => {
    envelope.pk = i + 1
    envelope.fields = r
    file.write(JSON.stringify(envelope))
    if (i + 1 !== reservations.length) file.write(',\n')
  })
  
  file.write(']')
}

if (require.main === module) {
  main()
}
