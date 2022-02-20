# This file may be distributed under the terms of the GNU GPLv3 license.

from twilio.rest import Client 
from twilio.base.exceptions import TwilioRestException

class smsnotification:

    def __init__(self, config):
        self.printer = config.get_printer()
        self.accsid = config.get('accsid', None)
        self.authtoken = config.get('authtoken', None)
        self.phoneto = config.get('phoneto', None)
        self.phonefrom = config.get('phonefrom', None)
        gcode = self.printer.lookup_object('gcode')
        gcode.register_command('SMSSEND', self.cmd_SMSSEND)
        
    def cmd_SMSSEND(self, gcmd):
        msg = gcmd.get('MSG', '')
        if(msg != ''):
            gcmd.respond_info(msg)
            try:
                client = Client(self.accsid, self.authtoken) 
                message = client.messages.create(
                to=self.phoneto, 
                from_=self.phonefrom,
                body=msg)
                gcmd.respond_info("SMS Notification Sent")
                        
            except TwilioRestException as errf:
                raise gcmd.error(errf)

        else:
            raise gcmd.error("No Message found."
            "Format command smssend msg=your message")


def load_config(config):
    return smsnotification(config)
