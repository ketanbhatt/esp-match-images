var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

io.on('connection', function(socket){
	console.log('a user connected');
	socket.on('join', function (data) {
		socket.join(data.channel);
		console.log("joined")
		io.sockets.in(data.channel).emit('new_msg', {msg: 'hello'});
	});
});


http.listen(3000, function(){
	console.log('listening on *:3000');
});

app.post('/pair', function(req, res){
	console.log("Pair hego re!")
	res.send('OK')
});