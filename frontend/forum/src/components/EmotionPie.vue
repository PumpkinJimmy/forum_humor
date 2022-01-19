<template>
  <div>
    <v-row>
      <v-col cols="9">
        <svg id="emotion-plot"></svg>
      </v-col>
      <v-col cols="3">
        <table id="emotion-legend">
          <tr v-for="(text, idx) of legend" :key="idx">
            <td>{{text}}</td>
            <td><div class="rect" :style="'background-color: ' + color[idx]"></div></td>
          </tr>
          <!-- <tr>
            <td>angry</td>
            <td>haha</td>
          </tr>
          <tr>
            <td>happy</td>
            <td>hehe</td>
          </tr> -->
        </table>
      </v-col>
    </v-row>
  </div>
</template>

<style scoped>
#emotion-legend {
  font-size: 0.8em;
}
.rect{
  width: 0.8em;
  height: 0.8em;
  /* background-color: red; */
}
</style>
<script>
import * as d3 from "d3";
export default {
  name: "EmotionPie",
  props: ["emotion"],
  data(){
    return {
      legend: [],
      summary: {},
      color: d3.schemeCategory10,
    }
  },
  mounted() {
    this.calcSummary();
    this.drawPie(this.summary);
  },
  watch: {
    emotion() {
      this.calcSummary();
      this.drawPie(this.summary);
    },
  },
  methods: {
    calcSummary(){
      
      if (!this.emotion) return;
      for (var k in this.emotion[0]){
        this.summary[k] = 0
      }
      for (var row of this.emotion){
        var s = 0;
        for (var i in row) {
          row[i] = Math.exp(row[i]);
          s += row[i];
        }
        for (i in row) {
          this.summary[i] += row[i] / s;
        }
      }
      console.log(this.summary)
    },
    drawPie(row) {
      this.legend = Object.keys(row);
      // var s = 0;
      
      console.log(row);
      var pie = d3.pie();
      var color = d3.schemeCategory10;
      var dat = Object.values(row);

      var piedata = pie(dat);
      var arc = d3.arc().innerRadius(0).outerRadius(40);

      var plot = d3.select("#emotion-plot");
      plot.attr("viewBox", "-100 -100 200 200");

      var arcs = plot.selectAll("g").data(piedata).enter();
      arcs
        .append("path")
        .attr("fill", (d, i) => color[i])
        .attr("d", (d) => arc(d))
        .transition()
        .duration(750)
        .ease(d3.easeLinear)
        .attrTween("d", (d) => {
          let it = d3.interpolate(d.startAngle, d.endAngle);
          return function (t) {
            d.endAngle = it(t);
            return arc(d);
          };
        });
    },
  },
};
</script>