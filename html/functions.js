var img     = null ;
var delay_0 =  100 ;
var delay_1 =  800 ;
var parity  =    0 ;

var images = [] ;
images['catbed'] = [ ['catbed1.jpg'] , ['catbed2.jpg'] ] ;
images['edith' ] = [ ['edith1.jpg' ] , ['edith2.jpg','edith3.jpg'] ] ;
var image_name = 'edith' ;
var image_name_from_URL = getParameterByName('image') ;
if(image_name_from_URL=='catbed'){
  image_name = 'catbed' ;
}
if(image_name_from_URL=='edith' ){
  image_name = 'edith'  ;
  delay_0 =  75 ;
  delay_1 = 100 ;
}

function start(){
  img = Get('img_morphing') ;
  var delay = delay_0+delay_1*Math.random() ;
  window.setTimeout(update_image, delay) ;
}
function update_image(){
  parity = (parity+1)%images[image_name].length ;
  var ran = Math.floor(images[image_name][parity].length*Math.random()) ;
  img.src = 'images/'+images[image_name][parity][ran] ;
  var delay = delay_0+delay_1*Math.random() ;
  window.setTimeout(update_image, delay) ;
}
function getParameterByName(name){
  // Taken from http://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
  var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search) ;
  return match && decodeURIComponent(match[1].replace(/\+/g, ' ')) ;
}
function Get(id){ return document.getElementById(id) ; }
