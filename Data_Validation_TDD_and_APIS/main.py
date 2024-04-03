from flask import Flask, jsonify, request
from pydantic import BaseModel, validator, ValidationError
app = Flask(__name__)

class Person(BaseModel):
    name: str
    age: int

    @validator('age')
    def validate_age(cls, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120 years old")
        return value
# Criação da rota de cadastro
@app.route('/signup', methods=['POST'])
def signup():
    try:
        user = Person.parse_raw(request.data)

        return jsonify(user.dict())
    
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True)