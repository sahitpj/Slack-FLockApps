var config = require('./config.js');
var express = require('express');
var request = require('request');
var bodyParser = require('body-parser');
const { RTMClient } = require('@slack/client');

app = express();

const PORT = 8080;


var sendMessage = function(rtm, text, res, conversationId){
	rtm.sendMessage(text , conversationId)
	  .then((res) => {
	    // `res` contains information about the posted message
	    console.log('Message sent: ', res.ts);
	  })
	  .catch(console.error);
};


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.listen(PORT, function(){
	console.log('listening on ' + PORT);
});

app.get('/oauth', function(req, res){
	console.log('Recieved request');
});


app.post('/command', function(req, res){
	//console.log(process.env.SLACK_TOKEN);
	console.log('Recieved a slask command request');
	console.log(req.body.token);
	res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify({
    "response_type": "in_channel",
    "text": "It's 80 degrees right now.",
    "attachments": [
        {
            "text":"Partly cloudy today and tomorrow"
        }
    ]
}));
});

const rtm = new RTMClient(config.token);
rtm.start();

rtm.on('message', (event) => {
  // Structure of `event`: <https://api.slack.com/events/message>
  console.log(`Message from ${event.user}: ${event.text}`);
  //console.log(event);
  rtm.sendMessage("hello world", event.channel)
   .then((res) => {
	    // `res` contains information about the posted message
	    console.log('Message sent: ', res.ts);
	  })
	.catch(console.error);
 });










