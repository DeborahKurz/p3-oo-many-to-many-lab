class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
        #for contract in Contract.all:
        #   if contract.author == name:
        #       return contract
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
        #for contract in contracts(Contract):
        #   if contract.book == self
        #       return contract.book

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        royalties = 0
        for contract in Contract.all:
            if contract.author == self:
                royalties = contract.royalties + royalties
        return royalties
        # royalties = sum(contract.royalties for contract in Contract.all if contract.author ==)
        # return royalties

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be type 'Author'")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book must be type 'book'")
        
    @property
    def date(self):
        return self._date
        
    @date.setter
    def date(self,date):
        if isinstance(date, str):
            self._date = date 
        else:
            raise Exception("Date must be type 'string'")
        

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties must be type 'integer'")

    @classmethod
    def contracts_by_date(cls,date):
        matching_contracts = []
        for contract in cls.all:
            if contract.date == date:
                matching_contracts.append(contract)
        return matching_contracts