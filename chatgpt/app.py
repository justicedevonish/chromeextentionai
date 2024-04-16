from flask import Flask
from openai import OpenAI
from api_keys import OPENAI_API_KEY

app = Flask(__name__)
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_response(prompt)
        return render_template('popup.html', response=response)
    return render_template('popup.html', response=None)

def generate_response(prompt):
    response = client.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
