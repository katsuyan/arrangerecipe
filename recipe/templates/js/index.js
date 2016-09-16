var ARRANGE = ARRANGE || {};


(function () {

  $.sygImageRadio( '.radioGroup1' );
  $.sygImageRadio( '.radioGroup2' );

  if (!$.cookie('key')){
    $('#mordal_button').click();
    $.cookie('key', 'visit', { expires: 999999999 });
  }

  if($('input[name=taste]:checked').val() & $('input[name=taste]:checked').val()){
    $('#cook_button').css('background-color', '#FF9933');
    $('#cook_button').css('color', 'White');
    $('#cook_button').prop("disabled", false);
  }

  $('#index').on('click', 'input[name=category]', function(e) {
    var taste_id = $('input[name=taste]:checked').val();
    if(!taste_id) {
      return false;
    }
    $('#cook_button').css('background-color', '#FF9933');
    $('#cook_button').css('color', 'White');
    $('#cook_button').prop("disabled", false);
  })


  $('#index').on('click', 'input[name=taste]', function(e) {
    var taste_id = $('input[name=taste]:checked').val();
    if(!taste_id) {
      return false;
    }
    $('#cook_button').css('background-color', '#FF9933');
    $('#cook_button').css('color', 'White');
    $('#cook_button').prop("disabled", false);
  })


  $('#index').on('click', '#cook_button', function(e) {
    var category_id = $('input[name=category]:checked').val();
    if(!category_id) {
      alert('カテゴリーを選択してください');
      return false;
    }
    var taste_id = $('input[name=taste]:checked').val();
    if(!taste_id) {
      alert('味付けを選択してください');
      return false;
    }
    location.href = '/detail/' + category_id + '/' + taste_id;
    // $.ajax({
    //   type: 'GET',
    //   url: '{% url "recipeid" %}',
    //   data: {category_id: category_id, taste_id: taste_id},
    //   success: function(data) {
    //     window.open('http://cookpad.com/recipe/' + data.id);
    //   },
    //   error: function(data) {
    //     console.log(data);
    //     alert("レシピが見つかりませんでした。");
    //   }
    // });
    return false;
  });

}());
