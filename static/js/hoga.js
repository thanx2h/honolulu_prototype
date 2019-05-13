// 전송 함수
function sendItemName(itemName) {
  // 입력 데이터 가져오기
  var itemName = document.getElementById('itemName').value;
  setHogaData(itemName)

}

function setHogaData(hoga) {
  // 입력 데이터 가져오기
  var hogaTable = document.getElementById('hogaTable')
  var hogaTableBody = document.getElementById('hogaTableBody')
  // tr.setAttribute("bgColor", "#FFFFCC"); // 배경색
  // tr.setAttribute("height", "30"); // 높이

  hoga = hoga.trim()

  if(hoga){
    var hogaTableLen = hogaTableBody.rows.length;
    console.log(hogaTableLen)

    for(var i=hogaTableLen; i>0; i--){
      console.log('delete')
      hogaTable.deleteRow(i);
    }

    for(var i=0; i<10; i++) {
      var row = hogaTableBody.insertRow(i)

      for(var j=0; j<6; j++){
        row.insertCell(j).innerHTML = hoga;
      }

      // var tr = document.createElement("tr");
      // var td1 = document.createElement("td");
      // // td1.setAttribute("width", "100"); // 넓이
      // td1.innerText = hoga;
      // var td2 = document.createElement("td");
      // // td2.setAttribute("width", "200"); // 넓이
      // td2.innerText = hoga;
      // var td3 = document.createElement("td");
      // // td1.setAttribute("width", "100"); // 넓이
      // td3.innerText = hoga;
      // var td4 = document.createElement("td");
      // // td2.setAttribute("width", "200"); // 넓이
      // td4.innerText = hoga;
      // var td5 = document.createElement("td");
      // // td1.setAttribute("width", "100"); // 넓이
      // td5.innerText = hoga;
      // var td6 = document.createElement("td");
      // // td2.setAttribute("width", "200"); // 넓이
      // td6.innerText = hoga;
      // tr.appendChild(td1);
      // tr.appendChild(td2);
      // tr.appendChild(td3);
      // tr.appendChild(td4);
      // tr.appendChild(td5);
      // tr.appendChild(td6);
      //
      // hogaTable.appendChild(tr);

    }
  }


}
