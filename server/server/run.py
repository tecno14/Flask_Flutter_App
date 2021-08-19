import os 
from app import app , databasePath , db

if not os.path.exists(databasePath):
    db.create_all() 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')