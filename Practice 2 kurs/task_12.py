from table import create_table
import math
from decimal import Decimal as dc

dict_results = {
    "results_Y": [],
    "results_F": [],
    "results_n": [],
    "results_x": [],
    "results_F-Y": [],
}

x = 0

while x <= dc("0.5"):
    
    Y = dc(math.atan(x))

    n = 1

    F = -x

    a_a = (x ** (2 * n + 1)) / (2 * n + 1)

    while abs(a_a) > dc(10 ** (-4)):
        F += a_a
        
        n += 1

        a_a = (x ** (2 * n + 1)) / (2 * n + 1)
    
    dict_results["results_x"].append(x)
    dict_results["results_F"].append(round(F, 4))
    dict_results["results_n"].append(n)
    dict_results["results_Y"].append(round(Y, 4))
    dict_results["results_F-Y"].append(round(abs(F - Y), 4))

    x += dc("0.05")
    

create_table(["x", "F", "Y", "n", "|F - Y|"], list(zip(
    dict_results["results_x"],
    dict_results["results_F"],
    dict_results["results_Y"],
    dict_results["results_n"],
    dict_results["results_F-Y"])))