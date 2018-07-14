class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "Your are registered as user: {name}, email: {email}, books read: {books}.".format\
            (name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

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

    def __hash__(self):
        return hash((self.name, self.email))

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
        return "Title: '{title}', ISBN: {isbn}".format\
            (title=self.title, isbn=self.isbn)

    def __eq__(self, other_user):
        if self.title == other_user.title and self.isbn == other_user.isbn:
            return True
        else:
            return False

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
        self.users = {"harmsen@gmail.com": floor}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, books=None):
        self.users[email] = User(name, email)
        if books is not None:
            for book, rating in books.items():
                self.add_book_to_user(book, email, rating)


    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        return(max(self.books, key=self.books.get))

    def highest_rated_book(self):
        average_ratings_books = {}
        for book in self.books:
            average_ratings_books[book] = book.get_average_rating()
        print(max(average_ratings_books, key=average_ratings_books.get))

    def most_positive_user(self):
        pass
        average_ratings_user = {}
        for user in self.users.values():
            average_ratings_user[user] = user.get_average_rating()
        print(max(average_ratings_user, key=average_ratings_user.get))

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
tome_rater_1 = TomeRater()
tome_rater_1.create_book("Just another book", 12345678)
#print(tome_rater_1)
tome_rater_1.add_book_to_user(otje, "harmsen1@gmail.com", 3)
tome_rater_1.add_book_to_user(otje, "harmsen@gmail.com", 3)
tome_rater_1.add_book_to_user(marching_powder, "harmsen@gmail.com", 4)
print(tome_rater_1.books)
tome_rater_1.add_user("Tom", "tom@gmail.com", {google: 3, marching_powder: 4})
tome_rater_1.add_user("Tom", "tom@gmail.com")
tome_rater_1.add_book_to_user(otje, "tom@gmail.com", 4)
print(tome_rater_1.users)

print("=====ANALYSIS METHODS=====")
print(tome_rater_1.print_catalog())
print(tome_rater_1.print_users())
print(tome_rater_1.most_read_book())
print(tome_rater_1.highest_rated_book())
print(tome_rater_1.most_positive_user())


print("=====TESTING=====")
D = {1:'a', 5:'b', 2:'a', 7:'a'}
for key in D.keys():
    print(key)

mydict = {'A':4,'B':10,'C':0,'D':87}
maximum = max(mydict, key=mydict.get)
print(maximum, mydict[maximum])

d= {'a':2,'b':5,'c':3}
print(max(d, key=d.get))