from flask import Blueprint, request
from .models import Product, Product_item, db

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api_v1')


@api_v1.route('/products', methods=['GET', 'POST'])
def products():
    response = {'message': 'Incorect request method!', 'code': 500}
    if request.method == 'GET':
        products = Product.query.all()
        if products:
            response = {
                'products': [product.json() for product in products],
                'code': 200
            }
        else:
            response = {'message': 'No products', 'code': 400}

    elif request.method == 'POST':
        name = request.json['name']
        description = request.json['description']
        img_url = request.json['img_url']

        product = Product(name=name, description=description, img_url=img_url)

        db.session.add(product)
        db.session.commit()

        response = {
            'message': 'Product with name %r added!' % name,
            'code': 200
        }
    return response


@api_v1.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def product(id):
    try:
        product = Product.query.get(id)
        if request.method == 'GET':
            response = {'product': product.json(), 'code': 200}

        elif request.method == 'PUT':
            product.name = request.json['name']
            product.description = request.json['description']
            product.img_url = request.json['img_url']
            # update db
            db.session.commit()
            # create responce
            response = {
                'message': 'Product %r with name %r have updated!' % (product.id, product.name), 
                'code': 200
            }
        elif request.method == 'DELETE':
            name = product.name
            # update db
            db.session.delete(product)
            db.session.commit()
            # create responce
            response = {
                'message': 'Product with name %r have deleted!' % name, 
                'code': 200
            }
    except:
        response = {'message': 'Incorect request!', 'code': 500}
    return response


@api_v1.route('/products/<int:product_id>/items', methods=['GET', 'POST'])
def product_items(product_id):
    product = Product.query.get(product_id)
    response = {'message': 'Incorect request method!', 'code': 500}
    if request.method == 'GET':
        items = product.items
        if items:
            response = {'items': [item.json() for item in items], 'code': 200}
        else:
            response = {'message': 'No items', 'code': 400}

    elif request.method == 'POST':
        name = request.json['name']
        price = float(request.json['price'])
        store = request.json['store']

        item = Product_item(name=name, price=price, store=store)
        product.items.append(item)

        db.session.commit()

        response = {'message': 'Item with name %r added!' % name, 'code': 200}
    return response


@api_v1.route('/products/<int:product_id>/items/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def product_item(product_id, id):
    try:
        product = Product.query.get(product_id)
        item = Product_item.query.with_parent(product).filter(Product_item.id == id).first()
        if request.method == 'GET':
            response = {'item': item.json(), 'code': 200}

        elif request.method == 'PUT':
            item.name = request.json['name']
            item.price = request.json['price']
            item.store = request.json['store']

            db.session.commit()
            
            response = {'message': 'Product %r with name %r have updated!' % (item.id, item.name), 'code': 200}
        
        elif request.method == 'DELETE':
            name = item.name
            db.session.delete(item)
            db.session.commit()

            response = {'message': 'Product with name %r have deleted!' % name, 'code': 200}

    except:
        response = {'message': 'Incorect request!', 'code': 500}
     
    return response



