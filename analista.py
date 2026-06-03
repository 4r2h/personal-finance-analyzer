import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("archivostexto\\distrisueldo.csv", names=["mes","ingresos"])

df2 = pd.read_csv("archivostexto\\gastosmes.csv", names=["mes","gastos"])

def ahorros_totales():
    acum = 0
    for i in range(len(df)):
        aux = df.loc[i,"ingresos"]
        if aux > 0:
            acum += aux * 0.3
    return acum 

def ingresos_totales():
    return df[df["ingresos"]>0]["ingresos"].sum()

def mostrar_graf():
    df_total = df.merge(df2, on="mes")
    plt.plot(df_total["mes"],df_total["ingresos"])
    plt.plot(df_total["mes"],df_total["gastos"])
    plt.xlabel("Mes")
    plt.ylabel("Monto")
    plt.title("Ingresos vs Gastos")
    plt.show()
    
def supragastos():
    df_total = df.merge(df2, on="mes")
    
    for i in range(len(df)):
        if df_total["gastos"][i] > df_total["ingresos"][i] * 0.3:
            print(f"Gastaste de más en {df_total['mes'][i]}")
        else: print(f"Te controlaste en {df_total['mes'][i]}, muy bien")

print(f"El ingreso total del año es: {ingresos_totales()}k")
print(f"El ahorro total del año es: {ahorros_totales()}k")
mostrar_graf()
#supragastos()