from flask import Flask, request, render_template_string, redirect
import urllib.parse

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Google Search</title>
<h2>Google Search Box</h2>
<form method="get" action="/search">
  <input type="text" name="q" placeholder="Type your query..." required>
  <input type="submit" value="Search">
</form>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if query:
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        return redirect(url)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)