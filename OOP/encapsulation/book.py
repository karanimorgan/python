class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self._price = price
        self.__discount = 0.1

    def get_book_info(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Price:{self._price}"
    
    def apply_discount(self):
        discounted_price = self._price * (1 - self.__discount)
        return discounted_price
    
    def set_discount(self, discount):
        if 0 <= discount <= 1:
            self.__discount = discount
        else:
            print("Discount must be between 0 and 1.")
    
    def get_discount(self):
        return self.__discount

book = Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 1200)
print(book.get_book_info())
print(f"Price after discount: KSH{book.apply_discount():.2f}")
# print(book.__discount) **Atribute error
print(book.get_discount())
book.set_discount(0.4)
print(f"Price after new discount: ksh {book.apply_discount():.2f}")