<template>
    <div class="emotion-view">
        <svg id="emotion-plot"></svg>
    </div>
</template>
<script>
import axios from 'axios';
import * as d3 from 'd3';
export default {
    name: 'EmotionView',
    data(){
        return{
            rows: {}
        }
    },
    mounted(){
        axios.get('http://127.0.0.1:5000/api/v1/ml/infer_all/')
            .then((resp)=>{
                var rows = resp.data.res;
                var row = rows[0];
                for (var i in row){
                    if (row[i] < 0){
                        delete row[i]
                    }
                }
                var pie = d3.pie()
                var color = d3.schemeCategory10;
                var dat = Object.values(row);
                //var maxv = Math.max(...dat), minv = Math.min(...dat);
                // dat = dat.map(x=>(x-minv)/(maxv-minv));
                console.log(JSON.stringify(dat))
                var piedata = pie(dat)
                var arc = d3.arc()
                    .innerRadius(0)
                    .outerRadius(40)

                var plot = d3.select('#emotion-plot');
                plot.attr('viewBox', '-100 -100 200 200')


                var arcs = plot.selectAll('g')
                 .data(piedata)
                 .enter()
                arcs
                 .append('path')
                 .attr('fill', (d,i)=>color[i])
                 .attr('d', d=>arc(d))
                arcs
                 .append('text')
                 .text((_,i)=>{
                     var label = Object.keys(row)[i];
                     console.log(label)
                     return label})
                 .attr('transform', (d)=>{
                     var pos = arc.centroid(d);
                     return `translate(${pos})`;
                 })
                 .attr("text-anchor","middle")
                 .attr('font-size', '7px')
                 
            })
    }
}
</script>