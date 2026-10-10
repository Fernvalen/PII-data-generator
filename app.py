from flask import Flask, render_template, request
import generator
import json

app = Flask("Data Generator")

@app.route('/', methods=['GET', 'POST'])
def index():
    data = []
    selected_type = ""
    error = None

    if request.method == 'POST':
        selected_type = request.form.get('data_type')
        count = int(request.form.get('count', 10))

        if selected_type == 'custom_schema':
            raw_schema = request.form.get('schema_json', '{}')
            try:
                schema_dict = json.loads(raw_schema)
                data = generator.generate_from_schema(schema_dict, count)
            except json.JSONDecodeError:
                error = "Invalid JSON format! Please check schema syntax."
        elif selected_type == 'user_profiles':
            data = generator.generate_user_profiles(count)
        elif selected_type == 'financial_transactions':
            data = generator.generate_financial_transactions(count)
        elif selected_type == 'healthcare_records':
            data = generator.generate_healthcare_records(count)

    return render_template('index.html', data=data, selected_type=selected_type, error=error)

if __name__ == '__main__':
    app.run(debug=True)

