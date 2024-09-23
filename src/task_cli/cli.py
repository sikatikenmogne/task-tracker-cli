import typer

from .task import add, update, delete, mark_done, list, mark_in_progress

app = typer.Typer()

app.command()(add)

app.command()(update)

app.command()(delete)

app.command()(mark_in_progress)

app.command()(mark_done)

app.command()(list)

    