#Condiciones con IF
balance=500

if balance>0:
    print("Banlance positivo")

if balance>500:
    print("Balance alto")
else: 
    print("Banlance positivo")

#Booleano
usuario_autenticado=True

if usuario_autenticado:
    print('Acceso concedido')
else:
    print('Acceso denegado')

#Array
lenguajes=['Java', 'Python', 'PHP', 'C#']

if 'PHP' in lenguajes:
    print('PHP está en la lista')

#Elif
ocupacion='Estudiante'

if ocupacion=='Estudiante':
    print('50% de descuento')
elif ocupacion=='Jubilado':
    print('75% de descuento')
elif ocupacion=='Desempleado':
    print('30% de descuento')
else:
    print('10% de descuento')

#AND
usuario_loguado=True
usuario_administrador=True

if usuario_loguado and usuario_administrador:
    print('Tienes mayores privilegios')