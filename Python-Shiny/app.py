from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        
    )
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 3}"


app = App(app_ui, server)
