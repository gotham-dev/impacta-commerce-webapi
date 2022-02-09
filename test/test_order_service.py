from api.service import order_service

def test_sum_total():
    # Given
    products = """
    [
        {
            "code": "1",
            "title": "Caneca Personalizada de Porcelana",
            "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-pers-porc.jpg",
            "qty": 1,
            "unitPrice": 123.45
        },
        {
            "code": "2",
            "title": "Caneca Importada Personalizada em Diversas Cores",
            "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-import-colors.jpg",
            "qty": 2,
            "unitPrice": 123.45
        },
        {
            "code": "3",
            "title": "Caneca de Tulipa",
            "tumbnailUrl": "http://meu-ecommerce.com/img/pr/tb-tuli.jpg",
            "qty": 1,
            "unitPrice": 123.45
        }
    ]
    """
    expected = 493.8
    # When
    actual = order_service.sum_total(products)

    # Then
    assert expected == actual