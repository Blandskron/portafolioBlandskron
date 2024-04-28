var colores = d3.schemeCategory20;

function fill(i, vector) {
  return vector[i % vector.length];
}

var data = [
    { text: "Effective Communication", size: 60 },
    { text: "Teamwork", size: 50 },
    { text: "Problem Solving", size: 40 },
    { text: "Adaptability", size: 20 },
    { text: "Critical Thinking", size: 50 },
    { text: "Creativity", size: 10 },
    { text: "Continuous Learning", size: 70 },
    { text: "Time Management", size: 40 },
    { text: "Empathy", size: 20 },
    { text: "Resilience", size: 30 }
];

var containerWidth = document.getElementById('wordcloud-container').offsetWidth;
var containerHeight = containerWidth * 0.5;

var layout = d3.layout.cloud()
    .size([containerWidth, containerHeight])
    .words(data)
    .padding(10)
    .rotate(0)
    .font("Questrial")
    .fontSize(function (d) { return d.size; })
    .on("end", draw);

layout.start();

function draw(words) {
    d3.select("#wordcloud-container").append("svg")
        .attr("width", containerWidth)
        .attr("height", containerHeight)
        .append("g")
        .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
        .selectAll("text")
        .data(words)
        .enter().append("text")
        .style("font-size", function (d) { return d.size + "px"; })
        .style("font-family", "Questrial")
        .style("fill", function (d, i) { return fill(i, colores); })
        .attr("text-anchor", "middle")
        .attr("transform", function (d) {
            return "translate(" + [d.x, d.y] + ")";
        })
        .text(function (d) { return d.text; });
}
