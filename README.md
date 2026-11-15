# 🌡️ Analisador de Temperatura

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)

Programa em Python que lê a temperatura média de cada mês do ano e gera um **resumo estatístico anual**.

## ✨ Funcionalidades

- Cálculo da **média anual**
- **Mês mais quente** e **mês mais frio**
- **Amplitude térmica** (diferença entre a máxima e a mínima)
- Lista dos **meses acima da média**
- Validação da entrada: aceita vírgula ou ponto e pede de novo se o valor for inválido

## 🚀 Como executar

Pré-requisito: [Python 3.9+](https://www.python.org/downloads/).

```bash
git clone https://github.com/Henrique-Soares801/Analisador-de-Temperatura.git
cd Analisador-de-Temperatura
python analisador.py
```

## 💻 Exemplo de saída

```
========================================
              RESUMO ANUAL
========================================
Média anual:     27.38 °C
Mês mais quente: Fevereiro (29.5 °C)
Mês mais frio:   Julho (25.0 °C)
Amplitude:       4.5 °C
========================================
Meses acima da média:
  - Janeiro    29.0 °C
  - Fevereiro  29.5 °C
  - Março      29.0 °C
  - Abril      28.0 °C
  - Novembro   28.0 °C
  - Dezembro   28.5 °C
========================================
```

## 🧠 Conceitos praticados

- Listas, tuplas e `zip()`
- Funções com responsabilidade única e type hints
- `sum()`, `max()`, `min()` e `list.index()`
- Tratamento de erros com `try/except`
- Formatação de saída com f-strings
