var ARRANGE = ARRANGE || {};

(function () {

  $('#index').on('click', '#cook_button', function(e) {
    var category_id = $('input[name=category]:checked').val()
    var taste_id = $('input[name=taste]:checked').val()
    $.ajax({
      type: 'GET',
      url: '{% url "recipeid" %}',
      data: {category_id: category_id, taste_id: taste_id},
      success: function(data) {
        window.open('http://cookpad.com/recipe/' + data.id)
      },
      error: function(data) {
        console.log(data)
        alert("失敗");
      }
    });
  });

}());
