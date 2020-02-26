<template>
  <div class="pure-g">
    <div class="schedule-header pure-u-1-1">
      <h2>Worspace: {{workspace.name}} <small>Address: {{workspace.address}} &#8226; Location: <a target="_blank" :href="`https://www.openstreetmap.org/#map=12/${workspace.latitude}/${workspace.longitude}`">{{workspace.latitude}}, {{workspace.longitude}}</a></small></h2>
    </div>
    <div class="schedule-nav pure-u-1-1">
      <form class="pure-form" action="javascript:void(0);">
        <label for="week">Week of Year</label>
        <input id="week" type="number" min="1" max="52" v-model="week"/>
      </form>
    </div>
    <div class="schedule-container pure-u-1-1">
      <div class="schedule">
        <div class="schedule-week"
             v-for="office in offices"
             :style="{ height: (reservations[office.id] || nullReservations).maxPerDay * 16 + 'px' }">
          
          <div class="schedule-week-head">
            {{office.label}}<br>
            ({{office.capacity}} desks on {{office.size}}m<sup>2</sup>)
          </div>
          
          <div class="schedule-day"
               v-for="(perDay, day) in (reservations[office.id] || nullReservations).reservations">
            
            <div class="reservation"
                 v-for="(reservation, index) in perDay"
                 :style="reservationStyles(reservation, index)">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
  @import '../styles/vars';

  $px-per-hour: 32px;
  $hours-per-day: 9;
  $hours-per-week: $hours-per-day * 5;
  $week-head-width: 140px;

  [class*=" pure-u"] {
    margin-top: 1.5em;
  }

  .schedule-header {
    h2 > small {
      float: right;
    }
  }

  .schedule-nav {
    #week {
      width: 50px;
      margin-left: .5em;
    }
  }

  .schedule-container {
    font-size: 12px;
    display: grid;
    overflow: scroll;
    max-height: 520px;
  }

  .schedule {
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
  }

  .schedule-week {
    display: flex;
    flex-direction: row;
    width: $px-per-hour * $hours-per-week + $week-head-width;
    // height: see template;

    &:nth-child(2n+1) {
      background: #eee;
    }
  }

  .schedule-week-head {
    position: sticky;
    z-index: 10;
    left: 0;
    width: $week-head-width;
    height: 100%;
    padding: .5em 1em;
    box-sizing: border-box;
    background: #eee;
  }

  .schedule-day {
    position: relative;
    display: inline-block;
    width: $px-per-hour*9;
    height: 100%;
  }

  .reservation {
    position: absolute;
    height: 15px;
    border-top: 1px solid #666;
    border-left: 1px solid #666;
    border-radius: 2px;
    background: $theme3;
  }
</style>

<script>

import axios from 'axios'
import moment from 'moment'
import { groupBy, sortBy, partial, reduce, mapValues } from 'lodash'
import { apiVersion } from '../config'

/**
 * constants
 */
const PX_PER_HOUR = 32

/**
 * helpers
 */
const _ = partial.placeholder
const sortOffices = partial(sortBy, _, 'capacity')
const groupByDay = partial(groupBy, _, r => r.begin.getDate())
const groupByOffice = partial(groupBy, _, 'office')
const sortReservations = partial(sortBy, _, 'begin', duration);
const maxItemLength = partial(reduce, _, (len, item) => Math.max(item.length, len), 0)

/** avoid subpixel rendering */
function px (n) {
  return Math.floor(n) + 'px'
}

/** hours with minute precision */
function timeToHours (d) {
  return d.getHours() + d.getMinutes() / 60
}

/** milliseconds to hours */
function millisToHours (m) {
  return m / 36e5
}

/** reservation duration in milliseconds */
function duration (r) {
  return r.end - r.begin
}

/**
 * component prototype
 */
export default {
  name: 'workspace',

  data () {
    return {
      week: moment().week(),
      offices: [],
      workspace: {},
      reservations: {},
      
      // fallback object
      nullReservations: {
        maxPerDay: 3,
        reservations: []
      }
    }
  },

  mounted () {
    const workspaceId = this.$route.params.id

    axios.get(`/api/${apiVersion}/workspaces/${workspaceId}/`)
      .then(response => this.workspace = response.data)
    
    axios.get(`/api/${apiVersion}/offices/`, { params: { workspace: workspaceId }})
      .then(response => this.offices = sortOffices(response.data.results))

    this.fetchReservations(this.week)
  },

  watch: {
    week (week) {
      this.fetchReservations(week);
    }
  },

  methods: {
    fetchReservations (week) {
      const options = {
        params: {
          week,
          workspace: this.$route.params.id
        }
      }

      axios.get(`/api/${apiVersion}/reservations/`, options).then(response => {

        // group reservations by office (row) and day (column) for tabular presentation
        this.reservations = mapValues(groupByOffice(response.data.results), perOffice => {
          var perDay = mapValues(groupByDay(perOffice), sortReservations)
          var maxPerDay = maxItemLength(perDay)
          return { maxPerDay, reservations: perDay }
        })
      })
    },

    reservationStyles (r, index) {
      return mapValues({
        // order is governed by `sortReservations`
        top: index * 16,
        // offices open at nine o'clock
        left: (timeToHours(r.begin) - 9) * PX_PER_HOUR,
        // bar length depends duration
        width: millisToHours(duration(r)) * PX_PER_HOUR
      }, px)
    }
  }
}  

</script>