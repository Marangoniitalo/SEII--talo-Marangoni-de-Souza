//Inclui a biblioteca padrão da linguagem C
#include <stdio.h>
// Inclui as funções de adição e multiplicação geradas no arquivo header
#include "addmultiply.h"

// Função main
int main()
{
    int n1, n2;
    //Passa dois números para as funções de adição e multiplicação
    printf("Escreva o primeiro número: ");
    scanf("%d", &n1);
    printf("Escreva o segundo número: ");
    scanf("%d", &n2);

    add(n1, n2);

    multiply(n1, n2);

    //printf definido no stdio,h
    printf("Processo completo\n");
    return 0;
}