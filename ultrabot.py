import json
import requests
import datetime
from NLP import Chatbot

class ultrachatbot():
    def __init__(self,json):
        self.json = json
        self.dict_messages=json['data']
        self.ultraAPIUrl = 'https://api.ultramsg.com/instance50227/'
        self.token='t7jqrsly31qa80zz'
    
    def send_requests(self,type,data):
        url=f"https://api.ultramsg.com/instance50227/{type}?token=t7jqrsly31qa80zz"
        headers={'content-type':'application/json'}
        answer=requests.request("POST",url,data=json.dumps(data),headers=headers)
        print(answer)
        return answer.json()
    
    def send_message(self,ChatID,text):
        data={'to':ChatID,'body':text}
        answer=self.send_requests('messages/chat',data)
        return answer
    
    def send_image(self,ChatID):
        data={'to':ChatID,'image':"https://file-example.s3-accelerate.amazonaws.com/images/test.jpeg"}
        answer=self.send_requests('messages/image',data)
        return answer
    
    def send_audio(self,ChatID):
        data={'to':ChatID,'audio':"https://file-example.s3-accelerate.amazonaws.com/audio/2.mp3"}
        answer=self.send_requests('messages/audio',data)
        return answer
    
    def send_video(self,ChatID):
        data={'to':ChatID, 'video':"https://file-example.s3-accelerate.amazonaws.com/video/test.mp4"}
        answer=self.send_requests('messages/video',data)
        return answer
    
    
    def send_voice(self,ChatID):
        data={'to':ChatID,'audio':"https://file-example.s3-accelerate.amazonaws.com/voice/oog_example.ogg"} 
        answer=self.send_requests('messages/voice',data)
        return answer
    
    def send_contact(self, chatID):
        data = {"to" : chatID,
                "contact" : "14000000001@c.us"}  
        answer = self.send_requests('messages/contact', data)
        return answer
    
    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%Y-%m-%d %H:%M:%S')
        return self.send_message(chatID, time)
    
    def welcome(self,ChatID,text='hi',noWelcome=False):
        welcome_str=''
        if noWelcome==False:
            welcome_str='HI, Welcome to Quarks Industrials\n'
        else:
            cb=Chatbot()
            welcome_str=cb.text_generation(text)
        return self.send_message(ChatID,welcome_str)
    
    def Processingـincomingـmessages(self):
        if self.dict_messages!=[]:
            messages=self.dict_messages
            text=messages['body']
            if not messages['fromMe']:
                ChatID=messages['from']
                if text.lower()=='hi':
                    return self.welcome(ChatID)
                elif text.lower()=='time':
                    return self.time(ChatID)
                elif text.lower()=='image':
                    return self.send_image(ChatID)
                elif text.lower()=='audio':
                    return self.send_audio(ChatID)
                elif text.lower()=='voice':
                    return self.send_voice(ChatID)
                elif text.lower()=='video':
                    return self.send_video(ChatID)
                elif text.lower()=='image':
                    return self.send_image(ChatID)
                elif text.lower()=='contact':
                    return self.send_contact(ChatID)
                else:
                    return self.welcome(ChatID,text,True)
        else: return 'NoCommand'

                


    