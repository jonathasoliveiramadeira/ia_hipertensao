# README.md

# IA de Predição de Hipertensão

Sistema de Inteligência Artificial desenvolvido em Python para análise preditiva de hipertensão arterial utilizando Machine Learning.

O projeto tem como objetivo auxiliar previamente na identificação de possíveis casos de hipertensão a partir de dados biométricos e clínicos do paciente.

---

# Objetivos do Projeto

* Desenvolver uma IA capaz de prever possíveis casos de hipertensão
* Utilizar Machine Learning supervisionado
* Trabalhar com análise de dados clínicos
* Permitir execução local e futura implantação em servidores
* Criar estrutura modular e reutilizável

---

# Tecnologias Utilizadas

| Tecnologia    | Finalidade                    |
| ------------- | ----------------------------- |
| Python        | Linguagem principal           |
| Pandas        | Manipulação de dados          |
| NumPy         | Operações matemáticas         |
| Scikit-Learn  | Machine Learning              |
| Random Forest | Algoritmo preditivo           |
| Matplotlib    | Visualização de dados         |
| Streamlit     | Interface web simples         |
| Pickle        | Salvamento do modelo treinado |

---

# Estrutura do Projeto

```text
IA_Hipertensao/
│
├── dataset/
│   └── hipertensao.xlsx
│
├── models/
│   └── modelo.pkl
│
├── train/
│   └── treinamento.py
│
├── app/
│   └── interface.py
│
├── requirements.txt
│
└── README.md
```

---

# Como Funciona

## Fluxo Geral

```text
Usuário → Interface → Modelo IA → Predição → Resultado
```

---

# Dataset

O sistema utiliza um dataset contendo informações biométricas e clínicas dos pacientes.

## Exemplos de dados utilizados

* idade
* peso
* altura
* sexo
* pressão sistólica
* pressão diastólica
* IMC
* classificação de hipertensão

---

# Formato Esperado do Dataset

Arquivo:

```text
EXAMES-PNS-2013-FINAL_05052023.xlsx
```

Exemplo de estrutura:

| idade | peso | altura | sexo | pressao_sistolica | pressao_diastolica | hipertenso |
| ----- | ---- | ------ | ---- | ----------------- | ------------------ | ---------- |
| 45    | 82   | 1.75   | M    | 150               | 90                 | 1          |
| 22    | 65   | 1.68   | F    | 110               | 70                 | 0          |

---

# Machine Learning Utilizado

## Tipo

Aprendizado supervisionado.

## Algoritmo principal

Random Forest.

O modelo aprende padrões a partir dos dados históricos dos pacientes e realiza previsões sobre possíveis casos de hipertensão.

---

# Divisão do Dataset

O conjunto de dados é dividido automaticamente em:

```text
60% treino
20% validação
20% teste
```

Objetivos:

* treinar o modelo
* validar desempenho
* evitar overfitting
* testar generalização

---

# Métricas de Avaliação

O sistema utiliza:

* acurácia
* precisão
* recall
* F1-score
* matriz de confusão

---

# Como Instalar

# 1. Instalar Python

Download:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

Durante a instalação:

✅ Marcar:

```text
Add Python to PATH
```

---

# 2. Clonar ou Baixar o Projeto

```bash
git clone https://github.com/jonathasoliveiramadeira/ia_hipertensao.git
```

Ou baixe manualmente.

---

# 3. Criar Ambiente Virtual

Dentro da pasta do projeto:

```bash
python -m venv venv
```

---

# 4. Ativar Ambiente Virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux/Mac

```bash
source venv/bin/activate
```

---

# 5. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

# Como Executar o Treinamento

Execute:

```bash
python train/treinamento.py
```

O sistema irá:

* carregar o dataset
* tratar os dados
* treinar a IA
* avaliar métricas
* salvar o modelo treinado

---

# Modelo Treinado

Após o treinamento será criado:

```text
models/modelo.pkl
```

Esse arquivo contém a IA treinada.

Ele será reutilizado futuramente pela interface do sistema.

---

# Interface do Sistema

O projeto será preparado para utilização via interface web simples utilizando Streamlit.

Futuramente poderá ser integrado em:

* sistemas hospitalares
* aplicações desktop
* APIs
* aplicações mobile
* servidores externos

---

# Objetivo de Arquitetura

O sistema está sendo desenvolvido com foco em:

* execução local
* modularidade
* reutilização
* futura implantação em servidores
* possibilidade de empacotamento executável

---

# Possíveis Expansões Futuras

* integração com smartwatches
* dashboard médico
* gráficos estatísticos
* API REST
* autenticação de usuários
* Deep Learning
* histórico clínico
* monitoramento em tempo real

---

# Execução Local

O projeto será totalmente executável localmente.

Futuramente poderá ser:

* empacotado em .exe
* instalado em servidores do campus
* implantado em Linux ou Windows Server
* transformado em aplicação web completa

---

# Sugestão de Stack Final

```text
Python
Pandas
Scikit-Learn
Random Forest
Streamlit
```

---

# Autor

Jonathas Madeira

Projeto acadêmico de Inteligência Artificial aplicada à saúde.
