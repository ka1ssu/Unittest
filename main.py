from flask import Flask, render_template, request
app = Flask(__name__)


var = {'RUB': 1, 'USD': 80, 'EUR': 86, 'TL': 4}


@app.route("/")
def index():
    return render_template('main.html')


@app.route('/', methods=['post', 'get'])
def count():
    str = "Результат = "
    user_chislo = float(request.form['name1'])
    valuta_start = request.form['name2']
    valuta_itog = request.form['name3']
    text = user_chislo * var[f'{valuta_start}'] / var[f'{valuta_itog}']
    return render_template('main.html', text=text)


def test1(summ):
    try:
        if type(summ) == str:
            return "That's wrong"
        var = int(summ)
        if var < 0:
            return "That's wrong"
    except:
        return var


if __name__ == "__main__":
    app.run(debug=True)