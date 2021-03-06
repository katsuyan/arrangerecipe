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
      return ;
    }
    $('#cook_button').css('background-color', '#FF9933');
    $('#cook_button').css('color', 'White');
    $('#cook_button').prop("disabled", false);
  })


  $('#index').on('click', 'input[name=taste]', function(e) {
    var taste_id = $('input[name=category]:checked').val();
    if(!taste_id) {
      return ;
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
    $.ajax({
      type: 'GET',
      url: '{% url "recipeid" %}',
      data: {category_id: category_id, taste_id: taste_id},
      success: function(data) {
        location.href = '/detail/' + category_id + '/' + taste_id;
      },
      error: function(data) {
        alert("レシピが見つかりませんでした。");
      }
    });
    return false;
  });

}());
