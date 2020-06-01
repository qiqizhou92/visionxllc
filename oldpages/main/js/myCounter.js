$('.counter').counterUp({
  delay: 10,
  time: 2000
});
$('.counter').addClass('animated fadeInDownBig');
$('h3').addClass('animated fadeIn');

$(document).ready(function() {
  $(window).scroll(function() {
    if ($(window).scrollTop() < 100) {
      $('.navbar').css({ 'background-color': 'transparent' });
    } else {
      $('.navbar').css({ 'background-color': 'black' });
    }
  });
});
