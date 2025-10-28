import sys

def perguntar(q, opcoes, resposta_certa, valor):
    print(f"\nPergunta (valor: R$ {valor:,}):")
    print(q)
    letras = ['A', 'B', 'C', 'D']
    for i, opt in enumerate(opcoes):
        print(f"  {letras[i]}) {opt}")
    while True:
        escolha = input("Sua resposta (A/B/C/D) ou Q para sair e sacar: ").strip().upper()
        if escolha in letras:
            idx = letras.index(escolha)
            return idx == resposta_certa
        if escolha == 'Q':
            return None
        print("Entrada inválida. Digite A, B, C, D ou Q.")


def format_money(x):
    return f"R$ {x:,.0f}".replace(',', '.')


def main():
    saldo = 0
    limite = 80000

    print('Bem-vindo! Você começa com R$ 0 e pode ganhar até R$ 80.000.')

    perguntas = [
        ("Qual é a capital do Brasil?", ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"], 1, 5000),
        ("Qual é a soma de 12 + 15?", ["26", "28", "27", "30"], 2, 10000),
        ("Quem escreveu 'Dom Casmurro'?", ["Machado de Assis", "José de Alencar", "Carlos Drummond", "Clarice Lispector"], 0, 15000),
        ("Qual planeta é conhecido como o Planeta Vermelho?", ["Vênus", "Marte", "Júpiter", "Saturno"], 1, 20000),
        ("Em que ano o Brasil foi descoberto?", ["1500", "1492", "1600", "1808"], 0, 25000),
        ("Qual é o elemento com símbolo 'O'?", ["Ouro", "Oxigênio", "Prata", "Cobre"], 1, 50000),
    ]

    for texto, opcoes, idx_correto, valor in perguntas:
        print('\nSaldo atual:', format_money(saldo))
        print(f"Pergunta (valor: {format_money(valor)}): {texto}")
        for i, o in enumerate(opcoes):
            print(f"  {chr(65+i)}) {o}")

        # ler resposta válida (A-D)
        while True:
            r = input('Resposta (A/B/C/D): ').strip().upper()
            if r in ('A', 'B', 'C', 'D'):
                escolha = ord(r) - 65
                break
            print('Entrada inválida. Digite A, B, C ou D.')

        if escolha == idx_correto:
            saldo += valor
            print('Correto! Você ganhou', format_money(valor))
        else:
            print('Errado. Você não ganhou esse valor.')

        if saldo >= limite:
            saldo = limite
            print('\nParabéns! Você alcançou o limite de', format_money(limite))
            break

    print('\nFim do jogo. Saldo final:', format_money(saldo))


if __name__ == '__main__':
    main()
