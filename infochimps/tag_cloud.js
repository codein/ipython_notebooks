d3.json("/tags_all.json", function(tags) {
var fill = d3.scale.category20();
var fontSize = fontSize = function(size) {
  if (size > 400) {
    return size / 10;
  } else if (400 > size && size > 200) {
    return size / 6;
  } else {
    return size / 3;
  }
};
  function draw(words) {
    d3.select("body").append("svg")
        .attr("width", 2000)
        .attr("height", 1000)
      .append("g")
        .attr("transform", "translate(1000,500)")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }

  d3.layout.cloud().size([2000, 1000])
      .words(tags)
      .padding(5)
      .rotate(0)
      .font("Impact")
      // .fontSize(function(d) { return d.size; })
      .fontSize(function(d) { return fontSize(d.size); })

      .on("end", draw)
      .start();
});