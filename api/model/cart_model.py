from api.model import db
from flask import json


class Cart(db.Model):
    """Cria a entidade de Cart"""
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    updated_at = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return '<Cart %r>' % self.title

    @property
    def serialized(self):
        return {
            'id': self.id,
            'code':  self.code,
            'createdAt': self.created_at.isoformat(),
            'updatedAt': self.updated_at.isoformat(),
            'products': json.loads(self.content),
        }
