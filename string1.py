#métodos de string:

nome = "mATHeus"
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   wello world!     "
print(texto.strip())
print(texto.lstrip() + '.')
print(texto.rstrip() + '.')

curso = "Python"
print('-'.join(curso))
print(curso.center(10,"#"))
