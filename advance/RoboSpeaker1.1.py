import os

if __name__ == '__main__':
    inp = input("enter what do you want to listen: ")
    command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{inp}')"
    os.system(command)