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
