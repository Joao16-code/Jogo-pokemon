import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da Janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pokémon Battle: Ultimate Edition 2026")

# Cores (RGB)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (50, 200, 50)
VERDE_ESCURO = (34, 139, 34)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (240, 240, 50)
CINZA = (200, 200, 200)
CINZA_ESCURO = (100, 100, 100)
ROXO = (148, 0, 211)
ROSA = (255, 105, 180)
MARROM = (139, 69, 19)

# --- BANCO DE DADOS ---
nomes = [
    "Charizard", "Blastoise", "Venusaur", "Raichu", "Gengar",
    "Alakazam", "Golem", "Pidgeot", "Dragonite", "Snorlax",
    "Typhlosion", "Feraligatr", "Meganium", "Ampharos", "Tyranitar",
    "Blaziken", "Swampert", "Sceptile", "Gardevoir", "Salamence",
    "Lapras", "Metagross", "Lucario", "Garchomp", "Togekiss",
    "Scizor", "Incineroar", "Greninja", "Decidueye", "Zeraora"
]
tipos = [
    "Fogo", "Água", "Planta", "Elétrico", "Fantasma",
    "Psíquico", "Terra", "Voador", "Dragão", "Normal",
    "Fogo", "Água", "Planta", "Elétrico", "Terra",
    "Fogo", "Água", "Planta", "Psíquico", "Dragão",
    "Água", "Aço", "Aço", "Dragão", "Voador",
    "Inseto", "Fogo", "Água", "Planta", "Elétrico"
]
vida_maxima = [
    180, 200, 190, 160, 150,
    140, 210, 165, 220, 250,
    175, 195, 192, 180, 215,
    185, 205, 170, 155, 210,
    230, 200, 165, 215, 180,
    165, 200, 155, 168, 160
]
velocidade = [
    100, 78, 80, 110, 110,
    120, 45, 101, 80, 30,
    100, 78, 80, 55, 61,
    80, 60, 120, 80, 100,
    60, 70, 90, 102, 80,
    65, 60, 122, 70, 143
]
cores = [
    VERMELHO, AZUL, VERDE, AMARELO, ROXO,
    ROSA, MARROM, CINZA, ROXO, CINZA,
    VERMELHO, AZUL, VERDE, AMARELO, MARROM,
    VERMELHO, AZUL, VERDE, ROSA, ROXO,
    AZUL, CINZA, AZUL, ROXO, BRANCO,
    VERMELHO, VERMELHO, AZUL, VERDE, AMARELO
]

ataques_nome = [
    ["Lança-Chamas", "Asa de Aço", "Giro de Fogo", "Giga Impacto"],
    ["Hidroclister", "Quebra-Crânio", "Raio de Gelo", "Surfar"],
    ["Raio Solar", "Chicote de Cipó", "Bomba de Sementes", "Giga Dreno"],
    ["Trovão", "Investida Trovão", "Onda de Choque", "Cauda de Ferro"],
    ["Bola Sombria", "Pulso Sombrio", "Bomba de Lodo", "Giga Dreno"],
    ["Psíquico", "Cortina de Luz", "Choque Psíquico", "Soco Focalizado"],
    ["Terremoto", "Lança-Rochas", "Rolamento", "Pancada Forte"],
    ["Ataque de Asa", "Furacão", "Ataque Rápido", "Ventania"],
    ["Fúria Dragão", "Hiper Raio", "Garra Dragão", "Soco de Fogo"],
    ["Pancada Corporal", "Terremoto", "Descansar", "Hiper Voz"],
    ["Roda de Fogo", "Explosão", "Lança-Chamas", "Ataque Rápido"],
    ["Bomba d'Água", "Mordida", "Garra de Metal", "Surfar"],
    ["Folha Navalha", "Pó de Sono", "Semente Sanguessuga", "Pancada"],
    ["Soco Focalizado", "Choque do T.", "Raio do Trovão", "Poder Oculto"],
    ["Desabamento", "Trituração", "Terremoto", "Gume de Pedra"],
    ["Chute Flamejante", "Gancho", "Brasas", "Chute Duplo"],
    ["Bomba de Lama", "Braço Martelo", "Jato d'Água", "Terremoto"],
    ["Lâmina de Folha", "Giga Dreno", "Ataque Rápido", "Pulso Sombrio"],
    ["Clarão Psíquico", "Sombra Not.", "Força Lunar", "Bola Sombria"],
    ["Garra do Dragão", "Lança-Chamas", "Asa de Aço", "Mordida"],
    ["Raio de Gelo", "Surfar", "Hidromba", "Pancada Corporal"],
    ["Punho Meteoro", "Terremoto", "Cabeçada de Ferro", "Psíquico"],
    ["Esfera de Aura", "Pulso Sombrio", "Velocidade Extrema", "Close C."],
    ["Fúria do Dragão", "Terremoto", "Gume de Pedra", "Triturar"],
    ["Clarão de Luz", "Ar do Jogo", "Velocidade Extrema", "Esfera Aura"],
    ["Tesoura X", "Cabeçada de Ferro", "Ataque Rápido", "Cortador F."],
    ["Chicote de Fogo", "Triturar", "Soco Sombrio", "Superpoder"],
    ["Shuriken de Água", "Pulso Sombrio", "Corte Noturno", "Asa de Aço"],
    ["Flecha Sombria", "Lâmina de Folha", "Ataque de Asa", "Pancada"],
    ["Punho de Plasma", "Raio Trovão", "Close Combat", "Ataque Rápido"]
]

ataques_dano = [
    [40, 25, 30, 45], [38, 28, 35, 36], [42, 22, 28, 30], [45, 20, 25, 28], [41, 24, 32, 28],
    [46, 15, 35, 30], [43, 23, 26, 35], [32, 40, 20, 25], [42, 50, 38, 28], [35, 40, 10, 32],
    [33, 48, 38, 20], [39, 26, 24, 35], [30, 15, 20, 25], [38, 22, 40, 24], [36, 34, 40, 42],
    [41, 32, 20, 26], [34, 38, 25, 40], [42, 28, 20, 32], [43, 25, 38, 35], [40, 38, 26, 24],
    [38, 34, 44, 32], [44, 38, 36, 35], [40, 30, 45, 46], [38, 42, 36, 34], [35, 38, 40, 36],
    [40, 38, 20, 25], [38, 32, 28, 44], [35, 34, 36, 24], [42, 38, 26, 22], [45, 38, 43, 20]
]

fonte_grande = pygame.font.SysFont("arial", 26, bold=True)
fonte_media = pygame.font.SysFont("arial", 15, bold=True)
fonte_pequena = pygame.font.SysFont("arial", 12, bold=True)

# --- ESTADOS DO JOGO ---
estado_jogo = "MENU"

time_jogador = []         
pokemon_atual_jog = 0     
time_adversario = []      
pokemon_atual_adv = 0     
vidas_jogador = []
vidas_adversario = []

texto1 = ""
texto2 = ""

etapa_turno = 0 
ataque_escolhido_jog = -1
ataque_escolhido_adv = -1
primeiro_a_atacar = "Jogador"

def calcular_multiplicador(tipo_ataque, tipo_defensor):
    if tipo_ataque == "Fogo" and tipo_defensor == "Planta": return 2.0
    if tipo_ataque == "Planta" and tipo_defensor == "Água": return 2.0
    if tipo_ataque == "Água" and tipo_defensor == "Fogo": return 2.0
    if tipo_ataque == "Elétrico" and tipo_defensor == "Água": return 2.0
    if tipo_ataque == "Terra" and tipo_defensor == "Elétrico": return 2.0
    if tipo_ataque == "Terra" and tipo_defensor == "Fogo": return 2.0
    if tipo_ataque == "Psíquico" and tipo_defensor == "Fantasma": return 2.0
    if tipo_ataque == "Fantasma" and tipo_defensor == "Psíquico": return 2.0
    if tipo_ataque == "Dragão" and tipo_defensor == "Dragão": return 2.0
    
    if tipo_ataque == "Planta" and tipo_defensor == "Fogo": return 0.5
    if tipo_ataque == "Água" and tipo_defensor == "Planta": return 0.5
    if tipo_ataque == "Fogo" and tipo_defensor == "Água": return 0.5
    if tipo_ataque == "Elétrico" and tipo_defensor == "Planta": return 0.5
    if tipo_ataque == "Elétrico" and tipo_defensor == "Terra": return 0.0
    return 1.0

# Loop Principal
rodando = True
while rodando:
    clicou = False
    pos_clique = (0, 0)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            clicou = True
            pos_clique = evento.pos

    tela.fill(BRANCO)

    # ==================== INTERFACE: MENU INICIAL ====================
    if estado_jogo == "MENU":
        txt_titulo = fonte_grande.render("POKÉMON BATTLE SIMULATOR", True, PRETO)
        tela.blit(txt_titulo, (LARGURA // 2 - txt_titulo.get_width() // 2, 180))
        
        rect_jogar = pygame.draw.rect(tela, VERDE, (300, 300, 200, 60))
        pygame.draw.rect(tela, PRETO, (300, 300, 200, 60), 3)
        txt_jogar = fonte_grande.render("JOGAR", True, PRETO)
        tela.blit(txt_jogar, (355, 313))
        
        if clicou and rect_jogar.collidepoint(pos_clique):
            time_jogador = []
            time_adversario = []
            vidas_jogador = []
            vidas_adversario = []
            estado_jogo = "SELECAO"

    # ==================== TELA DE SELEÇÃO ====================
    elif estado_jogo == "SELECAO":
        txt = fonte_grande.render(f"Escolha seu Time ({len(time_jogador)}/6)", True, PRETO)
        tela.blit(txt, (LARGURA // 2 - txt.get_width() // 2, 10))
        
        for i in range(len(nomes)):
            coluna = i % 6
            linha = i // 6
            
            x = 25 + (coluna * 128)
            y = 50 + (linha * 110)
            
            pygame.draw.rect(tela, cores[i], (x, y, 115, 85))
            pygame.draw.rect(tela, PRETO, (x, y, 115, 85), 2)
            
            if i in time_jogador:
                pygame.draw.rect(tela, CINZA_ESCURO, (x, y, 115, 85), 4)
            
            lbl_nome = fonte_media.render(nomes[i], True, PRETO)
            lbl_tipo = fonte_pequena.render(f"[{tipos[i]}]", True, PRETO)
            
            tela.blit(lbl_nome, (x + 5, y + 20))
            tela.blit(lbl_tipo, (x + 5, y + 45))
            
            if clicou and x <= pos_clique[0] <= x + 115 and y <= pos_clique[1] <= y + 85:
                if i not in time_jogador and len(time_jogador) < 6:
                    time_jogador.append(i)
                    vidas_jogador.append(vida_maxima[i])
                    
                    if len(time_jogador) == 6:
                        while len(time_adversario) < 6:
                            sorteado = random.randint(0, len(nomes) - 1)
                            if sorteado not in time_adversario:
                                time_adversario.append(sorteado)
                                vidas_adversario.append(vida_maxima[sorteado])
                                
                        pokemon_atual_jog = 0
                        pokemon_atual_adv = 0
                        texto1 = f"Seu {nomes[time_jogador[0]]} entrou!"
                        texto2 = f"O Rival enviou {nomes[time_adversario[0]]}! Escolha um ataque."
                        estado_jogo = "BATALHA"
                        etapa_turno = 0

    # ==================== TELA DE BATALHA ====================
    elif estado_jogo in ["BATALHA", "RESOLUCAO_TURNOS"]:
        idx_jog = time_jogador[pokemon_atual_jog]
        idx_adv = time_adversario[pokemon_atual_adv]
        
        pygame.draw.rect(tela, (135, 206, 235), (0, 0, LARGURA, 320))
        pygame.draw.rect(tela, VERDE_ESCURO, (0, 320, LARGURA, 280))
        pygame.draw.ellipse(tela, CINZA, (100, 280, 220, 60))
        pygame.draw.ellipse(tela, CINZA, (500, 190, 220, 60))
        
        # Desenho Aliado
        pygame.draw.circle(tela, cores[idx_jog], (210, 250), 55)
        tela.blit(fonte_grande.render(nomes[idx_jog], True, PRETO), (100, 160))
        pygame.draw.rect(tela, CINZA_ESCURO, (100, 195, 160, 15))
        pct_vida_jog = vidas_jogador[pokemon_atual_jog] / vida_maxima[idx_jog]
        pygame.draw.rect(tela, VERDE, (100, 195, int(pct_vida_jog * 160), 15))
        
        # Desenho Inimigo
        pygame.draw.circle(tela, cores[idx_adv], (610, 160), 45)
        tela.blit(fonte_grande.render(nomes[idx_adv], True, PRETO), (520, 65))
        pygame.draw.rect(tela, CINZA_ESCURO, (520, 100, 160, 15))
        pct_vida_adv = vidas_adversario[pokemon_atual_adv] / vida_maxima[idx_adv]
        pygame.draw.rect(tela, VERDE, (520, 100, int(pct_vida_adv * 160), 15))

        # Painel inferior
        pygame.draw.rect(tela, PRETO, (20, 370, 760, 210))
        pygame.draw.rect(tela, BRANCO, (30, 380, 740, 190))
        tela.blit(fonte_grande.render(texto1, True, PRETO), (50, 395))
        tela.blit(fonte_grande.render(texto2, True, PRETO), (50, 425))

        # --- SE OS DOIS ESTÃO VIVOS, O COMBATE ACONTECE NORMALMENTE ---
        if vidas_jogador[pokemon_atual_jog] > 0 and vidas_adversario[pokemon_atual_adv] > 0:
            if estado_jogo == "BATALHA":
                rects_atq = []
                for a in range(4):
                    bx = 50 + (a % 2 * 230)
                    by = 465 + (a // 2 * 50)
                    r = pygame.draw.rect(tela, CINZA, (bx, by, 210, 42))
                    pygame.draw.rect(tela, PRETO, (bx, by, 210, 42), 2)
                    tela.blit(fonte_media.render(ataques_nome[idx_jog][a], True, PRETO), (bx + 10, by + 12))
                    rects_atq.append(r)
                
                # Botão de Trocar Pokémon funcional
                rect_bt_troca = pygame.draw.rect(tela, AMARELO, (520, 465, 230, 92))
                pygame.draw.rect(tela, PRETO, (520, 465, 230, 92), 2)
                tela.blit(fonte_grande.render("Trocar Pokémon", True, PRETO), (545, 500))
                
                if clicou:
                    if rect_bt_troca.collidepoint(pos_clique):
                        estado_jogo = "TROCA"
                    else:
                        for a in range(4):
                            if rects_atq[a].collidepoint(pos_clique):
                                ataque_escolhido_jog = a
                                ataque_escolhido_adv = random.randint(0, 3)
                                
                                if velocidade[idx_jog] >= velocidade[idx_adv]:
                                    primeiro_a_atacar = "Jogador"
                                    texto1 = f"Seu {nomes[idx_jog]} agiu primeiro!"
                                else:
                                    primeiro_a_atacar = "Adversario"
                                    texto1 = f"{nomes[idx_adv]} rival agiu primeiro!"
                                
                                texto2 = "Clique no botão abaixo para prosseguir a rodada."
                                estado_jogo = "RESOLUCAO_TURNOS"
                                etapa_turno = 1

            elif estado_jogo == "RESOLUCAO_TURNOS":
                rect_avancar = pygame.draw.rect(tela, VERMELHO, (250, 500, 300, 50))
                tela.blit(fonte_grande.render("Avançar Combate", True, BRANCO), (305, 510))
                
                if clicou and rect_avancar.collidepoint(pos_clique):
                    if etapa_turno == 1:
                        if primeiro_a_atacar == "Jogador":
                            atq = ataque_escolhido_jog
                            dano_base = ataques_dano[idx_jog][atq]
                            mult = calcular_multiplicador(tipos[idx_jog], tipos[idx_adv])
                            dano_final = int((dano_base + random.randint(-4, 4)) * mult)
                            vidas_adversario[pokemon_atual_adv] -= dano_final
                            if vidas_adversario[pokemon_atual_adv] < 0: vidas_adversario[pokemon_atual_adv] = 0
                            texto1 = f"Seu {nomes[idx_jog]} usou {ataques_nome[idx_jog][atq]}!"
                            texto2 = f"Causou {dano_final} de dano no adversário."
                        else:
                            atq = ataque_escolhido_adv
                            dano_base = ataques_dano[idx_adv][atq]
                            mult = calcular_multiplicador(tipos[idx_adv], tipos[idx_jog])
                            dano_final = int((dano_base + random.randint(-4, 4)) * mult)
                            vidas_jogador[pokemon_atual_jog] -= dano_final
                            if vidas_jogador[pokemon_atual_jog] < 0: vidas_jogador[pokemon_atual_jog] = 0
                            texto1 = f"{nomes[idx_adv]} rival usou {ataques_nome[idx_adv][atq]}!"
                            texto2 = f"Causou {dano_final} de dano em você."
                        etapa_turno = 2
                        
                    elif etapa_turno == 2:
                        if vidas_jogador[pokemon_atual_jog] > 0 and vidas_adversario[pokemon_atual_adv] > 0:
                            if primeiro_a_atacar == "Adversario":
                                atq = ataque_escolhido_jog
                                dano_base = ataques_dano[idx_jog][atq]
                                mult = calcular_multiplicador(tipos[idx_jog], tipos[idx_adv])
                                dano_final = int((dano_base + random.randint(-4, 4)) * mult)
                                vidas_adversario[pokemon_atual_adv] -= dano_final
                                if vidas_adversario[pokemon_atual_adv] < 0: vidas_adversario[pokemon_atual_adv] = 0
                                texto1 = f"Seu {nomes[idx_jog]} resistiu e usou {ataques_nome[idx_jog][atq]}!"
                                texto2 = f"Causou {dano_final} de dano no adversário."
                            else:
                                atq = ataque_escolhido_adv
                                dano_base = ataques_dano[idx_adv][atq]
                                mult = calcular_multiplicador(tipos[idx_adv], tipos[idx_jog])
                                dano_final = int((dano_base + random.randint(-4, 4)) * mult)
                                vidas_jogador[pokemon_atual_jog] -= dano_final
                                if vidas_jogador[pokemon_atual_jog] < 0: vidas_jogador[pokemon_atual_jog] = 0
                                texto1 = f"{nomes[idx_adv]} rival resistiu e usou {ataques_nome[idx_adv][atq]}!"
                                texto2 = f"Causou {dano_final} de dano em você."
                            etapa_turno = 3
                        else:
                            texto1 = "O Pokémon mais lento foi nocauteado antes!"
                            texto2 = "Ele não pôde contra-atacar."
                            etapa_turno = 3
                            
                    elif etapa_turno == 3:
                        if vidas_adversario[pokemon_atual_adv] <= 0:
                            if pokemon_atual_adv == 5: 
                                estado_jogo = "FIM"
                            else:
                                estado_jogo = "BATALHA" 
                        elif vidas_jogador[pokemon_atual_jog] <= 0:
                            vivos = False
                            for v in vidas_jogador:
                                if v > 0: vivos = True
                            if vivos:
                                estado_jogo = "BATALHA"
                            else:
                                estado_jogo = "FIM"
                        else:
                            texto1 = "O que você vai fazer agora?"
                            texto2 = "Escolha outro ataque."
                            estado_jogo = "BATALHA"

        # --- SE ALGUÉM DESMAIOU, DETECTA E EXIBE O BOTÃO CORRETO DE TRANSIÇÃO ---
        else:
            if vidas_adversario[pokemon_atual_adv] <= 0:
                if pokemon_atual_adv < 5:
                    rect_prox = pygame.draw.rect(tela, AZUL, (250, 500, 300, 50))
                    tela.blit(fonte_grande.render("Próximo Rival", True, BRANCO), (325, 510))
                    if clicou and rect_prox.collidepoint(pos_clique):
                        pokemon_atual_adv += 1
                        texto1 = f"O Rival enviou {nomes[time_adversario[pokemon_atual_adv]]}!"
                        texto2 = "Escolha sua ação."
                        estado_jogo = "BATALHA"
                else:
                    estado_jogo = "FIM"
                    
            elif vidas_jogador[pokemon_atual_jog] <= 0:
                vivos = False
                for v in vidas_jogador:
                    if v > 0: vivos = True
                if vivos:
                    rect_forcar_troca = pygame.draw.rect(tela, ROXO, (250, 500, 300, 50))
                    tela.blit(fonte_grande.render("Substituir Pokémon", True, BRANCO), (290, 510))
                    if clicou and rect_forcar_troca.collidepoint(pos_clique):
                        estado_jogo = "TROCA"
                else:
                    estado_jogo = "FIM"

    # ==================== TELA DE TROCA RESTRETA AO TIME ====================
    elif estado_jogo == "TROCA":
        txt_t = fonte_grande.render("Selecione um Pokémon substituto:", True, PRETO)
        tela.blit(txt_t, (LARGURA // 2 - txt_t.get_width() // 2, 40))
        
        for i in range(6):
            idx_p = time_jogador[i]
            coluna = i % 3
            linha = i // 3
            
            x = 130 + (coluna * 190)
            y = 150 + (linha * 170)
            
            cor_box = cores[idx_p] if vidas_jogador[i] > 0 else CINZA_ESCURO
            rect_poke = pygame.draw.rect(tela, cor_box, (x, y, 150, 130))
            pygame.draw.rect(tela, PRETO, (x, y, 150, 130), 3)
            
            tela.blit(fonte_media.render(nomes[idx_p], True, PRETO), (x + 8, y + 20))
            tela.blit(fonte_pequena.render(f"Tipo: {tipos[idx_p]}", True, PRETO), (x + 8, y + 55))
            tela.blit(fonte_pequena.render(f"HP: {vidas_jogador[i]}", True, PRETO), (x + 8, y + 85))

            if i == pokemon_atual_jog and vidas_jogador[pokemon_atual_jog] > 0:
                tela.blit(fonte_pequena.render("[Em campo]", True, BRANCO), (x + 8, y + 105))
                
            if clicou and rect_poke.collidepoint(pos_clique):
                if vidas_jogador[i] > 0: 
                    if i != pokemon_atual_jog or vidas_jogador[pokemon_atual_jog] <= 0:
                        pokemon_atual_jog = i
                        texto1 = f"Você mandou {nomes[idx_p]} para o combate!"
                        texto2 = "Selecione o seu golpe."
                        estado_jogo = "BATALHA"

    # ==================== TELA DE FIM ====================
    elif estado_jogo == "FIM":
        soma_vida = sum(vidas_jogador)
        if soma_vida <= 0:
            txt_f = fonte_grande.render("Você Perdeu a Batalha! 😢", True, VERMELHO)
            txt_sub = fonte_media.render("Todos os seus Pokémon desmaiaram.", True, PRETO)
        else:
            txt_f = fonte_grande.render("Você é o Grande Campeão! 🏆", True, VERDE_ESCURO)
            txt_sub = fonte_media.render("Você derrotou com sucesso os 6 Pokémon do rival!", True, PRETO)
            
        rect_menu = pygame.draw.rect(tela, CINZA, (250, 380, 300, 60))
        pygame.draw.rect(tela, PRETO, (250, 380, 300, 60), 2)
        tela.blit(fonte_grande.render("Voltar para o Menu", True, PRETO), (295, 395))
        
        tela.blit(txt_f, (LARGURA // 2 - txt_f.get_width() // 2, 180))
        tela.blit(txt_sub, (LARGURA // 2 - txt_sub.get_width() // 2, 230))
        
        if clicou and rect_menu.collidepoint(pos_clique):
            estado_jogo = "MENU"

    pygame.display.flip()

pygame.quit()
sys.exit()
