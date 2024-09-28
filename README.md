# Task Tracker CLI

Task Tracker CLI is a command-line application built with Python and Typer to help you manage your tasks efficiently.

## Features

- [x] Add, Update, and Delete tasks
- [x] Mark a task as in progress or done
- [x] List all tasks
- [x] List all tasks that are done
- [x] List all tasks that are not done
- [x] List all tasks that are in progress

## Get started

### Option 1: Local Setup

1. Clone the repository:

    ```sh
    ## Cloning the repository
    git clone https://github.com/sikatikenmogne/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. Create and activate a virtual environment:

    ```sh
    ## Creating and activating a virtual environment
    python3 -m venv venv
    . venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    ## Installing dependencies
    pip install -r requirements.txt
    ```

4. Install the CLI application using pipx:

    ```sh
    ## Installing the CLI application using pipx
    pipx install .
    ```

<details>
<summary>Option 2: Using Docker</summary>

1. Clone the repository:

    ```sh
    ## Cloning the repository
    git clone https://github.com/sikatikenmogne/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. Build the Docker image:

    ```sh
    ## Building the Docker image
    docker build -t task-cli-app .
    ```

3. Run the Docker container:

    ```sh
    ## Running the Docker container
    docker run --rm -it task-cli-app
    ```

You can also run specific commands within the Docker container. For example, to mark a task as in progress:

```sh
## Marking a task as in progress using Docker
docker run --rm -it task-cli-app mark-in-progress 1
```

</details>

<details>
<summary>Option 3: Using Dev Container</summary>

1. Clone the repository:

    ```sh
    ## Cloning the repository
    git clone https://github.com/sikatikenmogne/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. Open the project in Visual Studio Code.

3. When prompted, reopen the project in a dev container.

4. The dev container will automatically build and set up the environment.

You can now run the CLI commands within the dev container terminal. For example:

```sh
## Adding a new task in the dev container
task-cli add "Buy groceries"
## Output: Task added successfully (ID: 1)
```

</details>


## Usage

Here are some examples of how to use the Task Tracker CLI:

```sh
## Adding a new task
task-cli add "Buy groceries"
## Output: Task added successfully (ID: 1)

## Listing all tasks
task-cli list

## Listing tasks by status
task-cli list --status in-progress

## Marking a task as completed
task-cli complete 1

## Marking a task as in-progress
task-cli mark-in-progress 1

## Deleting a task
task-cli delete 1
```

### Using Docker

You can also run the Task Tracker CLI commands within a Docker container. Here are the Docker equivalents for the above commands:

```sh
## Adding a new task
docker run --rm -it task-cli-app add "Buy groceries"
## Output: Task added successfully (ID: 1)

## Listing all tasks
docker run --rm -it task-cli-app list

## Listing tasks by status
docker run --rm -it task-cli-app list --status in-progress

## Marking a task as completed
docker run --rm -it task-cli-app complete 1

## Marking a task as in-progress
docker run --rm -it task-cli-app mark-in-progress 1

## Deleting a task
docker run --rm -it task-cli-app delete 1
```

## Contributing

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
