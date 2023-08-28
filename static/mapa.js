var filter_container = document.getElementById('popup-filter');
var filter_content = document.getElementById('filter-content');


var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');

const overlay = new ol.Overlay({
  element: container,
  autoPan: true,
  autoPanAnimation: {
          duration: 300,
  }       
});


var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
      source: new ol.source.OSM()
    })
  ],
  overlays: [overlay],
  view: new ol.View({
    center: ol.proj.fromLonLat([-58.1781400, -26.1775300]),
    zoom: 8
  })
});

closer.onclick = function() {
  overlay.setPosition(undefined);
  closer.blur();
  return false;
};

console.log(datos_obra)
const marcadores = []; 
coordenadas.forEach(coordenada => {
        
        let marcador = new ol.Feature({
            id: coordenada.id,
            geometry: new ol.geom.Point(
                ol.proj.fromLonLat([coordenada.longitud, coordenada.latitud])
            ),
        });
        marcador.setId(coordenada.id);
        marcador.setStyle(new ol.style.Style({
              image: new ol.style.Icon({
                  src: '/static/obra.png',
                  scale: 0.2,
            })
        }));
        marcadores.push(marcador);
    });

    let ultimaCapa = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: marcadores, 
    }),
});

map.addLayer(ultimaCapa)


map.on('click', function (e) {
  map.forEachFeatureAtPixel(e.pixel, function (feature, layer) {

    const coordinate = e.coordinate;
    
    
    datos_obra.forEach(data => {
      
      if(feature.getId() == data.id){
        
          content.innerHTML = '<div>' //inicio contenedor datos presentacion
            +'<div class="div-data">'
            +'<p class="data">Nombre de la obra: ' + data.nombre + ' </p>'
            +'<p class="data">Localidad: ' + data.localidad + ' </p>'
            +'<p class="data">Valor: ' + data.valor + ' </p>'
            +'<p class="data">Latitud: ' + data.latitud + ' </p>'
            +'<p class="data">Longitud: ' + data.longitud + ' </p>' 
            +'</div>'
            +'</div>' //fin contenedor datos renaper
            
          
            
          overlay.setPosition(coordinate);
          
      }
    })

    
  });
  
});


//FILTROS
$(document).ready(function() {
    $('#selectSector').change(function(){
        valor = $(this).val();
        console.log(valor);
       
    });
    $('#selectLocalidad').change(function(){
        valor = $(this).val();
        console.log(valor);
       
    });
    $('#selectEstado').change(function(){
        valor = $(this).val();
        console.log(valor);
        
    });
    $('#selectOrganismo').change(function(){
        valor = $(this).val();
        console.log(valor);
        
    });
})