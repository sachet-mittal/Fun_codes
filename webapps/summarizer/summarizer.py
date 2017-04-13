from flask import Flask, url_for, render_template, request
from flask_wtf import Form
import wtforms
from nlp.summary import summarize

app = Flask(__name__)
app.config['SECRET_KEY'] = "summary"

@app.route('/summary', methods=['GET', 'POST'])
def summary():
    class SummaryForm(Form):
        text = wtforms.TextAreaField("Input:")

    form = SummaryForm()
    result = None
    if form.validate_on_submit():
        result = summarize(form.text.data, 3)

    return render_template('summarize.jinja2', result=result, form=form)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
