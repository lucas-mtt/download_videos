# importando bibliotecas necessarias
from tkinter import messagebox
from tkinter import *
import pytube


# função para download
def fun_download():
    url = str(boxLink1.get())
    a = pytube.YouTube(url)
    b = a.streams.get_highest_resolution()
    b.download()
    messagebox.showinfo("Download Finalizado", b.title)


# funcção para limpar campo de inserir link
def fun_limpar():
    boxLink.delete(0, 'end')


# função para sair
def fun_sair():
        if messagebox.askokcancel('PyMP4', 'Tem certeza que deseja sair?'):
            master.destroy()


# criando e definindo informações a janela
master = Tk()
master.geometry("300x300")
master.title("Download Videos")
master.resizable(0,0)
master.configure(bg='#c0c0c0')


# frame titulo
frameTitulo = Frame(master, borderwidth=0.5, relief='solid')
frameTitulo.config(bg='black')
frameTitulo.place(x=0,y=0,width=300,height=65)


# label titulo dentro do frame titulo
labelTitulo = Label(frameTitulo, text='PyMP4', font=('Calibri', 18, 'bold'), fg='#c0c0c0', bg='black', relief='flat')
labelTitulo.place(x=110,y=15)


# label link
labelLink = Label(master, text='Link:', font=('Calibri', 12), fg='black', bg='#c0c0c0', relief='flat')
labelLink.place(x=5,y=100)


# edit box para inserir o link
boxLink1 = StringVar()
boxLink = Entry(master, textvariable=boxLink1, font=('Calibri', 11, 'italic'), fg='#c0c0c0', bg='black', relief='raised')
boxLink.place(x=5,y=130, width=288,height=30)


# botão para limpar campo de inserir link
btLimpar = Button(master, text='Limpar', font=('Calibri', 11, 'bold'), fg='#c0c0c0', bg='black', relief='raised', command=fun_limpar)
btLimpar.place(x=110,y=175,width=80,height=30)


# frame botões
frameBotoes = Frame(master, borderwidth=0.5, relief='solid')
frameBotoes.config(bg='black')
frameBotoes.place(x=0,y=235,width=300, height=65)


# botão download
btDownload = Button(frameBotoes, text='Download', font=('Calibri', 11, 'bold'), fg='black', bg='#c0c0c0', relief='raised', command=fun_download)
btDownload.place(x=40,y=15,width=80,height=30)


# botão sair
btSair = Button(frameBotoes, text='Sair', font=('Calibri', 11, 'bold'), fg='black', bg='#c0c0c0', relief='raised', command=fun_sair)
btSair.place(x=170,y=15,width=80,height=30)


master.mainloop()
