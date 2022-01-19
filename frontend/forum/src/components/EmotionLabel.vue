<template>
    <v-chip :class="emotion" :color="colorOf[emotion]">
        {{ emotion }}
    </v-chip>
</template>
<style scoped>
.anger{
    background-color:red;
    color:antiquewhite;
}
.joy{
    background-color: orange;
    color:antiquewhite;
}
.sadness{
    background-color:blueviolet;
    color:antiquewhite;
}
.fear{
    color:antiquewhite;
}
.surprise{
    color: black;
}

.love{
    color: antiquewhite;
}
</style>
<script>
import axios from 'axios'
export default {
  name: "EmotionLabel",
//   props: ['uid'],
  data(){
      return {
          summary: {},
          colorOf:{
              joy: 'orange',
              anger: 'red',
              sadness: 'purple',
              fear: 'green',
              love: 'pink',
              surprise: 'yellow',
          }
      }
  },
  computed: {
      emotion(){
        // return 'joy';
        for (var em in this.summary){
            if (this.summary[em] > 0.3){
                return em;
            }
        }
        return 'unknown';
      }
  },
  mounted(){
      axios.get(`http://${this.$store.state.api}/api/v1/ml/infer_user/${this.$store.state.user.uid}/`)
      .then((resp)=>{
          this.summary = this.calcSummary(resp.data.res);
      })
  },
  methods: {
    calcSummary(emotions) {
      var summary = {};
      if (!emotions) return;
      for (var k in emotions[0]) {
        summary[k] = 0;
      }
      for (var row of emotions) {
        var s = 0;
        for (var i in row) {
          row[i] = Math.exp(row[i]);
          s += row[i];
        }
        for (i in row) {
          summary[i] += row[i] / s / emotions.length;
        }
      }
      return summary;
    },
  },
};
</script>