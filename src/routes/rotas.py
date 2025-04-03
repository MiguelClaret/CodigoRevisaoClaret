from flask import request, Blueprint, render_template, jsonify
from models.tabela import Tabela
from models.database import db  

rotas_bp = Blueprint('rotas', __name__)

@rotas_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@rotas_bp.route('/all', methods=['GET'])
def all():
    caminhos = Tabela.query.all()
    return jsonify([caminho.as_dict() for caminho in caminhos])

@rotas_bp.route('/consultar-caminho/<int:caminho_id>', methods=['GET'])
def achar_caminho(caminho_id):
    
    caminho = db.session.query(Tabela).filter(
        Tabela.id == caminho_id
    ).first()

    if not caminho:
        return jsonify({'error': f'Caminho de id {caminho_id} não encontrado'}), 404

    return jsonify(caminho.as_dict())

@rotas_bp.route('/cadastrar-caminho', methods=['POST'])
def cadastrar_caminho():
    data = request.get_json()

    if not data['x'] or not data['y'] or not data['z']:
        return jsonify({'error': 'Preencher todos os campos'}), 404
        
    newCaminho = Tabela(
        x = data['x'],
        y = data['y'],
        z = data['z']
    )

    db.session.add(newCaminho)
    db.session.commit()

    return jsonify({
        'message':'Caminho cadastrado com sucesso'
    }), 200

@rotas_bp.route('/atualizar-caminho', methods=['PUT'])
def atualizar_caminho():

    data = request.get_json()

    if not data['x'] or not data['y'] or not data['z'] or not data['id']:
        return jsonify({"error": "Campos x, y e z são obrigatórios"}), 400
    
    caminho = db.session.query(Tabela).filter(
        Tabela.id == data['id']
    ).first()

    if not caminho:
        return jsonify({'error': f'Caminho de id {data['id']} não encontrado'}), 404

    caminho.x = data['x']
    caminho.y = data['y']
    caminho.z = data['z']

    db.session.commit()

    return jsonify({
        'message': 'Caminho atualizado com sucesso'
    }), 200

# Deletar a prescrição
@rotas_bp.route('/deletar-caminho/<int:caminho_id>', methods=['DELETE'])
def deletar_prescricao(caminho_id):

    caminho = db.session.query(Tabela).filter(
        Tabela.id == caminho_id
    ).first()

    if not caminho:
        return jsonify({'error': f'Caminho de id {caminho_id} não encontrado'}), 404

    db.session.delete(caminho)
    db.session.commit()
    return jsonify({'Message': 'Caminho deletado com sucesso'}), 200
