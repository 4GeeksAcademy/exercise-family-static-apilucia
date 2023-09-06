"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



#trae todos los miembros
@app.route('/members', methods=['GET'])
def handle_hello():

    members = jackson_family.get_all_members()#trae el class y dentro de ahi la funcion all members que es la que los lista a todos
    if members == [] :
        return 404
    return jsonify(members), 200#retorno los miembros  convertido en formato json


#agregar un miembro
@app.route('/member', methods=['POST'])
def add_member():
    new_member = json.loads(request.data)#request.data accede a los datos enviados en el cuerpo de la solicitud 
                #estás tomando la cadena JSON que se encuentra en el cuerpo de la solicitud   y la estás convirtiendo en un objeto Python 
    jackson_family.add_member(new_member) #la class jackson_family dentro de ella la funcion add member y le doy el nuevo miebro que quiero agregar que fue convertido a objeto python
    if new_member == []:
        return 400


    return jsonify(new_member), 200

#borrar un miembro
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):#se nesesita el parametro que seria el de la ruta int

    jackson_family.delete_member(member_id)#accedo a la funcion delete que esta en class jackson_family y le agrego el member_id que quiero eliminar
    
    # if {"done" : False} : esta mal hacerlo asi???
    #     return 400


    return jsonify({"done" : True}), 200 #?????

#traer un miembro
@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_member(member_id):
    member = jackson_family.get_member(member_id)
    if member == []:
        return 400
    return jsonify(member), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
