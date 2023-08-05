# Criando Sistema Bancário com Python



## Introdução
Esse código tem como objetivo, fazer um sistema bancário em linguagem Python. Nesse sistema, irá ser implementado 3 operações: depósito, saque e extrato. Com algumas regras abaixo para que o usuário tenha a melhor experiência, sem deixa-lo em maus bocados no futuro (conta no negativo).

## Instituições envolvidas
DIO e IFOOD.

## Regras para criação do código
* Todas as funções de saque e depósitos, serão armazenadas numa variavel 'Extrato';
* Será permitido somente 3 saques diários com limite de R$ 500,00 por saque. Caso o usuário tente efetuar algo fora disso, será mostrado uma mensagem alertando sobre o erro (Como falando anteriormentre, também será colocado na variável 'Extrato';
* Todo valor será exibido utilizando o formato R$ xxx,xx.

## Funções Utilizadas
While, If, Elif, Else.

## Criação do código
* A variável menu foi criada como uma string multipla (ou string tripla), permitindo que o usuário saíba as funções permitidas pelo caixa eletrônico, [d] para depósito, [s] para saque, [e] para extrato e [q] para ele finalizar as operações;
* Logo abaixo temos algumas variáveis onde vale resaltar a variável LIMITE_SAQUE, pois como podem ver ela está em caixa alta, isso se da para que quando um programados veja uma variável como essa, ele saiba que ela é imutável (apesar do programa permitir que outro programador altere a variável, consideramos colocar ela em caixa alta por prática de programadores);
* Começando o laço While (utilizado quando fazemos repetições sem saber a quantidade de loop exatas no momento do código), esse laço permite que o usuário fique dentro dele fazendo as opções informadas anteriormente (saque, depósito e extrato) até o próprio apertar a tecla [q] que finaliza o laço e continuará o programa.;
* Algumas regras foram criadas como por exemplo:
*  - Dentro do If [d], caso o usuário tente fazer um depósito negativo, ele será informado sobre o erro ocorrido, se tudo der certo, ele fará o depósito e a variável extrato receberá as informações do depósito;
   - Dentro do Elif [s], ele conseguirá efetuar o saque, caso as 3 variáveis abaixo do elif sejam False, caso uma delas seja True, ele cairá no if ou algum dos elifs e receberá uma mensagem sobre o erro, mas se tudo der certo, o saque ocorrerá normalmente e adicionará a variável extrato o valor sacado e a variável número_saque +1 (lembrando que ele tem o limite de 3 saques diários);
   - Dentro do Elif [e], teremos todo o extrato de depósitos e saque efetuados com sucesso (as tentativas não serão inclusas) com o saldo final da conta do usuário;
   - E por fim, dentro do laço temos o [q], que iremos utilizar para o usuário sair do laço de repetição (while), usamos o 'break' que força o parada imediata de qualquer função que ele esteja rodando e sai do laço(mas não finaliza o programa, somente sai do laço onde foi colocado);
   - Dentro do Else, ocorrerá caso o usuário coloque alguma letra para efetua uma operação  inválida.

## Agradecimentos
Esse projeto foi o primeiro de muitos que virão em um futuro bem próximo, graças a esse BootCamp organizado por essas 2 potências, fui capaz de olhar linhas de códigos e simplesmente falar, 'sim hoje consigo interprear tudo isso que leio', sei que para alguns veteranos isso pode ser muito pequeno, mas acreditem em si mesmo e nunca parém, pois cada dia que passa estudando, você será capaz de se aperfeiçoando e melhorando para a complexidade da vida.
