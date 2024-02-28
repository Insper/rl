# Revisão das implementações

## Review das entregas do Taxi driver

O objetivo deste exercício foi implementar um agente *taxi driver*. Um agente *taxi driver* pode pegar um passageiro em um ponto e deixar este passageiro em outro ponto considerando um mapa específico.

As soluções mais comuns apresentadas por esta turma foram: 

* **algoritmo de busca em largura**. Este algoritmo é **completo** e **ótimo**. No entanto, este algoritmo tem um alto requisito de memória em comparação com outros algoritmos, e a complexidade de tempo pode ser alta. Para este problema só funciona com mapas pequenos. 

* algoritmo **A Estrela** usando o pacote `AStar` ou implementado do zero. Este algoritmo usa o conceito de **heurísticas** para reduzir memória e tempo. Ele também é **completo** e **ótimo** desde que a heurística usada seja **admissível**. As heurísticas típicas para este tipo de problema são **distância manhattan** e **distância euclidiana**. Abaixo há um trecho de código usando o pacote `AStar`:  

```python
    def distance(n1, n2):
        return abs(n1[0]-n2[0]) + abs(n1[1]-n2[1])

    def cost(n, goal):
        return 1

    path1 = []
    if passenger != taxi:
        path1 = list(astar.find_path(taxi, passenger, neighbors_fnct=neighbors,
                    heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
    path2 = list(astar.find_path(passenger, target, neighbors_fnct=neighbors,
            heuristic_cost_estimate_fnct=cost, distance_between_fnct=distance))
    return path1 + path2
```

## Ambiente similar no projeto gymnasium

[Taxi Driver no Projeto Gymnasium](https://gymnasium.farama.org/environments/toy_text/taxi/)

```python
import gymnasium as gym
env = gym.make("Taxi-v3", render_mode='human').env

done = False
episodios = 1000

for i in range(episodios):
    state = env.reset()
    while not done:
        action = env.action_space.sample()
        next_state, reward, done, truncated, info = env.step(action)
```

## Implementações de jogadores de tic-tac-toe

O objetivo deste exercício foi implementar um jogador de **tic-tac-toe**. As soluções mais comuns apresentadas por esta turma foram: ...