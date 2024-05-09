import webbrowser
import os
content = "<p>This is paragraph. </p>"
print()
f = open('mission_result.html', 'w')

message = """<html>
<head>Mission result</head>
<body>""" + """<p>Hello World!</p>""" + content + """</body>
</html>"""

f.write(message)
f.close()

# Change path to reflect file location
filename = 'file:///' + os.getcwd() + '/' + 'mission_result.html'
webbrowser.open_new_tab(filename)