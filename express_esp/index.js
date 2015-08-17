var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var request = require('request')
var bodyParser = require('body-parser')
var djangoServer = 'http://127.0.0.1:8000/esp_game'
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
		request
		  .get(djangoServer + '/disconnected/' + channel + '/')
		  .on('response', function(response) {
		    console.log(response.statusCode) // 200 
		    console.log(response.headers['content-type']) // 'image/png' 
		  })
		// request.post({url:djangoServer + '/disconnected/' + channel + '/', form: {key:'value'}}, function(err,httpResponse,body){console.log(body)})
	});
});


http.listen(3000, function(){
	console.log('listening on *:3000');
});