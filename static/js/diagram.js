document.addEventListener("DOMContentLoaded", function() {
    var nodesElement = document.getElementById('nodes');
    var edgesElement = document.getElementById('edges');
    var currentNodeId = document.getElementById('currentNodeId'); // Aktif sorunun ID'si için

    if (nodesElement && edgesElement) {
        var allNodes = JSON.parse(nodesElement.textContent);
        var allEdges = JSON.parse(edgesElement.textContent);
        var currentId = currentNodeId ? parseInt(currentNodeId.textContent) : null;

        var nodes = new vis.DataSet(allNodes);
        var edges = new vis.DataSet(allEdges);

        // Aktif sorunun rengini değiştir
        if (currentId !== null) {
            nodes.update({id: currentId, color: {background: 'lightgreen', border: 'black'}, font: {color: 'black'}});
        }

        var container = document.getElementById('mynetwork');
        var data = {
            nodes: nodes,
            edges: edges
        };
        var options = {
            layout: {
                hierarchical: {
                    direction: "UD", // Yukarıdan aşağıya doğru düzen
                    sortMethod: "hubsize", // Düğümleri hub büyüklüğüne göre sırala
                    nodeSpacing: 200, // Düğümler arası mesafe
                    treeSpacing: 300, // Ağaç yapısındaki düğümler arası mesafe
                    levelSeparation: 300 // Seviye arası mesafe
                }
            },
            physics: {
                enabled: false, // Fiziksel simülasyon devre dışı
            },
            nodes: {
                shape: 'box', // Düğüm şekli
                margin: 20,
                font: {
                    size: 16,
                    face: 'Arial',
                    vadjust: 10,
                    color: 'black'
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
                navigationButtons: true, // Navigasyon butonları aktif
                keyboard: true // Klavye ile etkileşim aktif
            }
        };

        var network = new vis.Network(container, data, options);

        // Düğüme tıklanıldığında düğümü genişletin ve ilgili soru detay sayfasına yönlendirme yapın
        network.on("click", function (params) {
            if (params.nodes.length === 1) {
                var nodeId = params.nodes[0];
                window.location.href = '/soru/' + nodeId + '/';
            }
        });
    } else {
        console.error("Nodes or edges element not found");
    }
});
