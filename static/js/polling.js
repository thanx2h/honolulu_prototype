var chatManager = new function(){

  var interval    = 1000;
  var xmlHttp     = new XMLHttpRequest();
  var finalDate   = '';

  // Ajax Setting
  xmlHttp.onreadystatechange = function()
  {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
    {
      // JSON 포맷으로 Parsing
      res = JSON.parse(xmlHttp.responseText);

      // 호가창 데이터 보여주기
      chatManager.show(res);
    }
  }
  // 호가창 데이터 가져오기
  this.proc = function()
  {
    // Ajax 통신
    xmlHttp.open("post", "http://localhost:5000/v1/getHogaData", true);
    xmlHttp.send();
  }

  // 받은 데이터 보여주기
  this.show = function(data)
  {
    // console.log(data)
    var all = data.All;
    console.log(all)
    // 입력 데이터 가져오기
    var hogaTable = document.getElementById('hogaTable')
    var hogaTableBody = document.getElementById('hogaTableBody')
    // tr.setAttribute("bgColor", "#FFFFCC"); // 배경색
    // tr.setAttribute("height", "30"); // 높이
    console.log(all.buy)
    console.log(all.sell)

    if(data){
      var hogaTableLen = hogaTableBody.rows.length;
      console.log(hogaTableLen)

      for(var i=hogaTableLen; i>0; i--){
        console.log('delete')
        hogaTable.deleteRow(i);
      }

      for(var i=0; i< all.sell.length; i++) {
        var row = hogaTableBody.insertRow(i)
        for(var j=0; j<2; j++){
          row.insertCell(j).innerHTML = all.sell[4-i-1][2-j-1];
        }
        for(var j=2; j<4; j++){
          row.insertCell(j).innerHTML = "";
        }
      }

      var allLen = all.sell.length + all.buy.length

      for(var i=all.sell.length; i< allLen; i++) {
        var row = hogaTableBody.insertRow(i)
        for(var j=0; j<2; j++){
          row.insertCell(j).innerHTML = "";
        }
        for(var j=2; j<4; j++){
          row.insertCell(j).innerHTML = all.buy[i-4][j-2];
        }
      }
    }

    data = "";
  }

  this.startPolling = function(){
    // interval에서 지정한 시간마다 실행
    setInterval(this.proc, interval);
  }
}

function startPolling(){

  var hogaTableLen = hogaTableBody.rows.length;
  console.log(hogaTableLen)

  for(var i=hogaTableLen; i>0; i--){
    console.log('delete')
    hogaTable.deleteRow(i);
  }

  var itemName = document.getElementById('itemName').value;
  if( itemName == ""){
    console.log("startPolling, 비어 있음");
  }else{
    console.log("startPolling, 값이 있음");
    // chatManager.startPolling();
    // chatManager.proc();
    chatManager.startPolling()
  }

}
