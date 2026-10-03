id="u7k2qp"
import customtkinter as ctk

# =====================================
# CONFIGURAÇÕES
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# BANCO DE DADOS
# =====================================

empresas = []

# =====================================
# CÁLCULO INSS
# =====================================

def calcular_inss(salario):

    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14)
    ]

    inss = 0
    limite_anterior = 0

    for limite, aliquota in faixas:

        if salario > limite:

            inss += (
                limite - limite_anterior
            ) * aliquota

        else:

            inss += (
                salario - limite_anterior
            ) * aliquota

            return inss

        limite_anterior = limite

    return 908.86


# =====================================
# CÁLCULO IRRF
# =====================================

def calcular_irrf(base):

    if base <= 2259.20:
        return 0

    elif base <= 2826.65:
        return (base * 0.075) - 169.44

    elif base <= 3751.05:
        return (base * 0.15) - 381.44

    elif base <= 4664.68:
        return (base * 0.225) - 662.77

    else:
        return (base * 0.275) - 896.00


# =====================================
# MÁSCARA CNPJ
# =====================================

def formatar_cnpj(event=None):

    texto = campo_cnpj.get()

    numeros = ""

    for caractere in texto:

        if caractere.isdigit():

            numeros += caractere

    numeros = numeros[:14]

    cnpj = ""

    if len(numeros) >= 1:
        cnpj += numeros[:2]

    if len(numeros) >= 3:
        cnpj += "." + numeros[2:5]

    if len(numeros) >= 6:
        cnpj += "." + numeros[5:8]

    if len(numeros) >= 9:
        cnpj += "/" + numeros[8:12]

    if len(numeros) >= 13:
        cnpj += "-" + numeros[12:14]

    campo_cnpj.delete(0, "end")
    campo_cnpj.insert(0, cnpj)


# =====================================
# CADASTRAR EMPRESA
# =====================================

def cadastrar_empresa():

    nome_empresa = (
        campo_empresa.get().strip()
    )

    cnpj = (
        campo_cnpj.get().strip()
    )

    if not nome_empresa or not cnpj:

        mensagem_empresa.configure(
            text="Preencha todos os campos.",
            text_color="red"
        )

        return

    # VALIDAR CNPJ

    if len(cnpj) != 18:

        mensagem_empresa.configure(
            text="CNPJ inválido.",
            text_color="red"
        )

        return

    # VERIFICAR DUPLICIDADE

    for empresa in empresas:

        if empresa["cnpj"] == cnpj:

            mensagem_empresa.configure(
                text="CNPJ já cadastrado.",
                text_color="red"
            )

            return

    empresas.append({

        "empresa": nome_empresa,
        "cnpj": cnpj,
        "funcionarios": []

    })

    atualizar_empresas()

    mensagem_empresa.configure(
        text="Empresa cadastrada.",
        text_color="green"
    )

    campo_empresa.delete(0, "end")
    campo_cnpj.delete(0, "end")


# =====================================
# ATUALIZAR COMBOBOX
# =====================================

def atualizar_empresas():

    lista = []

    for empresa in empresas:

        texto = (
            f"{empresa['empresa']} "
            f"- {empresa['cnpj']}"
        )

        lista.append(texto)

    combo_empresa.configure(values=lista)

    combo_busca_empresa.configure(
        values=lista
    )


# =====================================
# OBTER EMPRESA
# =====================================

def obter_empresa(texto):

    for empresa in empresas:

        nome = (
            f"{empresa['empresa']} "
            f"- {empresa['cnpj']}"
        )

        if nome == texto:

            return empresa

    return None


# =====================================
# CADASTRAR FUNCIONÁRIO
# =====================================

def cadastrar_funcionario():

    empresa_texto = combo_empresa.get()

    empresa = obter_empresa(
        empresa_texto
    )

    if empresa is None:

        resultado.configure(
            text="Selecione uma empresa.",
            text_color="red"
        )

        return

    nome = campo_nome.get().strip()

    cargo = campo_cargo.get().strip()

    try:

        salario = float(
            campo_salario.get().replace(",", ".")
        )

        dependentes = int(
            campo_dependentes.get()
        )

    except ValueError:

        resultado.configure(
            text="Dados inválidos.",
            text_color="red"
        )

        return

    if not nome or not cargo:

        resultado.configure(
            text="Preencha todos os campos.",
            text_color="red"
        )

        return

    # DUPLICIDADE

    for funcionario in empresa["funcionarios"]:

        if (
            funcionario["nome"].lower()
            ==
            nome.lower()
        ):

            resultado.configure(
                text="Funcionário já existe.",
                text_color="red"
            )

            return

    # CÁLCULOS

    inss = calcular_inss(salario)

    base_irrf = (
        salario
        - inss
        - (dependentes * 189.59)
    )

    irrf = calcular_irrf(base_irrf)

    if irrf < 0:
        irrf = 0

    salario_liquido = (
        salario - inss - irrf
    )

    fgts = salario * 0.08

    # SALVAR

    empresa["funcionarios"].append({

        "nome": nome,
        "cargo": cargo,
        "dependentes": dependentes,
        "bruto": salario,
        "inss": inss,
        "irrf": irrf,
        "fgts": fgts,
        "liquido": salario_liquido

    })

    resultado.configure(
        text=
        f"Funcionário cadastrado.\n\n"
        f"Salário Líquido: "
        f"R$ {salario_liquido:,.2f}",
        text_color="green"
    )

    limpar_campos()

    atualizar_lista()


# =====================================
# MOSTRAR FUNCIONÁRIOS
# =====================================

def atualizar_lista():

    lista_funcionarios.configure(
        state="normal"
    )

    lista_funcionarios.delete(
        "1.0",
        "end"
    )

    empresa_texto = (
        combo_busca_empresa.get()
    )

    empresa = obter_empresa(
        empresa_texto
    )

    if empresa is None:

        lista_funcionarios.insert(
            "end",
            "Selecione uma empresa."
        )

        lista_funcionarios.configure(
            state="disabled"
        )

        return

    funcionarios = sorted(

        empresa["funcionarios"],

        key=lambda f:
        f["nome"].lower()

    )

    if not funcionarios:

        lista_funcionarios.insert(
            "end",
            "Nenhum funcionário."
        )

    else:

        for i, funcionario in enumerate(
            funcionarios,
            start=1
        ):

            lista_funcionarios.insert(
                "end",

                f"{i}. "
                f"{funcionario['nome']}\n"

                f"Cargo: "
                f"{funcionario['cargo']}\n"

                f"Dependentes: "
                f"{funcionario['dependentes']}\n\n"

                f"Salário Bruto: "
                f"R$ {funcionario['bruto']:,.2f}\n"

                f"INSS: "
                f"R$ {funcionario['inss']:,.2f}\n"

                f"IRRF: "
                f"R$ {funcionario['irrf']:,.2f}\n"

                f"FGTS: "
                f"R$ {funcionario['fgts']:,.2f}\n"

                f"Salário Líquido: "
                f"R$ {funcionario['liquido']:,.2f}\n"

                f"{'-'*45}\n"
            )

    lista_funcionarios.configure(
        state="disabled"
    )


# =====================================
# BUSCAR FUNCIONÁRIO
# =====================================

def buscar_funcionario():

    busca = (
        campo_busca.get()
        .strip()
        .lower()
    )

    empresa_texto = (
        combo_busca_empresa.get()
    )

    empresa = obter_empresa(
        empresa_texto
    )

    lista_funcionarios.configure(
        state="normal"
    )

    lista_funcionarios.delete(
        "1.0",
        "end"
    )

    if empresa is None:

        lista_funcionarios.insert(
            "end",
            "Selecione uma empresa."
        )

        lista_funcionarios.configure(
            state="disabled"
        )

        return

    encontrados = []

    for funcionario in empresa["funcionarios"]:

        if (
            busca in funcionario["nome"].lower()
            or
            busca in funcionario["cargo"].lower()
        ):

            encontrados.append(funcionario)

    encontrados = sorted(

        encontrados,

        key=lambda f:
        f["nome"].lower()

    )

    if not encontrados:

        lista_funcionarios.insert(
            "end",
            "Nenhum encontrado."
        )

    else:

        for i, funcionario in enumerate(
            encontrados,
            start=1
        ):

            lista_funcionarios.insert(
                "end",

                f"{i}. "
                f"{funcionario['nome']}\n"

                f"Cargo: "
                f"{funcionario['cargo']}\n"

                f"Dependentes: "
                f"{funcionario['dependentes']}\n\n"

                f"Salário Bruto: "
                f"R$ {funcionario['bruto']:,.2f}\n"

                f"INSS: "
                f"R$ {funcionario['inss']:,.2f}\n"

                f"IRRF: "
                f"R$ {funcionario['irrf']:,.2f}\n"

                f"FGTS: "
                f"R$ {funcionario['fgts']:,.2f}\n"

                f"Salário Líquido: "
                f"R$ {funcionario['liquido']:,.2f}\n"

                f"{'-'*45}\n"
            )

    lista_funcionarios.configure(
        state="disabled"
    )


# =====================================
# LIMPAR CAMPOS
# =====================================

def limpar_campos():

    campo_nome.delete(0, "end")
    campo_cargo.delete(0, "end")
    campo_salario.delete(0, "end")
    campo_dependentes.delete(0, "end")


# =====================================
# JANELA
# =====================================

app = ctk.CTk()

app.title(
    "Sistema Multiempresa"
)

largura = 900
altura = 850

x = (
    app.winfo_screenwidth() // 2
) - (largura // 2)

y = (
    app.winfo_screenheight() // 2
) - (altura // 2)

app.geometry(
    f"{largura}x{altura}+{x}+{y}"
)

fonte = ("Arial", 16)

# =====================================
# ABAS
# =====================================

abas = ctk.CTkTabview(app)

abas.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

aba_empresa = abas.add("Empresas")
aba_cadastro = abas.add("Cadastro")
aba_lista = abas.add("Funcionários")

# =====================================
# ABA EMPRESAS
# =====================================

ctk.CTkLabel(
    aba_empresa,
    text="Nome da Empresa",
    font=fonte
).pack(pady=5)

campo_empresa = ctk.CTkEntry(
    aba_empresa,
    width=350,
    font=fonte
)

campo_empresa.pack(pady=5)

ctk.CTkLabel(
    aba_empresa,
    text="CNPJ",
    font=fonte
).pack(pady=5)

campo_cnpj = ctk.CTkEntry(
    aba_empresa,
    width=350,
    font=fonte
)

campo_cnpj.pack(pady=5)

# MÁSCARA CNPJ

campo_cnpj.bind(
    "<KeyRelease>",
    formatar_cnpj
)

ctk.CTkButton(
    aba_empresa,
    text="Cadastrar Empresa",
    command=cadastrar_empresa,
    width=250,
    font=fonte
).pack(pady=15)

mensagem_empresa = ctk.CTkLabel(
    aba_empresa,
    text="",
    font=("Arial", 15)
)

mensagem_empresa.pack(pady=5)

# =====================================
# ABA CADASTRO
# =====================================

ctk.CTkLabel(
    aba_cadastro,
    text="Empresa",
    font=fonte
).pack(pady=5)

combo_empresa = ctk.CTkComboBox(
    aba_cadastro,
    values=[],
    width=450,
    font=fonte
)

combo_empresa.pack(pady=5)

ctk.CTkLabel(
    aba_cadastro,
    text="Nome",
    font=fonte
).pack(pady=5)

campo_nome = ctk.CTkEntry(
    aba_cadastro,
    width=350,
    font=fonte
)

campo_nome.pack(pady=5)

ctk.CTkLabel(
    aba_cadastro,
    text="Cargo",
    font=fonte
).pack(pady=5)

campo_cargo = ctk.CTkEntry(
    aba_cadastro,
    width=350,
    font=fonte
)

campo_cargo.pack(pady=5)

ctk.CTkLabel(
    aba_cadastro,
    text="Salário",
    font=fonte
).pack(pady=5)

campo_salario = ctk.CTkEntry(
    aba_cadastro,
    width=350,
    font=fonte
)

campo_salario.pack(pady=5)

ctk.CTkLabel(
    aba_cadastro,
    text="Dependentes",
    font=fonte
).pack(pady=5)

campo_dependentes = ctk.CTkEntry(
    aba_cadastro,
    width=350,
    font=fonte
)

campo_dependentes.pack(pady=5)

ctk.CTkButton(
    aba_cadastro,
    text="Cadastrar Funcionário",
    command=cadastrar_funcionario,
    width=250,
    font=fonte
).pack(pady=15)

resultado = ctk.CTkLabel(
    aba_cadastro,
    text="",
    font=("Arial", 15)
)

resultado.pack(pady=5)

# =====================================
# ABA FUNCIONÁRIOS
# =====================================

ctk.CTkLabel(
    aba_lista,
    text="Selecionar Empresa",
    font=fonte
).pack(pady=5)

combo_busca_empresa = ctk.CTkComboBox(
    aba_lista,
    values=[],
    width=450,
    font=fonte,
    command=lambda escolha:
    atualizar_lista()
)

combo_busca_empresa.pack(pady=5)

# BUSCA

ctk.CTkLabel(
    aba_lista,
    text="Buscar funcionário",
    font=fonte
).pack(pady=5)

campo_busca = ctk.CTkEntry(
    aba_lista,
    width=350,
    font=fonte
)

campo_busca.pack(pady=5)

ctk.CTkButton(
    aba_lista,
    text="Buscar",
    command=buscar_funcionario,
    width=220,
    font=fonte
).pack(pady=5)

ctk.CTkButton(
    aba_lista,
    text="Mostrar Todos",
    command=atualizar_lista,
    width=220,
    font=fonte
).pack(pady=5)

# LISTA

lista_funcionarios = ctk.CTkTextbox(
    aba_lista,
    width=760,
    height=450,
    font=("Arial", 14)
)

lista_funcionarios.pack(pady=15)

lista_funcionarios.configure(
    state="disabled"
)

# =====================================
# EXECUTAR
# =====================================

app.mainloop()





