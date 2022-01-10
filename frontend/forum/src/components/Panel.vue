<template>
  <div class="panel">
    <v-row>
      <v-col cols="10">
          <ObjectListEditor :modelName="modelName" />
      </v-col>
      <v-col cols="2">
        <v-card>
          <v-list>
            <v-subheader>Models</v-subheader>
            <v-list-item-group color="primary">
              <v-list-item
                v-for="(modelName, idx) in models"
                :key="idx"
                @click="setModel(modelName)"
                >{{ modelName }}
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from 'axios';
import ObjectListEditor from "./ObjectListEditor.vue";
export default {
  name: "Panel",
  data(){
      return {
          models: {},
          modelName: null,
      }
  },
  components: {
    ObjectListEditor,
  },
  mounted(){
      axios.get('http://127.0.0.1:5000/api/v1/model')
      .then((response)=>{
        this.models = response.data.models
      })
  },
  methods:{
      setModel(modelName){
          this.modelName = modelName;
      }
  }
}; 
</script>