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

# Entregável Python Orientação Objeto

Requisitos:
    5 atributos
    4 métodos

Atributos utilizados: self, numero_thursters, lista_sensores, ano_construcao, nome_veiculo, controlador (escolhido por mim)

Métodos e explicação do Código: 
    
    Dentro da classe AUVs, instaciei as três variáveis globalmente, que, ao longo do código, seria utilizado por alguns métodos e para execução da função.

    Teste 
        A classe foi estruturada de forma a possibilitar duas formas de execução:
        Utilizando os 5 atributos como parâmetro da classe (para respeitar o pedido pelo exercício)
        Testar sem dar nenhum parâmetro, visto que, um usuário, sem conhecer os AUVs ou o código plenamente, não teria como saber o que imputar para testar o programa.

        teste_sem_parametro = AUVs() => Caso execute o programa sem os atributos, é necessário escrever o nome do robo desejado e selecionar um dos botões que contém os demais métodos da classe.

        teste_com_parametro = AUVs(*grandpa)=> Caso o teste seja feito imputando os atributos, a caixa de texto da interface, apesar de funcionar, fica desabilitada e os comandos de execução são feitos pelos botões. Ou seja, caso impute uma das três listas instaciadas globalmente no início do código (lua, BrHUE, grandpa), basta clicar nos botões e ignorar a caixa de texto. Para imputar uma das listas globais  que contem os atributos, colocar "*" na frente para funcionar.

        
    -__init__ => esse método inicializa o programa instanciando os atributos e a interface gráfica que contém a tabela.

    -tabela_AUVs -> esse método é o responsável pela construção da interface gráfica e não precisa ser chamado pelo usuário para teste. Coloquei dentro do método __init__ para que a tabela aparecesse e dentro dela, o usuário pudesse navegar pelos demais métodos do programa.

    -robo_individual -> Esse método retorna os atributos do AUV selecionado individualmente. (printa no vscode, não na interface gráfica.). O código foi feito de forma a responder os dois tipos de execução. 

    -rank_robos -> não precisa de parâmetro ou de um valor na caixa de texto da interface para funcionar. Basta apertar o botão e o código retorna no vscode o ranking.

    -site_nautilus-> Esse método funciona de forma similar ao "robo_individual", ou seja no que diz respeito ao tipo de teste realizado (com ou sem parâmetros). E ele redireciona o usuário para a página da Nautilus na Web do AUV escolhido.

    Os métodos que são necessários escrever na caixa de texto da interface, caso seja imputado um valor não esperado pelo programa, é retornado no vscode uma mensagem de erro pedindo uma entrada válida. Não é necessário fechar a interface gráfica para fazer um novo teste (caso o teste tenha sido o sem parâmetro).

    Os dois testes estão comentados ao final do código como sugestão.