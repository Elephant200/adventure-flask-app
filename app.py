from flask import Flask, request, render_template, session, url_for, redirect
from werkzeug.exceptions import HTTPException, NotFound
import json
import traceback

app = Flask(__name__)
app.secret_key = "elephant"

with open("map.json", "r") as f:
    map = json.load(f)

ERROR_MESSAGES = {
    400: "The request could not be understood by the server due to malformed syntax.",
    403: "You don't have permission to access this resource.",
    404: "The requested URL was not found on this server.",
    418: "I'm a teapot. Seriously.",
    500: "Something went wrong on the server."
}

@app.route('/')
def home_page():
    session["key"] = False
    return render_template("index.html")

@app.route("/page")
def render_story():
    page_id = request.args.get("id")
    key_collected = session.get("key", False)

    if page_id == "key":
        session["key"] = True
        session.modified = True
    if page_id == "1":
        session["key"] = False

    if page_id in map:
        page_data = map[page_id]

        if page_id in map.get("keyPages", []):
            if key_collected:
                content = page_data.get("text_unlocked") if key_collected else page_data.get("text")
                choices = page_data.get("choices_unlocked") if key_collected else page_data.get("choices")
                ending = page_data.get("ending", None) if key_collected else None
            else:
                content = page_data.get("text")
                choices = page_data.get("choices")
                ending = None
        else:
            content = page_data.get("text")
            choices = page_data.get("choices")
            ending = page_data.get("ending", None)
        
        return render_template("page.html", content=content, choices=choices, ending=ending)
    else:
        raise NotFound()
    

@app.errorhandler(404)
def handle_404(e):
    return handle_all_errors(e)

@app.errorhandler(Exception)
def handle_all_errors(e):
    print("Error handler triggered")
    if isinstance(e, HTTPException):
        code = e.code
        name = e.name
        default_desc = e.description
    else:
        code = 500
        name = "Internal Server Error"
        default_desc = "An unexpected error occurred."

    extended_message = ERROR_MESSAGES.get(code, default_desc)

    debug_traceback = None
    if code == 500 and app.debug:
        debug_traceback = traceback.format_exc()

    return render_template("error.html", error_code=code, short_message=name, long_message=extended_message, debug_traceback=debug_traceback), code

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)