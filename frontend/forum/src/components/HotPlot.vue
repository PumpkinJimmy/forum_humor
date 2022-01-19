<template>
    <svg :id="'hot-plot-' + tname"></svg>
</template>

<script>
import axios from 'axios'
import * as d3 from 'd3'
export default {
    name: 'HotPlot',
    props: ['tname', 'ratio', 'strokeWidth'],
    data(){
        return {
            cnt: {},
        }
    },
    mounted(){
        axios.get(`http://${this.$store.state.api}/api/v1/hot/tag_hot/${this.tname}/`)
            .then((resp)=>{
                this.cnt = resp.data.hot_data;
                // d3.select('#hot-plot').append('text').text('HAHA');
                const ts = this.cnt.map(d=>d.timestamp)
                const min_ts = Math.min(...ts)
                const max_ts = Math.max(...ts)
                const max_cnt = Math.max(...this.cnt.map(d=>d.count))
                const height = 600;
                const ratio = this.ratio ? Number(this.ratio): 1;
                const width = height * ratio;
                var svg = d3.select(`#hot-plot-${this.tname}`);
                svg.attr('viewBox', [0, 0, width, height])
                var scaleY = d3.scaleLinear()
                    .domain([0, max_cnt])
                    .range([height, 0])
                
                var scaleX = d3.scaleTime()
                    .domain([new Date(min_ts), new Date(max_ts)])
                    .range([0, width*0.95])
                // svg.selectAll('g').data(this.cnt).enter()
                //     .append('circle')
                //     .attr('cx', function(d) {
                //     return scaleX(d.timestamp);
                //     })
                //     .attr('cy', function(d) {
                //     return scaleY(d.count);
                //     })
                //     .attr('r', 5)
                this.cnt = this.cnt.sort((a,b)=>(a.timestamp > b.timestamp))
                const line = d3.line()
                    .x(d=>scaleX(d.timestamp))
                    .y(d=>scaleY(d.count))
                const strokeWidth = this.strokeWidth ? this.strokeWidth : 2
                svg
                    .append('path')
                    .attr('d', line(this.cnt))
                    .attr('fill', 'none')
                    .attr('stroke-width', strokeWidth)
                    .attr('stroke', 'black')
                //     .attr('stroke', '#eeeeee')
                //     .attr('stroke-width', 1)
                    // .transition()
                    // .duration(750)
                    // .ease(d3.easeLinear)
                    // .attrTween("d", (d) => {
                    // let it = d3.interpolate(d.startAngle, d.endAngle);
                    // return function (t) {
                    //     d.endAngle = it(t);
                    //     return arc(d);
                    // };
                    // });
                // svg.selectAll('rect')
                //     .data(this.cnt).enter()
                //     .append('rect')
                //     .attr('x', function(d) {return scaleX(d.timestamp)})
                //     .attr('y', d=>600-scaleY(d.count))
                //     .attr('width', 5)
                //     .attr('height', d=>scaleY(d.count))
            })
        
    }
}
</script>