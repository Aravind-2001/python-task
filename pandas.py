dict={"country":["India","China","Brazil","Russia"],
      "capital":["NewDelhi","Beijing","Brasilis","Moscow"],
      "area":[3.456,9.872,8.516,17.32],
      "population":[1252,1357,200.4,143.5]}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

