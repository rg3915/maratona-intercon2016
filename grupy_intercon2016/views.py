from flask import render_template
from grupy_intercon2016 import app, pages

@app.route('/')
def index():
    return render_template('index.html')
    # posts = [page for page in pages if 'date' in page.meta]
    # # sort pages by date
    # sorted_posts = sorted(posts, reversed=True,
    #                         key=lambda page: page.meta['date'])
    # return render_template('index.html', pages=sorted_posts)

# @app.route('/<path:path>/')
# def page(path):
#     page = pages.get_or_404(path)
#     return render_template('page.html', page=page)
