<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="12">
        <v-card>
          <v-card-title class="headline"
            >Vilka bilar stödjer E10?
          </v-card-title>
          

          <v-card-text > 
              <v-autocomplete 
              v-model="car" 
              :items="cars"
              append-icon="mdi-magnify"
                return-object 
                item-text="brand"
                ></v-autocomplete>
                    <h3>
                        {{car.brand}}
                        
                    </h3>
                    <br/>
                      <v-container>
                        <v-row        v-for="item in car.info"
                        :key="item">
                        <v-text>
                            {{item}}
                        </v-text>
                            
                       </v-row>
                       <v-row v-if="car">
                           
                            <v-text ><br/>Källa: Bil Sweden</v-text>
                       </v-row>
                       
                      </v-container>
                      
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import carsFile from "./../assets/cars.json";

export default {
  data() {
    return {
      car: "",
      cars: carsFile

      }
    }
  }
</script>
