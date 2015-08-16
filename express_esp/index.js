var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var bodyParser = require('body-parser')

app.use(bodyParser.json());  

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
	io.sockets.in(req.body.game).emit('paired');
	res.send('OK')
});