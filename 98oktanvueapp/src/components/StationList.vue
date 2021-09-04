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
        :search="search"
        mobile-breakpoint="5"
        light
      ></v-data-table>
    </v-card>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Namn",
          align: "start",
          sortable: true,
          value: "name",
        },
        { text: "Avstånd (km)", value: "distance" },
        { text: "Adress", value: "adress" },
        { text: "98 Oktan", value: "oktan" },
      ],
      stations: [
        {
          name: "St1",
          distance: 159,
          adress: "Södra vägen 14 Uddevalla",
          oktan: "Ja",
        },
        {
          name: "OKQ8",
          distance: 256,
          adress: "Oslovägen 22 Strömstad",
          oktan: "Ja",
        },
        {
          name: "Tanka",
          distance: 159,
          adress: "Centrumvägen 1 Dingle",
          oktan: "Ja",
        },
        {
          name: "Trollhättan",
          distance: 12,
          adress: "Brastadsgatan 44",
          oktan: "Ja",
        },
      ],
    };
  },
};
</script>