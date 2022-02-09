from api.model import db
from flask import json


class Order(db.Model):
    """Cria a entidade de Order"""
    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.Text, unique=False, nullable=True)
    total_amount = db.Column(db.Numeric, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    updated_at = db.Column(db.DateTime, unique=False, nullable=False)
    status = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.id

    @property
    def serialized(self):
        return {
            'id': self.id,
            'totalAmount':  round(self.total_amount, 2),
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat(),
            'status': self.status.upper(),
            'products': json.loads(self.products),
        }
