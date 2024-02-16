# Revisão sobre algoritmos de busca competitivos e jogos

## Ambiente do jogo da velha e agentes

O jogo da velha é um jogo de tabuleiro bem simples porque o espaço de busca é muito pequeno e, em geral, podemos resolver esses tipos de problemas de forma manual. Além disso, este é um jogo muito bom para testar algoritmos de busca competitiva. Por esse motivo, alguns ambientes simulam esse jogo, como o [PettingZoo do projeto Farama](https://pettingzoo.farama.org/environments/classic/tictactoe/) ou o [Kaggle Environments Project](https://github.com/Kaggle/kaggle-environments).

No código abaixo é usado o projeto PettingZoo para simular um jogo da velha:

```python
#
# Reference: https://pettingzoo.farama.org/environments/classic/tictactoe/
#

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3

def play_random_agent(agent, obs):
    x = env.action_space(agent).sample()
    while obs['action_mask'][x] != 1:
        x = env.action_space(agent).sample()
    return x

def play_min_max_agent(agent, obs):
    # TODO you must implement your code here
    pass

env = tictactoe_v3.env(render_mode='human')
env.reset()

not_finish = True
while not_finish:
    for agent in ['player_1','player_2']:
        observation, reward, termination, truncation, info = env.last() 
        if termination or truncation:
            not_finish = False
        else:
            if agent == 'player_1':
                action = play_random_agent(agent,observation)  # this is where you would insert your policy/algorithm
            else:
                action = play_random_agent(agent,observation) # TODO change
            print(f'play: ',action)
            env.step(action)

print(env.rewards)
```

Para executar o código acima, você deve instalar os seguintes pacotes:

```bash
gymnasium
IPython
matplotlib
pettingzoo
```

Por favor, prepare um projeto, com toda a configuração, para executar o código apresentado acima. Você verá dois jogadores aleatórios jogando tic-tac-toe. Você deve entender o que está acontecendo com o código e se tiver alguma dúvida, por favor, acesse a documentação [aqui](https://pettingzoo.farama.org/environments/classic/tictactoe/) ou pergunte ao professor da disciplina.

## Ambientes

Na [primeira aula](../01_introduction/index.md), perguntei quais são as principais dimensões do ambiente. Uma possível resposta para essa pergunta é:

* em termos de **observações** e **ações**, existem duas alternativas: **discreto** ou **contínuo**. Os dois problemas (ou seja, o motorista de táxi e o jogo da velha) que vimos até agora são discretos em termos de observações e ações porque não temos valores contínuos para observações ou ações.

* em termos de **dinâmica**, existem duas alternativas: **determinístico** ou **estocástico**. Em ambos os casos, o ambiente é determinístico porque sabemos o resultado de cada ação com 100% de confiança.

* em termos de **observação**, temos duas alternativas: **total** e **parcial**. Nós termos um cenário de observação parcial quando o agente não tem todas as informações necessárias em cada estado para alcançar o objetivo final. De acordo com essa definição, ambos os casos listados acima são completos em termos de observação.

* em termos de **agência**, existem duas alternativas: **single-agent** e **multi-agent**. Se temos apenas nosso agente executando no ambiente, então temos um ambiente de agente único, caso contrário, temos um ambiente *multi-agent*. Quando temos um ambiente *multi-agent*, podemos ter um ambiente competitivo (como tic-tac-toe, xadrez, go) ou um ambiente colaborativo - onde os agentes tentam alcançar o mesmo objetivo juntos.

## Algoritmos de busca competitiva

Algoritmos de busca competitiva são usados em ambientes multi-agent competitivos e determinísticos. Exemplos de jogos que se encaixam nessa categoria são xadrez, go, shogi, tic-tac-toe e connect-4. Esses jogos são determinísticos porque não têm movimento ou ação estocástica. Eles são exemplos de ambientes multi-agent competitivos, determinísticos, discretos e completos. Exemplos de jogos com movimentos estocásticos são blackjack e roleta.

O [algoritmo Min-Max](https://en.wikipedia.org/wiki/Minimax) é um exemplo de algoritmo de busca competitiva. Podemos usar um algoritmo Min-Max para desenvolver agentes capazes de jogar Connect-4 e Xadrez, por exemplo. No [site](http://fbarth.net.br/Connect4-Python/) é possível ver um tutorial completo sobre como criar um agente capaz de jogar Connect-4 usando o algoritmo Min-Max. 

## Exercício: implementação de um jogador de jogo da velha usando Min-Max

A proposta deste exercício é implementar um agente que pode jogar o jogo da velha e que nunca perde. O agente deve ser capaz de ganhar ou empatar em todas as situações.

Para isso, você deve considerar o código acima e completar a função definida abaixo: 

```python
def play_min_max_agent(agent, obs):
    # TODO you must implement your code here
    pass
```

## Entrega

* Este exercício deve ser feito por um grupo de no máximo 3 alunos.

* O prazo de entrega é dia **25/02/2024 até às 23:30**

* A implementação deve ser entregue via *Github classroom*. Este é o link [https://classroom.github.com/a/RTuXpCvk](https://classroom.github.com/a/RTuXpCvk).

* Você deve adicionar tudo o que é necessário para executar este projeto no repositório, como o arquivo README, o arquivo *requirements.txt* e o código.