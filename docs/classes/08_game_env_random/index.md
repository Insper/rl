# Using RL in a competitive environment with random behavior

The goal of this activity is to implement an agent to play Blackjack using Q-Learning or Sarsa algorithms and show the results.

## Jogador de BlackJack

A biblioteca Gymnasium possui um ambiente que simula um jogo de [BlackJack (*Blackjack-v1*)](https://gymnasium.farama.org/environments/toy_text/blackjack/). A documentação deste ambiente está disponível neste link [https://gymnasium.farama.org/environments/toy_text/blackjack/](https://gymnasium.farama.org/environments/toy_text/blackjack/). 

Além da documentação, você tem acesso a duas implementações:

* [BlackJack_Manual.py](https://github.com/Insper/rl_code/blob/main/src/part_04/BlackJack_Manual.py): onde você pode jogar várias partidas de BlackJack e entender a representação de estado adotada pelo ambiente;
* [BlackJack_Agent.py](https://github.com/Insper/rl_code/blob/main/src/part_04/BlackJack_Agent.py): que tem uma implementação de agente que aprende a jogar BlackJack usando aprendizagem por reforço, e;
* [QLearning_Blackjack.py](https://github.com/Insper/rl_code/blob/main/src/part_04/QLearning_BlackJack.py): uma versão do algoritmo QLearning com adição de um método para tratamento dos estados do ambiente BlackJack. 

Atividades propostas: 

* Execute diversas vezes o arquivo [BlackJack_Manual.py](https://github.com/Insper/rl_code/blob/main/src/part_04/BlackJack_Manual.py) para entender como o ambiente funciona. Principalmente como a representação do espaço de estados funciona. 

* Execute o arquivo [BlackJack_Agent.py](https://github.com/Insper/rl_code/blob/main/src/part_04/BlackJack_Agent.py) com o objetivo de criar uma nova q-table.

Perguntas: 

* Como podemos obter um agente com o melhor desempenho possível? É possível criar um agente que ganha ou empata em no mínimo 85% dos jogos? Se sim, quais são os hiperparâmetros para este agente? Se não, qual é o melhor resultado encontrado? 

* É possível plotar a q-table? Este plot de q-table seria útil para um jogador de BlackJack real? Justifique a sua resposta. 

Entrega: 

* você também deve adicionar a sua implementação no diretório raiz do projeto no Github Classroom: [https://classroom.github.com/a/Qe2Tawio](https://classroom.github.com/a/Qe2Tawio).

* para a sua implementação estar completa você deve adicionar um script para validação na q-table no ambiente. 

* criar um arquivo README.md informando os hiperparâmetros utilizados para o treinamento. 

* (critério para A) usar o algoritmo Sarsa para este problema. Neste caso você deve fazer algo similar ao que está implementado no arquivo [QLearning_Blackjack.py](https://github.com/Insper/rl_code/blob/main/src/part_04/QLearning_BlackJack.py).   

* (critério para A+) apresentar um gráfico que resume a q-table, ou seja, que resume o que fazer em cada jogada. Comente também se é possível utilizar esta q-table em uma situação real ou não. 

## Algoritmo e hiperparâmetros utilizados para o treinamento

| Atributo        |  Valor     |
|:----------------|:----------:|
| Algoritmo       |            |
| alpha           |            |
| gamma           |            |
| epsilon         |            |
| epsilon_dec     |            |
| epsilon_min     |            |
| qtd_episodios   |            |


## Rubrica de avaliação

* Deixou de entregar um dos artefatos: q-table, implementação na forma de arquivo python ou arquivo README.md atualizado com os hiperparâmetros: igual a **Insuficiente (I)** - nota 2. 

* Entregou todos os artefatos mencionados acima e o desempenho do agente passou de 85% então nota igual a **8.0**.

* Entregou a implementação do algoritmo Sarsa com adição de um método para tratamento dos estados do ambiente BlackJack $\rightarrow$ **nota = 9.0**. 

* Entregou o gráfico que resume a q-table e explicou se é possível utilizar tal informação em uma situação real ou não então nota igual a **10.00**.

## Deadline

O deadline para a entrega desta atividade é 21 de março de 2023 às 23:30 horas. Este trabalho deve ser feito em grupo - o mesmo grupo da implementação do tic-tac-toe usando reinforcement learning. 

## Referências 

* https://gymnasium.farama.org/tutorials/training_agents/blackjack_tutorial/