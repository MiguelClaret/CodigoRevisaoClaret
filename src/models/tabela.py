from .database import db

#Criando a tabela
class Tabela(db.Model):
    __tablename__ = 'tabela' # Define o nome da tabela

    # Definindo as colunas
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    z = db.Column(db.Integer, nullable=False)

    # Função para transformar em json
    def as_dict(self):
        return{
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'z': self.z
            }