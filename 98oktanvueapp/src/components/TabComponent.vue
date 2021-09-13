<template>
  <v-container>
    <StationDetails v-model="dialog" :station="station" />
    <v-card>
      <v-card-title>
        <gmap-autocomplete @place_changed="goToSearchLocation">
          <template v-slot:input="slotProps">
            <v-text-field
              ref="input"
              v-model="search"
              v-on:listeners="slotProps.listeners"
              v:on="slotProps.attrs"
            ></v-text-field>
          </template>
        </gmap-autocomplete>
        <v-spacer></v-spacer>

        <v-btn color="primary" @click="goToCurrentLocation">Min plats</v-btn>
      </v-card-title>
      <v-card-text>
        <v-tabs v-model="tab" grow slider-color="primary">
          <v-tab key="map_tab">Karta</v-tab>
          <v-tab key="list_tab">Lista</v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab" touchless>
          <v-tab-item key="map_tab">
            <GoogleMap
              ref="maps"
              @showStationDetails="showStationDetails"
              :station="this.station"
            />
          </v-tab-item>
          <v-tab-item key="list_tab"
            ><StationList
              @showStationDetails="showStationDetails"
              @showStationOnMap="showStationOnMap"
              :station="this.station"
            />
          </v-tab-item>
        </v-tabs-items>
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
      tab: "map_tab",
      search: "",
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
    showStationDetails(station) {
      console.log(station.station);
      this.station = station;
      this.dialog = true;
    },
    showStationOnMap(station) {
      this.station = station;
      const maps = this.$refs.maps;
      maps.reCenterAt(station.position);
      this.tab = "map_tab";
    },
    goToSearchLocation(loc) {
      this.goToLocation(loc.geometry.location);
    },
    goToLocation(pos) {
      const maps = this.$refs.maps.$refs.maps;
      maps.$mapPromise.then((map) => {
        map.panTo(pos);
      });
    },
    goToCurrentLocation() {
      navigator.geolocation.getCurrentPosition((res) => {
        this.goToLocation(res);
      });
    },
  },
};
</script>
