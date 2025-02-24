import curses

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr("Enter book title: ")
        title = stdscr.getstr().decode("utf-8")
        stdscr.addstr("Enter book author: ")
        author = stdscr.getstr().decode("utf-8")
        stdscr.addstr("Enter book ISBN: ")
        isbn = stdscr.getstr().decode("utf-8")
        
        self.books.append({"Title": title, "Author": author, "ISBN": isbn})
        stdscr.addstr("\nBook added successfully! Press any key to return.")
        stdscr.getch()

    def search_book(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr("Enter title or author to search: ")
        query = stdscr.getstr().decode("utf-8").lower()
        
        results = [book for book in self.books if query in book["Title"].lower() or query in book["Author"].lower()]
        
        stdscr.clear()
        if results:
            stdscr.addstr("\nSearch Results:\n")
            for book in results:
                stdscr.addstr(f"Title: {book['Title']}, Author: {book['Author']}, ISBN: {book['ISBN']}\n")
        else:
            stdscr.addstr("No matching books found.\n")

        stdscr.addstr("\nPress any key to return.")
        stdscr.getch()

    def main_menu(self, stdscr):
        curses.curs_set(0)  # Hide cursor
        current_option = 0
        options = ["Add Book", "Search Book", "Exit"]

        while True:
            stdscr.clear()
            stdscr.addstr("Library Management System\n", curses.A_BOLD)
            for i, option in enumerate(options):
                if i == current_option:
                    stdscr.addstr(f"> {option}\n", curses.A_REVERSE)  # Highlight selected option
                else:
                    stdscr.addstr(f"  {option}\n")

            key = stdscr.getch()

            if key == curses.KEY_UP and current_option > 0:
                current_option -= 1
            elif key == curses.KEY_DOWN and current_option < len(options) - 1:
                current_option += 1
            elif key == 10:  # Enter key
                if current_option == 0:
                    self.add_book(stdscr)
                elif current_option == 1:
                    self.search_book(stdscr)
                elif current_option == 2:
                    break

if _name_ == "_main_":
    library = Library()
    curses.wrapper(library.main_menu)