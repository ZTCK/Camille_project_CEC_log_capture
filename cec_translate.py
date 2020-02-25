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
    #opcode
    cec_opcode_dictionary = {
        '00' : "Feature Abort",
        '04' : "Image View On",
        '05' : "Tuner Step Increment",
        '06' : "Tuner Step Decrement",
        '07' : "Tuner Device Status",
        '08' : "Give Tuner Device Status",
        '09' : "Record On",
        '0a' : "Record Status",
        '0b' : "Record Off",
        '0d' : "Text View On",
        '0f' : "Record TV Screen",
        '1a' : "Give Deck Status",
        '1b' : "Deck Status",
        '32' : "Set Menu Language",
        '33' : "Clear Analogue Timer",
        '34' : "Set Analogue Timer",
        '35' : "Timer Status",
        '36' : "Standby",
        '41' : "Play",
        '42' : "Deck Control",
        '43' : "Timer Cleared Status",
        '44' : "User Control Pressed",
        '45' : "User Control Released",
        '46' : "Give OSD Name",
        '47' : "Set OSD Name",
        '64' : "Set OSD String",
        '67' : "Set Timer Program Title",
        '70' : "System Audio Mode Request",
        '71' : "Give Audio Status",
        '72' : "Set System Audio Mode",
        '7a' : "Report Audio Status",
        '7d' : "Give System Audio Mode Status",
        '7e' : "System Audio Mode Status",
        '80' : "Routing Change",
        '81' : "Routing Information",
        '82' : "Active Source",
        '83' : "Give Physical Address",
        '84' : "Report Physical Address",
        '85' : "Request Active Source",
        '86' : "Set Stream Path",
        '87' : "Device Vendor ID",
        '89' : "Vendor Command",
        '8a' : "Vendor Remote Button Down",
        '8b' : "Vendor Remote Button Up",
        '8c' : "Give Device Vendor ID",
        '8d' : "Menu Request",
        '8e' : "Menu Status",
        '8f' : "Give Device Power Status",
        '90' : "Report Power Status",
        '91' : "Get Menu Language",
        '92' : "Select Analogue Service",
        '93' : "Select Degital Service",
        '97' : "Set Digital Timer",
        '99' : "clear Digital Timer",
        '9a' : "Set Audio Rate",
        '9d' : "Inactive Source",
        '9e' : "CEC Version",
        '9f' : "Get CEC Version",
        'a0' : "Vendor Command With ID",
        'a1' : "Clear External Timer",
        'a2' : "Set External Timer",
        'a3' : "Report Short Audio Descriptor",
        'a4' : "Request Short Audio Descriptor",
        'c0' : "Initiate ARC",
        'c1' : "Report ARC Initiated",
        'c2' : "Report ARC Terminated",
        'c3' : "Request ARC Initiation",
        'c4' : "Report ARC Termination",
        'c5' : "Terminate ARC",
        'f8' : "CDC Message",
        'ff' : "Abort Message",
    }
    
    Abort_Reason_Dictionary = {
        '00' : "Unrecognized opcode",
        '01' : "Not in correct mode to respond",
        '02' : "Cannot provide source",
        '03' : "invalid operand",
        '04' : "Refused",
        '05' : "Unable to determine",
    }
    
    Analogue_Broadcast_Type_Dictionary = {
        '00' : "Cable",
        '01' : "Satellite",
        '02' : "Terrestrial",
    }
    
    Audio_Rate_Dictionary = {
        '00' : "Rate Control Off",
        '01' : "Standard Rate : 100% rate",
        '02' : "Fast Rate : Max 101% rate",
        '03' : "Slow Rate : Min 99% rate",
        '04' : "Standard Rate : 100.0% rate",
        '05' : "Fast Rate : Max 100.1% rate",
        '06' : "Slow Rate : Min 99.9% rate",
    }
    
    CEC_Version_Dictionary = {
        '00' : "Reserved",
        '01' : "Reserved",
        '02' : "Reserved",
        '03' : "Reserved",
        '04' : "Version 1.3a",
        '05' : "Version 1.4",
    }
    
    '''def get_Channel_Number_Format(n) {
        if(n == '01') :
            return "1-part Channel Number"
        elif(n == '02') :
            return "2-part Channel Number"
    }
    
    def get_Broadcast_System(n) {
        if int(n) == 31 :
            return "Other System"
        elif int(n) < 31 and int(n) > 8 :
            return "Future Use"
        elif n = '0' : return "PAL B/G"
        elif n = '1' : return "SECAM L\'"
        elif n = '2' : return "PAL M"
        elif n = '3' : return "NTSC M"
        elif n = '4' : return "PAL I"
        elif n = '5' : return "SECAM DK"
        elif n = '6' : return "SECAM B/G"
        elif n = '7' : return "SECAM L"
        elif n = '8' : return "PAL DK"
    }
    
    def get_Audio_Volume_Status(n) {
        if(int("0x" + n, 16) <= 100) :
            return str(int("0x" + n, 16))
        elif n == "7f" :
            return "Current audio volume status is unknown"
        else :
            return "Reserved"
    }

    def get_Audio_Mute_Status(n) {
        if(n == '0') :
            return "Audio Mute Off"
        else :
            return "Audio Mute On"
    }

    def get_ASCII(n) {
        return n.decode("hex") 
    }
    
    def get_Analogue_Frequency(n) {
        return int("0x"+n, 16) * 62.5   #Khz, n = 2bytes    
    }
    '''
    #parameter x
    def translate_cec(self, initiator, destination, opcode) :
        return str(" initiator : \'" + cec_translate.cec_header_dictionary[initiator] + "\', destination : \'" + cec_translate.cec_header_dictionary[destination]
                   + "\', opcode : \'" + cec_translate.cec_opcode_dictionary[opcode] + '\'\n')
    
    def translate_cec_poll(self, initiator, destination) :
        return str("  initiator : \'" + cec_translate.cec_header_dictionary[initiator] + "\', destination : \'" + cec_translate.cec_header_dictionary[destination] + "\' #poll message \n")
        
    def translate_cec_parameter(self, initiator, destination, opcode, parameter) :
        return str(" initiator : \'" + cec_translate.cec_header_dictionary[initiator] + "\', destination : \'" + cec_translate.cec_header_dictionary[destination]
                   + "\', opcode : \'" + cec_translate.cec_opcode_dictionary[opcode] + "\', parameter : \'" + parameter + '\'\n')
    
    
    
    #parameter contents