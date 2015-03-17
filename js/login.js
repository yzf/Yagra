window.onload = function() {
  var btnLogin = document.getElementById("btn_login");
  btnLogin.onclick = function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (checkData(username, password)) {
      var url = 'login.py?username=' + username + '&password=' + password;
      ajax(url, function(responseText) {
        responseData = eval('(' + responseText + ')');
        if (responseData.status == 0) {
          // 注册成功
          window.location.href = 'upload_avatar.py';
        }
        else {
          // 注册失败
          alert(responseData.info);
        }
      });
    }
    else {
      alert('请输入有效的账号和密码');
    }
  };
};

