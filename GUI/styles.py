RPM_BAR = """
    QProgressBar::chunk
    {
        border-color: rgb(0, 0, 0);
        border-width: 3px;
        border-radius: 7px;
        background-color: rgb(%d, %d, %d);
        width: 15px;
        margin: 3px;
    }
"""

INFO_GEAR = """
    color: rgb(255, 219, 19);
    background-color: rgba(0, 0, 0, 0%);
    border-color: rgb(206,249,255);
    border-style: solid;
    border-width: 15px;
    border-radius: 20px;
"""

GEAR_STATUS = """
    background-color: rgb(%d, %d, %d);
    border-color: rgb(0, 0, 0);
    border-style: solid;
    border-width: 9px;
    border-radius: 20px;
"""

UNIT_RPM = """
    color:rgb(255, 219, 19);
    background-color: rgba(0, 0, 0, 0%);
    border-width: 0;
    border-radius: 0;
"""

INFO_RPM = """
    color: white;
    background-color: rgba(0, 0, 0, 0%);
    border-width: 0;
    border-radius: 0;
"""

INFO_RPM_2 = """
    color: white;
    background-color: rgba(0, 0, 0, 0%);
    border-width: 0;
    border-radius: 0;
"""

INFO_LABEL_TEXT = """
    color: rgb(255, 219, 19);
    background-color: rgba(0, 0, 0, 0%);
    border-width: 0;
    border-radius: 0px;
"""

INFO_LABEL_VALUE = """
    color: white;
    background-color: rgba(0, 0, 0, 0%);
    border-width: 0;
    border-radius: 0px;
"""

QFRAME_STYLE = """
    QFrame{
    border-color: rgb(206,249,255);
    border-style: solid;
    border-width: 9px;
    border-radius: 20px;
    background-color: rgba(0, 0, 0, 0%)
    }
"""

WARNING_QFRAME_STYLE = """
    color: white;
    font-weight: 900;
    background-color: rgb(%d, %d, %d);
    border-color: rgb(206,249,255);
    border-style: solid;
    border-width: 9px;
    border-radius: 20px;
"""
