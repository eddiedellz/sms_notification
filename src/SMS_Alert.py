from twilio.rest import Client 
from twilio.base.exceptions import TwilioRestException

class smsnotification:

    def __init__(self, config):
        self.printer = config.get_printer()
        self.ACCSID = config.get('ACCSID', None)
        self.AUTHTOKEN = config.get('AUTHTOKEN', None)
        self.PHONETO = config.get('PHONETO', None)
        self.PHONETO = config.get('PHONEFROM', None)
        self.MSG = config.get('MSG', None)
        self.printer.register_event_handler('klippy:ready', self._handle_ready)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('SMSSEND', self.cmd_SMSSEND)
        
    def cmd_SMSSEND(self, gcmd):
        self._handle_ready()
        try:
            client = Client(self.ACCSID, self.AUTHTOKEN) 
            
            message = client.messages.create(
            to="+17188252399", 
            from_="+18484208874",
            body=self.MSG)
            gcmd.respond_info(message.sid)
            
        except TwilioRestException as errf:
            raise gcmd.error(errf)

    def _handle_ready(self):
        self.reactor = self.printer.get_reactor()
        self.printProgress = 0
        self.displayStatus = self.printer.lookup_object('display_status')            

def load_config(config):
    return smsnotification(config)