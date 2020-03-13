'''
HDMI SPEC 1.4
from Major Channel Number
'''
class cec_translate :
    #header
    cec_header_dictionary = {
        '0' : "TV",
        '1' : "Recording 1",
        '2' : "Recording 2",
        '3' : "Tuner 1",
        '4' : "Playback 1",
        '5' : "Audio system",
        '6' : "Tuner 2",
        '7' : "Tuner 3",
        '8' : "Playback 2",
        '9' : "Recording 3",
        'a' : "Tuner 4",
        'b' : "Playback 3",
        'c' : "Reserved",
        'd' : "Reserved",
        'e' : "Specific Use",
        'f' : "Unregistered",
    }
    cec_destination_dictionary = {
        '0' : "TV",
        '1' : "Recording 1",
        '2' : "Recording 2",
        '3' : "Tuner 1",
        '4' : "Playback 1",
        '5' : "Audio system",
        '6' : "Tuner 2",
        '7' : "Tuner 3",
        '8' : "Playback 2",
        '9' : "Recording 3",
        'a' : "Tuner 4",
        'b' : "Playback 3",
        'c' : "Reserved",
        'd' : "Reserved",
        'e' : "Specific Use",
        'f' : "Broadcast",
    }
    #opcode
    cec_opcode_dictionary = {
        '00' : "FeatureAbort",
        '04' : "ImageViewOn",
        '05' : "TunerStepIncrement",
        '06' : "TunerStepDecrement",
        '07' : "TunerDeviceStatus",
        '08' : "GiveTunerDeviceStatus",
        '09' : "RecordOn",
        '0a' : "RecordStatus",
        '0b' : "RecordOff",
        '0d' : "TextViewOn",
        '0f' : "RecordTVScreen",
        '1a' : "GiveDeck Status",
        '1b' : "DeckStatus",
        '32' : "SetMenuLanguage",
        '33' : "ClearAnalogueTimer",
        '34' : "SetAnalogueTimer",
        '35' : "TimerStatus",
        '36' : "Standby",
        '41' : "Play",
        '42' : "DeckControl",
        '43' : "TimerClearedStatus",
        '44' : "UserControlPressed",
        '45' : "UserControlReleased",
        '46' : "GiveOSDName",
        '47' : "SetOSDName",
        '64' : "SetOSDString",
        '67' : "SetTimerProgramTitle",
        '70' : "SystemAudioModeRequest",
        '71' : "GiveAudioStatus",
        '72' : "SetSystemAudioMode",
        '7a' : "ReportAudioStatus",
        '7d' : "GiveSystemAudioModeStatus",
        '7e' : "SystemAudioModeStatus",
        '80' : "RoutingChange",
        '81' : "RoutingInformation",
        '82' : "ActiveSource",
        '83' : "GivePhysicalAddress",
        '84' : "ReportPhysicalAddress",
        '85' : "RequestActiveSource",
        '86' : "SetStreamPath",
        '87' : "DeviceVendorID",
        '89' : "VendorCommand",
        '8a' : "VendorRemoteButtonDown",
        '8b' : "VendorRemoteButtonUp",
        '8c' : "GiveDeviceVendorID",
        '8d' : "MenuRequest",
        '8e' : "MenuStatus",
        '8f' : "GiveDevicePowerStatus",
        '90' : "ReportPowerStatus",
        '91' : "GetMenuLanguage",
        '92' : "SelectAnalogueService",
        '93' : "SelectDegitalService",
        '97' : "SetDigitalTimer",
        '99' : "clearDigitalTimer",
        '9a' : "SetAudioRate",
        '9d' : "InactiveSource",
        '9e' : "CECVersion",
        '9f' : "GetCECVersion",
        'a0' : "VendorCommandWithID",
        'a1' : "ClearExternalTimer",
        'a2' : "SetExternalTimer",
        'a3' : "ReportShortAudioDescriptor",
        'a4' : "RequestShortAudioDescriptor",
        'c0' : "InitiateARC",
        'c1' : "ReportARCInitiated",
        'c2' : "ReportARCTerminated",
        'c3' : "RequestARCInitiation",
        'c4' : "ReportARCTermination",
        'c5' : "TerminateARC",
        'f8' : "CDCMessage",
        'ff' : "AbortMessage",
    }
    #parameter x
    def translate_cec(self, initiator, destination, opcode) :
        return str('{:>18}'.format(cec_translate.cec_header_dictionary[initiator]) + ' ==> ' + '{:<18}'.format(cec_translate.cec_destination_dictionary[destination])
                   + ' ' + '{:<28}'.format(cec_translate.cec_opcode_dictionary[opcode]) + '\r\n')
    
    def translate_cec_poll(self, initiator, destination) :
        return str('{:>18}'.format(cec_translate.cec_header_dictionary[initiator]) + ' ==> ' + '{:<18}'.format(cec_translate.cec_destination_dictionary[destination])
                   + ' '+ "poll message\r\n")
        
    def translate_cec_parameter(self, initiator, destination, opcode, parameter) :
        return str('{:>18}'.format(cec_translate.cec_header_dictionary[initiator]) + ' ==> ' + '{:<18}'.format(cec_translate.cec_destination_dictionary[destination])
                   + ' ' + '{:<28}'.format(cec_translate.cec_opcode_dictionary[opcode]) + " " + parameter.replace(":", " ") + '\r\n')
    
    
    
    #parameter contents