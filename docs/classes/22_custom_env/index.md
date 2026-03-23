# Criação de ambientes customizados

Para que o treinamento de um agente aconteça utilizando *reinforcement learning* é necessário, no mínimo, dois (2) componentes de software: 

* o agente ou o algoritmo de aprendizagem por reforço, e;
* o ambiente. 

O ambiente precisa ter a seguinte assinatura mínima: 

* `__init__` ou construtor; 
* `reset()` para a criação do estado inicial; 
* `step()` para a execução da ação. Basicamente, esta função step deve retonar o novo estado (consequência da execução da ação $a$ no estado atual), o $reward$ imediato e se o novo estado é terminal ou não; 
* uma função de `reward` que é codificada como parte da função `step`.

Existem diversas formas de se implementar um ambiente. Mas, a mais popular é usando o projeto `gymnasium`. 

## Proposta de atividade

Faça o *fork* do projeto [https://github.com/fbarth/gym_custom_env](https://github.com/fbarth/gym_custom_env) e siga o roteiro que está descrito no arquivo README.md deste repositório.

A última etapa do roteiro propõe o uso deste ambiente para problemas de *Coverage Path Planning* (CPP). O CPP é um problema de planejamento clássico onde o objetivo é encontrar um caminho que cubra uma área ou um conjunto de pontos. Este problema tem aplicações em diversas áreas, como robótica, logística e agricultura de precisão.

Para que este ambiente seja utilizado para problemas de CPP, é necessário obrigatoriamente mudar a função de `reward` para que o agente seja recompensado por cobrir novas células e punido por cobrir células já visitadas.

Você deverá: 

* criar um *branch* no seu repositório local pensando na implementação da nova função de `reward`; 
* documente a atual função de `reward` e a nova função de `reward` que você irá implementar. Este texto pode substituir o texto da última seção do arquivo `README.md` do repositório original;
* para escolher uma função de `reward` para ambientes de CPP, você pode se inspirar em trabalhos acadêmicos como: 

    * [A Deep Reinforcement Learning Approach for the Patrolling Problem of Water Resources Through Autonomous Surface Vehicles: The Ypacarai Lake Case](https://ieeexplore.ieee.org/document/9252944)
    * [A Comprehensive Survey on Coverage Path Planning for Mobile Robots in Dynamic Environments](https://ieeexplore.ieee.org/document/10946186)
  
* implemente a função de `reward` para o ambiente de CPP e teste o ambiente utilizando um agente aleatório. Em um primeiro momento, utilize um ambiente com dimensão pequena, como um grid 5x5, para facilitar a visualização do comportamento do agente;
* quando estiver satisfeito com a implementação, faça um *pull request* para o repositório original, e;
* no texto do *pull request* coloque o nome de quem participou da implementação. Esta atividade pode ser feita individualmente, em duplas ou trios. 

O prazo para envio dos *pull requests* é o dia **01 de abril de 2026**.