
import win32com.client as wincl

class speak :
        
    speaker_number = 1
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    SVSFlag = 11
    print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
    spk.Voice
    spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
    
    def sp(self,name):
        self.spk.Speak(f"{name}!")
    

class s1:
    spk = wincl.Dispatch("SAPI.SPvoice")

    def sp1(self,name):
        self.spk.Speak(f'shout out to {name}!')





l = ['ram','ramesh','suresh','Mukesh']

# s = s1()

# for i in l:
#     s.sp1(i)