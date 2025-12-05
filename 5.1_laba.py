class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания; {self.year}"

books = []

while True:
    print('Приветствуем в электронной библиотеке :)')

    while True:
        title = input('Введите название книги: ')
        if not title.strip():
            print("Ошибка: вы не ввели название ")
        else:
            title = title.strip()
            break

    while True:
        author = input('Введите ФИО автора: ')
        if not author.strip():
            print('Ошибка: вы не ввели ФИО')
        if len(author.strip()) <= 3:
            print('Ошибка: вы ввели не полное ФИО')
        else:
            author = author.strip()
            break

    while True:
        date = input("Введите дату издания книги: ")
        try:
            year = int(date)
            if year < 1600 and (year > 2025):
                print("Нету такого года издания")
            else:
                break
        except ValueError:
            print('Ошибка: год издания должен состоять из цифр')

    book = Book(title, author, year)
    books.append(book)

    print(f'Добавлена книга: {book.get_info()}')
    try:
        continue_choice = input("\nХотите добавить еще книгу? (да/нет): ").lower()
        if continue_choice != 'да':
            print("Программа завершена!")
            break
    except EOFError:
        print("\nПрограмма завершена!")
        break