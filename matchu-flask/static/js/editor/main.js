
/**
* Add functionality to page. This ist for testing only.
*/
var chart = null;
var selectedNode1 = null;
var selectedNode2 = null;

$(document).ready(function(){
	$.ajaxSetup({async:false, cache: true});
	// create the flowchart instance
	chart = new FlowChart($);
	
	// add your node templates in a key-value format
	// where key is the name and css class of the node and value is the content

	// set the root element position coordinates
	chart.rootElementPosition = {left: 5, top: 5};

	// set offset between parent and child node
	// nodes are always added from left to right horizontally
	chart.offsetForNextElement = 150;
	chart.lastHovered = $("#start-node");
	// set the effect for node action end, like node creation or movement
	var setTimeoutConst;

	
	// add nodes actions
	chart.addNodeActions = function(nodeObj, chartInstanceObj){
		nodeObj.on('click', function(event) {
			window.clearTimeout(setTimeoutConst);
			if (chart.lastHovered != nodeObj) {
				chartInstanceObj.changePropertiesForm(nodeObj)
			}
			setTimeout(function(){
				nodeObject = _t.getNodeFromNodesObject(nodeObj[0]['id'].replace("#", ""))
				//$("#dialog").dialog("option", "title", nodeObject['name']);
				$('#dialog').dialog("option", 'show', {
					effect: "slide",
					direction: "right",
					duration: 500
			  	})
				$("#dialog").dialog("open");
				return false;
			})
		})
		
		nodeObj.on('dblclick', function(event) {
			window.clearTimeout(setTimeoutConst);
			if (chart.lastHovered != nodeObj) {
				chartInstanceObj.changePropertiesForm(nodeObj)
			}
			setTimeout(function(){
				nodeObject = _t.getNodeFromNodesObject(nodeObj[0]['id'].replace("#", ""))
				//$("#dialog").dialog("option", "title", nodeObject['name']);
				$('#dialog').dialog("option", show, {
					effect: "slide",
					direction: "right",
					duration: 500
			  	})
				$("#dialog").dialog("open");
				return false;
			})
		})
	
		
		nodeObj.on('mouseenter', function(event){
			setTimeoutConst = window.setTimeout(function() {
				chart.changePropertiesForm(nodeObj)
				chart.lastHovered = nodeObj
			}, 100)
		});
		nodeObj.on('mouseleave', function() {
			window.clearTimeout(setTimeoutConst);
		});
		nodeObj.on('contextmenu', function(event){
			if (!$('#dialog').dialog('isOpen')) {
				if (chart.getNode(nodeObj.attr('id'))['node_type_name'] == "start-node") {
					return false
				}

				chartInstanceObj.deleteNode(nodeObj.attr('id'));
				
				if (chart.lastHovered == nodeObj) {
					$("#dialog").html("");
				}
				return false;
			} else {
				return false
			}

			
		});
	};
});
