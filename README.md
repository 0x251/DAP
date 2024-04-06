# DAP
Discord activity spammer, troll users by spamming the join and leave sound of an activity in discord VC's, this will also work if the vc is full (you dont need to join the vc for this to work)

### Usage
 - First You will need you're ``Authorization`` Token you can get this using inspect elemet and viewing a discord request it should be in the headers section, on line 14 in DAP.py replace where it says "Replace me" with that token
 - Second you will need the ``ChannelID`` and ``ServerID AKA GuildID`` when running DAP.py it will ask you for those two things
 - Have fun ear destorying the pour souls on discord
<br>
<img src="https://media.discordapp.net/attachments/1226017470079434906/1226043518309371974/image.png?ex=66235501&is=6610e001&hm=3a1dc3e7e33a488b45d0c7d147a152ccfe6d03328a5927381cdffbae138d51d4&=&format=webp&quality=lossless"></img>


### How this works
- First it will authorize you're discord user client to the activity
- Then it grabs Discord OAuth code that the activity returns
- After that it will use that to check if the activity was created or not and will print out a response, if you haven't joined the activity it will automatically create it (making the spam the join and connect sound)

### Issues
- There is a proxy implementation already you will just need to configure it to work with the requests, Since discord likes to ratelimit
- It breaks that current activity for everyone
- Sometimes Per client it breaks, so session id in DAP.py code will need to be replaced with a sessionID you can get this by joining a activity monitoring the requests and see the sessionID being sent and replace it in DAP.py code, these ID's expire every 3 hours

### Trolling
<img src="https://media.discordapp.net/attachments/1206601094663381012/1226159163403665530/image.png?ex=6623c0b5&is=66114bb5&hm=2ae382dd7af9155c6233055076656a43924d26104e4b35d1a5916b44401db21a&=&format=webp&quality=lossless"> </img>
<img src="https://media.discordapp.net/attachments/1206601094663381012/1226158245908054078/Screenshot_20240406_081449_Discord.jpg?ex=6623bfda&is=66114ada&hm=656e3cd8c9662cdb6d8476719bf5a92c168797094edc356f2ee5db644793b0da&=&format=webp&width=835&height=480"> </img>
<img src="https://media.discordapp.net/attachments/1206601094663381012/1226158246541262878/Screenshot_20240406_081500_Discord.jpg?ex=6623bfda&is=66114ada&hm=3f49590c3069edd0a090ee9c30b4148a800316f919267d308c79286aebde2f02&=&format=webp&width=850&height=480"> </img>
- you can also have multiple activitys in servers running even if you aren't in the server or VC

