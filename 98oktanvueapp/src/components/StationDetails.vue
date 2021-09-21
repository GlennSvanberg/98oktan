<template>
  <v-dialog
    transition="dialog-bottom-transition"
    max-width="600"
    v-model="show"
    persistent
    no-click-animation
  >
    <v-card class="text-wrap" v-if="station != null">
      <v-card-title class="text-h5 grey lighten-2">
        {{ station.station }},<br />
        {{ station.short_address }} {{ station.city }}
      </v-card-title>

      <v-card-text>
        <v-container>
          <v-row no-gutters>
            <v-col class="font-weight-bold md-4"> Adress: </v-col>
            <v-col class="md-8">
              {{ station.formatted_address }}
            </v-col>
          </v-row>

          <v-row no-gutters>
            <v-col class="font-weight-bold md-4"> Avstånd: </v-col>
            <v-col class="md-8"> {{ station.distance }} km </v-col>
          </v-row>
          <div class="ma-8"></div>

          <v-spacer></v-spacer>

          <v-row no-gutters>
            <v-col class="font-weight-bold md-4"> Bekräftat 98 oktan: </v-col>
            <v-col class="md-8">
              {{ station.updated }}
            </v-col>
          </v-row>

          <v-row no-gutters>
            <v-col class="font-weight-bold md-4">Källa:</v-col>
            <v-col class="md-8">
              <a v-bind:href="station.source">{{ station.source }}</a>
            </v-col>
          </v-row>
          <v-row>
            <v-col class="md-6">
              <v-btn class="primary" text @click="showOnMap">
                Visa på Karta
              </v-btn></v-col
            >
            <v-col class="md-6">
              <v-btn class="primary" text :href="`${navigate(station)}`">
                Navigera hit
              </v-btn></v-col
            >
          </v-row>
        </v-container>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="error" text @click.stop="show = false"> Stäng </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
    };
  },
  props: {
    value: Boolean,
    station: Object,
  },
  computed: {
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
  methods: {
    showOnMap(station) {
      this.$emit("showStationOnMap", station);
    },
    navigate(station) {
      console.log(station.formatted_address);
      const base_url = "https://www.google.com/maps/dir/?api=1";
      const encoded_address = encodeURIComponent(station.formatted_address);
      const address_query = "&destination=" + encoded_address;
      const nav = "&dir_action=navigate";
      return base_url + address_query + nav;
    },
  },
};
</script>
<style scoped>
.truncate {
  overflow-wrap: break-word;
}
.table-fixed {
  table-layout: fixed;
}
</style>