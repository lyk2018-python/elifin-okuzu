$(document).ready(function(){
  sayac = 0;
  $(".bar-menu").click(function(){
    sayac++;
    if (sayac % 2 != 0) {
      $('.mbl-menu').addClass('coming')
    }
    else {
      $('.mbl-menu').removeClass('coming')
    }
  })
})
