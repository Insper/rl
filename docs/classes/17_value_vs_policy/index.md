# Value-based vs Policy-based Methods

Em aprendizagem por reforço (RL), as abordagens policy-based e value-based diferem no foco e no modo de aprender a estratégia ótima do agente. 

Nos métodos do tipo value-based, o agente aprende uma função de valor (ex.: $𝑄(𝑠,𝑎)$) que estima “o quão bom” é estar em um estado ou tomar uma ação. A política é derivada indiretamente, escolhendo sempre a ação com maior valor estimado ($policy = \arg\max_{a} Q(s,a)$). Exemplos de algoritmos que utilizam esta estratégia são Q-Learning e Deep Q-Learning (DQN). Esta abordagem é mais *sample-efficient* (aproveita melhor cada experiência) e funciona bem em espaço de ações discreto e pequeno. Em contrapartida, tem dificuldade com ações contínuas (o $\arg\max$ fica inviável) e também pode ficar instável ao aproximar funções de valor com redes neurais. 

Nos métodos do tipo policy-based, o agente aprende diretamente uma política ($\pi_{\theta}(a|s)$). Dado um estado $s$, a política $\theta$ fornece uma probabilidade maior para ações $a$ que levam a maiores recompensas. Ou seja, o agente mapeia estados para ações, sem a necessidade de uma função de valor intermediária. A política é geralmente parametrizada (ex.: por uma rede neural) e otimizada diretamente para maximizar a recompensa esperada. Exemplo de algoritmo que utiliza esta estratégia é o REINFORCE. Esta abordagem lida melhor com espaços de ação contínuos e pode aprender políticas estocásticas. No entanto, tende a ser menos *sample-efficient*.





