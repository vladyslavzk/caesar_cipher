from flask import Flask, render_template, request


app = Flask(__name__)


def caesar(text, shift):
    res = ""

    ascii_upper_offsite = ord('A')
    ascii_lower_offsite = ord('a')

    for char in text:
        if char.isupper():
            res += chr((ord(char) + shift - ascii_upper_offsite) % 26 + ascii_upper_offsite)
        elif char.islower():
            res += chr((ord(char) + shift - ascii_lower_offsite) % 26 + ascii_lower_offsite)
        else:
            res += char
    
    return res




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == "encrypt":

            text = request.form['text']
            shift = int(request.form['shift'])
            result_text = caesar(text, shift)

            return render_template('result.html', result_text=result_text)
        
        elif request.form['action'] == 'decrypt':
            text = request.form['text']
            shift = int(request.form['shift'])
            result_text = caesar(text, -shift)

            return render_template("result.html", result_text=result_text)

    

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)