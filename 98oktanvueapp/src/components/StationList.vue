<template>
  <v-data-table
    :headers="headers"
    :items="stations"
    :items-per-page="25"
    :search="search"
    mobile-breakpoint="5"
    light
    @click:row="handleClick"
  >
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-1" @click="showOnMap(item)">
        mdi-map-marker
      </v-icon>
      <v-icon small class="mr-1" @click="showDetails(item)">
        mdi-information
      </v-icon>
    </template>
  </v-data-table>
</template>
<script>
import stationFile from "./../assets/stations.json";
export default {
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Namn",
          align: "start",
          sortable: true,
          value: "station",
        },
        { text: "Ort", value: "short_address" },
        { text: "Adress", value: "formatted_address" },
        { text: "98 Oktan", value: "oktan" },
        { text: "Karta", value: "actions", sortable: false },
      ],
      stations: stationFile,
    };
  },
  methods: {
    handleClick(station) {
      console.log("Row clicked", station.station);

      //this.$emit("showStationDetails", station);
    },
    showDetails(station) {
      console.log(station);
      this.$emit("showStationDetails", station);
    },
    showOnMap(station) {
      console.log("showOnMap");
      console.log(station);
      this.$emit("showStationOnMap", station);
    },
  },
};
</script>