from api.model.product_model import Product

def get_by_query(query):
    if query is None:
        return Product.query.all()
    else:
        return Product.query.filter(
            Product.title.like(f'%{query}%')
        ).all()