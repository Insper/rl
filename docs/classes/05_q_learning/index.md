# Algoritmo Q-Learning

## Definições e conceitos chave    

Nesta aula vamos utilizar os slides abaixo:

<embed src="reinforcementLearning.pdf" type="application/pdf" width="800" height="400">

## Implementação

Depois de uma breve conversa sobre os principais conceitos, vamos implementar o primeiro agente utilizando aprendizado por reforço. Por favor, siga as instruções abaixo:

* copie o arquivo [TaxiDriverGym.py](./src/TaxiDriverGym.py) para a sua máquina local. Este arquivo faz uso do ambiente `Taxi-v3` da biblioteca Gymanasium e do algoritmo Q-Learning. 

* copie o arquivo [QLearning.py](./src/QLearning.py) para a sua máquina local. Esta implementação está incompleta. Você terá que preencher o método `train` para que o algoritmo Q-Learning funcione corretamente. Mas antes disso, vamos entender a estrutura desta classe. 


### Arquivo QLearning.py

Este arquivo implementa o algoritmo Q-Learning. A classe implementada neste arquivo possui 4 métodos: 

* `__init__` (construtor): que recebe todos os hiperparâmetros do algoritmo Q-Learning e inicializa a Q-table com base no número de ações e estados informados pelo parâmetro *env*. Alguns destes hiperparâmetros não serão utilizados neste momento, mas vamos mantê-los. 

* `select_action`: dado um estado, este método seleciona uma ação que deve ser executada. 

* `train`: método responsável por executar as simulações e popular a **Q-table**. Este método retorna uma q-table, mas também atualiza um arquivo CSV com os dados da q-table e uma imagem que é um plot da quantidade de ações executadas em cada episódio. 

* `plotactions`: é um método que cria uma imagem com o plot da quantidade de ações executadas em cada episódio. 

### Atualizando os valores da Q-table

Dentro do método `train` tem-se o seguinte trecho de código: 

````python
for i in range(1, self.episodes+1):
    (state, _) = self.env.reset()
    rewards = 0
    done = False
    actions = 0

    while not done:
        #
        # escolher uma ação $a$ para um estado $s$
		# executar a ação $a$
		# observar a recompensa $r$ e o novo estado $s'$ 
		# Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{A'}Q(s',A') - Q(s,a)]
		# s recebe s'
        #
````

que é responsável por execurtar *N* episódios e atualizar a variável `self.q_table`. 

Este método é chamado pelo arquivo `TaxiDriverGym.py` nas linhas 11 e 12:

````python
qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
q_table = qlearn.train('data/q-table-taxi-driver.csv', 'results/actions_taxidriver')
#q_table = loadtxt('data/q-table-taxi-driver.csv', delimiter=',')
````

Atividades: 

* Complete o código do método `train` em `QLearning.py`. 

* Execute o arquivo `TaxiDriverGym.py` com o comando:

````bash
python TaxiDriverGym.py
````

Lembre-se que nesta execução o programa irá criar toda a Q-table e armazenar no arquivo `data/q-table-taxi-driver.csv`. Depois de calcular os valores para a Q-table o programa irá resolver um dos possíveis cenários considerando um estado inicial qualquer. Além disso, o programa irá gerar um plot no diretório results que descreve a quantidade de ações executadas em cada época. 

* Abra o arquivo `results/action_taxidriver.jpg` e faça uma análise do mesmo. O que este gráfico representa?

* Agora faça o algoritmo `TaxiDriverGym.py` ler a Q-table a partir do arquivo gerado anteriormente e veja qual é o comportamento. Execute diversas vezes.

* Qual é o comportamento do agente? Ele sempre consegue encontrar uma solução? As soluções parecem ser ótimas?  

Considerando os valores informados nos parâmetros do método `train`, se a sua implementação do `Q-learning` estiver correta então o agente `TaxiDriverGym.py` deve encontrar a solução para todos os casos apresentados. Se por algum motivo a sua solução não estiver convergindo então significa que tem algum *bug* na atualização da q-table. 

Uma vez que você confirmou que a sua implementação não tem *bugs* então você pode ajustar alguns dos hiperparâmetros. Por exemplo, diminuindo a quantidade de episódios e analisando a Q-table gerada. 

* O arquivo `results/action_taxidriver.jpg` é um plot da quantidade de episódios versus a quantidade de atividades. Teria alguma outra forma de visualizar a evolução do agente? E se usarmos `rewards` ao invés da quantidade de atividades? A visualização fica melhor? 

## Q-table pronta

Como resultado da etapa de treinamento, o agente terá uma *Q-table* que mostra a melhor ação que ele pode tomar em cada estado. A maneira de usar essas informações é muito simples:

```python
(state, _) = env.reset()
done = False
    
while not done:
    print(state)
    action = np.argmax(q_table[state])
    state, reward, done, truncated, info = env.step(action)
```

Aqui, o agente seleciona a ação com o maior valor em cada estado. Nós não temos nenhum comportamento aleatório. 






