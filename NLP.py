import transformers

class Chatbot:
    def __init__(self):
        self.name="Quarks Industrials"

    
    def text_generation(self,text):
        nlp=transformers.pipeline("conversational",model="microsoft/DialoGPT-medium")
        if any(i in text for i in ['bye','exit','close']):
            return "We hope to serve you again soon!"
        elif any(i in text for i in ['hi','hey','heyy']):
            return "HI, Welcome to "+self.name+'.'
        else:
            chat=nlp(transformers.Conversation(text),pad_token_id=50256)
            chat=str(chat)
            chat=chat[chat.find("bot >> ")+6:]
            return chat




