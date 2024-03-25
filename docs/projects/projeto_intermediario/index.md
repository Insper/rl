# Projeto intermediário

Segundo a literatura, o Double DQN não super valoriza o valor dos estados futuros. De fato, fornece estimativas mais realistas dos valores de ação. Isto tem algum impacto no aprendizado do agente? O aprendizado converge mais rápido? O aprendizado é mais estável? 

Sendo assim, a proposta desta atividade é **avaliar o impacto do Double DQN no aprendizado do agente**. Para tanto, cada equipe deverá treinar agentes usando os algoritmos DQN e Double DQN nos ambientes `LunarLander-v2` e `CartPole-v1` e comparar os resultados.

### Entrega básica

* Implementar o algoritmo Double Deep DQN e comparar os resultados com DQN nos ambientes `LunarLander-v2` e `CartPole-v1`.
* Executar no mínimo 5 treinamentos para cada algoritmo.
* No relatório apresentar: 
    * a curva de aprendizado na forma de um gráfico.
    * os hiperparâmetros utilizados.
* Os artefatos que devem ser entregues são: o código fonte, o relatório (preferencialmente na forma de arquivo `README.md`), o arquivo `requirements.txt` e os modelos treinados.

Ao fazer isto a equipe terá conceito **B**. 

### Entrega avançada

Para obter conceito **A+** nesta atividade a equipe deve incluir o treinamento de um agente para o ambiente [Flappy Bird](https://github.com/Talendar/flappy-bird-gym).

A mesma análise feita com os ambientes anteriores deve ser feita com o ambiente Flappy Bird. Para este ambiente a equipe deve prestar atenção especial no espaço de observação e consequentemente na arquitetura da rede neural.

## Deadline

O deadline para a entrega desta atividade é **05 de abril de 2024** às 23:30 horas. Este trabalho deve ser feito em grupo com até 4 integrantes.

## Referências

* [Material sobre Double DQN](../../classes/16_double_deep_q_learning/index.md)