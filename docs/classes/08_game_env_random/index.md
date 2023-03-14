# Using RL in a competitive environment with random behavior

The goal of this activity is to implement an agent to play Blackjack using Q-Learning or Sarsa algorithms and show the results.

## Jogador de BlackJack

A biblioteca Gym possui um ambiente que simula um jogo de [BlackJack (*Blackjack-v1*)](https://www.gymlibrary.dev/environments/toy_text/blackjack/). A documentação deste ambiente está disponível neste link [https://www.gymlibrary.dev/environments/toy_text/blackjack/](https://www.gymlibrary.dev/environments/toy_text/blackjack/). 

Além da documentação, você tem acesso a duas implementações:

* [BlackJack_Manual.py](./BlackJack_Manual.py): onde você pode jogar várias partidas de BlackJack e entender a representação de estado adotada pelo ambiente, e;
* [BlackJack_Agent.py](./BlackJack_Agent.py): que tem uma implementação de agente que aprende a jogar BlackJack usando aprendizagem por reforço. 

Atividades propostas: 

* Execute diversas vezes o arquivo [BlackJack_Manual.py](./BlackJack_Manual.py) para entender como o ambiente funciona. Principalmente como a representação do espaço de estados funciona. 

* Execute o arquivo [BlackJack_Agent.py](./BlackJack_Agent.py) com o objetivo de criar uma nova q-table. Qual o desempenho do agente? 

* Como podemos obter um agente com o melhor desempenho possível? É possível criar um agente que ganha ou empata em no mínimo 85% dos jogos? Se sim, quais são os hiperparâmetros para este agente? Se não, qual é o melhor resultado encontrado? 
