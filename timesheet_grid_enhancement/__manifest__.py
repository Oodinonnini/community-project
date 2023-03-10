# © 2022 Tobias Zehntner, Jérémy Van Driessche, Alexandre Van Ommeslaghe, Albin Gilles
# © 2022 Niboo SRL (https://www.niboo.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Timesheet - Timesheet grid enhancement",
    "category": "Project",
    "summary": "Improves Timesheet grid view",
    "description": """
    - Changed the display of the timer timesheet grid view.
    - Added a popup on click of a cell in grid view.
    - Remove null lines in grid view.
    - Adapted timer function to open a popup instead of creating the timesheet on the fly.
    """,
    "author": "Niboo",
    "website": "https://www.niboo.com",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["timesheet_grid", "hr_timesheet"],
    "data": [
        "templates/assets_backend.xml",
        "views/res_config_settings_views.xml",
        "views/timesheet_views.xml",
    ],
    "qweb": ["static/src/xml/timesheet_grid.xml"],
    "installable": True,
    "application": False,
}
