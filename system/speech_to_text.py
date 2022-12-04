import requests
import json
from pydub import AudioSegment


def speech_to_text(audioFile):
    url = "https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US"

    # payload=open("check.m4a","rb")
    headers = {
    'Ocp-Apim-Subscription-Key': '24aee5e3da7246b780aed3c3e85010ea',
    'Content-Type': 'audio/wav',
    'Authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJyZWdpb24iOiJlYXN0dXMiLCJzdWJzY3JpcHRpb24taWQiOiIyM2I2MmVkZDk0NDM0OTM0YWY3Y2ZmZDA3ZTA4NTgzYyIsInByb2R1Y3QtaWQiOiJTcGVlY2hTZXJ2aWNlcy5GMCIsImNvZ25pdGl2ZS1zZXJ2aWNlcy1lbmRwb2ludCI6Imh0dHBzOi8vYXBpLmNvZ25pdGl2ZS5taWNyb3NvZnQuY29tL2ludGVybmFsL3YxLjAvIiwiYXp1cmUtcmVzb3VyY2UtaWQiOiIvc3Vic2NyaXB0aW9ucy9hNmU0ZTYzZS0zYjdhLTRiOWEtOWM5OS0yNTY1ZDQ4OWJkZmUvcmVzb3VyY2VHcm91cHMvdGVtcC1yZXNvdXJjZS1ncm91cC9wcm92aWRlcnMvTWljcm9zb2Z0LkNvZ25pdGl2ZVNlcnZpY2VzL2FjY291bnRzL1Byb251bmNpYXRpb25DaGVja0FQSSIsInNjb3BlIjoic3BlZWNoc2VydmljZXMiLCJhdWQiOiJ1cm46bXMuc3BlZWNoc2VydmljZXMuZWFzdHVzIiwiZXhwIjoxNjY3NjU2NDkxLCJpc3MiOiJ1cm46bXMuY29nbml0aXZlc2VydmljZXMifQ.72B-ggb5SipEcc8sH3EyCBsedQJinwCDJ90wMEAoarM'
    }
    x = AudioSegment.from_file(audioFile)
    x.export("check.wav", format='wav')    # maybe use original resolution to make smaller
    response = requests.request("POST", url, headers=headers, data=open("check.wav",'rb'))
    print(response.text)
    return json.loads(response.text)