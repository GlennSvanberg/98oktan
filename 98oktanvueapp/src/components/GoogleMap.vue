<template>
  
  <v-container>
    
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
            v-for="(m, index) in locationMarkers"
            :position="m.position"
            @click="center = m.position"
            :icon="markerOptions"
          ></gmap-marker>
        </gmap-map>
      </v-card-text>
    </v-card>
  <v-spacer/>
    <v-card color="primary" dark>
      <v-card-title class="headline">
        Stationer med 98 oktan nära dig
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Sök"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="stations"
        :items-per-page="25"
        :search="search"
        mobile-breakpoint="5"
        light
      ></v-data-table>
    </v-card>
  </v-container>
</template>
 
<script>
const mapMarker = require("../assets/logo.png");
import stationFile from "./../assets/stations.json";
export default {
  name: "AddGoogleMap",
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
      locationMarkers: [],
      locPlaces: [],
      existingPlace: null,
    };
  },

  mounted() {
    this.locateGeoLocation();
    //this.locationMarkers.push({ position: okMarker });
    this.stations.forEach(station => {
      this.locationMarkers.push({position: station.location})
    });
  },

  methods: {
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
};
//OKQ8 Uddevalla 58.353525935703004, 11.916708812107629
</script>
