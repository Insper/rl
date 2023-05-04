# Proximal Policy Optimization (PPO)

Na primeira parte da aula vamos utilizar o conjunto de slides abaixo para entender o algoritmo PPO:

<embed src="ppo_slides.pdf" type="application/pdf" width="600" height="300">

## Proposta de atividade prática

Utilize a implementação do algoritmo PPO existente em [https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html) para implementar diversos agentes para diferentes ambientes. Faça uma análise se a política encontrada é uma política ótima, se demorou muito para treinar o agente e se a curva de aprendizado do agente é estável. 

Para aqueles que querem aprofundar ainda mais o seu conhecimento sobre o algoritmo PPO, proponho implementar o seu próprio algoritmo utilizando as referências citadas abaixo. Em especial este documento: [https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/).

## Referências

Para a produção deste material foram utilizadas as seguintes referências: 

* The 37 Implementation Details of Proximal Policy Optimization. Disponível [https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/). Último acesso em maio de 2023. 
		
* Schulman J, Levine S, Abbeel P, Jordan M, Moritz P. Trust region policy optimization. In International conference on machine learning 2015 Jun 1 (pp. 1889-1897). PMLR.v [https://doi.org/10.48550/arXiv.1502.05477](https://doi.org/10.48550/arXiv.1502.05477)
		
* Schulman J, Wolski F, Dhariwal P, Radford A, Klimov O. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347. 2017 Jul 20.
		
* Understanding Proximal Policy Optimization (Schulman et al., 2017). Disponível [https://blog.tylertaewook.com/post/proximal-policy-optimization](blog.tylertaewook.com/post/proximal-policy-optimization). Último acesso em maio de 2023. 
		
* Simonini, T. Proximal Policy Optimization (PPO). Unit 8, of the Deep Reinforcement Learning Class with Hugging Face. Disponível em [https://huggingface.co/blog/deep-rl-ppo](https://huggingface.co/blog/deep-rl-ppo). Último acesso em maio de 2023.