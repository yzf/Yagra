window.onload = function() {
  var btnRegister = document.getElementById("btn_register");
  btnRegister.onclick = function() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    // 验证通过，发送ajax进行注册
    if (checkData(username, password)) {
      var url = 'register.py?username=' + username + '&password=' + password;
      ajax(url, function(responseText) {
        responseData = eval('(' + responseText + ')');
        if (responseData.status == 0) {
          // 注册成功
          alert(responseData.info);
          window.location.href = 'login.py'
        }
        else {
          // 注册失败
          alert(responseData.info);
        }
      });
    }
    else {
      alert("账号或密码不符合要求");
    }
  };
};
