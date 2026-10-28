# 🧮 Calculadora Python Interativa

> **Desafio 1 — Imersão Engenharia de Software: Dev na Era da IA (Alura)**  
> Desenvolvido com auxílio do **Google AI Studio**.

Uma calculadora de linha de comando desenvolvida exclusivamente em **Python 3**, projetada para ser simples, robusta, didática e de fácil leitura. O projeto implementa as quatro operações aritméticas básicas com validação estrita de dados, formatação inteligente de resultados e tratamento de exceções.

---

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
- [Exemplos de Utilização](#-exemplos-de-utilização)
- [Conceitos de Python Aplicados](#-conceitos-de-python-aplicados)
- [Respostas ao Desafio 1 da Alura](#-respostas-ao-desafio-1-da-alura)
  - [1. Principais componentes do código](#1-quais-são-os-principais-componentes-do-código-gerado)
  - [2. Recepção de dados e identificação da operação](#2-como-a-aplicação-recebe-os-números-e-identifica-a-operação-escolhida)
  - [3. Lógica de cálculo e exibição dos resultados](#3-como-a-lógica-de-programação-é-utilizada-para-realizar-os-cálculos-e-apresentar-os-resultados)

---

## 🎯 Visão Geral

Este projeto foi construído para atender aos requisitos do **Desafio 1** da **Imersão Engenharia de Software: Dev na Era da IA**, promovida pela [Alura](https://www.alura.com.br/).

O propósito do desafio é aplicar a colaboração entre desenvolvedores e ferramentas de Inteligência Artificial — neste caso, o **Google AI Studio** — para estruturar uma solução limpa, funcional e educacional, compreendendo os pilares essenciais da lógica de programação e da sintaxe de Python.

---

## ✨ Funcionalidades

- ➕ **Adição (`+`)**: Soma dois números inteiros ou decimais.
- ➖ **Subtração (`-`)**: Subtrai o segundo número do primeiro.
- ✖️ **Multiplicação (`*`)**: Multiplica dois valores quaisquer.
- ➗ **Divisão (`/`)**: Realiza divisão precisa com prevenção e tratamento de divisão por zero.
- 🔢 **Suporte Numérico Abrangente**: Aceita inteiros, números negativos e números decimais.
- 🌐 **Ponto ou Vírgula**: O usuário pode digitar `3.5` ou `3,5`, pois a aplicação normaliza a pontuação automaticamente.
- 🛡️ **Validação de Entradas**: Qualquer caractere inválido (letras, símbolos aleatórios) é capturado com mensagens claras, sem interromper abruptamente a execução.
- 🔄 **Ciclo Contínuo**: Permite fazer múltiplas operações sequenciais sem precisar reiniciar o script.
- 🚪 **Encerramento Elegante**: Opção amigável de saída (`s/n`).
- 🎨 **Formatação Limpa de Saída**: Números inteiros são exibidos sem sufixo decimal (`5` em vez de `5.0`), e decimais têm precisão equilibrada.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** (versão 3.8 ou superior recomendada).
- **Biblioteca Padrão do Python**: nenhuma dependência ou biblioteca externa (como NumPy, Flask, Tkinter, etc.) é necessária.

---

## 📁 Estrutura do Projeto

O projeto é estritamente minimalista e autocontido:

```text
calculadora-python/
├── calculadora.py   # Código-fonte principal com funções matemáticas e loop interativo
└── README.md        # Documentação completa e respostas do Desafio 1
```

---

## ⚙️ Pré-requisitos

Para executar a aplicação, você só precisa do **Python 3** instalado em sua máquina.

Verifique se o Python está instalado abrindo o terminal (ou Prompt de Comando / PowerShell) e digitando:

```bash
python --version
# ou em ambientes Linux/macOS:
python3 --version
```

Caso ainda não possua o Python instalado, baixe a versão oficial em [python.org](https://www.python.org/).

---

## 🚀 Como Executar

1. **Abra o terminal** na pasta do projeto:
   ```bash
   cd calculadora-python
   ```

2. **Execute o arquivo `calculadora.py`**:
   ```bash
   python calculadora.py
   ```
   *(No Linux ou macOS, utilize `python3 calculadora.py` se necessário).*

3. **Interaja diretamente** com as instruções exibidas na tela.

---

## 💡 Exemplos de Utilização

### Exemplo 1: Adição com decimais (usando vírgula)

```text
================================================
        Calculadora Python Interativa
================================================
Bem-vindo! Realize cálculos matemáticos com facilidade.

----------------------------------------
Digite o primeiro número: 12,5

Operações disponíveis:
  [1] ou [+]  Adição
  [2] ou [-]  Subtração
  [3] ou [*]  Multiplicação
  [4] ou [/]  Divisão

Escolha a operação desejada: +
Digite o segundo número: 7.5

========================================
  Operação realizada: 12.5 + 7.5
  Resultado: 20
========================================

Deseja realizar outro cálculo? (s/n): s
```

### Exemplo 2: Tratamento de divisão por zero

```text
----------------------------------------
Digite o primeiro número: 100

Operações disponíveis:
  [1] ou [+]  Adição
  [2] ou [-]  Subtração
  [3] ou [*]  Multiplicação
  [4] ou [/]  Divisão

Escolha a operação desejada: /
Digite o segundo número: 0

[ERRO MATEMÁTICO]: Não é possível realizar divisão por zero.

Deseja realizar outro cálculo? (s/n): n

================================================
  Obrigado por usar a Calculadora Python! Até logo.
================================================
```

---

## 🧠 Conceitos de Python Aplicados

1. **Modularização em Funções**: Cada responsabilidade possui sua própria função (`adicionar`, `subtrair`, `multiplicar`, `dividir`, `obter_numero`, `obter_operacao`, `formatar_numero`, `perguntar_continuar`, `executar_calculadora`).
2. **Tipagem Estática Opcional (Type Hints)**: Anotações como `(a: float, b: float) -> float` facilitam a leitura do código e a manutenção.
3. **Controle de Fluxo**: Uso de `while True` para repetir solicitações até o recebimento de valores válidos e para manter o programa ativo até a decisão de saída.
4. **Tratamento de Exceções (`try / except`)**: Utilizado em `obter_numero` com `ValueError` para converter com segurança a string recebida em número float, e no cálculo de divisão para tratar divisões proibidas.
5. **Manipulação de Strings**: Método `.replace(",", ".")` para garantir suporte a vírgula e `.strip()` para evitar falhas por espaços em branco extras.
6. **Entrada do Módulo Principal (`if __name__ == "__main__":`)**: Boa prática que garante que a calculadora só será iniciada quando executada diretamente como script.

---

## 🎓 Respostas ao Desafio 1 da Alura

Abaixo encontram-se as respostas detalhadas às 3 questões analíticas solicitadas no desafio:

---

### 1. Quais são os principais componentes do código gerado?

O código da `calculadora.py` foi estruturado de forma modular e limpa, composto pelos seguintes blocos fundamentais:

- **Funções Matemáticas Puras**:
  - `adicionar(a, b)`: Retorna a soma aritmética dos dois parâmetros.
  - `subtrair(a, b)`: Retorna a diferença entre o minuendo e o subtraendo.
  - `multiplicar(a, b)`: Retorna o produto dos dois fatores.
  - `dividir(a, b)`: Realiza a checagem se $b = 0$. Caso seja, dispara uma exceção `ValueError` com mensagem explicativa; caso contrário, devolve o quociente exato.

- **Funções Auxiliares de Validação e Formatação**:
  - `obter_numero(mensagem)`: Conduz o usuário pelo terminal, substituindo vírgulas por pontos e convertendo a string digitada para número decimal (`float`).
  - `obter_operacao()`: Exibe o menu com as quatro operações e mapeia entradas tanto por símbolo (`+`, `-`, `*`, `/`) quanto por índice numérico (`1`, `2`, `3`, `4`).
  - `formatar_numero(valor)`: Avalia se o número é inteiro (usando `.is_integer()`) para exibi-lo sem casas decimais desnecessárias (ex.: `5` em vez de `5.0`), ou remove zeros redundantes ao final de decimais.
  - `perguntar_continuar()`: Lê a decisão do usuário sobre realizar uma nova operação ou finalizar a sessão.

- **Variáveis**:
  - Variáveis locais com nomes semânticos e claros (`num1`, `num2`, `operador`, `resultado`, `entrada_normalizada`, `mapa_opcoes`).

- **Estruturas Condicionais (`if`, `elif`, `else`)**:
  - Utilizadas para rotear a operação matemática escolhida, validar se respostas atendem ao padrão esperado e verificar condições de contorno (como divisor igual a zero).

- **Laços de Repetição (`while`)**:
  - Garantem resiliência: enquanto o usuário digitar algo inválido, o programa não trava, solicitando uma nova digitação.
  - Controlam o ciclo de vida do programa, permitindo efetuar vários cálculos consecutivamente.

- **Tratamento de Exceções (`try / except`)**:
  - Previne falhas fatais no programa quando o usuário digita letras ou caracteres não numéricos em `float()`, além de capturar o `ValueError` de divisão por zero.

---

### 2. Como a aplicação recebe os números e identifica a operação escolhida?

A comunicação com o usuário é realizada através da função nativa `input()`:

1. **Recepção e Tratamento Numérico**:
   - Quando `obter_numero()` é chamada, a função `input(mensagem)` aguarda a digitação do usuário no terminal.
   - A string retornada passa pelo método `.strip()`, que elimina eventuais espaços acidentais nas extremidades.
   - Em seguida, aplica-se `.replace(",", ".")`. No Brasil, o padrão comum de escrita decimal utiliza vírgula (ex.: `4,75`), enquanto a linguagem Python reconhece o ponto (`4.75`). Essa substituição oferece flexibilidade total ao usuário.
   - Dentro de um bloco `try:`, o comando `float(entrada_normalizada)` tenta converter a string em um número real. Se a conversão falhar (por exemplo, se o usuário digitou `"dez"` ou `"abc"`), o fluxo é interceptado pelo bloco `except ValueError:`, que emite um alerta amigável e repete a pergunta através do laço `while True`.

2. **Identificação da Operação**:
   - Na função `obter_operacao()`, é apresentado um menu claro no terminal.
   - Para maximizar a comodidade do usuário, foi definido um dicionário (`mapa_opcoes`) que aceita tanto o símbolo matemático direto (`+`, `-`, `*`, `/`) quanto o número ordinal da opção (`1`, `2`, `3`, `4`).
   - Uma verificação condicional `if escolha in mapa_opcoes:` confirma se a opção é válida e retorna o símbolo canônico correspondente (`+`, `-`, `*` ou `/`).
   - Se o usuário digitar qualquer operador inválido (ex.: `%` ou letras soltas), o programa avisa o erro e permanece no laço até receber uma opção válida.

---

### 3. Como a lógica de programação é utilizada para realizar os cálculos e apresentar os resultados?

O fluxo da aplicação é governado pela função `executar_calculadora()` e segue uma sequência lógica bem delineada:

1. **Fluxo Sequencial de Entrada**:
   - A calculadora solicita sequencialmente o primeiro número (`num1`), a operação desejada (`operador`) e o segundo número (`num2`).

2. **Roteamento e Invocação da Função Adequada**:
   - Uma cadeia de estruturas condicionais `if / elif` inspeciona a variável `operador`:
     ```python
     if operador == "+":
         resultado = adicionar(num1, num2)
     elif operador == "-":
         resultado = subtrair(num1, num2)
     elif operador == "*":
         resultado = multiplicar(num1, num2)
     elif operador == "/":
         resultado = dividir(num1, num2)
     ```
   - Cada bloco chama a respectiva função especializada, passando `num1` e `num2` como argumentos e armazenando o valor retornado na variável `resultado`.

3. **Tratamento de Regras de Negócio e Exceções**:
   - A chamada é envelopada por um bloco `try / except ValueError`. Caso ocorra uma tentativa de divisão por zero, a função `dividir` levanta a exceção com a mensagem `"Não é possível realizar divisão por zero."`, que é capturada e impressa na tela sem quebrar a execução.

4. **Apresentação Clara com `print()`**:
   - Antes de exibir o resultado final, os valores são tratados pela função `formatar_numero()` para garantir uma apresentação elegante:
     - `formatar_numero(num1)`
     - `formatar_numero(num2)`
     - `formatar_numero(resultado)`
   - O comando `print()` exibe uma moldura visual contendo:
     - A expressão matemática completa resolvida (ex.: `Operação realizada: 10 + 5`).
     - A linha de resultado em destaque (ex.: `Resultado: 15`).

5. **Controle de Continuidade ou Encerramento**:
   - Por fim, a função `perguntar_continuar()` verifica se o usuário deseja efetuar um novo cálculo. Se a resposta for afirmativa, o laço `while` repete o ciclo; se for negativa, exibe-se uma mensagem de agradecimento e a execução é finalizada com `break`.

---

*Projeto concluído para fins educacionais no âmbito da **Imersão Engenharia de Software da Alura** com suporte do **Google AI Studio**.*
