class Substituir:
    def __init__(self, texto, localizar, caractere_substituto):
        self.texto = texto
        self.localizar = localizar
        self.caractere_substituto = caractere_substituto

    def substituicao(self):

        if self.texto.strip():
            return self.texto.replace(self.localizar, self.caractere_substituto)
        return 'Texto Vazio'
