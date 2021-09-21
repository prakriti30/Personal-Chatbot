from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from Form import TopicForm
from Scraper import web_request, scrape_data



app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TopicForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        query = form.query.data
        query_result = web_request(query)
        query_resonse = scrape_data(query_result)
        print(query_resonse)
        return render_template('Main.html', form=form, result=query_resonse)
    return render_template('Main.html', form=form)


if __name__ == '__main__':
    app.run()
