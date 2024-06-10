class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        # Filter contracts by date
        filtered_contracts = [contract for contract in cls.all_contracts if contract.date == date]
        # Sort filtered contracts by date
        sorted_contracts = sorted(filtered_contracts, key=lambda contract: contract.date)
        return sorted_contracts

# Example Usage:
if __name__ == "__main__":
    # Creating authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Creating books
    book1 = Book("Book 1")
    book2 = Book("Book 2")

    # Signing contracts
    author1.sign_contract(book1, "2024-06-10", 10)
    author2.sign_contract(book1, "2024-06-11", 15)
    author2.sign_contract(book2, "2024-06-12", 20)

    # Retrieving contracts by date
    contracts_on_date = Contract.contracts_by_date("2024-06-10")
    for contract in contracts_on_date:
        print(f"Author: {contract.author.name}, Book: {contract.book.title}, Royalties: {contract.royalties}")

    # Total royalties for authors
    print(f"Total royalties for {author1.name}: {author1.total_royalties()}")
    print(f"Total royalties for {author2.name}: {author2.total_royalties()}")
