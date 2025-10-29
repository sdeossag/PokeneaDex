from flask import Blueprint, jsonify, render_template
import socket
from .pokeneas import get_random_pokenea

bp = Blueprint("main", __name__)

@bp.route("/api/pokenea")
def get_pokenea_json():
    pokenea = get_random_pokenea()
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": socket.gethostname()
    }
    return jsonify(response)

@bp.route("/pokenea")
def show_pokenea():
    pokenea = get_random_pokenea()
    container_id = socket.gethostname()
    return render_template("pokenea.html", pokenea=pokenea, container_id=container_id)
