var width = window.innerWidth;
var height = 1010;

var svg = d3.select("#network-graph")
  .append("svg")
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", `0 0 ${width} ${height}`)
  .attr("preserveAspectRatio", "xMinYMin meet")
  .style("display", "block");
   
    // .attr("preserveAspectRatio", "xMinYMin meet")

// Fetch data from the JSON endpoint
fetch('/jsongraph/')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        var nodes = data.nodes;
        var links = data.links;
        
        var simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id))
            .force("charge", d3.forceManyBody().strength(-100))
            .force("center", d3.forceCenter(width / 2, height / 2))
            .force("x", d3.forceX())
            .force("y", d3.forceY());

        var link = svg.selectAll(".link")
            .data(links)
            .enter()
            .append("line")
            .attr("class", "link");

        var node = svg.selectAll(".node")
            .data(nodes)
            .enter()
            .append("circle")
            .attr("class", "node")
            .attr("r", 10)
            .style("fill", d => d.color)
            .call(drag(simulation)) // Enable drag behavior for nodes
            // .on("click", showTooltip);// Show tooltip when the node is clicked
            .on("mouseover", function(d){tooltip.text(d); return tooltip.style("visibility", "visible");})
            .on("mousemove", function(){return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
            .on("mouseout", function(){return tooltip.style("visibility", "hidden");});

        node.append("title")
            .text(d => d.title);

        simulation.on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            // Set boundary constraints for nodes
            node
                .attr("cx", d => Math.max(10, Math.min(width - 10, d.x)))
                .attr("cy", d => Math.max(10, Math.min(height - 10, d.y)));
        });

        // Function to enable drag behavior for nodes
        function drag(simulation) {
            function dragStarted(event, d) {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }

            function dragged(event, d) {
                d.fx = event.x;
                d.fy = event.y;
            }

            function dragEnded(event, d) {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }

            return d3.drag()
                .on("start", dragStarted)
                .on("drag", dragged)
                .on("end", dragEnded);
        }

       
  var filteredNodes = null


function handleSearch() {
    var searchValue = document.getElementById("search-input").value.toLowerCase();

   
    var filteredNodes = nodes.filter(node => node.title.toLowerCase().includes(searchValue));

    var filteredlinks = links.filter(link =>{
        return filteredNodes.some(node => node.title === link.source.title) &&
                filteredNodes.some(node => node.title === link.target.title);
    });

    var linkselection = svg.selectAll('.link')
        .data(filteredlinks)

    // Update the node selection with the filtered nodes
    var nodeSelection = svg.selectAll(".node")
        .data(filteredNodes, d => d.title);


    linkselection.exit().remove();
    nodeSelection.exit().remove();

    var newLinkselection = linkselection.enter()
    .append('line')
    .attr('class', 'link')
    .merge(linkselection)

    // Append new nodes from the filtered selection
    var newNodeSelection = nodeSelection.enter()
        .append("circle")
        .attr("class", "node")
        .attr("r", 10)
        .style("fill", d => d.color)
        .call(drag(simulation))
        // .on("hover", showTooltip)
        .on("mouseover", function(d){tooltip.text(d); return tooltip.style("visibility", "visible");})
      .on("mousemove", function(){return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
      .on("mouseout", function(){return tooltip.style("visibility", "hidden");})
        .merge(nodeSelection); // Merge the enter and update selections

    // Update the node positions using the simulation
    simulation.nodes(filteredNodes)
        .on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);
            
            newLinkselection
            .attr('x1', d => Math.max(10, Math.min(width - 10, d.source.x)))
            .attr('y1', d => Math.max(10, Math.min(width - 10, d.source.y)))
            .attr('x2', d => Math.max(10, Math.min(width - 10, d.target.x)))
            .attr('y2', d => Math.max(10, Math.min(width - 10, d.target.y)))
            // Set boundary constraints for nodes
            newNodeSelection
                .attr("cx", d => Math.max(10, Math.min(width - 10, d.x)))
                .attr("cy", d => Math.max(10, Math.min(height - 10, d.y)));
        });

        node
                .attr("cx", d => Math.max(10, Math.min(width - 10, d.x)))
                .attr("cy", d => Math.max(10, Math.min(height - 10, d.y)));

    simulation.alpha(1).restart(); // Restart the simulation to update the positions
}

// Attach the search event to the input field
document.getElementById("search-input").addEventListener("input", handleSearch);


})
    .catch(error => console.error('Error fetching data:', error));


