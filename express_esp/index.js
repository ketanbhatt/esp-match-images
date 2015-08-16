var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
	res.sendfile('connect.html');
});

io.on('connection', function(socket){
	console.log('a user connected');
	socket.on('join', function (data) {
		socket.join(data.email);
		console.log("joined")
	});
});

http.listen(3000, function(){
	console.log('listening on *:3000');
});

// io.sockets.in('user1@example.com').emit('new_msg', {msg: 'hello'});