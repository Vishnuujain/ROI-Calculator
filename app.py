from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    average_revenue = float(data.get('averageRevenue', 0))
    cv_screening = int(data.get('cvScreening', 0))
    telephonic_screening = int(data.get('telephonicScreening', 0))
    
    # Simple calculation (you can expand this later)
    efficiency_increase = (cv_screening + telephonic_screening) / 100
    additional_revenue = average_revenue * efficiency_increase
    
    return jsonify({
        'efficiencyIncrease': f"{efficiency_increase:.2%}",
        'additionalRevenue': f"₹{additional_revenue:.2f}"
    })

if __name__ == '__main__':
    app.run(debug=True)
