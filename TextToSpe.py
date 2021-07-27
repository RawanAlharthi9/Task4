from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/d5841ae1-7685-4f46-9a6e-a9662f71e71f'
apikey = 'bwH1SSwJNdSlbyGWtxrYvR7-QyJ9p96nzj4lTpn3XeG1'


authenticator = IAMAuthenticator(apikey)

tss = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open ('./speech-tts.mp3','wb') as audio_file:
    res = tts.synthesize ('Hello World!' ,accept = 'audio/mp3' , voice= 'en_US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

