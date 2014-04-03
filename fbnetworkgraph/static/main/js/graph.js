var whynotyouwork;
var newdata;

$.ajax({
  url : "data",
  dataType: "text",
  success : function(data) {
    console.log(data);
    localStorage.setItem('graphdata',data);
  }
});

newdata = localStorage.getItem('graphdata');
console.log(newdata);

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
    
    console.log(newdata);
    whynotyouwork = eval('(' + newdata + ')'); //converts string into an object
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