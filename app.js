// 설치한 express 모듈 불러오기
// @@JD : express가 무엇인지 확인하기
const express = require('express');

// 설치한 socket.io 모듈 불러오기
// @@JD : socket.io가 무엇인지 확인하기
const socket = require('socket.io');

// node.js 기본 내장 모듈 불러오기
const http = require('http');
const fs = require('fs');

// express 객체 생성
const app = express();

// express http 서버 생성
const server = http.createServer(app);

// 생성된 서버를 socket.io에 바인딩
const io = socket(server);

// app_py.js 선언
const app_py = require('./app_py')

// 데이터 parsing 관련 모듈 선언
const bodyParser = require('body-parser');

app.use('/css', express.static('./static/css'));
app.use('/js', express.static('./static/js'));
app.use(bodyParser.json())

app.get('/', function(request, response) {
  console.log("The user has connected with '/'.");

  var data = request.body;
  var all = JSON.stringify(data);
  console.log("python: " + all);

  fs.readFile('./static/html/index.html', function(err, data){
    if(err){
      response.send('error')
      console.log(err);
    } else {
      response.writeHead(200, {'Content-Type':'text/html'});
      response.write(data);
      response.end();
    }
  });
});

var roomId = '';


// 소켓 관련 메소드
io.sockets.on('connection', function(socket) {

  // 임의의 방 입장
  socket.on('joinRoom', function(data) {
    console.log(data);
    socket.join(data.roomId);

    // 소켓에 이름 저장
    socket.name = data.name;

    // 퇴장을 위해 방 저장
    roomId = data.roomId;
    // 방에있는 모든 소켓에게 전송
    io.sockets.in(data.roomId).emit('update', {
      type: 'connect',
      name: 'SERVER',
      message: data.name + ' is logged on, room : ' + data.roomId
    });
  });

  // 새로운 유저가 접속했을 경우 다른 소켓에게도 알림
  socket.on('newUser', function(name) {
    console.log(name + ' is logged on');
    // 소켓에 이름 저장
    // socket.name = name;
    //
    // // 모든 소켓에게 전송
    // io.sockets.emit('update', {
    //   type: 'connect',
    //   name: 'SERVER',
    //   message: name + ' is logged on'
    // });
  });

  // // 전송한 메세지 받기
  // socket.on('sendMessage', function(data) {
  //   // 받은 데이터에 누가 보냈는지 이름을 추가
  //   data.name = socket.name;
  //   console.log(data);
  //   // 보낸 사람을 제외한 나머지 유저에게 메세지 전송
  //   socket.broadcast.emit('update', data);
  // });

  // Broadcast to room
  socket.on('sendMessage', function(data) {
    data.name = socket.name;
    console.log(data)
    socket.broadcast.to(data.roomId).emit('update', data);
  });

  // 접속 종료
  socket.on('disconnect', function() {
    console.log(socket.name + ' is logged out');

    socket.leave(roomId);

    console.log(io.sockets.adapter.rooms);
    
    socket.broadcast.to(roomId).emit('update', {
      type: 'disconnect',
      name: 'SERVER',
      message: socket.name + ' is logged out, room : ' + roomId
    });

    // socket.broadcast.emit('update', {
    //   type: 'disconnect',
    //   name: 'SERVER',
    //   message: socket.name + " is logged out"
    // })
  })
});

//서버를 8080포트로 listen
server.listen(8080, function() {
  console.log('Server is excuting...');

});
