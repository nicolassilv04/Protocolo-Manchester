class Fila:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo

        def __str__(self):
            return str(self.valor)

    def __init__(self):
        self.__cabeca = None
        self.__cauda = None
        self.__quantidade = 0

    def __len__(self):
        return self.__quantidade

    def __str__(self):
        return '[' + ', '.join([str(valor) for valor in self]) + ']'

    def __iter__(self):
        atual = self.__cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def is_empty(self):
        return self.__quantidade == 0

    def enqueue(self, valor):
        novo = self.No(valor)
        self.__quantidade += 1

        if self.__cabeca is None:
            self.__cabeca = novo
            self.__cauda = novo
            return

        self.__cauda.proximo = novo
        self.__cauda = novo

    def dequeue(self):
        if self.is_empty():
            raise IndexError('A fila está vazia')

        valor_removido = self.__cabeca.valor
        self.__cabeca = self.__cabeca.proximo
        self.__quantidade -= 1

        if self.__cabeca is None:
            self.__cauda = None

        return valor_removido

class NodoArvore:
    def __init__(self, pergunta=None, cor=None, descricao=None, ramo_sim=None, ramo_nao=None):
        self.pergunta = pergunta
        self.cor = cor
        self.descricao = descricao
        self.ramo_sim = ramo_sim
        self.ramo_nao = ramo_nao

    def is_folha(self):
        return self.pergunta is None

def montar_arvore():
    folha_vermelho = NodoArvore(cor="Vermelho", descricao="emergência (atendimento imediato)")
    folha_laranja = NodoArvore(cor="Laranja", descricao="muito urgente")
    folha_amarelo = NodoArvore(cor="Amarelo", descricao="urgente")
    folha_verde = NodoArvore(cor="Verde", descricao="pouco urgente")
    no_dor = NodoArvore(
        pergunta="Está com dor intensa? (s/n)",
        ramo_sim=folha_amarelo,
        ramo_nao=folha_verde
    )
    no_consciencia = NodoArvore(
        pergunta="Está consciente? (s/n)",
        ramo_sim=no_dor,
        ramo_nao=folha_laranja
    )
    raiz = NodoArvore(
        pergunta="O paciente está respirando? (s/n)",
        ramo_sim=no_consciencia,
        ramo_nao=folha_vermelho 
    )
    return raiz

def triagem(arvore_raiz):
    no_atual = arvore_raiz
    while not no_atual.is_folha():
        resposta = ""
        while resposta not in ['s', 'n']:
            resposta = input(f"{no_atual.pergunta}: ").lower().strip()

        if resposta == 's':
            no_atual = no_atual.ramo_sim
        else: 
            no_atual = no_atual.ramo_nao
    
    return no_atual

def main():
    arvore_triagem = montar_arvore()
    
    filas = {
        "Vermelho": Fila(),
        "Laranja": Fila(),
        "Amarelo": Fila(),
        "Verde": Fila(),
        "Azul": Fila()
    }
    
    ordem_prioridade = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"]

    while True:
        print("\n=== SISTEMA DE TRIAGEM MANCHESTER ===")
        print("1 - Cadastrar paciente")
        print("2 - Chamar paciente")
        print("3 - Mostrar status das filas")
        print("0 - Sair")
        
        escolha = input("Escolha: ")

        if escolha == '1':
            nome_paciente = input("Nome do paciente: ")
            resultado = triagem(arvore_triagem)
            
            cor = resultado.cor
            descricao = resultado.descricao
            
            filas[cor].enqueue(nome_paciente)
            
            print(f"\nCor atribuída: {cor} - {descricao}")
            print(f"Paciente {nome_paciente} adicionado à fila {cor.lower()}.")

        elif escolha == '2':
            paciente_chamado = False
            for cor in ordem_prioridade:
                if not filas[cor].is_empty():
                    paciente = filas[cor].dequeue()
                    print(f"\nChamando paciente da fila {cor}: {paciente}")
                    paciente_chamado = True
                    break
            
            if not paciente_chamado:
                print("\nNão há pacientes nas filas para chamar.")

        elif escolha == '3':
            print("\nSTATUS")
            for cor in ordem_prioridade:
                tamanho = len(filas[cor])
                print(f"Fila {cor}: {tamanho} paciente(s)")


        elif escolha == '0':
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")
