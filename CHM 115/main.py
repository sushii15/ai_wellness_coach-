from flask import Flask, render_template, request
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form.get('user_input')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"You are a health coach. {user_input}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
