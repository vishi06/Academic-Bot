from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
app = Flask(__name__)
my_bot = ChatBot("Academic_bot")
conversation=open('conv.txt','r').readlines()


trainer = ListTrainer(my_bot)
trainer.train(conversation)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/get")
def get_bot_response():
        userText = request.args.get('msg')
        return str(my_bot.get_response(userText))

if __name__ == "__main__":
    app.debug =True
    app.run()