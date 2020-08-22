def cmpfunction (element1, element2):
    if element1 == element2:
        return 0

@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst