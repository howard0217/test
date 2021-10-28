import Chatbot.console as console
import Chatbot.chatbot as Chatbot

c = console.Console(model_path='word2vec.model')#括號內為自己加的
#bot=Chatbot.Chatbot(w2v_model_path='word2vec.model')#這行自己加的
while True:
    speech = input('Input a sentence:')
    res,path = c.rule_match(speech)
    c.write_output(speech,res,path)

#chatter = Chatbot.Chatbot()
#chatter.waiting_loop()
