# Sistema Multiempresa
## gerenciamento de empresas e funcionários.

    Aplicação desktop desenvolvida em Python com CustomTkinter para gerenciamento de empresas e funcionários.

    O sistema permite cadastrar empresas, associar funcionários a cada empresa e realizar cálculos de INSS, IRRF, FGTS e salário líquido com base no salário informado e na quantidade de dependentes.

# Funcionalidades
## Cadastro de empresas
    Cadastro do nome da empresa.

    Cadastro do CNPJ.

    Máscara automática para o CNPJ no formato 00.000.000/0000-00.

    Validação básica do CNPJ.

    Impedimento de cadastro de empresas com CNPJ duplicado.

    Associação de uma lista de funcionários a cada empresa.

# Cadastro de funcionários
    Cada funcionário pode ser cadastrado com:

    Nome.

    Cargo.

    Salário bruto.

    Quantidade de dependentes.

    Empresa à qual pertence.

    O sistema impede o cadastro de dois funcionários com o mesmo nome dentro da mesma empresa.

# Cálculos trabalhistas
    Ao cadastrar um funcionário, o sistema calcula automaticamente:

    INSS

    IRRF

    FGTS

    Salário líquido

    O cálculo do IRRF considera a base após o desconto do INSS e da dedução por dependentes.

# Consulta de funcionários
    É possível:

    Selecionar uma empresa.

    Visualizar todos os funcionários cadastrados.

    Buscar funcionários pelo nome.

    Buscar funcionários pelo cargo.

    Visualizar salário bruto, INSS, IRRF, FGTS e salário líquido.

    Ordenar os funcionários alfabeticamente pelo nome.

# Fluxo resumido
    Cadastrar Empresa
        ↓
    Selecionar Empresa
        ↓
    Cadastrar Funcionário
        ↓
    Calcular INSS, IRRF e FGTS
        ↓
    Calcular Salário Líquido
        ↓
    Consultar Funcionários
        ↓
    Buscar por Nome ou Cargo

# Interface
    A aplicação possui uma interface gráfica dividida em três abas:

    Aba	Função
    Empresas	Cadastro de empresas e CNPJ
    Cadastro	Cadastro de funcionários
    Funcionários	Consulta e busca de funcionários

    A interface utiliza o tema escuro e o esquema de cores azul disponibilizados pelo CustomTkinter.

# Tecnologias utilizadas

    Python 3.14

    CustomTkinter

    Tkinter

    O projeto utiliza apenas armazenamento em memória. Os dados são mantidos na variável empresas enquanto a aplicação estiver aberta.

# Como instalar e executar

    4. **Instale o CustomTkinter**

    Execute o comando:

    pip install customtkinter

    O Tkinter normalmente já vem incluído na instalação do Python para Windows.

    5. **Execute o sistema**

    Execute o arquivo principal do projeto:

    python sistema-multiempresa

    Caso o arquivo principal tenha outro nome, substitua main.py pelo nome correto do arquivo.

# Requisitos
    Python 3.14 ou superior
    CustomTkinter
    Tkinter
    Windows, Linux ou macOS
    Não é necessário banco de dados
    Não é necessária conexão com a internet para utilizar o sistema após a instalação das dependências

## Possíveis problemas

    Se o comando pip não for reconhecido, tente:

    python -m pip install customtkinter

    Para verificar se o Python está instalado corretamente:

    python --version

    Para verificar a instalação do CustomTkinter:

    pip show customtkinter

# Exemplo de uso
    1. **Cadastrar uma empresa**

    Na aba Empresas, informe:

    Nome da Empresa: Tech Solutions
    CNPJ: 12.345.678/0001-90

    Depois clique em Cadastrar Empresa.

    A empresa será adicionada ao sistema e ficará disponível para cadastro de funcionários. O sistema também impede o cadastro de um CNPJ duplicado.

    2. **Cadastrar um funcionário**

    Na aba Cadastro, selecione a empresa:

    Empresa: Tech Solutions - 12.345.678/0001-90
    Nome: João Silva
    Cargo: Desenvolvedor
    Salário: 3500
    Dependentes: 1

    Depois clique em Cadastrar Funcionário.

    O sistema calcula automaticamente:

    INSS
    IRRF
    FGTS
    Salário Líquido

    O cálculo do salário líquido é realizado descontando o INSS e o IRRF do salário bruto, enquanto o FGTS é calculado separadamente.

    3. **Consultar funcionários**

    Na aba Funcionários, selecione:

    Tech Solutions - 12.345.678/0001-90

    Clique em Mostrar Todos.

    O sistema exibirá informações como:

    1. **João Silva**
    Cargo: Desenvolvedor
    Dependentes: 1

    Salário Bruto: R$ 3.500,00
    INSS: R$ XX,XX
    IRRF: R$ XX,XX
    FGTS: R$ XX,XX
    Salário Líquido: R$ XX,XX

    Os funcionários são organizados em ordem alfabética pelo nome.

    4. **Buscar um funcionário**

    No campo Buscar funcionário, digite:

    João

    Depois clique em Buscar.

    Também é possível pesquisar pelo cargo. Por exemplo:

    Desenvolvedor

    O sistema procura o texto informado tanto no nome quanto no cargo do funcionário.

# Observação sobre os cálculos
    As faixas e valores de INSS, IRRF e dependentes estão fixados diretamente no código-fonte. Portanto, os valores utilizados pelo programa podem precisar ser atualizados conforme mudanças na legislação tributária.

    Este projeto possui finalidade educacional e de demonstração e não deve ser utilizado como única fonte para cálculo oficial de folha de pagamento.

# Autor e contato:
[linkedin] (https://www.linkedin.com/in/vinicius-santos21/)

[github] (https://github.com/viniciusSantos1-gi/viniciusSantos1-gi)


# Licença
    Este projeto não possui uma licença de software especificada atualmente.

    Caso o projeto seja publicado em um repositório, recomenda-se adicionar uma licença, como MIT, de acordo com a finalidade e os direitos que o autor deseja conceder.