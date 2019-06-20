var socket = io();
var roomId = '';
var name = '';

function touchEnter(){
  if(event.keyCode == 13){
         sendMsg();  // 실행할 이벤트
    }
}

// 접속 되었을 때 실행
socket.on('connect', function() {
  name = prompt('반갑습니다. 닉네임을 입력해주세요', '');
  // var input = document.getElementById('message');
  // input.value = "Connection success";

  if (!name) {
    name = '익명';
  }

  socket.emit('newUser', name);

});

function joinRoom(){
  roomId = document.getElementById('itemName').value;
  console.log(roomId);
  if(itemName == ""){
    console.log("joinRoom, 비어 있음");
    // Join to room
  }else{
    console.log("joinRoom, 값이 있음");
    socket.emit('joinRoom', {roomId: roomId, name:name});
  }
}

socket.on('update', function(data) {
  console.log("chat.js, update : " + data.type);
  var chat = document.getElementById('chat');

  var message = document.createElement('div');
  var node = document.createTextNode(`${data.name}:${data.message}`);
  console.log(`${data.name}: ${data.message}`);
  var className = '';

  // type에 따라 적용할 클래스를 다르게 지정
  switch (data.type) {
    case 'message':
      className = 'other';
      break;

    case 'connect':
      className = 'connect'
      break;

    case 'disconnect':
      className = 'disconnect'
      break;
  }

  message.classList.add(className);
  message.appendChild(node);
  chat.appendChild(message);

});

// 전송 함수
function sendMsg() {
  // 입력 데이터 가져오기
  var message = document.getElementById('message').value;

  // 가져오고 빈칸으로 변경
  document.getElementById('message').value = '';

  // 내가 전송할 메세지 클라이언트에게 표시
  var chat = document.getElementById('chat');
  var msg = document.createElement('div');
  var node = document.createTextNode(message);

  msg.classList.add('me');
  msg.appendChild(node);
  chat.appendChild(msg);

  // socket.emit('message', {
  //   type: 'message',
  //   message: message
  // });

  socket.emit('sendMessage', {
    type: 'message',
    roomId : roomId,
    message: message
  });

}
