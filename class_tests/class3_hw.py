# try:
#     a = 1/0
# except ZeroDivisionError as my_error:
#     print(my_error)
#


# try:
#     my_file = open('C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/words.txt', 'r', encoding='utf-8')
#     content = my_file.read()
#     print(content)
# except IOError as x:
#     print(x)
# finally:
#     my_file.close()

##### 11.
from flask import Flask

app = Flask(__name__)


# returns the content of any txt file and status code 200
@app.route("/content")
def read_file():
    with open('/class_tests/words.txt', 'r', encoding='utf-8') as my_file:
        file_content = my_file.read()
    return file_content, 200  # status code


# using default
@app.route('/register')
def write_hello():
    with open('/class_tests/words.txt', 'w', encoding='utf-8') as my_file:
        my_file.write("""
                        <html>
                        <body>
                        <h1>My Heading</h1>
                        <p>My paragraph.</p>
                        <img src="https://media.giphy.com/media/U6YxrKZ84AfppW48r4/giphy.gif" alt="test_gal_pic">
                        </body>
                        </html>""")
    return 'success', 201  # status code


# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=30000)



##### 12.
# from PIL import Image
#
# new = Image.new(mode="RGBA", size=(1920,1080), color="pink")
# new.save('C:/Users/GalBoyanjo/PycharmProjects/devOpsExperts/pic.png', "PNG")
# new.show()
