import pandas as pd
import dtale
import dtale.app as dtale_app

dtale_app.USE_COLAB = True

# Creamos un DataFrame de ejemplo y lo mostramos con D-Tale
df = pd.DataFrame([1, 2, 3, 4, 5], columns=['numeros'])
dtale.show(df)
