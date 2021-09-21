<template>
  <v-dialog
    transition="dialog-bottom-transition"
    max-width="800"
    v-model="show"
  >
    <v-card v-if="station != null">
      <v-card-title class="text-h5 grey lighten-2">
        {{ station.station }},<br />
        {{ station.short_address }} {{ station.city }}
      </v-card-title>

      <v-card-text class="pr-20">
        <table class="pt-4 text-body-1 lighten-2 table-fixed">
          <tr>
            <td class="font-weight-bold">Adress:</td>
            <td class="truncate">
              {{ station.formatted_address }}
            </td>
          </tr>
          <tr>
            <td class="font-weight-bold">Avstånd:</td>
            <td class="truncate">{{ station.distance }} km</td>
          </tr>

          <tr>
            <div class="ma-6"></div>
          </tr>
          <tr>
            <td class="font-weight-bold">Har 98 Oktan:</td>
            <td class="truncate">
              {{ station.oktan }}
            </td>
          </tr>
          <tr>
            <td class="font-weight-bold">Bekräftat den:</td>
            <td class="truncate">
              {{ station.updated }}
            </td>
          </tr>
          <tr>
            <td class="font-weight-bold">Källa:</td>
            <td class="truncate">
              <a class="truncate" v-bind:href="station.source">{{
                station.source
              }}</a>
            </td>
          </tr>
          <tr>
            <td>
              <v-btn class="primary ma-4" text @click="showOnMap">
                Karta
              </v-btn>
            </td>
            <td>
              <v-btn class="primary ma-4" text :href="`${navigate(station)}`">
                Navigera hit
              </v-btn>
            </td>
          </tr>
        </table>
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