// carousel from homepage
var homeCarousel = document.querySelector('#homeCarousel')
var carousel = new bootstrap.Carousel(homeCarousel, {
//   interval: 7000,
  wrap: true
})

// templates carousel
var templateCarousel = document.querySelector('#templateCarousel')
var carousel2 = new bootstrap.Carousel(templateCarousel, {
  interval: false,
  keyboard: true,
  ride:false,
  wrap: true
})


$(document).ready(function(){

  var selectedTemplate = $('#templateCarousel .carousel-inner .carousel-item card');
  $selectedTemplate.click(function(e){
    $('#templateCarousel .carousel-inner .carousel-item card').removeClass('selectedTemplate');
          e.target.classList.add('selectedTemplate');
  })





});




