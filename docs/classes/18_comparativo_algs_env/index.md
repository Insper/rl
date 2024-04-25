# Atividade de comparação

O objetivo desta atividade é comparar o desempenho de diferentes algoritmos de reinforcement learning em diferentes ambientes. 

Os algoritmos que serão comparados são: 

* DQN
* A2C
* PPO

Vamos utilizar as implementações da biblioteca [https://stable-baselines3.readthedocs.io/en/master/](https://stable-baselines3.readthedocs.io/en/master/).

Os ambientes que serão utilizados na comparação são: 

* Bipedal Walker
* Car Racing, discreto e contínuo
* CartPole
* Lunar Lander

Vamos utilizar os ambientes disponibilizados na biblioteca [https://gymnasium.farama.org/](https://stable-baselines3.readthedocs.io/en/master/)

## Matriz de comparação

[Documento com a matriz de comparação a ser executada nesta atividade](img/m.pdf)

Cada estudante da disciplina deverá selecionar uma comparação. Ou seja, uma célula da matriz de comparação.

## Repositório do projeto

Todas as análises deverão ser armazenadas em um único repositório: [https://github.com/fbarth/rl_compare](https://github.com/fbarth/rl_compare). Neste respositório já existe um exemplo de experimento e a estrutura inicial do repositório já está definida.

## Contribuições dos estudantes

Cada estudante deverá contribuir com a execução de um experimento. Esta contribuição deve ser na forma de **pull request** para o repositório do projeto.

Ao fazer o pull request o estudante deve incluir uma descrição clara sobre qual experimento está sendo executado, o arquivo python, o arquivo do modelo na pasta `models` e os resultados obtidos na pasta `results/<diretorio_especifico>`.

Cada **pull request** deve possuir os seguintes arquivos:

* Um arquivo python com o experimento. Este arquivo python deve ter o nome no formato `env_algoritmo.py`.
* O arquivo do modelo treinado na pasta `models` com o nome `env_algoritmo.zip`.
* Os arquivos de resultados na pasta `results/<diretorio_especifico>`.

Cada aluno deve encontrar a melhor configuração de hiperparâmetros para o algoritmo e ambiente escolhido.

## Prazo para entrega

O prazo para entrega desta atividade é 24/04/2024. No entanto, acredita-se que é possível finalizar a atividade durante a aula de hoje. 

