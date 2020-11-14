import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/wallet", methods=["GET","POST"])
@login_required
def add():
    if request.method =="GET":
        return render_template("wallet.html")
    else:
        add = request.form.get("add")
        a = db.execute("SELECT username,hash,cash FROM users WHERE id= :id",id = session['user_id'])
        db.execute("UPDATE users SET cash =:leftmoney WHERE id= :idd",idd = session['user_id'],leftmoney = a[0]["cash"] + int(add))
        #above is updating user cash
        #above is updating cash
        return redirect("http://e1835471-243d-4a15-ad68-ff53252cf117-ide.cs50.xyz/", code=301)

@app.route("/")
@login_required
def index():

    c = db.execute("SELECT symbol,compname,price,shares FROM mainpage WHERE id=:ida",ida=session['user_id'])
    f = db.execute("SELECT cash FROM users WHERE id=:ida",ida=session['user_id'])
    return render_template("index.html", c=c,totalmoney="{:.2f}".format(f[0]["cash"]))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method =="GET":
        return render_template("buy.html")
    else:
        c = db.execute("SELECT symbol,compname,price,shares FROM mainpage WHERE id=:ida",ida=session['user_id'])
        symbol = lookup(request.form.get("symbol"))
        if symbol == None:
            return apology("No share found for this symbol")
        if float(request.form.get("shares")) < 0:
            return apology("Share number must be positive")
        symbol = lookup(request.form.get("symbol"))
        sym = request.form.get("symbol")
        shares = request.form.get("shares")
        a = db.execute("SELECT username,hash,cash FROM users WHERE id= :id",id = session['user_id'])
        boughtshare = float(symbol["price"]) * float(shares)
        #print(a[0]["cash"],symbol["price"])
        if a[0]["cash"] < boughtshare:
            #print(a,float(symbol["price"]) * float(shares))
            return apology("Not enough balance")
        else:
            db.execute("UPDATE users SET cash =:leftmoney WHERE id= :idd",idd = session['user_id'],leftmoney = a[0]["cash"] - boughtshare)

            if len(db.execute("SELECT symbol,price,compname,shares FROM 'mainpage' WHERE id = :ida AND symbol =:symbol",ida = session['user_id'], symbol = sym)) == 0:
                db.execute("INSERT INTO mainpage (id,symbol,shares,compname,price,totalprice) VALUES (:ida,:symbol,:shares,:compname,:price,:totalprice)", ida= session['user_id'], symbol=sym , shares = int(shares)  , compname=symbol["name"], price= symbol["price"], totalprice= 0)
            else:
                shares = request.form.get("shares")
                b = db.execute("SELECT sum(shares) FROM mainpage WHERE id=:idd AND symbol =:symbol ",idd = session["user_id"],symbol =sym)
                print(b)
                sumshare = int(shares) + int(b[0]["sum(shares)"])
                db.execute("UPDATE mainpage SET shares= :sumshare WHERE id= :idd AND symbol =:symbol",idd = session['user_id'],symbol=sym, sumshare=sumshare)
            db.execute("INSERT INTO transactions (id,symbol,shares,compname,price) VALUES (:ida,:symbol,:shares,:compname,:price)", ida= session['user_id'], symbol=sym , shares = int(shares)  , compname=symbol["name"], price= symbol["price"])
            #db.execute("INSERT INTO users (username, hash) VALUES (:name,:hash)",name=name,hash=password)
            return redirect("http://e1835471-243d-4a15-ad68-ff53252cf117-ide.cs50.xyz/", code=301)



@app.route("/history")
@login_required
def history():
    a = db.execute("SELECT symbol,price,shares,compname,transtime FROM transactions WHERE id=:ida ORDER BY transtime DESC;",ida=session['user_id'])
    return render_template("history.html",a = a)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method =="GET":
        return render_template("quote.html")
    else:
        symbol = lookup(request.form.get("symbol"))
        if symbol == None:
            return apology("No share found for this symbol")

        sym = request.form.get("symbol")
        return render_template("quoted.html", symbol=symbol["name"],sym=sym,cost="{:.2f}".format(symbol["price"]))



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    #return apology("TODO")

    else:
        if request.form.get("password") != request.form.get("passwordagain"):
            return apology("Please type in the same password")
        name = request.form.get("name")
        password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES (:name,:hash)",name=name,hash=password)
        return render_template("login.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        d = db.execute("SELECT symbol FROM 'mainpage' WHERE id = :ida",ida = session['user_id'])
        return render_template("sell.html", d=d)
    else:
        e = db.execute("SELECT symbol,shares,price FROM 'mainpage' WHERE id = :ida",ida = session['user_id'])
        symbol = lookup(request.form.get("symbol"))
        sym = request.form.get("symbol")
        shares = request.form.get("shares")
        if symbol == None:
            return apology("No share found for this symbol")
        if float(request.form.get("shares")) < 0:
            return apology("Share number must be positive")
        if e[0]["shares"] < int(shares):
            return apology("You don't have enough shares")
        else:
            a = db.execute("SELECT username,hash,cash FROM users WHERE id= :id",id = session['user_id'])
            boughtshare = float(symbol["price"]) * float(shares)
            db.execute("UPDATE users SET cash =:leftmoney WHERE id= :idd",idd = session['user_id'],leftmoney = a[0]["cash"] + boughtshare)
            #above is updating user cash
            #above is updating cash
            sumshare = e[0]["shares"] - int(shares)
            db.execute("UPDATE mainpage SET shares= :sumshare WHERE id= :idd AND symbol =:symbol",idd = session['user_id'],symbol=sym, sumshare=sumshare)
            db.execute("INSERT INTO transactions (id,symbol,shares,compname,price) VALUES (:ida,:symbol,:shares,:compname,:price)", ida= session['user_id'], symbol=sym , shares = - (int(shares))  , compname=symbol["name"], price= symbol["price"])
            return redirect("http://e1835471-243d-4a15-ad68-ff53252cf117-ide.cs50.xyz/", code=301)

        return apology("SMTGWENTWRONG")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
