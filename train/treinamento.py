import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import pickle


CAMINHO_DATASET = "dataset/EXAMES-PNS-2013-FINAL_05052023.xlsx"

dados = pd.read_excel(CAMINHO_DATASET)

print("\n===== PRIMEIROS REGISTROS =====")
print(dados.head())

print("\n===== INFORMAÇÕES DO DATASET =====")
print(dados.info())

print("\n===== VALORES NULOS =====")
print(dados.isnull().sum())


dados = dados.dropna()


dados["sexo"] = dados["sexo"].map({
    "M": 0,
    "F": 1
})


dados["imc"] = dados["peso"] / (dados["altura"] ** 2)


X = dados[
    [
        "idade",
        "peso",
        "altura",
        "imc",
        "sexo",
        "pressao_sistolica",
        "pressao_diastolica"
    ]
]


y = dados["hipertenso"]


X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


modelo = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


modelo.fit(X_treino, y_treino)


print("\n===== MODELO TREINADO COM SUCESSO =====")


previsoes = modelo.predict(X_teste)


acuracia = accuracy_score(y_teste, previsoes)

print("\n===== ACURÁCIA =====")
print(f"Acurácia do modelo: {acuracia:.2f}")


print("\n===== MATRIZ DE CONFUSÃO =====")
print(confusion_matrix(y_teste, previsoes))


print("\n===== RELATÓRIO DE CLASSIFICAÇÃO =====")
print(classification_report(y_teste, previsoes))


with open("models/modelo.pkl", "wb") as arquivo:
    pickle.dump(modelo, arquivo)


print("\n===== MODELO SALVO COM SUCESSO =====")
print("Arquivo salvo em: models/modelo.pkl")


paciente = [[
    52,
    88,
    1.75,
    88 / (1.75 ** 2),
    0,
    150,
    95
]]

resultado = modelo.predict(paciente)

probabilidade = modelo.predict_proba(paciente)


print("\n===== TESTE MANUAL =====")

if resultado[0] == 1:
    print("Possível hipertensão detectada.")
else:
    print("Baixa probabilidade de hipertensão.")


print(f"Probabilidade: {probabilidade[0][1] * 100:.2f}%")
