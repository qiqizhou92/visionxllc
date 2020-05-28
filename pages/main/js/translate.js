function googleTranslateElementInit() {
  new google.translate.TranslateElement(
    { pageLanguage: 'en' },
    'google_translate_element'
  );
}

setInterval(function() {
  if ($('html').hasClass('translated-ltr')) {
    $('.navbar').css('margin-top', '30px');
  } else {
    $('.navbar').css('margin-top', '0px');
  }
}, 3000);
