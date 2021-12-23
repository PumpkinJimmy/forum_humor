<template>
  <v-dialog v-model="value" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="text-h5">{{type == 'create' ? "Create Object" : "Edit Object"}}</span>
      </v-card-title>

      <v-card-text>
        <v-container>
          <v-row>
            <!-- <v-col
              v-for="(attr, idx) in model.attrs"
              :key="idx"
              cols="12"
              sm="6"
              md="4"
            >
              <v-text-field
                v-model="editedItem[attr]"
                :label="attr"
              ></v-text-field>
            </v-col> -->
          </v-row>
          <v-row
          v-for="( v, k, idx) in form"
          :key="idx">
          <v-col cols="12">
            <v-text-field
              v-model="form[k]"
              :label="k"
              ></v-text-field>
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
export default {
  name: "DialogEditObject",
  props: ["form", "value", "type"],
  watch: {
      value(bool){
          this.$emit('input', bool);
      }
  },
  methods:{
    close(){
      this.value = false;
    }
  }
};
</script>
