class libraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

# createanother class book that inherits from libraryItem
class Book(libraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author, genre)
        self.genre = genre
    def book_details(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"
# create another class magazine that inherits from libraryItem
class Magazine(libraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author, issue_number)
        self.issue_number = issue_number
    def magazine_details(self):
        return f"Title: {self.title}, Author: {self.author}, Issue Number: {self.issue_number}"
# create another class DVD that inherits from libraryitem
class DVD(libraryItem):
    def __init__(self, title, author, duration):
        super().__init__(title, author, duration)
        self.duration = duration
    def dvd_details(self):
        return f"Title: {self.title}, Author: {self.author}, Duration: {self.duration} minutes"
# Book should have an additional attribute (genre)
# magazine has additional attribute (issue_number)
# DVD has additional attribute (duration)
# create a method in each subclass that returns string with the details of the item(e.g for book include genre, for magazine include issue number, for DVD include duration)
# create instances of each subclass and call the method to display their information
book1 = Book("Kidagaa Kimemwozea", "Ken Walibora", "Novel")
magazine1 = Magazine("Shujaaz", "Dj B", 202)
dvd1 = DVD("first blood", "Ted Kotchef", 90)
print(book1.book_details())
print(magazine1.magazine_details())
print(dvd1.dvd_details())