def display_register():
    """
    Imagine que você está trabalhando com um dispositivo embarcado
    que tem um registro de status de 32 bits.

    Cada bit neste registro representa um recurso, sinalizador ou
    estado específico do dispositivo.

    Atribuições de bits:

    |Bit    |Description                        |
    |-------|-----------------------------------|
    | 0     | Device Power On (1 = ON, 0 = OFF) |
    | 1     | Error Flag (1 = Error, 0 = OK)    |
    | 2     | Ready Status (1 = Ready, 0 = Busy)|
    | 3     | Overheat Warning (1 = Overheat)   |
    | 4-7   | Reserved                          |
    | 8-15  | Device Mode (8 bits: Mode ID)     |
    | 16-31 | Reserved for future use           |

    Requisitos:

    Implementar um programa que leia duas entradas (reg e ModeID), e trabalhe a fim de apresentar o estado do registro.

    Os dados de reg poderão vir no formato decimal, hexadecimal ou binario.

    Entrada
    O programa deve receber dois valores do usuário:

    1️⃣Vaor do registrador (em decimal, binário 0bXXXX, ou hexadecimal 0xXXXX).
    2️⃣ Mode ID (valor entre 0 e 255).

    ===========================
     REGISTER STATE
    ===========================
      Power On : No/Yes
      Error : No/Yes
      Ready : No/Yes
      Overheat : No/Yes
      Mode ID : 999

    Saída
    ===========================
     REGISTER STATE
    ===========================
      Power On : No/Yes
      Error : No/Yes
      Ready : No/Yes
      Overheat : No/Yes
      Mode ID : 999

    :return:
    """
    valor = input()
    modelo = input()
    if valor[0:2] != "0b":
        if valor[0:2] == "0x":
            binario = bin(int(valor, 16))
        else:
            binario = bin(int(valor))
    else:
        binario = valor
    binario = binario[2:]
    binario = binario[::-1]
    while len(binario) < 4:
        binario += "0"
    binario = binario[::-1]
    binario = binario[-4:]
    if binario[3] == "1":
        power = "Yes"
    else:
        power = "No"
    if binario[2] == "1":
        erro = "Yes"
    else:
        erro = "No"
    if binario[1] == "1":
        leia = "Yes"
    else:
        leia = "No"
    if binario[0] == "1":
        overheat = "Yes"
    else:
        overheat = "No"
    print("===========================")
    print("      REGISTER STATE       ")
    print("===========================")
    print(f"  Power On    : {power}")
    print(f"  Error       : {erro}")
    print(f"  Ready       : {leia}")
    print(f"  Overheat    : {overheat}")
    print(f"  Mode ID     : {modelo}")


display_register()
