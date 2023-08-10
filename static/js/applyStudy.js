function applyStudy(study_id) {
  var csrftoken = getCookie('csrftoken');
  $.ajax({
    url: 'apply_study/',
    type: 'POST',
    data: {
      'study_id': study_id,
      'csrfmiddlewaretoken': csrftoken
    },
    success: function(response) {
  // 서버에서 업데이트된 값을 받아와서 변수에 저장
  var updated_people = parseInt(response.updated_people);

  // 해당 스터디의 인원 수 업데이트
  var people_element = $("#people-" + study_id);
  people_element.text(updated_people);
},
    error: function(xhr, status, error) {
      // 요청 실패
    }
  });
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(document).on('click', '.apply-study-btn', function() {
  var study_id = $(this).data('study-id');
  applyStudy(study_id);
});

$('#apply-study-btn').addClass('apply-study-btn');

$(".apply-study-btn").click(function() {
  var study_id = $(this).data("study-id");
  applyStudy(study_id);
});