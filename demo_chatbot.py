import Chatbot.chatbot as Chatbot

'''import Chatbot.console as console
c = console.Console(model_path='word2vec.model')'''

chatter = Chatbot.Chatbot(w2v_model_path='word2vec.model')#括號內的為自己加的
chatter.waiting_loop()
