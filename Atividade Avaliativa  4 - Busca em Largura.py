from collections import deque

class Grafo:
    def __init__(self):
        self.adj = {}

    def adicionar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def adicionar_aresta(self, u, v):
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Busca em Largura Padrão 

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        ordem = []

        while fila:
            atual = fila.popleft()

            if atual not in visitados:
                visitados.add(atual)
                ordem.append(atual)

                for vizinho in self.adj[atual]:
                    if vizinho not in visitados:
                        fila.append(vizinho)

        return ordem

    # Busca em Largura para encontrar Menor Caminho

    def menor_caminho(self, origem, destino):
        visitados = set()
        fila = deque([origem])
        pai = {origem: None}

        while fila:
            atual = fila.popleft()

            if atual == destino:
                break

            for vizinho in self.adj[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    pai[vizinho] = atual
                    fila.append(vizinho)

        if destino not in pai:
            return None

        caminho = []
        atual = destino

        while atual is not None:
            caminho.append(atual)
            atual = pai[atual]

        caminho.reverse()
        return caminho
