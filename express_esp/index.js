var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var bodyParser = require('body-parser')

app.use(bodyParser.json());  

io.on('connection', function(socket){
	console.log('a user connected');
	var channel
	socket.on('join', function (data) {
		channel = data.channel
		socket.join(data.channel);
		console.log("joined")
	});
	socket.on('paired_server', function (data) {
		socket.broadcast.in(channel).emit('paired', data);
	});
	socket.on('player_waiting_server', function (data) {
		channel = data.channel
		socket.broadcast.in(data.channel).emit('player_waiting');
	});
	socket.on('answers_match_server', function (data) {
		channel = data.channel
		io.sockets.in(data.channel).emit('answers_match', {newQuestion: data.newQuestion});
	});
	socket.on('match_fail_server', function (data) {
		channel = data.channel
		io.sockets.in(data.channel).emit('match_fail');
	});
	socket.on('disconnect', function () {
		console.log("disconnected from " + channel)
		io.sockets.in(channel).emit('player_disconnect', {channel: channel});
	});
});


http.listen(3000, function(){
	console.log('listening on *:3000');
});