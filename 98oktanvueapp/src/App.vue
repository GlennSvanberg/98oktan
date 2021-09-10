<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
        <v-spacer></v-spacer>
        <h1>98 Oktan</h1>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main class="primary lighten-3">
      <WelcomeMessage />
      <GoogleMap />
    </v-main>
  </v-app>
</template>

<script>
import WelcomeMessage from "./components/WelcomeMessage";
import GoogleMap from "./components/GoogleMap.vue";

export default {
  name: "App",

  components: {
    GoogleMap,
    WelcomeMessage,
  },

  data: () => ({
    //
  }),
};
</script>
