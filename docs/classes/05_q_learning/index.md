# Q-Learning Algorithm
    
## Definition and key concepts

In this class we will the slides below: 

<embed src="reinforcementLearning.pdf" type="application/pdf" width="600" height="300">

## Implementation

After a brief explanation of definitions and key concepts, we will implement the first agent using reinforcement learning. Please, follow the instructions below: 

### Clone the project and configure your machine

All the code necessary for this subject will be at [https://github.com/Insper/rl_code](https://github.com/Insper/rl_code). Faça o clone ou fork do projeto na sua máquina. Para esta atividade vamos utilizar os códigos que estão em `src/part_01`.

O processo recomendado é criar um ambiente virtual (*virtualenv*). Na pasta `src/part_01/`, digite: 

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements_part_01.txt
````

### Trabalhe com o arquivo TaxiDriverGym_introduction.py

* Leia a descrição do ambiente em [https://gymnasium.farama.org/environments/toy_text/taxi/](https://gymnasium.farama.org/environments/toy_text/taxi/).

* No diretório `src/part_01`, abra o arquivo `TaxiDriverGym_introduction.py`.

* Execute cada um dos comandos que estão no arquivo `TaxiDriverGym_introduction.py` em um interpretador python para entender o que o que é environment, reward e action. Além de entender detalhes do ambiente. 

* Quantos espaços possíveis o ambiente Taxi-v3 possui? 

* Quantas ações o agente que atua no ambiente Taxi-v3 possui? 

* O que a variável reward retornada por `env.step(<number>)` significa? 

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
    state = self.env.reset()
    reward = 0
    done = False
    actions = 0

    while not done:
        action = self.select_action(state)
        next_state, reward, done, _ = self.env.step(action) 
        
        # Adjust Q value for current state
        old_value = #pegar o valor na q-table para a combinacao action e state
        next_max = #np.max(`do maior valor considerando next_state`)
        new_value = #calcula o novo valor
        self.q_table[state, action] = new_value
                
        # atualiza para o novo estado
        state = next_state
````

que é responsável por execurtar *N* episódios e atualizar a variável `self.q_table`. 

Este método é chamado pelo arquivo `TaxiDriverGym.py` nas linhas 11 e 12:

````python
# only execute the following lines if you want to create a new q-table
qlearn = QLearning(env, alpha=0.1, gamma=0.6, epsilon=0.7, epsilon_min=0.05, epsilon_dec=0.99, episodes=100000)
q_table = qlearn.train('data/q-table-taxi-driver.csv', 'results/actions_taxidriver')
#q_table = loadtxt('data/q-table-taxi-driver.csv', delimiter=',')
````

Atividades: 

1. Complete o código do método `train` em `QLearning.py`. 

2. Execute o arquivo `TaxiDriverGym.py` com o comando:

````bash
python TaxiDriverGym.py
````

Lembre-se que nesta execução o programa irá criar toda a Q-table e armazenar no arquivo data/q-table-taxi-driver.csv. Depois de calcular os valores para a Q-table o programa irá resolver um dos possíveis cenários considerando um estado inicial qualquer. Além disso, o programa irá gerar um plot no diretório results que descreve a quantidade de ações executadas em cada época. 

3. Abra o arquivo `src/part_01/results/action_taxidriver.jpg` e faça uma análise do mesmo. O que este gráfico representa?

4. Agora faça o algoritmo `TaxiDriverGym.py` ler a Q-table a partir do arquivo gerado anteriormente e veja qual é o comportamento. Execute diversas vezes.

5. Qual é o comportamento do agente? Ele sempre consegue encontrar uma solução? As soluções parecem ser ótimas?  

Considerando os valores informados nos parâmetros do método `train`, se a sua implementação do `Q-learning` estiver correta então o agente `TaxiDriverGym.py` deve encontrar a solução para todos os casos apresentados. Se por algum motivo a sua solução não estiver convergindo então significa que tem algum *bug* na atualização da q-table. 

Uma vez que você confirmou que a sua implementação não tem *bugs* então você pode ajustar alguns dos hiperparâmetros. Por exemplo, diminuindo a quantidade de episódios e analisando a Q-table gerada. 

6. O arquivo `src/part_01/results/action_taxidriver.jpg` é um plot da quantidade de episódios versus a quantidade de atividades. Teria alguma outra forma de visualizar a evolução do agente? E se usarmos `rewards` ao invés da quantidade de atividades? A visualização fica melhor? 