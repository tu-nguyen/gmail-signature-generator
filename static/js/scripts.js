$(document).ready(function(){
  // carousel from homepage
  let homeCarousel = document.querySelector('#homeCarousel')
  let carousel = new bootstrap.Carousel(homeCarousel, {
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
      document.getElementById("styleform_pre-template_style").value = e.target.id;
    }
    return false;
  })

  // final copypasta function
  document.getElementById("copy").addEventListener("click", function() {
    var inputs = document.getElementById('dataform');
    var collapseThree = document.getElementById('flush-collapseThree');

    if((inputs[0].value == "" || inputs[1].value == "") && !collapseThree.classList.contains('show')){
        // found an empty field that is required
        // alert("Please fill all required fields");
        document.getElementById('testt').click();
        return false;
    } else {
      document.getElementById("styleform").submit();
    }
  });
});


  
