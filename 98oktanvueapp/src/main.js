import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

import * as VueGoogleMaps from "vue2-google-maps"
import VueGtag from "vue-gtag";


Vue.config.productionTip = false


Vue.use(VueGtag, {
  config: { id: 'UA-101647824-2' }
});


Vue.use(VueGoogleMaps, {
  load: {
    key: "APIKEY",
    libraries: "places"
  }
})


new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
