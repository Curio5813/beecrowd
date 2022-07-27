def main():
    from decimal import Decimal
    taxa1, taxa2, taxa3 = float(Decimal('0.08')), float(Decimal('0.18')), float(Decimal('0.28'))
    renda = float(Decimal(input()))
    if 0.00 <= renda <= 2000.00:
        print('Isento')
    elif 2000.01 <= renda <= 3000.00:
        imposto = taxa1 * (renda - 2000.00)
        print(f'R$ {imposto:.2f}')
    elif 3000.01 <= renda <= 4500.00:
        imposto = taxa1 * 1000.00 + taxa2 * (renda - 3000.00)
        print(f'R$ {imposto:.2f}')
    elif renda > 4500.00:
        imposto = taxa1 * 1000.00 + taxa2 * 1500.00 + taxa3 * (renda - 4500.00)
        print(f'R$ {imposto:.2f}')


if __name__ == '__main__':
    main()
