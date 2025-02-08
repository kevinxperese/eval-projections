import os

from ExcelWriter.worksheets import worksheets
from ExcelWriter.make_data_underlying_figures import make_quality_data
from great_tables import GT, loc, style


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
HTML_PATH = os.path.abspath(f"{CURRENT_PATH}/../output_data/HTML")

projection_years = [2, 6, 11]

worksheets['Figure 1']['data'] = make_quality_data('deficit', projection_years)

table = (
    GT(worksheets['Figure 1']['data'])
    .tab_header(
        title = worksheets['Figure 1']['title'],
        subtitle = 'Percentage of GDP'
    )
    .tab_style(
        style = style.text(font="Times New Roman", weight="bold", align="left"),
        locations = loc.title()
    )
    .tab_style(
        style = style.text(align="left"),
        locations = loc.subtitle()
    )

)


table.write_raw_html(os.path.join(HTML_PATH, 'index.html'))