var config = require('./config.js');
var express = require('express');
var request = require('request');

app = express();

const PORT = 8080;
app.listen(PORT, function(){
	console.log('listening on ' + PORT);
});

app.get('/oauth', function(req, res){
	console.log(response);
	
});


