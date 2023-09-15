from flask import Flask, render_template, request, url_for, flash, redirect, url_for, session
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask import Blueprint

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cryptocrud'

mysql = MySQL(app)
crud_blueprint = Blueprint('crud', __name__)


@app.route('/insert_crypto_type', methods=['POST'])
def insert_crypto_type():
    if request.method == "POST":
        flash("Cryptocurrency Type Inserted Successfully")
        name = request.form['name']
        symbol = request.form['symbol']

        cur = mysql.connection.cursor()
        cur.execute("""
        INSERT INTO cryptocurrency_types (name, symbol)
        VALUES (%s, %s)
        """, (name, symbol))
        mysql.connection.commit()
        return redirect(url_for('types'))
    
@app.route('/delete_crypto_type/<string:id_data>', methods=['GET'])
def delete_crypto_type(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cryptocurrency_types WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('types'))

@app.route('/update_crypto_type', methods=['POST'])
def update_crypto_type():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        symbol = request.form['symbol']  

        cur = mysql.connection.cursor()
        
        try:
            cur.execute("""
            UPDATE cryptocurrency_types SET 
            name=%s, symbol=%s
            WHERE id=%s
            """, (name, symbol, id_data))
            
            mysql.connection.commit()
            flash("Cryptocurrency Types Data Updated Successfully")
        except Exception as e:
            # Print the error message for debugging
            print("Error:", str(e))
            mysql.connection.rollback()
            flash("An error occurred while updating data. Please try again.", "error")
        finally:
            cur.close()

        return redirect(url_for('types'))

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cryptocurrency_prices")
    data = cur.fetchall()

    # Fetch cryptocurrency types for the dropdown
    cur.execute("SELECT * FROM cryptocurrency_types")
    crypto_types = cur.fetchall()
    
    cur.execute("""
    SELECT cp.id, cp.price_date, ct.name, ct.symbol, cp.open_price, cp.highest_price, cp.lowest_price, cp.close_price, cp.adjusted_close_price, cp.volume
    FROM cryptocurrency_prices cp
    JOIN cryptocurrency_types ct ON cp.cryptotype = ct.id
    """)
    alldata = cur.fetchall()
    
    cur.close()

    return render_template('index.html', cryptocurrency_prices=data, cryptocurrency_types=crypto_types, alldata=alldata)

@app.route('/insert_price', methods=['POST'])
def insert_price():
    if request.method == "POST":
        flash("Cryptocurrency Price Data Inserted Successfully")
        price_date = request.form['price_date']
        cryptotype = request.form['cryptotype']  # Use the ID as FK
        open_price = request.form['open_price']
        highest_price = request.form['highest_price']
        lowest_price = request.form['lowest_price']
        close_price = request.form['close_price']
        adjusted_close_price = request.form['adjusted_close_price']
        volume = request.form['volume']

        cur = mysql.connection.cursor()
        cur.execute("""
        INSERT INTO cryptocurrency_prices (price_date, cryptotype, open_price, highest_price, lowest_price, close_price, adjusted_close_price, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (price_date, cryptotype, open_price, highest_price, lowest_price, close_price, adjusted_close_price, volume))
        mysql.connection.commit()
        return redirect(url_for('prices'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cryptocurrency_prices WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('prices'))
    
@app.route('/update_price', methods=['POST'])
def update_price():
    if request.method == 'POST':
        id_data = request.form['id']
        price_date = request.form['price_date']
        cryptotype = request.form['cryptotype']  # Use the ID as FK
        open_price = request.form['open_price']
        highest_price = request.form['highest_price']
        lowest_price = request.form['lowest_price']
        close_price = request.form['close_price']
        adjusted_close_price = request.form['adjusted_close_price']
        volume = request.form['volume']

        cur = mysql.connection.cursor()
        
        try:
            cur.execute("""
            UPDATE cryptocurrency_prices SET 
            price_date=%s, cryptotype=%s, open_price=%s, 
            highest_price=%s, lowest_price=%s, close_price=%s, 
            adjusted_close_price=%s, volume=%s
            WHERE id=%s
            """, (price_date, cryptotype, open_price, highest_price, lowest_price, close_price, adjusted_close_price, volume, id_data))
            
            mysql.connection.commit()
            flash("Cryptocurrency Prices Data Updated Successfully")
        except Exception as e:
            # Print the error message for debugging
            print("Error:", str(e))
            mysql.connection.rollback()
            flash("An error occurred while updating data. Please try again.", "error")
        finally:
            cur.close()

        return redirect(url_for('prices'))
    
    
@app.route('/bitcoin_info')
def bitcoin_info():
    # Execute a query to retrieve the highest price for Bitcoin
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT MAX(cp.highest_price)
        FROM cryptocurrency_prices cp
        JOIN cryptocurrency_types ct ON cp.cryptotype = ct.id
        WHERE ct.symbol = 'BTC'
    """)
    bitcoin_highest = cur.fetchone()[0]
    cur.close()

    # Pass the highest_price value to the template
    return render_template('index.html', bitcoin_highest=bitcoin_highest)



@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cryptocurrency_prices")
    data = cur.fetchall()

    # Fetch cryptocurrency types for the dropdown
    cur.execute("SELECT * FROM cryptocurrency_types")
    crypto_types = cur.fetchall()
    
    cur.execute("""
    SELECT cp.id, cp.price_date, ct.name, ct.symbol, cp.open_price, cp.highest_price, cp.lowest_price, cp.close_price, cp.adjusted_close_price, cp.volume
    FROM cryptocurrency_prices cp
    JOIN cryptocurrency_types ct ON cp.cryptotype = ct.id
    """)
    alldata = cur.fetchall()
    
    cur.close()

    return render_template('dashboard.html', cryptocurrency_prices=data, cryptocurrency_types=crypto_types, alldata=alldata)



@app.route('/prices', methods=['GET', 'POST'])
def prices():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cryptocurrency_prices")
    data = cur.fetchall()

    # Fetch cryptocurrency types for the dropdown
    cur.execute("SELECT * FROM cryptocurrency_types")
    crypto_types = cur.fetchall()
    
    cur.execute("""
    SELECT cp.id, cp.price_date, ct.name, ct.symbol, cp.open_price, cp.highest_price, cp.lowest_price, cp.close_price, cp.adjusted_close_price, cp.volume
    FROM cryptocurrency_prices cp
    JOIN cryptocurrency_types ct ON cp.cryptotype = ct.id
    """)
    alldata = cur.fetchall()
    
    cur.close()

    return render_template('prices.html', cryptocurrency_prices=data, cryptocurrency_types=crypto_types, alldata=alldata)

@app.route('/types', methods=['GET', 'POST'])
def types():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cryptocurrency_prices")
    data = cur.fetchall()

    # Fetch cryptocurrency types for the dropdown
    cur.execute("SELECT * FROM cryptocurrency_types")
    crypto_types = cur.fetchall()
    
    cur.execute("""
    SELECT cp.id, cp.price_date, ct.name, ct.symbol, cp.open_price, cp.highest_price, cp.lowest_price, cp.close_price, cp.adjusted_close_price, cp.volume
    FROM cryptocurrency_prices cp
    JOIN cryptocurrency_types ct ON cp.cryptotype = ct.id
    """)
    alldata = cur.fetchall()
    
    cur.close()

    return render_template('types.html', cryptocurrency_prices=data, cryptocurrency_types=crypto_types, alldata=alldata)


@app.route('/analytics', methods=['GET', 'POST'])
def analytics():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cryptocurrency_prices")
    data = cur.fetchall()

    # Fetch cryptocurrency types for the dropdown
    cur.execute("SELECT * FROM cryptocurrency_types")
    crypto_types = cur.fetchall()
    
    cur.execute("""
    SELECT cp.id, cp.price_date, ct.name, ct.symbol, cp.open_price, cp.highest_price, cp.lowest_price, cp.close_price, cp.adjusted_close_price, cp.volume
    FROM cryptocurrency_prices cp
    JOIN cryptocurrency_types ct ON cp.cryptotype = ct.id
    """)
    alldata = cur.fetchall()
    
    cur.close()

    return render_template('analytics.html', cryptocurrency_prices=data, cryptocurrency_types=crypto_types, alldata=alldata)
