from book_class import Book
from library_system import EBook, PrintBook, Library
from polymorphism_demo import Rectangle, Circle
from class_static_methods_demo import Calculator  # NEW import


def test_book_class():
    print("=== Testing book_class.Book ===")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book


def test_library_system():
    print("\n=== Testing library_system ===")
    my_library = Library()
    classic_ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    my_library.add_book(classic_ebook)
    my_library.add_book(paper_book)
    my_library.list_books()


def test_polymorphism():
    print("\n=== Testing polymorphism_demo ===")
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


def test_calculator():
    print("\n=== Testing class_static_methods_demo ===")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    test_book_class()
    test_library_system()
    test_polymorphism()
    test_calculator()
