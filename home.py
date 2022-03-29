from flask import Flask, render_template

myobj = Flask(__name__)
name = "Filler"
city_names=["Hanford", "Hanford 2, Electric Boogaloo", "test"]
def printCity(ary, index):
    if (index<len(ary)-1):
        return '''<li>'''+ary[index]+'''</li>'''+printCity(ary, index+1)
    else:
        return '''<li>'''+ary[index]+'''</li>'''

@myobj.route("/")
def home():
    return '''
    <html>
    <body>
    <h1>Welcome ''' + name +'''!</h1>
    <a href="www.google.com">notgoogle</a><br/>
    '''+printCity(city_names, 0)+'''  
    </body>
    </html>'''

#myapp_obj.run()