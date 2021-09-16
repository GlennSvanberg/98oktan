<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center">
        <v-img
          alt="98 OKTAN LOGO"
          class=""
          contain
          :src="logo"
          transition="scale-transition"
          width="200"
        />
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main class="primary lighten-3">
      <WelcomeMessage />
      <TabComponent />
    </v-main>
  </v-app>
</template>

<script>
import WelcomeMessage from "./components/WelcomeMessage";

import TabComponent from "./components/TabComponent.vue";
const logoFile = require("./assets/98oktanFull.png");
export default {
  name: "App",
  components: {
    WelcomeMessage,
    TabComponent,
  },

  data: () => ({
    logo: logoFile,
  }),
};
</script>
