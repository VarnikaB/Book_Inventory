from flask import  render_template,url_for,redirect,request,jsonify
from flask import Flask
from google_book_api import list_books
import sqlite3

app = Flask(__name__)

 
@app.route('/', methods = ['POST', 'GET'])
def red():
    return redirect("/login")


@app.route("/create",methods=["GET","POST"])
def create():
    if request.method=="GET":
        return render_template("create_account.html")
    elif request.method=="POST":
        user=request.form["username"]
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        pwd=request.form["pass"]               
        stmt = 'Select * from User where '+'Username = "'+user+'"'
        cur.execute(stmt)
        print(cur.fetchall())
        res = cur.fetchall()
        
        if len(res) != 0:
            return '<h1>Username already present please try with a different username</h1><br><a href="/">Go Back</a>'
        stmt = 'Insert into User values ("'+user+'","'+pwd+'")'
        cur.execute(stmt)
        con.commit()
        con.close()
        return render_template("login.html",flag=True)

@app.route("/login",methods=["GET","POST"])
def login():
    """ cursor = con. cursor()
    cursor. execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor. fetchall()) """
    if request.method=="GET":
        return render_template("login.html",flag=False)
    elif request.method=="POST":
        user=request.form["username"]
        pwd=request.form["pass"]
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        stmt = 'Select * from User where '+'Username = "'+user+'"'        
        cur.execute(stmt)
        if cur.rowcount != 0:
            #print(cur.fetchall(),'hi')
            res = cur.fetchall()
            con.close()
            #print(res[0][1], user, pwd)
            if res == None:
                return render_template("not_exist.html",flag=False,value = "User does not exist")
            elif pwd ==res[0][1]:
                return redirect(f"/{user}/Overview")            
            else:
                return render_template("not_exist.html",flag=False,value = "Wrong Password")      
        else:
            return render_template("not_exist.html",flag=False,value = "User does not exist")     
 

@app.route("/<string:username>/Overview",methods=["GET","POST"])
def overview(username):
    user = username
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    stmt = 'Select * from Store where '+'Username = "'+user+'"'
    print(stmt)
    cur.execute(stmt)
    res = cur.fetchall()
    con.close()
    if request.method == 'GET':
        print('hi')
        return render_template('loc.html',title = 'Stores',details = res, flag = False,username = user)
    else:
        print('hello')
        return f"<h1>Something not right</h1>"


@app.route("/<string:username>/addStore",methods=["GET","POST"])
def addStore(username):
    if request.method == 'POST':
        store_name = request.form['storename']
        con = sqlite3.connect('database.db')
        cur1 = con.cursor()
        stmt = "Insert into Store ('Store_Name','Username') values ('{}','{}')".format(store_name, username)
        cur1.execute(stmt)
        con.commit()
        con.close()
        return redirect(f"/{username}/Overview")
    else:
        print('Add Problem')

@app.route("/<string:username>/<int:store_id>/deleteStore",methods=["GET","POST"])
def deleteStore(username, store_id):
    if request.method == 'GET':
        con = sqlite3.connect('database.db')        
        cur = con.cursor()
        stmt = "Delete from Store where Store_ID = {}".format(store_id)
        cur.execute(stmt)
        con.commit()
        con.close()
        return redirect(f"/{username}/Overview")
    else:
        print('Delete Problem')

@app.route("/<string:username>/<int:store_id>/editStore",methods=["GET","POST"])
def editStore(username, store_id):
    print(request.method)
    if request.method == 'POST':
        store_name = request.form['storename_edit']
        conn = sqlite3.connect('database.db', check_same_thread=False)
        cur = conn.cursor()
        stmt = "update Store set Store_Name = '{}' where Store_ID = {}".format(store_name, store_id)
        print(stmt, 'yyy')
        cur.execute(stmt)
        conn.commit()
        conn.close()
        return redirect(f"/{username}/Overview")
    else:
        return redirect(f"/{username}/Overview")

@app.route("/<string:username>/<int:storeid>/Store",methods=["GET","POST"])
def displaybook(username, storeid):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    stmt = 'Select * from Books where Store_id = {}'.format(storeid)
    print(stmt)
    cur.execute(stmt)
    res = cur.fetchall()
    con.close()
    if request.method == 'GET':
        print('hi')
        return render_template('books.html',title = 'Books',details = res, flag = False,username = username,storeid = storeid)
    else:
        print('hello')
        return "<h1>Something not right</h1>"

@app.route('/<string:username>/<int:storeid>/addBook',methods=["GET","POST"])
def addBook(username, storeid):
    if request.method == 'POST':
        book_id = request.form['bookid']
        book_name = request.form['bookname']
        k = list_books(book_name)
        qty = k['totalItems']
        con = sqlite3.connect('database.db')
        cur1 = con.cursor()
        stmt = "Insert into Books values ('{}','{}',{},{})".format(book_id, book_name,qty,storeid)
        cur1.execute(stmt)
        con.commit()
        con.close()        
        return redirect(f"/{username}/{storeid}/Store")
    else:
        print('Add Problem')

@app.route('/<string:username>/<int:storeid>/<string:bookid>/deleteBook',methods=["GET","POST"])
def deletebook(username, storeid,bookid):
    if request.method == 'GET':
        print('hello')
        con = sqlite3.connect('database.db')        
        cur = con.cursor()
        stmt = "Delete from Books where Store_ID = {} and Book_ID = '{}'".format(storeid,bookid)
        print(stmt)
        cur.execute(stmt)
        con.commit()
        con.close()
        return redirect(f"/{username}/{storeid}/Store")
    else:
        print('Delete Problem')

@app.route('/<string:username>/<int:storeid>/<string:bookid>/editBook',methods=["GET","POST"])
def editBook(username, storeid, bookid):
    if request.method == 'POST':
        qty = request.form['qty_edit']
        conn = sqlite3.connect('database.db', check_same_thread=False)
        cur = conn.cursor()
        stmt = "update Books set Number_of_books = '{}' where Store_ID = {} and Book_ID = '{}'".format(qty, storeid, bookid)
        print(stmt, 'yyy')
        cur.execute(stmt)
        conn.commit()
        conn.close()
        return redirect(f"/{username}/{storeid}/Store")
    else:
        return redirect(f"/{username}/{storeid}/Store")


app.run(host='localhost', port=7000)