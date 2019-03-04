import ui
import web

user_input = ""

while True:
    ui.print_header()

    if user_input.lower() == "e":
        ui.clear()
        break
    elif user_input.lower() == "l":
        data = web.get_all_artists()
        for entry in data:
            ui.echo(entry)
        ui.line(True)
    elif user_input.lower() == "v":
        ui.print_header()
        t = ui.prompt("Artist name")
        data = web.linear_view_artist(t)
        if data == 0:
            ui.line(True)
            ui.header("ERROR")
            ui.line(True)
            ui.echo("Artist not found.")
            ui.line()
        else:
            ui.line(True)
            ui.header(data["name"])
            ui.line(True)
            ui.echo("Members:\t" + ", ".join(data["members"]))
            ui.echo("Genres:\t" + ", ".join(data["genres"]))
            ui.echo("Years active:\t" + ", ".join(data["years_active"]))
            ui.line()
    else:
        ui.echo("Welcome to a world of Music!")
        ui.line()

    ui.echo("L | List artists")
    ui.echo("V | View artist profile")
    ui.echo("E | Exit application")
    ui.line()
    user_input = ui.prompt("Selection")



