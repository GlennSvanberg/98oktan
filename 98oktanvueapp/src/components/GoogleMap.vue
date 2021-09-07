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

          <button @click="addLocationMarker">Add</button>
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
  </v-container>
</template>
 
<script>
const mapMarker = require("../assets/logo.png");
export default {
  name: "AddGoogleMap",
  data() {
    return {
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
    const okMarker = {
      lat: 58.353525935703004,
      lng: 11.916708812107629,
    };
    this.locationMarkers.push({ position: okMarker });
  },

  methods: {
    initMarker(loc) {
      this.existingPlace = loc;
    },
    addLocationMarker() {
      if (this.existingPlace) {
        const marker = {
          lat: this.existingPlace.geometry.location.lat(),
          lng: this.existingPlace.geometry.location.lng(),
        };
        this.locationMarkers.push({ position: marker });
        this.locPlaces.push(this.existingPlace);
        this.center = marker;
        this.existingPlace = null;
      }
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
