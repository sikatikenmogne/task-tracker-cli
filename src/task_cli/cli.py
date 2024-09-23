import typer

from .task import task

app = typer.Typer()
app.command()(task)

if __name__ == "__main__":
    app()
    