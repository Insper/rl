# Algoritmo Reinforce

O objetivo deste grupo de aulas é explorar uma categoria de algoritmos de Reinforcement Learning baseados em *policy optimization*. 

Esta aula está dividida em duas etapas: 

* uma parte expositiva que irá utilizar o conjunto de slides abaixo, e;
* uma atividade onde o objetivo é implementar o algoritmo *Reinforce* ou uma versão do *Vanilla Policy Gradient*.

Para tanto, será utilizado este conjunto de slides para uma aula expositiva inicial: 

<embed src="reinforce_slides.pdf" type="application/pdf" width="600" height="300">

## Implementação em sala de aula

* Implemente uma versão do algoritmo Reinforce com base no pseudo-código deste material e com base nos trechos de códigos disponibilizados. 

* Não esqueça de coletar os dados para avaliar a curva de aprendizagem do agente. 

* Utilize os ambientes `MountainCar-v0`, `CartPole-v1` e `LunarLander-v3` para testar o algoritmo.

* Compare os resultados obtidos com o `DQN` e `Double DQN`. 

## Exemplo de funcionamento do algoritmo Reinforce

O código [reinforce_frozen_lake.py](./src/reinforce_frozen_lake.py) possui uma implementação do algoritmo Reinforce atuando no ambiente Frozen Lake determinístico. O objetivo deste código é mostrar o funcionamento do algoritmo Frozen Lake e algumas particularidades a utilização do modelo. 

Para ser mais fácil a visualização, algumas alterações foram feitas no ambiente e no algoritmo, entre elas: 

* alteração da função de reward;
* configuração do ambiente em modo determinístico, e;
* representação do estado como um vetor de tamanho 16. 

