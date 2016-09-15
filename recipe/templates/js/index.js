var ARRANGE = ARRANGE || {};

(function () {

  $('#index').on('click', '#cook_button', function(e) {
    //window.open('http://cookpad.com/recipe/3141186')

    console.log($('input[name=category]:checked').val())
    console.log($('input[name=taste]:checked').val())
  });

}());
