from flask import Flask
from controller import get_answer, translate
from schema import question, translating

app = Flask(__name__)

@app.get("/")
def working():
    return "API Working"

@app.post('/ask')
def askQuestion(ques:question):
    return get_answer(ques.question)

@app.post('/translate')
def translater(translating: translating):
    return translate(translating.sentence,translating.code)

if '__main__'==__name__:
    # uvicorn.run(
    #     'main:app',
    #     reload=True,
    #     port=8000,
    #     host='localhost'
    # )
    app.run(debug=True)