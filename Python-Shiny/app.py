from shiny import App, render, ui
import pandas as pd

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(), 
        ui.panel_main(ui.output_table("summary")))
)


def server(input, output, session):
    @output
    @render.table
    def summary():
        df = pd.read_csv("./ddbb/BrazilConflicts2018.csv")
        return df


app = App(app_ui, server)
