<template>
  <v-container>
    <StationDetails v-model="dialog" :station="station" />
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Sök"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-card-text>
        <v-tabs grow slider-color="primary">
          <v-tab>Karta</v-tab>
          <v-tab>Lista</v-tab>
          <v-tab-item>
            <GoogleMap
              @showStationDialog="doSomething"
              :station="this.station"
            />
          </v-tab-item>
          <v-tab-item><StationList /> </v-tab-item>
        </v-tabs>
      </v-card-text>
    </v-card>
  </v-container>
</template>
<script>
import GoogleMap from "./GoogleMap.vue";
import StationList from "./StationList.vue";
import StationDetails from "./StationDetails.vue";
export default {
  data() {
    return {
      dialog: false,
      station: null,
    };
  },
  components: {
    GoogleMap,
    StationList,
    StationDetails,
  },
  methods: {
    doSomething(station) {
      console.log(station.station);
      this.station = station;
      this.dialog = true;
    },
  },
};
</script>
