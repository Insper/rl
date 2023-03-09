# Using RL in non-deterministic environments
    
O ambiente [Frozen Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a tarefa e tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a tarefa com 0 pontos de reward. Cada ação que não leva para um estado terminal tem reward igual a 0.  

Neste ambiente o agente consegue executar 4 ações: ir para cima, ir para baixo, ir para esquerda e ir para direita. **Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo**, por exemplo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico.

##  Trabalhe com o arquivo `FrozenLake_introduction.py`

1. Este arquivo está disponível em [https://github.com/Insper/rl_code/tree/main/src/part_03](https://github.com/Insper/rl_code/tree/main/src/part_03).

1. Leia a documentação do código fonte disponível em [https://gymnasium.farama.org/environments/toy_text/frozen_lake/](https://gymnasium.farama.org/environments/toy_text/frozen_lake/)

1. Veja o que está codificado no arquivo `FrozenLake_introduction.py` e execute o mesmo.

3. Quantos estados e quantas ações o ambiente FrozenLake-v1 tem?

4. O que aconteceu com a execução das ações? O resultado foi o esperado? Descreva o que aconteceu.

## Trabalhe com o arquivo `FrozenLake.py`

* Este arquivo também está em [https://github.com/Insper/rl_code/tree/main/src/part_03](https://github.com/Insper/rl_code/tree/main/src/part_03)

* Abra em um editor de texto e descomente as linhas 12 e 13 e comente a linha 14. O código deve ficar como abaixo:

````python
# only execute the following lines if you want to create a new q-table
qlearn = QLearning(env, alpha=0.9, gamma=0.95, epsilon=0.8, epsilon_min=0.0001, epsilon_dec=0.9999, episodes=500000)
q_table = qlearn.train('data/q-table-frozen-lake.csv','results/actions_frozen_lake')
#q_table = loadtxt('data/q-table-frozen-lake.csv', delimiter=',')
````

* Execute o arquivo `FrozenLake.py` com o comando:

````bash
python FrozenLake.py
````

* Agora faça o algoritmo `FrozenLake.py` ler a Q-table a partir do arquivo gerado anteriormente e veja qual é o comportamento. Execute diversas vezes. Ele consegue chegar ao objetivo sempre? Ele consegue chegar ao objetivo na maioria das vezes? 

* E se executarmos 100 vezes? Quantas vezes o agente consegue atingir o objetivo? Execute o comando abaixo:

````bash
python FrozenLake100times.py
````

* Como podemos melhorar o desempenho deste agente?

* Teste diferentes configurações de hiperparâmetros. Qual é o comportamento visto no gráfico de episódios versus rewards? 

## E o algoritmo Sarsa?

* Será que o algoritmo Sarsa tem um desempenho melhor para problemas não-determinísticos? 

* Em [https://github.com/Insper/rl_code/tree/main/src/part_03](https://github.com/Insper/rl_code/tree/main/src/part_03) tem um arquivo chamado `FrozenLakeSarsa.py` que você pode utilizar para responder esta pergunta. 

## Outro mapa

Existem dois mapas pré-configurados em [https://gymnasium.farama.org/environments/toy_text/frozen_lake/](https://gymnasium.farama.org/environments/toy_text/frozen_lake/). O mapa 4x4 e um mapa 8x8. E se mudarmos o mapa para 8x8? 

````python
import gymnasium as gym
env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
````

* O que muda? O problema se torna mais complexo? É necessário mudar algum dos hiperparâmetros? Qual é o melhor algoritmo? *Sarsa* ou *Q-Learning*? 

Considere o seguinte objetivo: *desenvolver um agente capaz de chegar ao ponto final em mais de 80% das vezes". Faça o *clone* do projeto [https://classroom.github.com/a/Ag-dCmlJ](https://classroom.github.com/a/Ag-dCmlJ). Você deve adicionar neste projeto e fazer o commit dos seguintes artefatos: 

* o arquivo `q-table.csv` dentro do diretório `data`. Já existe um arquivo q-table neste projeto, mas ele é para a versão do ambiente 4x4. Quando você executar o arquivo `test_frozenlake.py` usando o comando `pytest` irá ocorrer um erro de `IndexError`. Você deve substituir este arquivo pelo arquivo gerado pelo seu agente durante o período de treinamento; 

* depois de substituir o arquivo `data/q-table.csv`, você poderá executar os testes e verificar se o mesmo é aprovado em todos os testes. São quatro testes: o primeiro executa o ambiente 1000 vezes e verifica se o agente conseguiu chegar ao final em no mínimo 700 vezes. Os outros 3 testes fazem exatamente a mesma coisa: executam o agente no ambiente 1000 vezes e verificam se o agente conseguiu chegar ao final em no mínimo 800 vezes;

* você também deve adicionar a sua implementação no diretório raiz deste projeto, e;

* alterar o arquivo README.md informando os hiperparâmetros utilizados para o treinamento. 

* (critério para A+) apresentar um gráfico comparando a curva de aprendizagem de diversas abordagens utilizadas durante o treinamento. A imagem deste gráfico deve ser adicionada ao projeto e o texto explicando os resultados ao arquivo README.md.  

### Algoritmo e hiperparâmetros utilizados para o treinamento

| Atributo        |  Valor     |
|:----------------|:----------:|
| Algoritmo       |            |
| alpha           |            |
| gamma           |            |
| epsilon         |            |
| epsilon_dec     |            |
| epsilon_min     |            |
| qtd_episodios   |            |


### Rubrica de avaliação

* Deixou de entregar um dos artefatos: q-table, implementação na forma de arquivo python ou arquivo README.md atualizado com os hiperparâmetros: igual a **Insuficiente (I)** - nota 2. 

* Entregou todos os artefatos mencionados acima então a nota é calculada de acordo com o número de testes aprovados: 
    * 1 teste aprovado = 2.5, 
    * 2 testes aprovados = 5.0, 
    * 3 testes aprovados = 7.5, 
    * 4 testes aprovados = 9.0

* Foi aprovado em todos os testes e entregou o gráfico comparando a curva de aprendizagem de diversas abordagens utilizadas ao longo do treinamento então nota igual a **10 (dez)**. 

### Deadline

O deadline para a entrega desta atividade é 12 de março de 2023 às 23:30 horas. 