## Module to convert pandas dataframe to rich table.
## These are modified methods found online
##
## Referred from:
## https://gist.githubusercontent.com/neelabalan/33ab34cf65b43e305c3f12ec6db05938/raw/24f7db8459629ed6744f726754b1a4a068314026/df_to_table.py
## https://github.com/davidsa03/numerize

# Import modules
from typing import Optional
import pandas as pd
from rich.table import Table
from decimal import Decimal

# Method to round numbers
def round_num(n, decimal=2):
    n = Decimal(n)
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimal)

# Method to numbersize numbers
def numerize(n, decimal=2):
    # 60 sufixes
    sufixes = [ "", "K", "M", "B", "T", "Qa", "Qu", "S", "Oc", "No",
                "D", "Ud", "Dd", "Td", "Qt", "Qi", "Se", "Od", "Nd","V",
                "Uv", "Dv", "Tv", "Qv", "Qx", "Sx", "Ox", "Nx", "Tn", "Qa",
                "Qu", "S", "Oc", "No", "D", "Ud", "Dd", "Td", "Qt", "Qi",
                "Se", "Od", "Nd", "V", "Uv", "Dv", "Tv", "Qv", "Qx", "Sx",
                "Ox", "Nx", "Tn", "x", "xx", "xxx", "X", "XX", "XXX", "END"]

    sci_expr = [1e0, 1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27,
                1e30, 1e33, 1e36, 1e39, 1e42, 1e45, 1e48, 1e51, 1e54, 1e57,
                1e60, 1e63, 1e66, 1e69, 1e72, 1e75, 1e78, 1e81, 1e84, 1e87,
                1e90, 1e93, 1e96, 1e99, 1e102, 1e105, 1e108, 1e111, 1e114, 1e117,
                1e120, 1e123, 1e126, 1e129, 1e132, 1e135, 1e138, 1e141, 1e144, 1e147,
                1e150, 1e153, 1e156, 1e159, 1e162, 1e165, 1e168, 1e171, 1e174, 1e177]
    try:
        minus_buff = n
        n = abs(n)
        for x in range(len(sci_expr)):
            try:
                if n >= sci_expr[x] and n < sci_expr[x+1]:
                    sufix = sufixes[x]
                    if n >= 1e3:
                        num = str(round_num(n/sci_expr[x], decimal))
                    else:
                        num = str(n)
                    return num + sufix if minus_buff > 0 else "-" + num + sufix
            except IndexError:
                print("You've reached the end")

    except:
        return n

# Method to convert pandas dataframe to rich table
def dft(
    pandas_dataframe: pd.DataFrame,
    show_index: bool = True,
    index_name: Optional[str] = None,
    title_name: str = "NoTitle",
    convert: bool = True,
) -> Table:
    """Convert a pandas.DataFrame obj into a rich.Table obj.
    Args:
        pandas_dataframe (DataFrame): A Pandas DataFrame to be converted to a rich Table.
        rich_table (Table): A rich Table that should be populated by the DataFrame values.
        show_index (bool): Add a column with a row count to the table. Defaults to True.
        index_name (str, optional): The column name to give to the index column. Defaults to None, showing no value.
    Returns:
        Table: The rich Table instance passed, populated with the DataFrame values."""

    rich_table = Table(title=title_name, show_header=True, header_style="bold magenta")

    if show_index:
        index_name = str(index_name) if index_name else ""
        rich_table.add_column(index_name)
        rich_indexes = pandas_dataframe.index.to_list()

    for column in pandas_dataframe.columns:
        rich_table.add_column(str(column))

    for index, value_list in enumerate(pandas_dataframe.values.tolist()):
        row = [str(rich_indexes[index])] if show_index else []
        if convert:
            row += [str(numerize(x)) for x in value_list]
        else:
            row += [str(x) for x in value_list]
        rich_table.add_row(*row)

    return rich_table