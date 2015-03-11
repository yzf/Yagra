var ajax = function(url, callback) {
  //1.创建对象
  var oAjax = null;
  if (window.XMLHttpRequest){
    oAjax = new XMLHttpRequest();
  }
  else {
    oAjax = new ActiveXObject("Microsoft.XMLHTTP");
  }
  //2.连接服务器
  oAjax.open('GET', url, true);   //open(方法, url, 是否异步)
  //3.发送请求
  oAjax.send();
  //4.接收返回
  oAjax.onreadystatechange = function() {  //OnReadyStateChange事件
    if (oAjax.readyState == 4) {  //4为完成
      if (oAjax.status == 200) {    //200为成功
        callback(oAjax.responseText)
      }
    }
  };
};
