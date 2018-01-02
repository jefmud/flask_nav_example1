from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav(app)

nav.register_element('my_navbar',
                        Navbar('thenav',
                        View('Home Page', 'index'),
                        View('Item One', 'item', item=1),
                        View('Item Two', 'item', item=2),
                        Link('Google', 'https://google.com'),
                        Separator(),
                        Text('Some Text'),
                        Subgroup('Extras',Link('yahoo','https://www.yahoo.com'),
                        View('Item 42', 'item', item=42))
                        ))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items/<item>')
def item(item):
    return render_template('items.html', item=item)
    #return '<h1>Item Page</h1>\n<p>The item is: {}</p>\n'.format(item)

if __name__ == '__main__':
    app.run(debug=True)
