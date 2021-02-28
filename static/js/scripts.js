$(document).ready(function(){
  // carousel from homepage
  let homeCarousel = document.querySelector('#homeCarousel')
  let carousel = new bootstrap.Carousel(homeCarousel, {
  //   interval: 7000,
    wrap: true
  })

  // templates carousel
  let templateCarousel = document.querySelector('#templateCarousel')
  let carousel2 = new bootstrap.Carousel(templateCarousel, {
    interval: false,
    keyboard: true,
    ride:false,
    wrap: true
  })

  // template select
  let $select = $('#template .carousel-inner')
  $select.click(function(e){
    if ($(e.target).parent().hasClass('selectedTemplate')){
      // alert(1);
    } else {
      $('.card').removeClass('selectedTemplate');
      $(e.target).closest('.card').addClass('selectedTemplate');
    }
    return false;
  })

  // final copypasta function
  // document.getElementById("copy").addEventListener("click", function() {
  //   alert(1);
  //   document.getElementById("styleform").submit();
  //   document.getElementById("dataform").submit();
  // });
  
  document.ready(function(){
    $("#copy").click(function(){        
        $("#copyform").submit(); // Submit the form
    });
});


});


  
