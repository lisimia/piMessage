# piMessage
python wrapper for iMessage on OSX


This project has 1 goal. get iMessage to work on Windows. 


When set up properly these pieces all come together to proxy messages onto a configured backend or remote server and accept user input from remote server or configured backend


## example 1 ##
iMessage arrives on mac, => pop up notification on native windows app
native windows app sends reply => sent thorough Mac & iMsg

## example 2 ##
Imessage arrives on mac, => message is relayed to a webserver, client connects to web server and uses IMprogram on the webserver, server relays the message back to the mac & iMsg



-------------------------------------------------------------------

Comes with 2 other pieces that make life easier

#applescript#
piMessage.applescript will send incoming messages to server
needs to be configured for local machine
requires a running server

#server#
a flask server will accept incoming requests from the applescript
