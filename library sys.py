class Book:
    def __init__(self,title,author,year):

        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def show_info(self):
        if self. available == True:
            print(f'Available! The Book Is {self.title} The Author Is {self.author}')
        else :
            print("Not Found")

    def borrow(self):
        if self.available == True:
            
            self.available = False
            print(f"You Have Borrowed {self.title}")
        else:
            print("not available")

    def return_book(self):

        self.available = True
        print(f'{self.title} is now available')


class Fiction(Book):

    def __init__(self,title,author,year,gener):
        super().__init__(title,author,year)
        self.gener = gener

    def show_info(self):
        print(f'The Book Gener Is {self.gener}')
        
        
        
class Science(Book):
    def __init__(self,title,author,year,field):
        super().__init__(title,author,year)
        self.field = field

    def show_info(self):
        print(f'The Book Gener Is {self.field}')

f1 = Fiction("python for kids",'Fatma',2024,'Programming')
f1.show_info()
s1 = Fiction("python for kids",'Fatma',2024,'math')
s1.show_info()
        



              
            
