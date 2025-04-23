# Criação de ambientes customizados

Para que o treinamento de um agente aconteça utilizando *reinforcement learning* é necessário, no mínimo, dois (2) componentes de software: 

* o agente ou o algoritmo de aprendizagem por reforço, e;
* o ambiente. 

O ambiente precisa ter a seguinte assinatura mínima: 

* `__init__` ou construtor; 
* `reset()` para a criação do estado inicial; 
* `step()` para a execução da ação. Basicamente, esta função step deve retonar o novo estado (consequência da execução da ação $a$ no estado atual), o $reward$ imediato e se o novo estado é terminal ou não; 
* uma função de `reward` que é codificada como parte da função `step`.

Existem diversas formas de se implementar um ambiente. Mas, talvez, a mais popular é usando o projeto `gymnasium`. 

## Proposta de atividade

Faça o clone do projeto [https://github.com/fbarth/gym_custom_env](https://github.com/fbarth/gym_custom_env) e siga o roteiro que está descrito no arquivo README.md deste repositório. 