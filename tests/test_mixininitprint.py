def test_product_init_mixininitprint(capsys, product_init):
    captured = capsys.readouterr()
    assert "Product(Samsung Test Ultra,Описание,500.0,5,)" in captured.out


def test_smartphone_init_mixininitprint(capsys, smartphone_init):
    captured = capsys.readouterr()
    assert "Smartphone(Samsung Test Ultra,Описание,500.0,5,Серый)" in captured.out


def test_lawngrass_init_mixininitprint(capsys, lawngrass_init):
    captured = capsys.readouterr()
    assert "LawnGrass(Газонная трава,Элитная трава для газона,500.0,20,Зеленый)" in captured.out
