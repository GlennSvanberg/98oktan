<template>
  <gmap-map
    :zoom="10"
    :center="center"
    style="width: 100%; height: 600px"
    ref="maps"
    :options="{
      zoomControl: true,
      mapTypeControl: false,
      scaleControl: false,
      streetViewControl: false,
      rotateControl: false,
      fullscreenControl: false,
      disableDefaultUi: true,
    }"
  >
    <gmap-marker
      :key="index"
      v-for="(station, index) in stations"
      :position="station.position"
      @click="showStation(station)"
      :icon="markerOptions"
    ></gmap-marker>
  </gmap-map>
</template>
 
<script>
const mapMarker = require("../assets/logo.png");
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
      ],
      stations: stationFile,
      markerOptions: {
        url: mapMarker,
        size: { width: 60, height: 75, f: "px", b: "px" },
        scaledSize: { width: 30, height: 45, f: "px", b: "px" },
      },
      center: {
        lat: 57.55519704544182,
        lng: 11.45177158556096,
      },
      markers: [],
      station: null,
    };
  },
  methods: {
    reCenterAt(pos) {
      console.log("recentering:", pos);
      this.center = pos;
    },
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
      this.$emit("showStationDetails", this.station);
      console.log(station.formatted_address);
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
