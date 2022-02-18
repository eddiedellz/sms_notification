from twilio.rest import Client 
from twilio.base.exceptions import TwilioRestException
import os

class twilioacc:
#ACCSID: "AC0620680188289306ff143107d740e559"
#AUTHTOKEN: "XXXXXXXXXXXXXX"
#PHONETO: "+1XXXXXXXXXX"
#SMSMESSAGE: "+1XXXXXXXXXX" 

    def __init__(self, config):
        self.printer = config.get_printer()
        self.ACCSID = config.get('ACCSID', None)
        self.AUTHTOKEN = config.get('AUTHTOKEN', None)
        self.PHONETO = config.get('PHONETO', None)
        self.MSG = config.get('MSG', None)
        self.printer.register_event_handler('klippy:ready', self._handle_ready)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('SMSSEND', self.cmd_SMSSEND)
        
    def cmd_SMSSEND(self, gcmd):
        self._handle_ready()
        try:
            client = Client(self.ACCSID, self.AUTHTOKEN) 
	    client.api.account.messages.create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+18484208874',
                        to='+17188252399'
                 )
            
        except TwilioRestException as errf:
            raise gcmd.error(errf, " " & self.AUTHTOKEN)

    def _handle_ready(self):
        self.reactor = self.printer.get_reactor()
        self.printProgress = 0
        self.displayWEStatus = self.printer.lookup_object('display_status')

            
def load_config(config):
    return twilioacc(config)