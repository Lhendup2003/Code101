books_list =[]
authors_set = set()
books_dict = {}

books_list.append("python programming")
authors_set.add("john smith")
books_dict["python programming"] = "john smith"
books_list.append("data structure and algorithms")
authors_set.add("jane doe")
books_dict["data structure and algorithms"] = "jane doe"
books_list.append("machine learning basics")
authors_set.add("alice johnson")
books_dict["machine learning basics"] = "alice johnson"

search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found!")

print("List of books:")
for book in books_list:
    print(book)

remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successfully!")
else:
    print("Book not found.")
