def log(*args, **kwargs):
    prefix = kwargs.get('prefix', 'LOG: ')
    sep = kwargs.get('sep', ' ')
    
    print(prefix, end='')
    print(*args, sep=sep)

# Ejemplo de uso de la función log con diccionario desempaquetado
diccionario = {'mensaje': 'Mensaje', 'accion': 'prueba'}
log(**diccionario, prefix="CUSTOM: ", sep='-')  # Output: CUSTOM: Mensaje-prueba
