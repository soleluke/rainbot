# rainbot
##Rainbot is a very basic IRC bot to provide rain/snow/other weather alerts to a given IRC channel via the MetaWeather API


#Usage: `./rainbot.py <path-to-con-info`


##Connection Info
###The JSON structure must be as follows
####Required:
```
{
	"addr":"irc.freenode.net",
	"port":"6667",
	"nick":"rainbot",
	"channels": ["channel1","chanel2",...,"channel-n:],
}
```
####Optional
```
{
	"autojoin":"true",
	"password":"password"
}
```
#####Note: the nick would need to already be registered on the network for identification to work
