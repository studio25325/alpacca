function XMLHttpRequestInGet(){
  //------------ using jQuery---------------//
  $.ajax('/send_Request', {
    data: {
        id: 'some-unique-id'
    }
  })
  .then(
      function success(name) {
          alert(name+' is done!');
      },

      function fail(data, status) {
          alert('Request failed.  Returned status of ' + status);
      }
  );
}



  function XMLHttpRequestInPOST(){

 //------------ using pure javascript---------------//

  function parse_cookies() {
      var cookies = {};
      if (document.cookie && document.cookie !== '') {
          document.cookie.split(';').forEach(function (c) {
              var m = c.trim().match(/(\w+)=(.*)/);
              if(m !== undefined) {
                  cookies[m[1]] = decodeURIComponent(m[2]);
              }
          });
      }
      return cookies;
  }
  var cookies = parse_cookies();
  console.log(cookies)
  var user={'user':'soup01'}
  var xhr = new XMLHttpRequest();

  xhr.open("POST", "/post_request/");
  xhr.setRequestHeader('X-CSRFToken', cookies['csrftoken']);
  xhr.send({user});

    xhr.onload = function() {
    if (xhr.status === 200) {
        alert('status code is 200. \n Your responseText is: ' + xhr.responseText);
    }
    else if (xhr.status !== 200) {
        alert('Request failed.  Returned status of ' + xhr.status);
    }
};
}
