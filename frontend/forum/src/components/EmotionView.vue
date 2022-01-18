<template>
    <div class="emotion-view">
        <emotion-pie :emotion="rows[2]"></emotion-pie>
        <!-- <svg id="emotion-plot"></svg> -->
    </div>
</template>
<script>
import axios from 'axios';
import EmotionPie from './EmotionPie.vue'
// import * as d3 from 'd3';
export default {
    name: 'EmotionView',
    data(){
        return{
            rows: []
        }
    },
    components: {EmotionPie},
    mounted(){
        axios.get('http://localhost:5000/api/v1/ml/infer_all/')
            .then((resp)=>{
                
                var rows = resp.data.res;
                this.rows = rows;
                // var row = rows[2];
                // var s = 0;
                // for (var i in row){
                //     row[i] = Math.exp(row[i]);
                //     s += row[i];
                // }
                // for (i in row){
                //     row[i] /= s;
                // }
                // console.log(row);
                // var pie = d3.pie()
                // var color = d3.schemeCategory10;
                // var dat = Object.values(row);

                // var piedata = pie(dat)
                // var arc = d3.arc()
                //     .innerRadius(0)
                //     .outerRadius(40)

                // var plot = d3.select('#emotion-plot');
                // plot.attr('viewBox', '-100 -100 200 200')


                // var arcs = plot.selectAll('g')
                //  .data(piedata)
                //  .enter()
                // arcs
                //  .append('path')
                //  .attr('fill', (d,i)=>color[i])
                //  .attr('d', d=>arc(d))
                //  .transition()
                //  .duration(750)
                //  .ease(d3.easeLinear)
                //  .attrTween('d', (d)=>{
                //      let it = d3.interpolate(d.startAngle,d.endAngle);
                //      return function(t){
                //          d.endAngle= it(t);
                //          return arc(d);
                //      }
                //  })
                // arcs
                //  .append('text')
                //  .text((_,i)=>{
                //      var label = Object.keys(row)[i];
                //      return label})
                //  .attr('transform', (d)=>{
                //      var pos = arc.centroid(d);
                //      return `translate(${pos})`;
                //  })
                //  .attr("text-anchor","middle")
                //  .attr('font-size', '7px')
                
            })
    }
}
</script>