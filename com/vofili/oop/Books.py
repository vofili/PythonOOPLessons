class Book():
    #Define a class attribute
    BOOK_TYPES=("HARDCOVER","PAPERBACK","DIGITAL")

    __booklist=None
    def __init__(self, title,pages,price,booktype):
        self.title = title
        self.pages=pages
        self.price=price
        self.__secret="this is a secret"
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid Book Type")
        else:
            self.booktype=booktype

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def get_book_list():
        if Book.__booklist==None:
            Book.__booklist=[]
        return Book.__booklist
    def set_title(self,title):
        self.title= title
    def setDiscount(self, perc):
        self._discount = perc
    def getPrice(self):
        if  hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

class NewsPaper():
    def __init__(self, name):
        self.name = name




# create new books
b1 = Book("Harry Potter and the Chamber of Secrets",1000, 20.00,"DIGITAL")
b2 = Book("Manchurian Candidate",650,15.00,"DIGITAL")
n1 = NewsPaper("Daily Trust")

print("Book Types: ", Book.get_book_types())
print( type(n1) == type (b1))
print( type(b2) ==  type(b2))

print(isinstance(n1,Book))
print(isinstance(b1,Book))

thebooklist =  Book.get_book_list()
thebooklist.append(b1)
thebooklist.append(b2)
print(thebooklist)

# print(b1.price)
# print(b1.title)
# print(b1.pages)
# print(b1.getPrice())
# b1.setDiscount(0.50)
# print(b1.getPrice())

