import streamlit as st
# Sistema CRUD simples para gerenciar uma lista de frutas
list_fruit = [] # esta lista está fora do loop!


while True:
    print ("                          SISTEMA CRUD                ")
    print("1.ADCIONAR ITEMS","\n2.LER A LISTA DE ITEMS","\n3.EDITAR ITEMS","\n4.EXCLUIR ITEM","\n5.EXIT")
    menu = int(input())
    if menu == 1:
        while True: 
            tip_fruit = input("\nQual fruta deseja adcionar: ")
            list_fruit.append(tip_fruit)
            stop_fruit = input("\nVocê deseja adcionar mais frutas? (S/N)").strip().upper()
            if stop_fruit == "N":
                break 
            else:
                print ("Opcao invalida")
    elif menu == 2:
        print("lista de frutas adcionadas: ",list_fruit)
    elif menu == 3:
        print("\nlista de frutas adcionadas: ",list_fruit)
        fruit_to_edit = input("\nQual fruta deseja editar? ").strip()
        if fruit_to_edit in list_fruit:
            new_fruit = input("\nDigite o novo nome da fruta ")
            list_fruit[list_fruit.index(fruit_to_edit)] = new_fruit
            print("\nFruta editada com sucesso!!")
        else:
            print("\nFruta não encontrada")
    elif menu == 4:
        print("\nlista de frutas adcionadas: ",list_fruit)
        fruit_to_remove = input("\nQual fruta deseja excluir:  ")
        if fruit_to_remove in list_fruit:
            list_fruit.remove(fruit_to_remove)
            print("Fruta removida com sucesso")
        else:
            print("\nFruta não encontrada!")
    elif menu == 5:
        print("\nSaindo do Sistema ...")
        break