<template>
  <v-data-table
    :headers="headers"
    :items="stations"
    :items-per-page="25"
    :search="search"
    :sort-by.sync="sortBy"
    :sort-desc.sync="sortDesc"
    mobile-breakpoint="5"
    light
    @click:row="handleClick"
  >
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-1" @click="showDetails(item)">
        mdi-information
      </v-icon>
    </template>
    <template v-slot:[`item.map`]="{ item }">
      <v-icon small class="mr-1" @click="showOnMap(item)">
        mdi-map-marker
      </v-icon>
    </template>
  </v-data-table>
</template>
<script>
import stationFile from "./../assets/stations.json";
export default {
  data() {
    return {
      sortBy: "Namn",
      sortDesc: false,
      pos: "",
      search: "",
      headers: [
        {
          text: "Namn",
          align: "start",
          sortable: true,
          value: "station",
        },
        { text: "Ort", value: "short_address", sortable: false },
        { text: "Adress", value: "formatted_address", sortable: false },
        { text: "Avstånd", value: "distance" },
        { text: "Detaljer", value: "actions", sortable: false },
        { text: "Karta", value: "map", sortable: false },
      ],
      stations: stationFile,
    };
  },
  props: ["searchPos"],
  watch: {
    searchPos: function (newVal) {
      this.sortByDistance(newVal);
    },
  },
  mounted: function () {
    if (this.searchPos) {
      this.sortByDistance(this.searchPos);
    }
  },
  methods: {
    handleClick(station) {
      console.log("Row clicked", station.station);

      //this.$emit("showStationDetails", station);
    },
    showDetails(station) {
      this.$emit("showStationDetails", station);
    },
    showOnMap(station) {
      this.$emit("showStationOnMap", station);
    },
    sortByDistance(pos) {
      this.pos = pos;
      this.stations.forEach((s) => {
        s.distance = Math.round(
          this.distance(pos.lat, pos.lng, s.position.lat, s.position.lng)
        );

        this.sortBy = "distance";
      });
    },
    distance(lat1, lon1, lat2, lon2) {
      var radlat1 = (Math.PI * lat1) / 180;
      var radlat2 = (Math.PI * lat2) / 180;
      var theta = lon1 - lon2;
      var radtheta = (Math.PI * theta) / 180;
      var dist =
        Math.sin(radlat1) * Math.sin(radlat2) +
        Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
      if (dist > 1) {
        dist = 1;
      }

      dist = Math.acos(dist);
      dist = (dist * 180) / Math.PI;
      dist = dist * 60 * 1.1515;

      // Turn to Km
      dist = dist * 1.609344;

      return dist;
    },
  },
};
</script>