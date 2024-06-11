document.addEventListener("DOMContentLoaded", function() {
    var nodes = new vis.DataSet(JSON.parse(document.getElementById('nodes').textContent));
    var edges = new vis.DataSet(JSON.parse(document.getElementById('edges').textContent));

    var container = document.getElementById('mynetwork');
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {
        layout: {
            hierarchical: {
                direction: "UD",
                sortMethod: "hubsize",
                nodeSpacing: 200,
                treeSpacing: 300,
                levelSeparation: 300
            }
        },
        physics: {
            enabled: true,
            hierarchicalRepulsion: {
                nodeDistance: 300,
                centralGravity: 0.0,
                springLength: 300,
                springConstant: 0.01,
                damping: 0.09
            },
            solver: 'hierarchicalRepulsion',
            stabilization: {
                iterations: 1000
            }
        },
        nodes: {
            shape: 'box',
            margin: 20,
            font: {
                size: 16,
                face: 'Arial',
                vadjust: 10
            },
            widthConstraint: {
                minimum: 200,
                maximum: 300
            }
        },
        edges: {
            arrows: {
                to: {enabled: true, scaleFactor: 1}
            }
        },
        interaction: {
            navigationButtons: true,
            keyboard: true
        }
    };
    var network = new vis.Network(container, data, options);

    network.on("click", function (params) {
        if (params.nodes.length === 1) {
            var nodeId = params.nodes[0];
            window.location.href = '/soru/' + nodeId + '/';
        }
    });
});
