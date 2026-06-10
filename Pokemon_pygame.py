from random import randint

# ===================================
# HISTÓRIA
# ===================================

print("=== LIGA POKÉMON DO EDUARDO ===")
print()
print("Eduardo domina a Liga Pokémon.")
print("Para enfrentá-lo você deve derrotar:")
print("- Renan")
print("- Pitombeira")
print("- Israely")
print()
print("Monte sua equipe e torne-se o novo Mestre Pokémon!")
print()

# ===================================
# NOMES DOS POKÉMONS
# ===================================

nomes = [

# FOGO
"Charizard",
"Typhlosion",
"Blaziken",
"Infernape",
"Emboar",
"Delphox",
"Incineroar",
"Cinderace",
"Skeledirge",
"Arcanine",

# ÁGUA
"Blastoise",
"Feraligatr",
"Swampert",
"Empoleon",
"Samurott",
"Greninja",
"Primarina",
"Inteleon",
"Gyarados",
"Milotic",

# PLANTA
"Venusaur",
"Meganium",
"Sceptile",
"Torterra",
"Serperior",
"Chesnaught",
"Decidueye",
"Rillaboom",
"Meowscarada",
"Roserade",

# ELÉTRICO
"Raichu",
"Jolteon",
"Ampharos",
"Luxray",
"Electivire",
"Zebstrika",
"Eelektross",
"Heliolisk",
"Toxtricity",
"Bellibolt",

# TERRA
"Golem",
"Steelix",
"Donphan",
"Flygon",
"Krookodile",
"Excadrill",
"Garchomp",
"Golurk",
"Mudsdale",
"Clodsire",

# VOADOR
"Pidgeot",
"Fearow",
"Noctowl",
"Swellow",
"Staraptor",
"Unfezant",
"Talonflame",
"Toucannon",
"Corviknight",
"Crobat",

# PEDRA
"Onix",
"Rhydon",
"Rhyperior",
"Tyranitar",
"Gigalith",
"Lycanroc",
"Aerodactyl",
"Coalossal",
"Rampardos",
"Bastiodon"

]

# ===================================
# TIPOS
# ===================================

tipos = []

for i in range(70):

    if i < 10:
        tipos.append("Fogo")

    elif i < 20:
        tipos.append("Água")

    elif i < 30:
        tipos.append("Planta")

    elif i < 40:
        tipos.append("Elétrico")

    elif i < 50:
        tipos.append("Terra")

    elif i < 60:
        tipos.append("Voador")

    else:
        tipos.append("Pedra")
        # ===================================
# ATRIBUTOS
# ===================================

hp = []
ataque = []
velocidade = []

for i in range(70):

    if tipos[i] == "Pedra":

        hp.append(randint(380,500))
        ataque.append(randint(90,130))
        velocidade.append(randint(20,70))

    elif tipos[i] == "Voador":

        hp.append(randint(280,400))
        ataque.append(randint(80,120))
        velocidade.append(randint(90,140))

    else:

        hp.append(randint(300,450))
        ataque.append(randint(80,130))
        velocidade.append(randint(40,130))
        # ===================================
# GOLPES
# ===================================

golpes = []

for i in range(70):

    if tipos[i] == "Fogo":

        golpes.append([
            "Lança-Chamas",
            "Roda de Fogo",
            "Explosão de Fogo",
            "Inferno"
        ])

    elif tipos[i] == "Água":

        golpes.append([
            "Surf",
            "Hidro Bomba",
            "Canhão de Água",
            "Tsunami"
        ])

    elif tipos[i] == "Planta":

        golpes.append([
            "Folha Navalha",
            "Raio Solar",
            "Tempestade Verde",
            "Raiz Gigante"
        ])

    elif tipos[i] == "Elétrico":

        golpes.append([
            "Choque do Trovão",
            "Raio",
            "Trovão",
            "Tempestade Elétrica"
        ])

    elif tipos[i] == "Terra":

        golpes.append([
            "Terremoto",
            "Pedregulho",
            "Avalanche",
            "Fúria da Terra"
        ])

    elif tipos[i] == "Voador":

        golpes.append([
            "Ataque Aéreo",
            "Vendaval",
            "Furacão",
            "Asa de Aço"
        ])

    else:

        golpes.append([
            "Pedra Afiada",
            "Deslizamento de Pedra",
            "Impacto Rochoso",
            "Colapso"
        ])
        # ===================================
# DANO DOS GOLPES
# ===================================

danos = []

for i in range(70):

    danos.append([
        40,
        60,
        80,
        100
    ])
    # ===================================
# MOSTRAR POKÉMONS
# ===================================

for i in range(70):

    print(
        i + 1,
        "-",
        nomes[i],
        "|",
        tipos[i],
        "| HP:",
        hp[i],
        "| ATK:",
        ataque[i],
        "| VEL:",
        velocidade[i]
    )
    # ===================================
# ESCOLHER TIME
# ===================================

def montar_time():

    time = []

    print()
    print("ESCOLHA SEUS 6 POKÉMONS")
    print()

    while len(time) < 6:

        escolha = int(input("Pokémon: ")) - 1

        if escolha >= 0 and escolha < 70:

            repetido = False

            for pokemon in time:

                if pokemon == escolha:
                    repetido = True

            if repetido == False:

                time.append(escolha)

                print(
                    nomes[escolha],
                    "foi adicionado!"
                )

    return time

# ===================================
# ESCOLHA INICIAL
# ===================================

time_jogador = montar_time()

# ===================================
# TROCAR TIME ENTRE BATALHAS
# ===================================

def trocar_time():

    global time_jogador

    print()
    print("Deseja trocar seu time?")
    print("1 - Sim")
    print("2 - Não")

    escolha = int(input("Opção: "))

    if escolha == 1:

        time_jogador = montar_time()

# ===================================
# HP DO TIME
# ===================================

def criar_hp_time():

    hp_time = []

    for pokemon in time_jogador:

        hp_time.append(
            hp[pokemon]
        )

    return hp_time

# ===================================
# TIMES DOS CAPANGAS
# ===================================

renan = []
pitombeira = []
israely = []

for i in range(6):

    renan.append(
        randint(0,69)
    )

    pitombeira.append(
        randint(0,69)
    )

    israely.append(
        randint(0,69)
    )

# ===================================
# TIME DO EDUARDO
# ===================================

eduardo = [

    3,   # Infernape
    15,  # Greninja
    27,  # Rillaboom
    34,  # Electivire
    46,  # Garchomp
    63   # Tyranitar

]

# ===================================
# VANTAGENS DE TIPO
# ===================================

def vantagem(tipo1,tipo2):

    if tipo1 == "Fogo" and tipo2 == "Planta":
        return 2

    elif tipo1 == "Planta" and tipo2 == "Água":
        return 2

    elif tipo1 == "Água" and tipo2 == "Fogo":
        return 2

    elif tipo1 == "Elétrico" and tipo2 == "Água":
        return 2

    elif tipo1 == "Terra" and tipo2 == "Elétrico":
        return 2

    elif tipo1 == "Pedra" and tipo2 == "Voador":
        return 2

    elif tipo1 == "Voador" and tipo2 == "Planta":
        return 2

    elif tipo1 == tipo2:
        return 1

    return 0.5

# ===================================
# ESCOLHER POKÉMON VIVO
# ===================================

def escolher_pokemon(hp_time):

    print()

    for i in range(6):

        print(
            i + 1,
            "-",
            nomes[time_jogador[i]],
            "| HP:",
            int(hp_time[i])
        )

    escolha = int(input("Escolha: ")) - 1

    while (
        escolha < 0 or
        escolha > 5 or
        hp_time[escolha] <= 0
    ):

        escolha = int(
            input("Escolha válida: ")
        ) - 1

    return escolha

# ===================================
# CRÍTICO
# ===================================

def critico():

    numero = randint(1,100)

    if numero <= 15:
        return True

    return False

# ===================================
# ACERTO
# ===================================

def acertou():

    numero = randint(1,100)

    if numero <= 90:
        return True

    return False

print()
print("Parte 2A carregada!")
print()
# ===================================
# BATALHA
# ===================================

def batalha(nome_treinador,time_inimigo):

    print()
    print("================================")
    print("BATALHA CONTRA", nome_treinador)
    print("================================")
    print()

    # Cura total para esta batalha

    hp_time = criar_hp_time()

    hp_inimigo = []

    for pokemon in time_inimigo:

        hp_inimigo.append(
            hp[pokemon]
        )

    atual_jogador = escolher_pokemon(
        hp_time
    )

    atual_inimigo = 0

    while True:

        # ============================
        # VERIFICAR DERROTA DO JOGADOR
        # ============================

        vivos_jogador = 0

        for valor in hp_time:

            if valor > 0:
                vivos_jogador += 1

        if vivos_jogador == 0:

            print()
            print("Você perdeu!")
            print()

            return False

        # ============================
        # VERIFICAR DERROTA DO INIMIGO
        # ============================

        vivos_inimigo = 0

        for valor in hp_inimigo:

            if valor > 0:
                vivos_inimigo += 1

        if vivos_inimigo == 0:

            print()
            print("Você venceu!")
            print()

            return True

        # ============================
        # ESCOLHER POKÉMON INIMIGO
        # ============================

        while (
            atual_inimigo < 6 and
            hp_inimigo[atual_inimigo] <= 0
        ):

            atual_inimigo += 1

        if atual_inimigo >= 6:

            return True

        meu = time_jogador[
            atual_jogador
        ]

        rival = time_inimigo[
            atual_inimigo
        ]

        print()
        print("----------------------------")
        print(
            nomes[meu],
            "VS",
            nomes[rival]
        )
        print("----------------------------")

        print(
            "Seu HP:",
            int(
                hp_time[
                    atual_jogador
                ]
            )
        )

        print(
            "HP Inimigo:",
            int(
                hp_inimigo[
                    atual_inimigo
                ]
            )
        )

        print()

        # ============================
        # MENU
        # ============================

        print("1 - Atacar")
        print("2 - Trocar Pokémon")

        opcao = int(
            input("Escolha: ")
        )

        if opcao == 2:

            atual_jogador = (
                escolher_pokemon(
                    hp_time
                )
            )

            continue

        # ============================
        # ESCOLHER GOLPE
        # ============================

        print()

        for i in range(4):

            print(
                i + 1,
                "-",
                golpes[meu][i]
            )

        golpe = int(
            input("Golpe: ")
        )

        while (
            golpe < 1 or
            golpe > 4
        ):

            golpe = int(
                input(
                    "Golpe válido: "
                )
            )

        # ============================
        # JOGADOR MAIS RÁPIDO
        # ============================

        if velocidade[meu] >= velocidade[rival]:

            if acertou():

                dano = (
                    danos[meu][
                        golpe - 1
                    ]
                    + ataque[meu]
                )

                dano = (
                    dano *
                    vantagem(
                        tipos[meu],
                        tipos[rival]
                    )
                )

                if critico():

                    dano = dano * 2

                    print()
                    print("CRÍTICO!")

                hp_inimigo[
                    atual_inimigo
                ] -= dano

                print()

                print(
                    nomes[meu],
                    "usou",
                    golpes[meu][
                        golpe - 1
                    ]
                )

                print(
                    "Dano:",
                    int(dano)
                )

            else:

                print()
                print(
                    nomes[meu],
                    "errou!"
                )

            # inimigo vivo

            if (
                hp_inimigo[
                    atual_inimigo
                ] > 0
            ):

                golpe_inimigo = (
                    randint(0,3)
                )

                if acertou():

                    dano = (
                        danos[rival][
                            golpe_inimigo
                        ]
                        + ataque[rival]
                    )

                    dano = (
                        dano *
                        vantagem(
                            tipos[rival],
                            tipos[meu]
                        )
                    )

                    if critico():

                        dano = dano * 2

                        print()
                        print(
                            "CRÍTICO INIMIGO!"
                        )

                    hp_time[
                        atual_jogador
                    ] -= dano

                    print()

                    print(
                        nomes[rival],
                        "usou",
                        golpes[rival][
                            golpe_inimigo
                        ]
                    )

                    print(
                        "Dano:",
                        int(dano)
                    )

                else:

                    print()

                    print(
                        nomes[rival],
                        "errou!"
                    )

        # ============================
        # INIMIGO MAIS RÁPIDO
        # ============================

        else:

            golpe_inimigo = (
                randint(0,3)
            )

            if acertou():

                dano = (
                    danos[rival][
                        golpe_inimigo
                    ]
                    + ataque[rival]
                )

                dano = (
                    dano *
                    vantagem(
                        tipos[rival],
                        tipos[meu]
                    )
                )

                if critico():

                    dano = dano * 2

                    print()
                    print(
                        "CRÍTICO INIMIGO!"
                    )

                hp_time[
                    atual_jogador
                ] -= dano

                print()

                print(
                    nomes[rival],
                    "usou",
                    golpes[rival][
                        golpe_inimigo
                    ]
                )

                print(
                    "Dano:",
                    int(dano)
                )

            else:

                print()

                print(
                    nomes[rival],
                    "errou!"
                )

            # jogador vivo

            if (
                hp_time[
                    atual_jogador
                ] > 0
            ):

                if acertou():

                    dano = (
                        danos[meu][
                            golpe - 1
                        ]
                        + ataque[meu]
                    )

                    dano = (
                        dano *
                        vantagem(
                            tipos[meu],
                            tipos[rival]
                        )
                    )

                    if critico():

                        dano = dano * 2

                        print()
                        print(
                            "CRÍTICO!"
                        )

                    hp_inimigo[
                        atual_inimigo
                    ] -= dano

                    print()

                    print(
                        nomes[meu],
                        "usou",
                        golpes[meu][
                            golpe - 1
                        ]
                    )

                    print(
                        "Dano:",
                        int(dano)
                    )

                else:

                    print()

                    print(
                        nomes[meu],
                        "errou!"
                    )

        # ============================
        # MOSTRAR HP
        # ============================

        print()

        print(
            nomes[meu],
            "HP:",
            max(
                0,
                int(
                    hp_time[
                        atual_jogador
                    ]
                )
            )
        )

        print(
            nomes[rival],
            "HP:",
            max(
                0,
                int(
                    hp_inimigo[
                        atual_inimigo
                    ]
                )
            )
        )

        # ============================
        # POKÉMON DERROTADO
        # ============================

        if (
            hp_time[
                atual_jogador
            ] <= 0
        ):

            print()
            print(
                nomes[meu],
                "foi derrotado!"
            )

            vivos = 0

            for valor in hp_time:

                if valor > 0:
                    vivos += 1

            if vivos > 0:

                print()
                print(
                    "Escolha outro Pokémon!"
                )

                atual_jogador = (
                    escolher_pokemon(
                        hp_time
                    )
                )

        if (
            hp_inimigo[
                atual_inimigo
            ] <= 0
        ):

            print()
            print(
                nomes[rival],
                "foi derrotado!"
            )
            # ===================================
# CAMPANHA
# ===================================

print()
print("================================")
print("INÍCIO DA SUA JORNADA")
print("================================")
print()

# -------------------------------
# RENAN
# -------------------------------

if batalha("Renan", renan):

    print()
    print("Você derrotou Renan!")
    print()

    trocar_time()

    # ---------------------------
    # PITOMBEIRA
    # ---------------------------

    if batalha("Pitombeira", pitombeira):

        print()
        print("Você derrotou Pitombeira!")
        print()

        trocar_time()

        # -----------------------
        # ISRAELY
        # -----------------------

        if batalha("Israely", israely):

            print()
            print("Você derrotou Israely!")
            print()

            trocar_time()

            print()
            print("================================")
            print("VOCÊ CHEGOU AO BOSS FINAL!")
            print("================================")
            print()

            # -------------------
            # EDUARDO
            # -------------------

            if batalha("Eduardo", eduardo):

                print()
                print("================================")
                print("PARABÉNS!")
                print("VOCÊ DERROTOU EDUARDO!")
                print("VOCÊ É O NOVO")
                print("MESTRE POKÉMON!")
                print("================================")

            else:

                print()
                print("================================")
                print("Eduardo venceu...")
                print("A Liga continua sob seu controle.")
                print("================================")

        else:

            print()
            print("================================")
            print("Israely venceu a batalha!")
            print("Fim de jogo.")
            print("================================")

    else:

        print()
        print("================================")
        print("Pitombeira venceu a batalha!")
        print("Fim de jogo.")
        print("================================")

else:

    print()
    print("================================")
    print("Renan venceu a batalha!")
    print("Fim de jogo.")
    print("================================")
    
