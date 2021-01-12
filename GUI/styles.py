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
    font-size: 30px;
    background-color: rgba(50,0,0,50%);
    border-width: 0;
    border-radius: 0;
"""

DISPLAY_STYLE = """
    QFrame{
    border-color: white;
    border-style: solid;
    border-width: 5px;
    border-radius: 20px;
    }
   

"""

INFO_GEAR = """
    color: white;
    font-size: 160px;
    background-color: rgba(0,0,0,0%);
    border-color: white;
    border-style: solid;
    border-width: 10px;
    border-radius: 20px;
   
"""

INFO_RPM = """
    color: white;
    font-size: 100px;
    background-color: rgba(0, 50, 0, 50%);
    border-width: 0;
    border-radius: 0;
"""

STATUS_LABEL_STYLES = """
    color: white;
    font-size: %dpx;
    background-color: rgba(0, 0, 0, 0%);
    border: 3px inset %s;
"""

OFFSET = 20
GEAR_SIZE = 160