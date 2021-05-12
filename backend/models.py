from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), default='name', nullable=False)
    price = db.Column(db.Float)
    store = db.Column(db.String(), default='store', nullable=False)
    url = db.Column(db.String(), default='url', nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('items', lazy=True, cascade="all, delete"))

    def __repr__(self):
        return 'Product item: %r from %r' % (self.name, self.store)

    def json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'price': str(self.price),
            'store': self.store
        }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(512), nullable=False)
    img_url = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return 'Product: %r' % self.name

    def json(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'img-url': self.img_url,
            'items': [item.json() for item in self.items]
        }
