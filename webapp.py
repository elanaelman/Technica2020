from flask import Flask, render_template, request
app = Flask(__name__)

projects = ["Stars", "Graphics"]

@app.route("/")
def home():
    title = "Scattered Projects of Elana Elman"
    content = "Welcome to my project site. I'll try to keep this updated with my little experiments."
    return render_template('home.html', projects=projects, title=title, content=content)

@app.route("/Stars")
def stars():
    title = "I made a program about star polygons"
    content = "yoooooooooo"
    status = "Completed"
    return render_template('project.html', projects=projects, title=title, content=content, status=status)

@app.route("/Graphics")
def graphics():
    title = "idk some stuff I guess"
    content = "yeeeeeeee"
    status = "On Hold"
    return render_template('project.html', projects=projects, title=title, content=content, status=status)

if __name__ == "__main__":
    app.run()
