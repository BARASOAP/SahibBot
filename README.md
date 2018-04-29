# SahibBot
The Discord Bot That Does Everything

## Installing

SahibBot requires a keys.py to store all of your user data.

The format is as follows:

```
botToken = "<Discord Bot Token"
directory = {
    "<@User>": "+1<UserPhone1>", 
    "<@User2>": "+<UserPhone2>", 
    "<@User3>": "+<UserPhone3>"
    }
```

For Example:

```
botToken = "MzYwMzEzNTY0ODczMDk3MjE2.DcQIrA.BfaGXIbOsK5V-m3Mo7cyK6oQIZA"
directory = {
    "<@000000000000000001>": "+10000000001", 
    "<@123456789012345678>": "+13218675309", 
    "<@999999999999999999>": "+11234567890"
    }
```

The Phone Number format is E.164 so Twilio can recognize it. i.e. +1 XXX - XXX - XXXX