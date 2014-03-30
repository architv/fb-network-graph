var newdata;
var whynotyouwork;
$.ajax({
          url : "data.txt",
          dataType: "text",
          success : function (data) {
            localStorage.setItem('graphdata',data);
          }
      });

newdata = localStorage.getItem('graphdata');

$(function(){ // on dom ready

$('#cy').cytoscape({
  layout: { 
    name: 'random',
    ready: undefined, // callback on layoutready
    stop: undefined, // callback on layoutstop
    fit: true // whether to fit to viewport
  },
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

    elements: [],

  ready: function(){
    window.cy = this;
    
    whynotyouwork = eval('(' + newdata+ ')'); //converts string into an object
    cy.load(whynotyouwork);
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

}); // on dom ready