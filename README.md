# 🌡️ Analisador de Temperatura

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)

Programa em Python que lê a temperatura média de cada um dos 12 meses do ano e calcula a **média anual**.

## ✨ O que o programa faz

- Pede a temperatura média de cada mês, do mês 1 ao mês 12
- Soma as temperaturas usando um laço `for`
- Calcula e mostra a média anual com duas casas decimais

## 🚀 Como executar

**1. Instale o Python**

Baixe a versão mais recente em [python.org/downloads](https://www.python.org/downloads/). No Windows, marque a opção **"Add Python to PATH"** durante a instalação.

**2. Baixe o projeto**

```bash
git clone https://github.com/Henrique-Soares801/Analisador-de-Temperatura.git
cd Analisador-de-Temperatura
```

Ou clique no botão verde **Code → Download ZIP** no topo desta página e extraia a pasta.

**3. Rode o programa**

```bash
python analisador.py
```

> 💡 Se o comando `python` não for reconhecido no Windows, use `py` no lugar dele.

## 💻 Exemplo de saída

```
--- Análise de Temperatura Anual  ---
Digite a temperatura média (em ºC) de cada mês do ano:
Temperatura do mês 1: 29
Temperatura do mês 2: 29.5
...
Temperatura do mês 12: 28.5

==============================
🌡️ Média anual calculada: 27.38 ºC
==============================
```

## 🧠 Conceitos praticados

- Laço de repetição `for` com `range()`
- Acumulador para somar valores
- Cálculo de média
- Formatação de saída com f-strings
