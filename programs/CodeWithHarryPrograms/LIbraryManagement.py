
class Library:

    no_of_books = 0
    books = []

    def add_books(self):

        self.no_of_books = int(input('Enter the no. of books : '))

        while True :

            book_name = input(f'Enter the Book Name : ')
            
            self.books.append(book_name)

            more = input('Want to add More Books (Y/N) : ').lower()
            
            if more == 'n' :
                self.check_books()
                break
            
    def check_books(self):

        if self.no_of_books != len(self.books):
            print(f'No. of Books {self.no_of_books} are not equals to books {len(self.books)}')


l1 = Library()


l1.add_books()