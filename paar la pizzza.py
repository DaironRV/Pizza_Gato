

print("comprar ingredientes para pizza")

print("================================================")

my_dict_p = {0: "Masa " "Masa",
             1: "Queos " "queso",
             2: " Salsa " "salsa",
             3: "champiñones " " Campiñones"}

lista_ingredientes = ["masa",
                      "queso",
                      "salsa",
                      "champiñones"]

# print(my_dict_p ["0"])

print(lista_ingredientes)

print(my_dict_p)

necesito = int(input("escoje el ingrediente:"))

print("================================================")

if necesito == 0:
    print(my_dict_p[0])
    print("como quieres compara la masa?")
    virtual_precensial = int(input("1:virtual / 2:precensial"))
    while virtual_precensial < 2 or virtual_precensial > 2:
        print(" selecionaset virtual ")
        print("Los paso a seguir son:")
        print("1) entar a la APP/Paina Web")
        print("2)entrar a la sección de alimentos")
        print("3)hacer la compra.")
        print("Erro => sin coneccion")
        virtual_precensial = int(input("1:virtual / 2:precensial"))
    print("================================================")
    print("seleccionaste presencial")
    print("los pasos que siguen son:")
    print("1)Voy a la tienda")
    print("2) compras")

    print("================================================")

elif necesito == 1:
    print(my_dict_p[1])
    print("como quieres comprar el Queso")
    virtual_precensial = int(input("1:virtual / 2:precensial"))
    while virtual_precensial < 2 or virtual_precensial > 2:
        print(" selecionaset virtual ")
        print("Los paso a seguir son:")
        print("1) entar a la APP/Paina Web")
        print("2)entrar a la sección de alimentos")
        print("3)hacer la compra.")
        print("Erro => sin coneccion")
        virtual_precensial = int(input("1:virtual / 2:precensial"))
    print("================================================")
    print("seleccionaste presencial")
    print("los pasos que siguen son:")
    print("1)Voy a la tienda")
    print("2) compras")

    print("================================================")

elif necesito == 2:
    print(my_dict_p[2])
    print("Como quieres comprar las salsas?")
    virtual_precensial = int(input("1:virtual / 2:precensial"))
    while virtual_precensial < 2 or virtual_precensial > 2:
        print(" selecionaset virtual ")
        print("Los paso a seguir son:")
        print("1) entar a la APP/Paina Web")
        print("2)entrar a la sección de alimentos")
        print("3)hacer la compra.")
        print("Erro => sin coneccion")
        virtual_precensial = int(input("1:virtual / 2:precensial"))
    print("================================================")
    print("seleccionaste presencial")
    print("los pasos que siguen son:")
    print("1)Voy a la tienda")
    print("2) compras")

    print("================================================")

elif necesito == 3:
    print(my_dict_p[3])
    print("como quieres comprar los champiñones?")
    virtual_precensial = int(input("1:virtual / 2:precensial"))
    while virtual_precensial < 2 or virtual_precensial > 2:
        print(" selecionaset virtual ")
        print("Los paso a seguir son:")
        print("1) entar a la APP/Paina Web")
        print("2)entrar a la sección de alimentos")
        print("3)hacer la compra.")
        print("Erro => sin coneccion")
        virtual_precensial = int(input("1:virtual / 2:precensial"))
    print("================================================")
    print("seleccionaste presencial")
    print("los pasos que siguen son:")
    print("1)Voy a la tienda")
    print("2) compras")

    print("================================================")

elif necesito == 4:
    print("Never gonna give you up Never gonna let you down Never gonna turn around and desert you Never gonna make you cry Never gonna say goodbyeNever gonna tell a lie and hurt you")

elif necesito == 5:
    print("🦇 🖤 i'm vengeance")

else:
    print("esa opcion no esta en la lista => Error")

print("fin de la compra")


# intente agregar este bucle pero no pude pipipi
'''
print("hay o no hay?")
hay_No_hay = int (input("tiene  en la tienda?", "(si=3/no=4)"))
while hay_No_hay<3 or hay_No_hay>3:
    print("vas a otra tienda")                                        
    hay_No_hay = int (input("tiene  en la tienda?", "(si=3/no=4)"))
print("2)compras.")

'''
