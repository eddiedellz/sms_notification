# SMS-Notifications
Plug-in to allow klipper to send yourself text message notifications.

## First Step
You will need a Twilio account. Go to [Twilios website](http://www.twilio.com) and sign up for an account. Although this is a pay service you can start with the trial account and get a bank of text messages.

## Installation

The module can be installed into a existing Klipper installation with an install script. 

    cd ~
    git clone https://github.com/eddiedellz/sms_notification.git
    cd sms_notification
    ./install-sms_notification.sh

Add the below [sms_notification] to your config file. 

    [sms_notification]
    accsid = XXXXX #Replace with Account SID from Twilio account
    authtoken = XXXXX #Replace with Auth Token from Twilio account
    phoneto = +13479999999 #Replace with phone number you want the notifications sent to
    phonefrom = +13479999999 #Replace with phone number from Twilio account
    
Replace XXXXX with your Twilio Account SID, Auth token, Twilio phone number. Change YOURPHONE=+13479999999 to your phone number area code first. for example if your phone number is 1-347-999-999 YOURPHONE=+13479999999. If you are useing the trial account the phone number you send the sms to must be the verified phone number in your Twilio account.

## Useage
Add GCode smssend msg="the message you want to send" to the event you want to be notifed.

For example, if you want to be notified of a filament runout:

    [filament_motion_sensor filament_sensor]
    detection_length: 10
    extruder: extruder
    switch_pin: ^P1.24
    pause_on_runout: True
    #insert_gcode:
    runout_gcode:
           smssend msg="Filament Motion Sensor Stoped"
           PAUSE
