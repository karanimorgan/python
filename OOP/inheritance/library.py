class libraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

# createanother class book that inherits from libraryItem
# create another class magazine that inherits from libraryItem
# create another class DVD that inherits from libraryitem
# Book should have an additional attribute (genre)
# magazine has additional attribute (issue_number)
# DVD has additional attribute (duration)
# create a method in each subclass that returns string with the details of the item(e.g for book include genre, for magazine include issue number, for DVD include duration)
# create instances of each subclass and call the method to display their information