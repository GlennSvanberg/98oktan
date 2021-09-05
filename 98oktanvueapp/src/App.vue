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

    <v-main class="primary lighten-1">
      <WelcomeMessage />
      <StationList />
    </v-main>
  </v-app>
</template>

<script>
import WelcomeMessage from "./components/WelcomeMessage";
import StationList from "./components/StationList";

export default {
  name: "App",

  components: {
    WelcomeMessage,
    StationList,
  },

  data: () => ({
    //
  }),
};
</script>
