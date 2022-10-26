$().ready(function () {
  $('div#add_item').on('click', function () {
    $('ul.my_list').append('<li>new Element</li>');
    console.log('add');
  });
  $('div#remove_item').on('click', function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').on('click', function () {
    $('ul.my_list li').remove();
  });
});
