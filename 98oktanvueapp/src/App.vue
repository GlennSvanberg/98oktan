<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="d-flex align-center pl-8 pr-4">
        <v-img
          alt="98 Oktan logo"
          class=""
          contain
          :src="logo"
          transition="scale-transition"
          width="45"
        />
      </div>

      <h1 class="p2 display-2 font-weight-bold mb-3 pt-3">98 Oktan</h1>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main class="primary lighten-3">
      <WelcomeMessage />
      <TabComponent />
      <FooterComponent />
      <v-footer padless color="primary" dark>
        <v-col class="text-center" cols="12">
          {{ new Date().getFullYear() }} — &copy;98oktan.se
        </v-col>
      </v-footer>
    </v-main>
  </v-app>
</template>

<script>
import WelcomeMessage from "./components/WelcomeMessage";

import TabComponent from "./components/TabComponent.vue";
import FooterComponent from "./components/FooterComponent.vue"
const logoFile = require("./assets/pumplogo.png");
export default {
  name: "App",
  components: {
    WelcomeMessage,
    TabComponent,
    FooterComponent,
  },

  data: () => ({
    logo: logoFile,
  }),
};
</script>
