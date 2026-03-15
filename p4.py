library_books={
    "Python Basics":10,
    "Data Science":5,
    "Machine Learning":7,
    "Deep Learning":3,
    "AI for Beginners" :8
}
print(library_books)
library_books["Computer Vision"]=6
print(library_books)
library_books["Python Basics"]=5
print(library_books)
library_books.pop("Deep Learning")
print(library_books)
print("courses and copies")
print("Books with stock less than 7:")
for books, copies in library_books.items():
    if copies < 7:
        print(books, ":", copies)