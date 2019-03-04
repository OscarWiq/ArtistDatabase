import ui
import web


s = ""

while True:
    ### Header section
    ui.clear()
    ui.line()
    ui.header("ARTIST DATABASE")
    ui.line()
    
    ### Data section
    if s.lower() == "e":
        ui.clear()
        break
    elif s.lower() == "l":
        data = web.get_all_artists()
        #Prints each entry in data, one by one.
        for entry in data:
            ui.echo(entry)
        ui.line(True)
    elif s.lower() == "v":
        ui.clear()
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
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
    
    ### Selection section
    ui.echo("L | List artists")
    ui.echo("V | View artist profile")
    ui.echo("E | Exit application")
    ui.line()
    s = ui.prompt("Selection")
