from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    items = request.form.getlist("food")
    co2_values = request.form.getlist("co2")
    water_values = request.form.getlist("water")

    report = []
    total_co2, total_water = 0, 0

    for i in range(len(items)):
        food = items[i].strip()
        if food and co2_values[i] and water_values[i]:
            co2 = float(co2_values[i])
            water = float(water_values[i])
            report.append({"item": food, "co2": co2, "water": water})
            total_co2 += co2
            total_water += water

    return render_template("result.html",
                           report=report,
                           total_co2=total_co2,
                           total_water=total_water)

if __name__ == "__main__":
    app.run(debug=True)
