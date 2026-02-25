# Q-Learning Algorithm

## Definições e conceitos chave    

Nesta aula vamos utilizar os slides abaixo:

<embed src="q_learning_v2.pdf" type="application/pdf" width="800" height="400">

## Implementação

Depois de uma breve conversa sobre os principais conceitos, siga as instruções abaixo:

1. Utilize como base o código que você implementou na [aula anterior](../04_toolings_envs/index_pt.md).
2. Considere apenas o ambiente do *Taxi Driver*.
3. Na linha 8 `agent.update(action, state, reward)`, implemente a equação de Bellman para atualizar os valoes da Q-table. 
4. Implemente a linha 6 `action = agent.select_action(state)` para selecionar a ação com base na política epsilon-greedy.
5. Detalhe importante: a variável `state` da linha 6 é o estado atual, e a variável `state` da linha 7 é  de fato o `next_state`. 
6. Persista a Q-table em um arquivo de formato CSV.
7. Para cada episódio use uma variável que armazena a recompensa acumulada da trajetória executada naquele episódio. Basicamente, você vai ter que inicializar esta variável com zero no início de cada episódio e atualizá-la a cada ação tomada com o reward recebido. 
8.  Ao final de cada ação executada pelo agente não esqueça de atualizar o estado atual com o `next_state`. 
9.  Ao final de cada episódio, registre a recompensa acumulada em um arquivo de log onde você irá informar o número do episódio e a recompensa acumulada.

O script implementado acima deve gerar:

* um arquivo de log com o número do episódio e a recompensa acumulada, e;
* um arquivo com a Q-table.

Crie mais dois artefatos de software que: 

* imprime a curva de aprendizado do agente. A curva de aprendizado do agente precisa ser um gráfico que mostra o número do episódio no eixo x e a recompensa acumulada no eixo y.
* faz uso da Q-table para executar o agente no ambiente do *Taxi Driver*. O agente deve ser capaz de executar o ambiente sem treinamento.

Depois de treinado o agente, recomenda-se executar o agente treinado em modo gráfico para verificar se o agente realmente aprendeu a atuar no ambiente.

Você deverá testar três (3) configurações diferentes para os valores de $\alpha$, $\epsilon$ e $\gamma$. Para cada configuração, você deve gerar os artefatos de software descritos acima.

No arquivo README.md do projeto você deve adicionar uma seção de análise dos resultados obtidos. Nesta seção, você deve comparar as três configurações diferentes para os valores de $\alpha$, $\epsilon$ e $\gamma$. Para isso, você deve comparar as curvas de aprendizado obtidas para cada configuração. Você deve analisar qual configuração apresentou a melhor curva de aprendizado e justificar o motivo.

Você deve indicar no arquivo README.md qual é a melhor Q-table obtida para o ambiente do *Taxi Driver* e justificar o motivo.

## Entrega

Coloque todos os arquivos em um mesmo projeto e submeta-os para o [https://classroom.github.com/a/opNo2-Dk](https://classroom.github.com/a/opNo2-Dk). Esta atividade é individual e o **prazo é 02/03/2026 23:30.** Eventualmente, você não conseguirá terminar a atividade no tempo estipulado. Neste caso, submeta o que você conseguiu fazer. No arquivo README.md você deve informar o que está faltando. 