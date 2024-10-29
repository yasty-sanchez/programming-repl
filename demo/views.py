from django.shortcuts import render

# Create your views here.


def programming(request):
    context = {
        "example1": """import numpy as np

display(np.sqrt(4))""",
        "example2": """import numpy as np
import pandas as pd
from pyscript import display

df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD')).cumsum()
display(df)""",
    }

    return render(request, "programming.html", context)
