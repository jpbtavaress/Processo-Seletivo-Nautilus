#Processo-Seletivo-Nautilus

Esse repositório armazenará os entregáveis do processo seletivo da Nautilus.

O primeiro arquivo a ser comittado será o entregável Python. Nele estão os 4 programas solicitados e sugestões de testes comentados para verificação de suas funcionalidades.

O primeiro programa é bem simples e é constituido de 1 função. Basicamente intancia duas variáveis que guardam o primeiro e último elemento respectivamente e retorna um boleano (True ou False) com o resultado da comparação entre as duas variáveis.

O segundo programa foi feito modularmente para facilitar a compreensão do código (boas práticas) e tambem para otimizar sua implementação. Foi dividido em 3 funções:
	-Divisores é responsável por gerar uma lista dos divisores de um número. Decidi por construir a lista de forma decrescente (do maior divisor para o menor) já que o problema pedia o MENOR divisor primo.
	-"e_primo", é responsável por verificar se o número é primo ou não. Essa função utiliza a lista dos divisores geradas pela primeira função para verificar se o número é primo ou não (se for maior que 1 e tiver 2 divisores ou menos, é primo).
	-Ultimo divisor primo, por fim, itera a lista de divisores gerada pela função "Divisores" verificando se seus elementos são primos, utilizando a função "e_primo". Como a lista foi feita do maior para o menor, o número de iterações é mínimo de forma que o primeiro número primo a ser constatado, retorna o maior divisor primo e a iteração acaba.

O terceiro programa tem como objetivo verificar se um determinado número é palíndromo, ou seja, quando invertido tem o mesmo valor.Para esse programa uma função foi necessária. Nela, foi instanciado uma variável que guardava o número dado como parâmetro da função invertido. Para invertê-lo, transformei o número em uma string e inverti seus algarismos, passando para inteiro novamente. E se o número número dessa variável instanciada fosse igual ao do parâmetro, a função printa uma resposta positiva.

O quarto programa foi feito com uma função e guarda em uma lista (armazenada em uma variável instanciada) todos os números primos menores que 1000. Para isso, foi necessário fazer um for lopp que iterava todos os numeros menores que 1000, verificando através da função "e-primo" do programa 2, se esse número era primo. Caso fosse, era apendado nessa lista vazia criada. Ela retorna não só a soma dos elementos dessa lista, através da função built-in 'sum', como também o tamanho da lista, ou seja, a quantidade de números primos menor que 1000.  
