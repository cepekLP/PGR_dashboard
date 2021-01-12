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
    font-size: 20px;
    background-color: rgba(0,0,0,0%);
    border-width: 0;
    border-radius: 0px;
"""

QFRAME_STYLE = """
    QFrame{
    border-color: white;
    border-style: solid;
    border-width: 5px;
    border-radius: 30px;
    }
"""

INFO_GEAR = """
    color: white;
    font-size: 160px;
    background-color: rgba(0,0,0,0%);
    border-color: white;
    border-style: solid;
    border-width: 10px;
    border-radius: 30px;   
"""

UNIT_RPM = """
    color: white;
    font-size: 30px;
    border-width: 0;
    border-radius: 0;
"""

INFO_RPM = """
    color: white;
    font-size: 110px;
    background-color: rgba(0, 0, 0, 0%);
    border-width: 0;
    border-radius: 0;
"""

WARNING_QFRAME_STYLE = """
    color: white;
    background-color: rgb(%d, %d, %d);
    border-color: white;
    border-style: solid;
    border-width: 5px;
    border-radius: 30px;
"""

OFFSET = 20
GEAR_SIZE = 160