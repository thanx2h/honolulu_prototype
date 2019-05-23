// 전송 함수
function sendItemName() {
  // 입력 데이터 가져오기
  var itemName = document.getElementById('itemName').value;
  if( itemName == ""){
    console.log("비어 있음");
  }else{
    console.log("값이 있음");
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
          console.log(xhr.responseText)
        }
      }
      xhr.open('GET', 'http://localhost:5000/v1/getItemCode?itemName='+itemName, true);
      xhr.send(null);
  }
}

// function setHogaData(hoga) {
//   // 입력 데이터 가져오기
//   var hogaTable = document.getElementById('hogaTable')
//   var hogaTableBody = document.getElementById('hogaTableBody')
//   // tr.setAttribute("bgColor", "#FFFFCC"); // 배경색
//   // tr.setAttribute("height", "30"); // 높이
//
//   hoga = hoga.trim()
//
//   if(hoga){
//     var hogaTableLen = hogaTableBody.rows.length;
//     console.log(hogaTableLen)
//
//     for(var i=hogaTableLen; i>0; i--){
//       console.log('delete')
//       hogaTable.deleteRow(i);
//     }
//
//     for(var i=0; i<10; i++) {
//       var row = hogaTableBody.insertRow(i)
//
//       for(var j=0; j<6; j++){
//         row.insertCell(j).innerHTML = hoga;
//       }
//     }
//   }
//
// }
