<template>
  <div class="pure-g">
    <div class="schedule-header pure-u-1-1">
      <h2>Worspace: {{workspace.name}}
        <small>
          Address: {{workspace.address}} &#8226;
          Location: <a target="_blank" :href="`https://www.openstreetmap.org/#map=12/${workspace.latitude}/${workspace.longitude}`">
            {{workspace.latitude}}, {{workspace.longitude}}
          </a>
        </small>
      </h2>
    </div>
    <div class="schedule-nav pure-u-1-1">
      <p>This view shows the workspace's offices and its reservations for week <input id="week" type="number" min="1" max="52" v-model="week"/> of the current year. The number of reservations is limited by the number of desks available. The reservations are sorted chronologically in order to spot congestions easier and find remaining space, well time actually.</p>
    </div>
    <div class="schedule-container pure-u-1-1">
      <div class="schedule">
        
        <div class="schedule-timescale">
          <div class="schedule-corner">Office</div>
          <div class="schedule-day-head"
               v-for="date in weekdates">
            
            <div class="date">{{formatDateOfWeek(week, date)}}</div>
            <div class="hours">
              <span class="hour">9H</span>
              <span class="hour">12H</span>
              <span class="hour">15H</span>
              <span class="hour">18H</span>
            </div>
          </div>
        </div>

        <div class="schedule-week"
             v-for="office in offices"
             :style="{ height: (reservations[office.id] || nullReservations).maxPerDay * 16 + 'px' }">
          
          <div class="schedule-week-head">
            <span class="office-label">{{office.label}}</span>
            ({{office.capacity}} desks on {{office.size}}m<sup>2</sup>)
          </div>
          
          <div class="schedule-day"
               v-for="date in weekdates">
            
            <div class="reservation"
                 v-for="(reservation, index) in ((reservations[office.id] || nullReservations).reservations[date] || [])"
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
  $day-head-height: 32px;
  $week-head-width: 144px;
  $schedule-width: $px-per-hour * $hours-per-week + $week-head-width;

  [class*=" pure-u"] {
    margin-top: 1em;
  }

  .schedule-header {
    h2 > small {
      font-size: 14px;
      margin-bottom: -.2em;
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

  .schedule-timescale {
    position: sticky;
    z-index: 15;
    top: 0;
    width: $schedule-width;
    height: $day-head-height;
    display: flex;
    flex-direction: row;

    background: white url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8'%3E%3Cpath d='M8 0 V8 8 H0 8' stroke='%23999' stroke-width='1' fill='none'/%3E%3C/svg%3E") 0 0 repeat-x;
    background-position: left bottom;
  }

  .schedule-corner {
    position: sticky;
    z-index: 20;
    top: 0;
    left: 0;
    width: $week-head-width;
    height: $day-head-height;
    background: #fff;
    padding: .5em 1em;
    border: 1px solid #aaa;
    border-top: none;
  }

  .schedule-day-head {
    display: flex;
    flex-direction: column;
    justify-content: center;

    width: $px-per-hour*9;
    height: $day-head-height;
    border-right: 1px solid #aaa;

    .date {
      display: block;
      text-align: center;
    }

    .hours {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      padding: .2em;
    }
    
    .hour {
      color: #999;
      background: #fff
    }
  }

  .schedule-week {
    display: flex;
    flex-direction: row;
    width: $schedule-width;
    // height: see template;

    // thx: https://yoksel.github.io/url-encoder/;
    background: transparent url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='16'%3E%3Cpath d='M8 0 V8 16 H0 8' stroke='%23ccc' stroke-width='1' fill='none'/%3E%3C/svg%3E") 0 0 repeat;
    
    &:nth-child(2n) {
      background-color: #eee;
      & .schedule-week-head {
        background-color: #eee;
      }
    }
  }

  .schedule-week-head {
    position: sticky;
    z-index: 10;
    left: 0;
    width: $week-head-width;
    height: 100%;
    padding: .5em 1em;
    background: #fff;
    &:nth-child(2n) {
      background: #eee;
    }
    border-left: 1px solid #aaa;
    border-right: 1px solid #aaa;
  }

  .office-label {
    display: block;
    white-space: nowrap;
    text-overflow: ellipsis;
  }

  .schedule-day {
    position: relative;
    display: inline-block;
    width: $px-per-hour*9;
    height: 100%;
    border-right: 1px solid #aaa;
  }

  .reservation {
    position: absolute;
    height: 13px;
    border-top: 1px solid #666;
    border-left: 1px solid #666;
    border-radius: 3px;
    background: $theme3;
  }
</style>

<script>

import axios from 'axios'
import moment from 'moment'
import { groupBy, sortBy, partial, reduce, mapValues, range } from 'lodash'
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

  computed: {
    weekdates () {
      // TODO explicitely choose monday as first day of week (locale)
      const m = moment().week(this.week).startOf('week')
      return range(5).map(d => m.add(1, 'days').date())
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
        top: index * 16 + 1,
        // offices open at nine o'clock
        left: (timeToHours(r.begin) - 9) * PX_PER_HOUR,
        // bar length depends duration
        width: millisToHours(duration(r)) * PX_PER_HOUR
      }, px)
    },

    /** pure function to format date in week */
    formatDateOfWeek (week, date) {
      return moment().week(week).date(date).format('dddd, Do MMM')
    }
  }
}  

</script>