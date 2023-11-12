# A1G
from flask import Flask

app = Flask(__name__)


# Reine Funktion (Pure Function)
def square_number(x):
    return x ** 2


# Prozedur (Procedure) mit Seiteneffekt
def change_global_variable(value):
    global global_variable
    global_variable += value


# Globale Variable für die Prozedur
global_variable = 10


# Flask Route für die reine Funktion
@app.route('/square/<int:number>')
def square_route(number):
    result = square_number(number)
    return f"Square Result: {result}"


# Flask Route für die Prozedur
@app.route('/change_variable/<int:value>')
def change_variable_route(value):
    change_global_variable(value)
    return f"Global Variable After Change: {global_variable}"


if __name__ == '__main__':
    app.run(debug=True)

# A1F
from flask import Flask

app = Flask(__name__)


# Beispiel für immutable values (unveränderlich)
def square_number(x):
    result = x ** 2
    return f"The square of {x} is {result}"


# Beispiel für mutable values (veränderlich)
def append_to_list(my_list, element):
    my_list.append(element)
    return f"The list after appending {element}: {my_list}"


# Flask Route für immutable values
@app.route('/square/<int:number>')
def square_route(number):
    result = square_number(number)
    return result


# Flask Route für mutable values
@app.route('/append/<element>')
def append_route(element):
    my_list = [1, 2, 3]
    result = append_to_list(my_list, element)
    return result


if __name__ == '__main__':
    app.run(debug=True)

# A1E
from flask import Flask, render_template_string

app = Flask(__name__)


# Objektorientierte Klasse
class Greeting:
    def __init__(self, message):
        self.message = message


# Prozedurale Funktion
def generate_procedural_greeting(name):
    return f"Hello, {name}! This is a procedural greeting."


# Funktionale Funktion
def generate_functional_greeting(name):
    return f"Hi, {name}! This is a functional greeting."


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Objektorientierte Instanz
    oo_greeting = Greeting("Welcome to the Flask App!")

    # Prozedurale Grußnachricht
    procedural_greeting = generate_procedural_greeting("User")

    # Funktionale Grußnachricht
    functional_greeting = generate_functional_greeting("User")

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App</title>
    </head>
    <body>
        <h1>{{ oo_greeting }}</h1>
        <p>{{ procedural_greeting }}</p>
        <p>{{ functional_greeting }}</p>
    </body>
    </html>
    """

    # Flask-Template verwenden, um die Ergebnisse anzuzeigen
    return render_template_string(html_template,
                                  oo_greeting=oo_greeting.message,
                                  procedural_greeting=procedural_greeting,
                                  functional_greeting=functional_greeting)


if __name__ == '__main__':
    app.run(debug=True)

# B1G
from flask import Flask

app = Flask(__name__)


# Algorithmus zur Berechnung der Fakultät
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


# Flask Route für die Fakultätsberechnung
@app.route('/factorial/<int:number>')
def factorial_route(number):
    result = calculate_factorial(number)
    return f"The factorial of {number} is {result}"


if __name__ == '__main__':
    app.run(debug=True)

# B1F
from flask import Flask

app = Flask(__name__)


# Funktionaler Teil: Begrüßung erstellen
def generate_greeting(name):
    return f"Hello, {name}! Welcome to the Flask App."


# Funktionaler Teil: Generiere eine personalisierte Nachricht
def generate_personalized_message(name):
    return f"Hi, {name}! This is a personalized message."


# Funktionaler Teil: Führe eine einfache Berechnung durch
def perform_calculation(num1, num2):
    result = num1 + num2
    return f"The result of the calculation is: {result}"


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Funktionaler Teil: Generiere Begrüßung
    greeting = generate_greeting("User")

    # Funktionaler Teil: Generiere personalisierte Nachricht
    personalized_message = generate_personalized_message("User")

    # Funktionaler Teil: Führe Berechnung durch
    calculation_result = perform_calculation(5, 3)

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App - Functional Example</title>
    </head>
    <body>
        <h1>{greeting}</h1>
        <p>{personalized_message}</p>
        <p>{calculation_result}</p>
    </body>
    </html>
    """

    return html_content


if __name__ == '__main__':
    app.run(debug=True)

# B1E
from flask import Flask

app = Flask(__name__)


# Funktion zur Überprüfung, ob eine Zahl eine Primzahl ist
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Flask Route für die Primzahlüberprüfung
@app.route('/is_prime/<int:number>')
def is_prime_route(number):
    result = is_prime(number)
    return f"Is {number} a prime number? {'Yes' if result else 'No'}"


if __name__ == '__main__':
    app.run(debug=True)

# B2G
from flask import Flask

app = Flask(__name__)


# Funktion, die eine personalisierte Begrüßung generiert
def generate_greeting(name):
    return f"Hello, {name}!"


# Funktion, die eine allgemeine Nachricht erstellt
def generate_message(name, message_func):
    return message_func(name)


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Funktion als Objekt behandeln und in Variable speichern
    greeting_function = generate_greeting

    # Funktion als Argument an eine andere Funktion weitergeben
    personalized_message = generate_message("User", greeting_function)

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App - Function as Object Example</title>
    </head>
    <body>
        <p>{personalized_message}</p>
    </body>
    </html>
    """

    return html_content


if __name__ == '__main__':
    app.run(debug=True)

# B2F
from flask import Flask

app = Flask(__name__)


# Funktion zur Addition
def add(x, y):
    return x + y


# Funktion zur Multiplikation
def multiply(x, y):
    return x * y


# Funktion zur Berechnung und Anzeige des Ergebnisses
def calculate_and_display(operation, x, y):
    result = operation(x, y)
    return f"The result of the operation is: {result}"


# Flask Route für die Addition
@app.route('/add/<int:num1>/<int:num2>')
def add_route(num1, num2):
    return calculate_and_display(add, num1, num2)


# Flask Route für die Multiplikation
@app.route('/multiply/<int:num1>/<int:num2>')
def multiply_route(num1, num2):
    return calculate_and_display(multiply, num1, num2)


if __name__ == '__main__':
    app.run(debug=True)

# B2E
from flask import Flask

app = Flask(__name__)


# Funktion, die eine andere Funktion als Objekt zurückgibt (Closure)
def create_closure_function(base_message):
    def inner_function(name):
        return f"{base_message}, {name}!"

    return inner_function


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Funktion als Objekt behandeln und in Variable speichern
    greeting_closure = create_closure_function("Hello")

    # Closure-Funktion aufrufen und das Ergebnis erhalten
    personalized_greeting = greeting_closure("User")

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App - Closures Example</title>
    </head>
    <body>
        <p>{personalized_greeting}</p>
    </body>
    </html>
    """

    return html_content


if __name__ == '__main__':
    app.run(debug=True)

# B3G
from flask import Flask

app = Flask(__name__)

# Lambda-Ausdruck für Quadratberechnung
square = lambda x: x ** 2

# Lambda-Ausdruck für Konvertierung in Großbuchstaben
uppercase = lambda s: s.upper()


# Flask Route für die Quadratberechnung
@app.route('/square/<int:number>')
def square_route(number):
    result = square(number)
    return f"The square of {number} is {result}"


# Flask Route für die Konvertierung in Großbuchstaben
@app.route('/uppercase/<string:text>')
def uppercase_route(text):
    result = uppercase(text)
    return f"Uppercase of '{text}': {result}"


if __name__ == '__main__':
    app.run(debug=True)

# B3F
from flask import Flask

app = Flask(__name__)

# Lambda-Ausdruck, der mehrere Argumente verarbeitet
multiply = lambda x, y: x * y


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Verwendung des Lambda-Ausdrucks mit mehreren Argumenten
    result = multiply(5, 3)

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App - Lambda Example</title>
    </head>
    <body>
        <p>The result of the multiplication is: {result}</p>
    </body>
    </html>
    """

    return html_content


if __name__ == '__main__':
    app.run(debug=True)

# B3E
from flask import Flask, jsonify

app = Flask(__name__)

# Liste von Benutzern (jeder Benutzer ist ein Dictionary)
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Lambda-Ausdruck für die Sortierung nach Alter
sort_by_age = lambda user: user['age']


# Flask Route für die Sortierung nach Alter
@app.route('/sort_by_age')
def sort_by_age_route():
    sorted_users = sorted(users, key=sort_by_age)
    return jsonify(sorted_users)


if __name__ == '__main__':
    app.run(debug=True)

# B4G
from flask import Flask

app = Flask(__name__)

# Liste von Zahlen
numbers = [1, 2, 3, 4, 5]


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Funktion map: Quadriere jede Zahl in der Liste
    squared_numbers = list(map(lambda x: x ** 2, numbers))

    # Funktion filter: Filtere ungerade Zahlen aus der Liste
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    # Funktion reduce: Multipliziere alle Zahlen in der Liste
    product_of_numbers = __import__('functools').reduce(lambda x, y: x * y, numbers)

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App - Map, Filter, Reduce Example</title>
    </head>
    <body>
        <p>Original Numbers: {numbers}</p>
        <p>Squared Numbers: {squared_numbers}</p>
        <p>Even Numbers: {even_numbers}</p>
        <p>Product of Numbers: {product_of_numbers}</p>
    </body>
    </html>
    """

    return html_content


if __name__ == '__main__':
    app.run(debug=True)

# B4F
from flask import Flask, jsonify

from functools import reduce

app = Flask(__name__)

# Liste von Zahlen
numbers = [1, 2, 3, 4, 5]

# Funktionen für Map, Filter und Reduce
square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0
sum_squares = lambda x, y: x + y


# Flask Route für die kombinierte Verwendung
@app.route('/process_numbers')
def process_numbers():
    # Map: Quadrat jeder Zahl
    squared_numbers = list(map(square, numbers))

    # Filter: Nur gerade Zahlen behalten
    even_numbers = list(filter(is_even, squared_numbers))

    # Reduce: Summe der Quadratzahlen
    result = reduce(sum_squares, even_numbers)

    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)

# B4F Refactoring
from flask import Flask

app = Flask(__name__)

# Liste von Benutzerobjekten
users = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 22, 'city': 'Chicago'},
]


# Flask-Route für die Startseite
@app.route('/')
def home():
    # Funktion map: Extrahiere die Namen der Benutzer
    user_names = list(map(lambda user: user['name'], users))

    # Funktion filter: Filtere Benutzer über 25 Jahre
    adult_users = list(filter(lambda user: user['age'] > 25, users))

    # Funktion reduce: Aggregiere das Durchschnittsalter der Benutzer
    total_age = sum(map(lambda user: user['age'], users))
    average_age = total_age / len(users)

    # HTML direkt in Python-Code (anstatt eines externen Templates)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App - Data Processing Example</title>
    </head>
    <body>
        <p>User Names: {user_names}</p>
        <p>Adult Users: {adult_users}</p>
        <p>Average Age: {average_age}</p>
    </body>
    </html>
    """

    return html_content


if __name__ == '__main__':
    app.run(debug=True)

# B4E
from flask import Flask

app = Flask(__name__)

# Liste von Büchern (jedes Buch ist ein Dictionary)
books = [
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': '1984', 'author': 'George Orwell'}
]


# Flask-Route für die Anzeige der Bücher
@app.route('/books')
def display_books():
    return render_template('books.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)

# C1G
from flask import Flask, render_template

app = Flask(__name__)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Liste von Büchern (jedes Buch ist ein Objekt der Klasse Book)
books = [
    Book('The Catcher in the Rye', 'J.D. Salinger'),
    Book('To Kill a Mockingbird', 'Harper Lee'),
    Book('1984', 'George Orwell')
]


# Flask-Route für die Anzeige der Bücher
@app.route('/books')
def display_books():
    return render_template('books.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)

# C1F
from flask import Flask

app = Flask(__name__)

# Liste von Benutzerobjekten
users = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 22, 'city': 'Chicago'},
]


# Flask-Route für die Startseite
@app.route('/')
def home():
    user_names = extract_user_names(users)
    adult_users = filter_adult_users(users)
    average_age = calculate_average_age(users)

    return f"User Names: {user_names}<br>Adult Users: {adult_users}<br>Average Age: {average_age}"


def extract_user_names(users):
    return list(map(lambda user: user['name'], users))


def filter_adult_users(users):
    return list(filter(lambda user: user['age'] > 25, users))


def calculate_average_age(users):
    total_age = sum(map(lambda user: user['age'], users))
    return total_age / len(users)


if __name__ == '__main__':
    app.run(debug=True)

# C1E
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Datenmodell als Dictionary
books_dict = [
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': '1984', 'author': 'George Orwell'}
]


# Flask-Route für die Anzeige der Bücher als JSON
@app.route('/books_dict')
def display_books_dict():
    return jsonify({'books': books_dict})


# Refactoring: Datenmodell zu SQLite-Datenbankverbindung
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')

# Fülle die Datenbank mit Beispielbüchern
conn.executemany('INSERT INTO books (title, author) VALUES (?, ?)', [('The Catcher in the Rye', 'J.D. Salinger'),
                                                                     ('To Kill a Mockingbird', 'Harper Lee'),
                                                                     ('1984', 'George Orwell')])


# Flask-Route für die Anzeige der Bücher aus der Datenbank als JSON
@app.route('/books_db')
def display_books_db():
    cursor = conn.execute('SELECT title, author FROM books')
    books_db = [{'title': title, 'author': author} for title, author in cursor.fetchall()]
    return jsonify({'books': books_db})


if __name__ == '__main__':
    app.run(debug=True)
