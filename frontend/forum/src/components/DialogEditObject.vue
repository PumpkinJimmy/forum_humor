<template>
  <v-dialog v-model="value" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="text-h5">{{type == 'create' ? "Create Object" : "Edit Object"}}</span>
      </v-card-title>

      <v-card-text>
        <v-container>
          <v-row
          v-for="(ftype,fname,idx) in model.fields"
          :key="idx">
          <v-col cols="12">
            <v-text-field 
            v-if="(ftype=='char')"
            :label="fname"
            >
            </v-text-field>

            <v-text-field
            v-if="ftype=='email'"
            :label="fname"
            :rules="[rules.email]">
            </v-text-field>

            <v-text-field
            v-if="ftype=='auto'"
            :label="fname">
            </v-text-field>

            <v-text-field
            v-if="ftype=='password'"
            :label="fname">
            </v-text-field>

            <v-select
            v-if="ftype=='enum'"
            :label="fname"
            >
            </v-select>

            <v-select
            v-if="ftype=='foreign'"
            :label="fname"
            >
            </v-select>

            <v-file-input 
            v-if="(ftype == 'image') || (ftype=='file')"
            :label="fname"
            ></v-file-input>

            <v-input
            v-if="ftype == 'datetime'"
            :label="fname"
            >
            <datepicker :date="tmp"></datepicker>
            </v-input>
           
          </v-col>
          </v-row>
        </v-container>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="normal" text @click="close"> Cancel </v-btn>
        <v-btn color="primary" text @click="save"> Save </v-btn>
        <v-btn color="error" text @click="del"> Delete </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import Datepicker from 'vue-datepicker';
export default {
  name: "DialogEditObject",
  props: ["model", "value", "type"],
  components:{
    datepicker: Datepicker
  },
  data(){
    return {
      tmp: {},
      componentType:{
        email: 'V-text-field',
        enum: 'v-text-field',
        password: 'v-text-field',
        image: 'v-textarea',
        auto: 'v-text-field',
        char: 'v-text-field',
        integer: 'v-text-field',
      },
      rules: {
          required: value => !!value || 'Required.',
          counter: value => value.length <= 20 || 'Max 20 characters',
          email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
        },
    }
  },
  watch: {
      value(bool){
          this.$emit('input', bool);
      }
  },
  methods:{
    close(){
      this.value = false;
    },
    save(){

    },
    del(){

    }
  }
};
</script>
