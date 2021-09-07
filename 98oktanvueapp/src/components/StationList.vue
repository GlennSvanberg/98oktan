<template>
  <v-container>
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
          value: "Station",
        },
        { text: "Ort", value: "City" },
        { text: "Adress", value: "Adress" },
        { text: "98 Oktan", value: "Oktan" },
      ],
      stations: stationFile,
    };
  },
};
</script>