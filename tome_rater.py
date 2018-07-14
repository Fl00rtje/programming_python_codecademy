class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "Your are registered as user: {name}, email: {email}, books read: {books}.".format\
            (name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        pass
        # Still have to code this one.

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Your email has been updated to: {email}".format(email=self.email))

    def read_book(self, book, rating=None):
        self.rating = rating
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        number_values = 0
        for key, value in self.books.items():
            number_values += 1
            sum += value
            average = sum / number_values
        return average

    #def get_books(self):
    #    for key, value in self.books.items():
    #        print key
    #        print value

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "Title: {title}, ISBN: {isbn}".format\
            (title=self.title, isbn=self.isbn)

    def __eq__(self, other_user):
        pass
        #Still have to code this one.

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Your ISBN has been updated to: {isbn}".format(isbn=self.isbn))

    def add_rating(self, rating):
        if rating in range(5):
            self.ratings.append(rating)
        else:
            print("This is an invalid rating.")

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    #def get_ratings(self):
    #    return self.ratings

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

    def get_author(self):
        return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format\
            (title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

print("=====ADD USERS=====")
floor = User("Floor Harmsen", "floor.harmsen@gmail.com")
print(floor)
floor.change_email("harmsen@gmail.com")
print(floor)

print("=====ADD BOOKS AND RATINGS FOR BOOKS=====")
otje = Book("Otje", 1234567890)
google = Book("What would Google do?", 987654231)
marching_powder = Book("Marching Powder", 567891234)
print(otje)
print(google)
#otje.set_isbn(1357902468)
#print(otje)
otje.add_rating(4)
otje.add_rating(3.0)
otje.add_rating(1)
#print(otje.get_ratings())
#print(otje)
google.add_rating(3)

print("=====ADD FICTION BOOKS=====")
murder_on_5th_avenue = Fiction("Murder on 5th Avenue", "Aghata Christie", 987654321)
print(murder_on_5th_avenue)

print("=====ADD NON-FICTION BOOKS=====")
microeconomic_theory = Non_Fiction("Microeconomic Theory", "Economics", "beginner", "12345")
print(microeconomic_theory)

print("=====USER METHODS=====")
floor.read_book(otje, 4)
floor.read_book(google, 4.0)
floor.read_book(marching_powder, 2)
#print(floor.get_books())
print(floor.get_average_rating())

print("=====BOOK METHODS=====")
print(otje.get_average_rating())

print("=====TOMERATOR=====")
book1 = TomeRater()
book1.create_book("Just another book", 12345678)
print(book1)