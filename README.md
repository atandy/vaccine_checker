# Vaccine Checker
This script currently checks CVS Pharmacy locations to see if there are any appointment availabilites for scheduling a vaccine. If there are, the script will send you a text message using Twilio.

# Disclaimer
Currently only supports checking CVS Pharmacy in the state of california. You'll have to adjust the URL in the script to change it to other states.

If you want to receive the text message, you'll need Twilio

# Setting up on a Cron
I set up a crontab with the script to run it every 5 minutes. 

![alt text](message_screenshot.jpg "Text Message Screenshot")

