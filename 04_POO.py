class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())

#SUPER -> palavra reservada para trazer implementação(s) da classe pai super().__init__(**kw) ou uma função específica return super().função()
class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()
bar.hello()
print()

teste = Foo()
teste.hello()


