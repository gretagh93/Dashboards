from shiny import App, render, ui
import pandas as pd

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(ui.input_slider(
            id="fatalities",
            label="Number of fatalities",
            min=0,
            max=5,
            value=1,
            )), 
        ui.panel_main(ui.output_table("summary"))) # Call the funtion summary to draw a table
)


def server(input, output, session):
    @output
    @render.table
    def summary():
        df = pd.read_csv("Python-Shiny/data/BrazilConflicts2018.csv")
        df = df.loc[df["FATALITIES"] >= (input.fatalities())]
        return df

app = App(app_ui, server)
