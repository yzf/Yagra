window.onload = function() {
  var btn_register = document.getElementById("btn_register");
  btn_register.onclick = function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var url = 'register.py?username=' + username + '&password=' + password;
    ajax(url, function(responseText) {
      responseData = eval('(' + responseText + ')');
      if (responseData.status == 0) {
        // 注册成功
        alert(responseData.info);
      }
      else {
        // 注册失败
        alert(responseData.info);
      }
    });
  };
};

