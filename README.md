# Library Manager CLI

Library Manager CLI is a Python command-line application that allows users to manage their personal book collections efficiently. It provides features such as adding, listing, editing, and deleting book entries, along with the capability to save and load the library from a file.

## Features

- **Add Book**: Users can add a book with details like title, author, publication year, and genre.
- **List Books**: Display all books in the library or filter them by author or genre.
- **Edit Book**: Modify the details of an existing book.
- **Delete Book**: Remove a book entry from the library.
- **Save and Load Library**: Automatically load the library from a file on startup and save any changes to the file before exiting.

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone https://github.com/AbedAwaisy/library_manager_cli.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd library_manager_cli
   ```

## Usage Examples

- **Add a Book**:

  ```bash
  python main.py --add "The Great Gatsby" "F. Scott Fitzgerald" 1925 "Fiction"
  ```

- **List Books**:

  ```bash
  python main.py --list
  ```

- **Edit Book Details**:

  ```bash
  python main.py --edit "The Great Gatsby" --author "F. Scott Fitzgerald" --year 1922
  ```

- **Remove a Book**:

  ```bash
  python main.py --remove "The Great Gatsby"
  ```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.