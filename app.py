from flask import Flask, render_template
app = Flask(__name__)

CONFIG = {
    "site_title": "Choose Your Own Adventure",
    "site_name": "Choose Your Own Adventure",
    "site_description": "A website where you can choose your own adventure!",
}

@app.route('/')
def page_1():
    start_text = """
    You’re sitting at your desk during a perfectly ordinary math lesson when, out of nowhere, the
    blackboard erupts in a dazzling flash of light. There, resting against the wall, is a shimmering
    sword—clearly out of place among the textbooks and chalk dust. Your heart thunders. No one else
    in the room seems to notice, as if the sword has cast some sort of invisible cloak over itself,
    visible only to you. Do you dare investigate this strange weapon?
    """
    choices = [
        {"text": "Pick up the sword", "route": "page_2"},
        {"text": "Call for your teacher's help", "route": "page_3"},
    ]
    return render_template('page.html', content=start_text, choices=choices, config=CONFIG)

@app.route('/page_2')
def page_2():
    text = """
    You wrap your fingers around the sword’s hilt, and a tingling sensation races up your arm,
    sending shivers down your spine. The blade hums with unearthly energy, bright runes dancing
    along its surface. Almost immediately, the classroom around you starts to shift: one of your
    classmates’ shadows twists into a snarling monster, red eyes glowing. This creature is clearly
    drawn to the sword’s power. Do you stand your ground, sword at the ready, to battle this
    abomination? Or do you drop everything and flee?
    """
    choices = [
        {"text": "Fight the monster", "route": "page_5"},
        {"text": "Run in search of help", "route": "page_3"},
    ]
    return render_template('page.html', content=text, choices=choices, config=CONFIG)

@app.route('/page_3')
def page_3():
    text = """
    You sprint to the teacher’s desk, waving your arms in panic. At first, the teacher is
    perplexed—until they see the sword in your hand. Shock washes over their face. “That sword...
    it’s cursed!” they exclaim. The teacher insists you hand it over immediately for everyone’s
    safety. But something in your gut warns you: what if the teacher is acting under the sword’s
    influence, or perhaps something more sinister lies in wait if you let the blade go?
    """
    choices = [
        {"text": "Hand over the sword", "route": "page_4"},
        {"text": "Refuse to give up the sword", "route": "page_2"},
    ]
    return render_template('page.html', content=text, choices=choices, config=CONFIG)

@app.route('/page_4')
def page_4():
    text = """
    The moment the teacher touches the sword, a malevolent force crackles through the air. Their
    eyes turn pitch-black, and they twist toward you with a horrifying smile. Before you can react,
    the cursed sword swings in a vicious arc, and everything goes dark. Your last thought is that
    you should have never surrendered the weapon.
    <br><br>
    <b>Bad Ending: You Have Perished.</b>
    """
    choices = [
        {"text": "Start Over", "route": "/"},
    ]
    return render_template('page.html', content=text, choices=choices, config=CONFIG)


@app.route('/page_5')
def page_5():
    text = """
    Steeling your courage, you brandish the glowing sword. The monster snarls, launching itself at
    you. Sparks fly as your blade meets the creature’s claws in a furious clash. Drawing on an inner
    strength you never knew you had, you thrust the sword forward. The monster disintegrates in a
    burst of smoky darkness, leaving only trembling silence in its wake. Your classmates remain
    safe, and the haunted sword’s glow softens as if it, too, is finally at peace.
    <br><br>
    <b>Good Ending: You Emerge Triumphant.</b>
    """
    choices = [
        {"text": "Start Over", "route": "/"},
    ]
    return render_template('page.html', content=text, choices=choices, config=CONFIG)