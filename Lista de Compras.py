import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Super Lista de Compras")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f8ff")
        
        # Estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, font=('Helvetica', 10))
        self.style.configure("TLabel", background="#f0f8ff", font=('Helvetica', 12))
        
        # Lista de compras
        self.lista_compras = []
        self.carregar_lista()
        
        # Widgets
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(
            main_frame, 
            text="📋 MINHA LISTA DE COMPRAS", 
            font=('Helvetica', 16, 'bold'),
            foreground="#d61d1d"
        )
        titulo.pack(pady=10)
        
        # Entrada de item
        self.frame_entrada = ttk.Frame(main_frame)
        self.frame_entrada.pack(fill=tk.X, pady=10)
        
        self.entry_item = ttk.Entry(
            self.frame_entrada, 
            font=('Helvetica', 12),
            width=30
        )
        self.entry_item.pack(side=tk.LEFT, padx=5)
        self.entry_item.bind("<Return>", lambda e: self.adicionar_item())
        
        btn_adicionar = ttk.Button(
            self.frame_entrada, 
            text="➕ Adicionar", 
            command=self.adicionar_item,
            style="Accent.TButton"
        )
        btn_adicionar.pack(side=tk.LEFT)
        
        # Lista de itens
        self.frame_lista = ttk.Frame(main_frame)
        self.frame_lista.pack(fill=tk.BOTH, expand=True)
        
        self.lista_box = tk.Listbox(
            self.frame_lista,
            font=('Helvetica', 12),
            bg="white",
            selectbackground="#2e86de",
            selectforeground="white",
            height=12,
            activestyle="none"
        )
        self.lista_box.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(self.lista_box)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista_box.yview)
        
        # Botões de ação
        self.frame_botoes = ttk.Frame(main_frame)
        self.frame_botoes.pack(fill=tk.X, pady=10)
        
        btn_remover = ttk.Button(
            self.frame_botoes, 
            text="❌ Remover Selecionado", 
            command=self.remover_item
        )
        btn_remover.pack(side=tk.LEFT, padx=5)
        
        btn_limpar = ttk.Button(
            self.frame_botoes, 
            text="🧹 Limpar Tudo", 
            command=self.limpar_lista
        )
        btn_limpar.pack(side=tk.LEFT)
        
        btn_salvar = ttk.Button(
            self.frame_botoes, 
            text="💾 Salvar Lista", 
            command=self.salvar_lista
        )
        btn_salvar.pack(side=tk.RIGHT)
        
        # Atualizar lista
        self.atualizar_lista()
        
        # Configuração de estilo especial
        self.style.configure("Accent.TButton", foreground="white", background="#2e86de")
        
    def adicionar_item(self):
        item = self.entry_item.get().strip()
        if item:
            self.lista_compras.append(item)
            self.atualizar_lista()
            self.entry_item.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Digite um item para adicionar!")
    
    def remover_item(self):
        try:
            index = self.lista_box.curselection()[0]
            self.lista_compras.pop(index)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um item para remover!")
    
    def limpar_lista(self):
        if messagebox.askyesno("Confirmar", "Deseja limpar toda a lista?"):
            self.lista_compras = []
            self.atualizar_lista()
    
    def atualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for i, item in enumerate(self.lista_compras, 1):
            self.lista_box.insert(tk.END, f"{i}. {item}")
    
    def carregar_lista(self):
        if os.path.exists("lista_compras.txt"):
            with open("lista_compras.txt", "r", encoding="utf-8") as f:
                self.lista_compras = [linha.strip() for linha in f.readlines()]
    
    def salvar_lista(self):
        with open("lista_compras.txt", "w", encoding="utf-8") as f:
            for item in self.lista_compras:
                f.write(f"{item}\n")
        messagebox.showinfo("Sucesso", "Lista salva com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaComprasApp(root)
    root.mainloop()
    