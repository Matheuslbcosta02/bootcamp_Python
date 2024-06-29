#atributos de classe são compartilhadas entre os objetos
#atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia)

class Estudante:
    escola = "DIO"
    def __init__ (self,nome,matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__ (self) -> str:
        return f"{self.nome} = {self.matricula} - {self.escola}"
    
#escola é uma varável de classe
#nome e matricula são variáveis de instância, self é instância
aluno1 = Estudante("Gui",1)
aluno2 = Estudante("Gio",2)
aluno3 = Estudante("fii",9)
print(aluno1)
print(aluno2)
print(aluno3)
#só vai refletir em aluno1
aluno1.escola = "python"
print(aluno1)
print(aluno2)
print(aluno3)

#vai refletir em todos os objetos da classe, exceto no 1, ele vai respeitar-
Estudante.escola = "teste"
print(aluno1)
print(aluno2)
print(aluno3)
