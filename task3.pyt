import tkinter as tk
from tkinter import messagebox

# List to store books
books = []

# Function to add a book
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    
    if title and author and isbn:
        book = {
            "title": title,
            "author": author,
            "isbn": isbn
        }
        books.append(book)
        messagebox.showinfo("Success", f"Book '{title}' by {author} added successfully!")
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        isbn_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Function to search for a book
def search_book():
    search_term = search_entry.get().lower()
    found_books = []
    
    for book in books:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            found_books.append(book)
    
    if found_books:
        result_text = "Search Results:\n\n"
        for book in found_books:
            result_text += f"Title: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\n\n"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No books found matching your search.")

# Create the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x300")

# Add Book Section
add_frame = tk.LabelFrame(root, text="Add a Book", padx=10, pady=10)
add_frame.pack(pady=10)

tk.Label(add_frame, text="Title:").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(add_frame, width=30)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(add_frame, text="Author:").grid(row=1, column=0, sticky="w")
author_entry = tk.Entry(add_frame, width=30)
author_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(add_frame, text="ISBN:").grid(row=2, column=0, sticky="w")
isbn_entry = tk.Entry(add_frame, width=30)
isbn_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(add_frame, text="Add Book", command=add_book)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Search Book Section
search_frame = tk.LabelFrame(root, text="Search for a Book", padx=10, pady=10)
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search by Title/Author:").grid(row=0, column=0, sticky="w")
search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(search_frame, text="Search", command=search_book)
search_button.grid(row=1, column=0, columnspan=2, pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Run the application
root.mainloop()