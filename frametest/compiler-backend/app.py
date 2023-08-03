# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
#from flask_mysqldb import MySQL

#---- Importing CORS (Cross origin Resource sharing)
from flask_cors import CORS 

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '54321'
# app.config['MYSQL_DB'] = 'xobin_db'

CORS(app)



#--- Importing routes------
from routes import appRoutes






#Other logic goes here -------













#Till here -------------




if __name__=="__main__":
    app.run(debug=True) 










