"""
Calculadora Python Interativa
-----------------------------
Projeto desenvolvido para o Desafio 1 da Imersão Engenharia de Software:
Dev na Era da IA - Alura.

Desenvolvido com auxílio do Google AI Studio.
"""


def adicionar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão do primeiro número pelo segundo.
    Lança ValueError se o divisor for zero.
    """
    if b == 0:
        raise ValueError("Não é possível realizar divisão por zero.")
    return a / b


def formatar_numero(valor: float) -> str:
    """
    Formata um número para exibição amigável:
    Se o valor for inteiro (ex: 5.0), exibe como 5.
    Se possuir casas decimais relevantes, exibe formatado com até 4 casas decimais sem zeros à direita.
    """
    if valor.is_integer():
        return str(int(valor))
    
    # Formata com até 4 casas decimais e remove zeros desnecessários ao final
    texto = f"{valor:.4f}".rstrip("0").rstrip(".")
    return texto


def obter_numero(mensagem: str) -> float:
    """
    Solicita um número ao usuário via terminal e valida a entrada.
    Aceita inteiros, decimais (com ponto ou vírgula) e números negativos.
    Repete a solicitação até que uma entrada válida seja fornecida.
    """
    while True:
        entrada = input(mensagem).strip()
        # Permite o uso de vírgula como separador decimal, substituindo por ponto
        entrada_normalizada = entrada.replace(",", ".")
        
        try:
            numero = float(entrada_normalizada)
            return numero
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido (ex: 10, -5, 3.14 ou 2,5).")


def obter_operacao() -> str:
    """
    Apresenta as opções de operação disponíveis e solicita a escolha do usuário.
    Valida a entrada aceitando tanto os símbolos matemáticos (+, -, *, /)
    quanto os números das opções (1, 2, 3, 4).
    """
    print("\nOperações disponíveis:")
    print("  [1] ou [+]  Adição")
    print("  [2] ou [-]  Subtração")
    print("  [3] ou [*]  Multiplicação")
    print("  [4] ou [/]  Divisão")
    
    mapa_opcoes = {
        "1": "+",
        "+": "+",
        "2": "-",
        "-": "-",
        "3": "*",
        "*": "*",
        "4": "/",
        "/": "/"
    }
    
    while True:
        escolha = input("\nEscolha a operação desejada: ").strip()
        if escolha in mapa_opcoes:
            return mapa_opcoes[escolha]
        print("Operador inválido! Escolha uma opção válida (+, -, *, / ou 1 a 4).")


def perguntar_continuar() -> bool:
    """
    Pergunta ao usuário se deseja realizar outro cálculo.
    Retorna True se sim e False se não.
    """
    while True:
        resposta = input("\nDeseja realizar outro cálculo? (s/n): ").strip().lower()
        if resposta in ["s", "sim", "y", "yes"]:
            return True
        elif resposta in ["n", "nao", "não", "no"]:
            return False
        else:
            print("Resposta inválida! Digite 's' para continuar ou 'n' para sair.")


def executar_calculadora() -> None:
    """
    Controla o fluxo principal de execução da calculadora interativa.
    """
    print("=" * 48)
    print("        Calculadora Python Interativa")
    print("=" * 48)
    print("Bem-vindo! Realize cálculos matemáticos com facilidade.")
    
    while True:
        print("\n" + "-" * 40)
        # 1. Obtenção dos números
        num1 = obter_numero("Digite o primeiro número: ")
        operador = obter_operacao()
        num2 = obter_numero("Digite o segundo número: ")
        
        # 2. Execução do cálculo
        try:
            if operador == "+":
                resultado = adicionar(num1, num2)
            elif operador == "-":
                resultado = subtrair(num1, num2)
            elif operador == "*":
                resultado = multiplicar(num1, num2)
            elif operador == "/":
                resultado = dividir(num1, num2)
            else:
                print("Erro: Operador não reconhecido.")
                continue

            # 3. Exibição clara e amigável do resultado
            num1_fmt = formatar_numero(num1)
            num2_fmt = formatar_numero(num2)
            res_fmt = formatar_numero(resultado)
            
            print("\n" + "=" * 40)
            print(f"  Operação realizada: {num1_fmt} {operador} {num2_fmt}")
            print(f"  Resultado: {res_fmt}")
            print("=" * 40)
            
        except ValueError as erro:
            print(f"\n[ERRO MATEMÁTICO]: {erro}")
        
        # 4. Verificação de continuidade
        if not perguntar_continuar():
            print("\n" + "=" * 48)
            print("  Obrigado por usar a Calculadora Python! Até logo.")
            print("=" * 48 + "\n")
            break


if __name__ == "__main__":
    executar_calculadora()
