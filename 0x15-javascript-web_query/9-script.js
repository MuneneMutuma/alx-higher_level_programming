$.ajax({
  type: 'GET',
  crossDomain: true,
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  success: function (response, status) {
    $('div#hello').text(response.hello);
  }
});
