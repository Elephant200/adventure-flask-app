from flask import Flask, abort, request, render_template, session
from werkzeug.exceptions import HTTPException, NotFound
import json
import traceback

app = Flask(__name__)
app.secret_key = "elephant"

with open("map.json", "r") as f:
    map = json.load(f)

ERROR_MESSAGES = {
    # 4xx Client Error Messages
    400: "The request could not be understood by the server due to malformed syntax.",
    401: "You need to provide valid authentication credentials.",
    402: "Access to this resource requires payment.",
    403: "You don't have permission to access this resource.",
    404: "The requested URL was not found on this server.",
    405: "The method used in the request is not allowed for this resource.",
    406: "The requested resource is not available in a format that is acceptable.",
    407: "You need to authenticate with the proxy server first.",
    408: "The server timed out waiting for the request.",
    409: "The request could not be completed due to a conflict with the current state of the resource.",
    410: "The resource you are trying to access is no longer available and will not be coming back.",
    411: "The request is missing a required Content-Length header.",
    412: "The server rejected the request because a precondition was not met.",
    413: "The request entity is too large for the server to process.",
    414: "The requested URL is too long for the server to process.",
    415: "The request contains an unsupported media type.",
    416: "The requested range is not satisfiable.",
    417: "The server cannot meet the expectations set in the Expect request header.",
    418: "I'm a teapot. Seriously.",
    421: "The request was misdirected and cannot be handled by this server.",
    422: "The request was well-formed but could not be processed due to semantic errors.",
    423: "The resource is locked and cannot be accessed.",
    424: "The request failed because it depends on another request that failed.",
    425: "The server is unwilling to process the request because it was sent too early.",
    426: "The client must upgrade to a different protocol to access this resource.",
    428: "The request requires a precondition that was not met.",
    429: "You have sent too many requests in a short period of time. Slow down.",
    431: "The request headers are too large for the server to process.",
    451: "The requested resource is unavailable due to legal reasons.",
    
    # 5xx Server Error Messages
    500: "Something went wrong on the server.",
    501: "The server does not recognize the request method or cannot fulfill it.",
    502: "The server received an invalid response from an upstream server.",
    503: "The server is currently unavailable, possibly due to maintenance or overload.",
    504: "The server did not receive a timely response from an upstream server.",
    505: "The server does not support the HTTP protocol version used in the request.",
    506: "The server encountered a variant negotiation error.",
    507: "The server does not have enough storage space to process the request.",
    508: "The server detected an infinite loop while processing the request.",
    510: "The request requires further extensions to be fulfilled.",
    511: "You need to authenticate with the network before sending the request."
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
    if code >= 500 and app.debug:
        debug_traceback = traceback.format_exc()

    return render_template("error.html", error_code=code, short_message=name, long_message=extended_message, debug_traceback=debug_traceback), code


# Error Testing
@app.route('/error')
def trigger_error():
    error_type = request.args.get("type")

    if not error_type or not error_type.isdigit():
        abort(400)

    error_code = int(error_type)

    if error_code in range(400, 512):
        abort(error_code)
    
    abort(400)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)