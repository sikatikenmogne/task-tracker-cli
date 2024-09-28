# Task Tracker CLI

Task Tracker CLI is a command-line application built with Python and Typer to help you manage your tasks efficiently.

## Features

- [x] Add, Update, and Delete tasks
- [x] Mark a task as in progress or done
- [x] List all tasks
- [x] List all tasks that are done
- [x] List all tasks that are not done
- [x] List all tasks that are in progress

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/sikatikenmogne/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    . venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Install the CLI application using pipx:

    ```sh
    pipx install .
    ```

## Usage

Here are some examples of how to use the Task Tracker CLI:

- **Add a new task**:

    ```sh
    task-cli add "Buy groceries"
    ```

- **List all tasks**:

    ```sh
    task-cli list
    ```

- **Mark a task as completed**:

    ```sh
    task-cli complete 1
    ```

- **Delete a task**:

    ```sh
    task-cli delete 1
    ```

## Development

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
