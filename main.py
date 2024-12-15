from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for tours
tours = [
    {"id": 1, "name": "Тур по Карпатах", "description": "Чудова подорож в гори з відвідуванням озера Синевир.", "price": 3000},
    {"id": 2, "name": "Тур до Львова", "description": "Оглядова екскурсія по місту Лева.", "price": 2000}
]

@app.route('/')
def home():
    return render_template('home.html', tours=tours)

@app.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    if request.method == 'POST':
        # Collect form data
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        # Add the new tour to the list
        new_tour = {
            "id": len(tours) + 1,
            "name": name,
            "description": description,
            "price": int(price)
        }
        tours.append(new_tour)

        return redirect(url_for('home'))

    return render_template('add_tour.html')

if __name__ == '__main__':
    app.run(debug=True)