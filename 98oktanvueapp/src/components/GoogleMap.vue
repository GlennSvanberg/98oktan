<template>
  <v-container>
    <div class="text-center">
      <v-dialog
        transition="dialog-bottom-transition"
        v-model="dialog"
        max-width="800"
      >
        <v-card v-if="station != null">
          <v-card-title class="text-h5 grey lighten-2">
            {{ station.station }}, {{ station.short_address }}
          </v-card-title>

          <v-card-text>
            <br />Adress:{{ station.formatted_address }} <br />98 Oktan:
            {{ station.oktan }}<br />
            <a v-bind:href="station.source">Källa</a>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-btn color="primary" text :href="`${navigate(station)}`">
              Navigera hit
            </v-btn>
            <v-spacer></v-spacer>

            <v-btn color="primary" text @click="dialog = false"> Stäng </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>

    <v-card>
      <v-card-title class="headline">
        Sök plats
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Sök"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-card-text>
        <label>
          <gmap-autocomplete @place_changed="initMarker"></gmap-autocomplete>
        </label>
        <br />
        <gmap-map
          :zoom="10"
          :center="center"
          style="width: 100%; height: 600px"
        >
          <gmap-marker
            :key="index"
            v-for="(station, index) in stations"
            :position="station.position"
            @click="showStation(station)"
            :icon="markerOptions"
          ></gmap-marker>
        </gmap-map>
      </v-card-text>
    </v-card>
  </v-container>
</template>
 
<script>
const mapMarker = require("../assets/logo.png");
import stationFile from "./../assets/stations.json";
export default {
  data() {
    return {
      dialog: false,
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
      ],
      stations: stationFile,
      markerOptions: {
        url: mapMarker,
        size: { width: 60, height: 75, f: "px", b: "px" },
        scaledSize: { width: 30, height: 45, f: "px", b: "px" },
      },
      center: {
        lat: 58.55519704544182,
        lng: 11.45177158556096,
      },
      markers: [],
      existingPlace: null,
      station: null,
    };
  },

  methods: {
    navigate(station) {
      console.log(station.formatted_address);
      const base_url = "https://www.google.com/maps/dir/?api=1";
      const encoded_address = encodeURIComponent(station.formatted_address);
      const address_query = "&destination=" + encoded_address;
      const nav = "&dir_action=navigate";
      return base_url + address_query + nav;
    },
    showStation(station) {
      this.station = station;
      this.dialog = true;
      console.log(station.formatted_address);
    },
    initMarker(loc) {
      this.existingPlace = loc;
    },
    locateGeoLocation: function () {
      navigator.geolocation.getCurrentPosition((res) => {
        this.center = {
          lat: res.coords.latitude,
          lng: res.coords.longitude,
        };
      });
    },
  },
  mounted() {
    this.locateGeoLocation();
    this.stations.forEach((station) => {
      this.markers.push({
        station,
      });
    });
  },
};
//OKQ8 Uddevalla 58.353525935703004, 11.916708812107629
</script>
