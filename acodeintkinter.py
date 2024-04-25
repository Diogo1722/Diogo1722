#Beleza, vamos começar criando nossa linda interface gráfica.

from tkinter import *
import os


def seleção():
    posição = vfutworld.get()
    pos.config(state='normal')
    pos.delete(1.0, END)
    if posição == 'pd':
        pos.insert(END, f'O ponta no futebol é o jogador que joga pelos lados do campo ofensivamente. Ele sempre é um jogador mais armador e que busca o drible. Costumam ser velozes e lisos.')
    elif posição == 'ca':
        pos.insert(END, f'O centroavante no futebol é um jogador mais fixo e centralizado no ataque. Sua principal função é receber passes e marcar o gol, ou até mesmo distrair a marcação. Tem papel fundamental no jogo.')
    elif posição == 'zg':
        pos.insert(END, f'O zagueiro é o principal defensor na linha. Pode até ajudar na construção de jogo, mas tem seu principal papel em impedir uma finalização do adversário, ou evitar grandes riscos em sua área.')
    elif posição == 'gk':
        pos.insert(END, f'O goleiro é o único jogador que não é de linha no jogo. Sua função é defender finalizações através de suas mãos')
    elif posição == 'lt':
        pos.insert(END, f'O lateral é o tipo de jogador mais equilibrado. Vai jogar pelas pontas tanto no setor defensivo quanto pelo ofensivo, sempre buscando achar um equilíbrio entre apoio ofensivo e defensivo.')
    elif posição == 'mei':
        pos.insert(END, f'O meia é responsável por ser o cerébro do jogo.costuma ter uma visão e inteligência de jogo acima da média, sendo geralmente o maior passador da equipe e o maior criador de chances.')
    elif posição == 'vol':
        pos.insert(END, f'O volante é uma espécie de zagueiro, só que um pouco mais avançado. Busca um equilíbrio entre apoio ofensivo, apoio defensivo e controle do jogo central. Digamos que ele corta o mal pela raíz.')

intgra=Tk()
intgra.title('INTERFACE GRÁFICA')
intgra.geometry('700x400')
intgra.configure(background='#9ACD32')

#Basicamente, eu quero unir radiobuttons + gravar dados + menu.
#Como eu vou fazer isso? Através do fut, kkkkk. Essa interface gráfica HORROROSA, quer dizer, honrosa, tem o objetivo de fazer você escolher um time de futebol, e aí ela insere o seu time e pá. Vou ficar pensando em ideias melhores enquanto penso. Primeiramente, vou fazer os negócio bonitin né, o menu.


vfutworld=StringVar()

futworld=Label(intgra,text='Posições')
futworld.pack

botãodoponta=Radiobutton(intgra,text='Ponta',value='pd',variable=vfutworld, width=10)
botãodoponta.pack(anchor='w', ipady=0, ipadx=0)

botão_futworld=Button(intgra,text='Selecionar posição: ',command=seleção, width=0)
botão_futworld.pack(anchor='w', side='right', ipadx=0, ipady=0)

botãodocentroavante=Radiobutton(intgra,text='Centroavante',value='ca',variable=vfutworld, width=10)
botãodocentroavante.pack(anchor='w',ipadx=0, ipady=10)

botãodomeia=Radiobutton(intgra,text='Meia',value='mei',variable=vfutworld, width=10)
botãodomeia.pack(anchor='w', ipady=10, ipadx=0)

botãodovolante=Radiobutton(intgra, text='Volante', value='vol',variable=vfutworld, width=10)
botãodovolante.pack(anchor='w', ipady=10, ipadx=0)

botãodozagueiro=Radiobutton(intgra, text='Zagueiro', value='zg', variable=vfutworld, width=10)
botãodozagueiro.pack(anchor='w', ipady=10, ipadx=0)

botãodolateral=Radiobutton(intgra, text='Lateral', value='lt', variable=vfutworld, width=10)
botãodolateral.pack(anchor='w', ipady=10, ipadx=0)

botãodogoleiro=Radiobutton(intgra, text='Goleiro', value='gk', variable=vfutworld, width=10)
botãodogoleiro.pack(anchor='w', ipady=10, ipadx=0)

pos = Text(intgra, height=5, width=40)
pos.pack(anchor='w', padx=0, pady=10)
pos.insert(END, 'Posição selecionada: ')
pos.config(state='disabled')

#Finalmente terminei de desenvolver a parte dos Radiobuttons. Demorou! Agora, vou fazer ele gravar dados no sistema. Esse é o melhor programa que eu já fiz!! Agora vamos para a parte do vôlei.

def funçãonovo():
    volei = Toplevel(intgra)
    volei.title('Interface')
    volei.geometry('500x300')
    volei.configure(background='#7FFFD4')
    Label(volei, text='O que é o vôlei? ', background='#dde', foreground='#009', anchor=W).place(x=0, y=0, width=200, height=20)
    voleioque = Text(volei)
    voleioque.place(x=0, y=20, width=200, height=80)
    voleioque.insert(END, f'Voleibol é um esporte praticado numa quadra dividida em duas partes por uma rede, possuindo duas equipes de seis jogadores em cada lado. O voleibol foi originalmente chamado de Mintonette, devido à sua semelhança com o Badminton.')
    voleioque.config(state='disabled')
    Label(volei, text='Quais as posições do vôlei?', background='#dde', foreground='#009', anchor=W).place(x=0,y=100,width=200, height=20)
    voleipos = Text(volei)
    voleipos.place(x=0, y=120, width=200, height=80)
    voleipos.insert(END, f'Levantador.\nOposto.\nPonteiro (Pontas)\nCentral ou meio-de-rede.\nLíbero.')
    voleipos.config(state='disabled')
    Label(volei, text='Como jogar? ', background='#dde', foreground='#009', anchor=W).place(x=0,y=200, width=200, height=20)
    voleicj = Text(volei)
    voleicj.place(x=0, y=220, width=200, height=80)
    voleicj.insert(END, f'O jogo é iniciado por uma das equipes que dão o saque, lançando a bola para o lado da equipe adversária. Após o saque, a bola deve ultrapassar a rede, onde os jogadores adversários evitam que caia em seu campo, utilizando no máximo três toques. O jogo é dividido em sets, quem vencer os três primeiros, ganha a partida.')
    voleicj.config(state='disabled')

conjuntodemenus=Menu(intgra)
opçõesnomenu=Menu(conjuntodemenus, tearoff=0)
opçõesnomenu.add_command(label='Sobre Vôlei', command=funçãonovo)
opçõesnomenu.add_separator()
opçõesnomenu.add_command(label='Fechar', command=intgra.quit)
conjuntodemenus.add_cascade(label='Opções', menu=opçõesnomenu)

intgra.config(menu=conjuntodemenus)

#Basicamente, o que eu fiz aqui: Criei um menu com duas opções. Você pode fechar sua interface gráfica, ou abrir uma nova interface gráfica sobre vôlei(eca, esporte ruim da porra)

intgra.mainloop()
                 