# SahibBot
The Discord Bot That Does Everything

## Installing

SahibBot requires a keys.py to store all of your user data.

The format is as follows:

```
botToken = "<Discord Bot Token>"
directory = {
    "<@User1>": "+1<UserPhone1>", 
    "<@User2>": "+1<UserPhone2>", 
    "<@User3>": "+1<UserPhone3>"
    }
twilioNumber = "+1<twilioNumber>"
twilioAccountSid = "<Twilio Account SID>"
twilioAuthToken  = "<Twilio Auth Token>"
```

For Example:

```
botToken = "MzYwMzEzNTY0ODczMDk3MjE2.donotusethis.thisisasampletoken"
directory = {
    "<@000000000000000001>": "+10000000001", 
    "<@123456789012345678>": "+13218675309", 
    "<@999999999999999999>": "+11234567890"
    }
twilioNumber = "+19999999999"
twilioAccountSid = "AC1966966966996666thisisfake"
twilioAuthToken  = "445dc5554s946421679thisisfaketoo"
```

The Phone Number format is E.164 so Twilio can recognize it. i.e. +1 XXX-XXX-XXXX