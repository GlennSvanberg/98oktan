<template>
  <v-data-table
    :headers="headers"
    :items="stations"
    :items-per-page="25"
    :search="search"
    mobile-breakpoint="5"
    light
  ></v-data-table>
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
      ],
      stations: stationFile,
    };
  },
};
</script>