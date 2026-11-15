"""Analisador de temperatura anual.

Lê a temperatura média de cada mês do ano e apresenta um resumo
estatístico: média anual, mês mais quente, mês mais frio, amplitude
térmica e os meses que ficaram acima da média.
"""

MESES = (
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',
)


def ler_temperatura(mes: str) -> float:
    """Pede a temperatura de um mês até o usuário digitar um número válido."""
    while True:
        valor = input(f'Temperatura média de {mes} (°C): ').replace(',', '.')
        try:
            return float(valor)
        except ValueError:
            print('Valor inválido. Digite um número, por exemplo 27.5.')


def ler_temperaturas() -> list[float]:
    """Lê as temperaturas dos 12 meses, na ordem do calendário."""
    return [ler_temperatura(mes) for mes in MESES]


def resumo_anual(temperaturas: list[float]) -> dict:
    """Calcula as estatísticas do ano a partir das 12 temperaturas."""
    media = sum(temperaturas) / len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    return {
        'media': media,
        'maxima': maxima,
        'mes_mais_quente': MESES[temperaturas.index(maxima)],
        'minima': minima,
        'mes_mais_frio': MESES[temperaturas.index(minima)],
        'amplitude': maxima - minima,
        'acima_da_media': [
            (mes, temp) for mes, temp in zip(MESES, temperaturas) if temp > media
        ],
    }


def exibir_resumo(resumo: dict) -> None:
    """Mostra o resumo anual formatado no terminal."""
    linha = '=' * 40
    print(f'\n{linha}')
    print('RESUMO ANUAL'.center(40))
    print(linha)
    print(f'Média anual:     {resumo["media"]:.2f} °C')
    print(f'Mês mais quente: {resumo["mes_mais_quente"]} ({resumo["maxima"]:.1f} °C)')
    print(f'Mês mais frio:   {resumo["mes_mais_frio"]} ({resumo["minima"]:.1f} °C)')
    print(f'Amplitude:       {resumo["amplitude"]:.1f} °C')
    print(linha)

    if resumo['acima_da_media']:
        print('Meses acima da média:')
        for mes, temp in resumo['acima_da_media']:
            print(f'  - {mes:<10} {temp:.1f} °C')
    else:
        print('Nenhum mês ficou acima da média.')
    print(linha)


def main() -> None:
    print('--- Análise de Temperatura Anual ---')
    print('Digite a temperatura média (em °C) de cada mês do ano.\n')
    temperaturas = ler_temperaturas()
    exibir_resumo(resumo_anual(temperaturas))


if __name__ == '__main__':
    main()
