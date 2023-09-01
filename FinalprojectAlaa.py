class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level
        self.is_available = True


class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # TODO : implement Library methods
    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        for book in self.books:
            print(
                f"ID\t | {book.book_id} \t | Title\t | {book.title}\t | Author\t | {book.author}"
                f"\t | Level\t | {book.level}\t | Availability\t | "
                f"{'Available' if book.is_available else 'Not Available'}")



    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def display_members(self):
        print("ID\t\t | Name\t\t\t | Email\t\t | Level\t\t\t ")
        print("=" * 80)
        for member in self.members:
            print(f"{member.member_id}\t\t | {member.name}\t\t | {member.email}\t\t | {member.level}")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


library = Library()
welcome = "Welcome to the Library System"
print(welcome.center(100, "-"))
choices = ''' 
1.Add Member  
2.Edit Member  
3.Show members  
4.Delete Member 
5.Add Book 
6.Show Books 
7.Borrow Book 
8.Return Book 
9.Exit 
'''

while True:
    print(choices)
    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        name = input('Enter member name:')
        email = input("Enter member email:")
        level = input("Enter member level(A/B/C):")
        if level.lower() or level.upper():
            print("Member details Updated successfully.")
        else:
            input(f"Invalid input! Please enter the Member Level again (A/B/C): ")
        new_member = Member(name, email, level)
        library.add_member(new_member)
    elif choice == 2:
        member_id = int(input("Enter member ID:"))
        new_name = input("Enter new name:")
        new_email = input("Enter new email")
        new_level = input("Enter member level(A/B/C):")
        if level.lower() or level.upper():
            print("Member details Updated successfully.")
        else:
            input(f"Invalid input! Please enter the Member Level again (A/B/C): ")
        Member.name = new_name
        Member.email = new_email
        Member.level = new_level
    elif choice == 3:
        library.display_members()
    elif choice == 4:
        member_id_to_delete = int(input("*Enter Member ID to delete : "))
        member_to_delete = None

        for member in library.members:
            if member.member_id == member_id_to_delete:
                member_to_delete = member
                break

        if member_to_delete:
            library.members.remove(member_to_delete)
            print(" Member deleted successfully.")
        else:
            print(" MemberID Not Found!!")

    elif choice == 5:
        title = input("Enter book title:")
        author = input("Enter author:")
        level = input("Enter member level(A/B/C):")
        if level.lower() or level.upper():
            print("book details Updated successfully.")
        else:
            input(f"Invalid input! Please enter the book Level again (A/B/C): ")
        new_book = Book(title, author, level)
        library.add_book(new_book)
    elif choice == 6:
        library.display_books()
    elif choice == 7:
        member_id = int(input("*Enter Member ID : "))
        book_id = int(input("*Enter Book ID : "))
        member = library.find_member(member_id)
        book = library.find_book(book_id)
        if member and book:
            if book.is_available and member.level.upper() == book.level.upper():
                book.is_available = False
                member.borrowed_books.append(book)
                print(f"{member.name} has borrowed the book : {book.title} ")
            elif not book.available:
                print("Book is not available for borrowing.")
            else:
                print("Member level is not suitable for borrowing this  book  !!")
        else:
            print("Member or Book not Found !!")

    elif choice == 8:
        member_id = int(input("*Enter Member ID : "))
        book_id = int(input("*Enter Book ID : "))
        member = library.find_member(member_id)
        book = library.find_book(book_id)
        if member and book:
            for borrowed_book in member.borrowed_books:
                if borrowed_book == book:
                    book.is_available = True
                    member.borrowed_books.remove(book)
                    print(f"#{member.name} has returned the book : {book.title} ")
                else:
                    print("Sorry !! , Not found :(")
        else:
            print("Member or Book not Found !!")
    elif choice == 9:
        print("Thank you for visiting !")
        break
    else:
       print("Invalid choice. Please select a valid option.")

# TODO : implement the menu