/*Ao fim do processamento o valor da variável SOMA será 91. Ao observar o código podemos ver que se trata de uma soma de números inteiros (int), 
e ele diz que enquanto K for menor que o INDICE o programa deverá fazer esses cálculos e ao fim o resultado da SOMA é 91. 
O "enquanto" se trata de uma estrutura de repetição utilizada para comparar dados e refazer as operações até que o requisito seja alcançado, normalmente é visto como "while" ou "do-while". 
Essa estrutura de repetição é o ideal para esses casos onde devemos ir acrescentando valores a uma variável que se torna dinâmica. Um exemplo do funcionamento desse código na linguagem de programação C é:*/

int INDICE = 13, SOMA = 0, K = 0;

   while(K < INDICE){

       K = K + 1;

       SOMA = SOMA + K;

   }

   printf("%d",SOMA);

return 0;
