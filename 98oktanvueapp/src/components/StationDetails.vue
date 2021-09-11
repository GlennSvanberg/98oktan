<template>
  <v-dialog
    transition="dialog-bottom-transition"
    max-width="800"
    v-model="show"
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

        <v-btn color="primary" text @click.stop="show = false"> Stäng </v-btn>
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