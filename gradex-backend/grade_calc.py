from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory data storage
courses_data = {
    "CSC209": [
        {"A1": (40, 100)},
        {"A2": (20, 80)}
    ]
}

@app.route('/')
def courses():
    """
    Returns the dictionary of course data.
    ok
    """
    return render_template("courses.html", courses_data=courses_data)

@app.route('/course', methods=['POST'])
def add_course():
    data = request.get_json()
    course_name = data.get('course_name')
    if course_name not in courses_data:
        courses_data[course_name] = []
    return jsonify({'message': 'Course added successfully'})


# Function to add assignments to JSON file
def add_assignments():
    """
    Add new assignments to the JSON file.

    Args:
    assignments_data (dict): Dictionary containing assignments data.

    Returns:
    str: Message indicating success or failure.
    """
    return None


if __name__ == "__main__":
    app.run(debug=True, port=4999)
