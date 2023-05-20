from shiny import App, render, ui
import pandas as pd

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(ui.input_slider(
            id="Fatalities",
            label="Number of fatalities",
            min=0,
            max=5,
            value=0.5,
            )), 
        ui.panel_main(ui.output_table("summary"))) # Call the funtion summary
)


def server(input, output, session):
    @output
    @render.table
    def summary():
        df = pd.read_csv("Python-Shiny/data/BrazilConflicts2018.csv")
        df_table = df
        return df_table

app = App(app_ui, server)
