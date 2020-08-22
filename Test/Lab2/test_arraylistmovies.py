@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def books ():
    books = []
    books.append({'book_id':'1', 'book_title':'Title 1', 'author':'author 1'})
    books.append({'book_id':'2', 'book_title':'Title 2', 'author':'author 2'})
    books.append({'book_id':'3', 'book_title':'Title 3', 'author':'author 3'})
    books.append({'book_id':'4', 'book_title':'Title 4', 'author':'author 4'})
    books.append({'book_id':'5', 'book_title':'Title 5', 'author':'author 5'})
    print (books[0])
    return books