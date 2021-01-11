WHITE_FONT = "color: white;"

BORDER = "border: 5px inset gray;"

TRANSPARENT_BACKGROUND = "background-color: rgba(0, 0, 0, 0%);"


PROGRESS_BAR_STYLES = """
    QProgressBar{
        border: 3px inset %s;
        background-color: black;
        text-align: right
    }
    QProgressBar::chunk {
        background-color: %s;
    }
"""

INFO_LABEL_STYLES = """
    color: white;
    font-size: 40px;
    background-color: rgba(0,0,0,0%);
"""



INFO_GEAR = """
    color: white;
    font-size: 160px;
    background-color: rgba(128,0,0,50%);
"""

STATUS_LABEL_STYLES = """
    color: white;
    font-size: %dpx;
    background-color: rgba(0,0,0,0%);
    border: 3px inset %s;
"""

OFFSET = 20
GEAR_SIZE = 160