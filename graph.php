<!DOCTYPE html>
<html>
<head>
<meta name="description" content="[An example of getting started with Cytoscape.js]" />
<link rel="stylesheet" type="text/css" href="style.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<meta charset=utf-8 />
<title>Cytoscape.js initialisation</title>
  <script src="http://cytoscape.github.io/cytoscape.js/api/cytoscape.js-latest/cytoscape.min.js"></script>
</head>
<body>
<?php
	$data = file_get_contents("https://graph.facebook.com/870175569_10153817832045570?fields=likes.fields(pic_square,name).limit(100),comments&access_token="); //change the access token here
	if($data) {
		$initx = 0;
		$inity = 0;
		$likes = json_decode($data);
		$real_likes = $likes->likes->data;
		$no = count($real_likes);
		$details = array();

		for($i=0; $i<$no; $i++) {
			$details[$i] = (string)($real_likes[$i]->name);
		}
	}
	echo '<script type="text/javascript">';
	echo '$(function(){';
	echo "$('#cy').cytoscape({
			  style: cytoscape.stylesheet()
			    .selector('node')
			      .css({
			        'content': 'data(name)',
			        'text-valign': 'center',
			        'color': 'white',
			        'text-outline-width': 2,
			        'text-outline-color': '#888'
			      })
			    .selector('edge')
			      .css({
			        'target-arrow-shape': 'triangle'
			      })
			    .selector(':selected')
			      .css({
			        'background-color': 'red',
			        'line-color': 'blue',
			        'target-arrow-color': 'blue',
			        'source-arrow-color': 'blue'
			      })
			    .selector('.faded')
			      .css({
			        'opacity': 0.25,
			        'text-opacity': 0
			      }),
			  
			  elements: {
			    nodes: [
			    	{ position:{x:450, y:300}, data: { id: 'post-id:870175569_10153929919780570', name: 'fb Post' } },";

		    for($i=0;$i<$no;$i++) {
		    	$initx = $initx+100;
		    	$inity +=100;
		    	echo "{ position:{ x:$initx, y:$inity }, data: { id: '$details[$i]' , name: '$details[$i]'  } },";
		    }

    		echo " ], edges: [";

		    for($i=0;$i<$no;$i++) {
		    	echo "{ data: { source:'post-id:870175569_10153929919780570' , target: '$details[$i]' } },";
		    }
			    echo "]
			  },
			  
			  ready: function(){
			    window.cy = this;
			    
			    // giddy up...
			    
			    cy.elements().selectify();
			    
			    cy.on('tap', 'node', function(e){
			      var node = e.cyTarget; 
			      var neighborhood = node.neighborhood().add(node);
			      
			      cy.elements().addClass('faded');
			      neighborhood.removeClass('faded');
			    });
			    
			    cy.on('tap', function(e){
			      if( e.cyTarget === cy ){
			        cy.elements().removeClass('faded');
			      }
			    });
			  }
			});

			});";

echo "</script>";
?>
  <div id="cy"></div>
</body>
</html>