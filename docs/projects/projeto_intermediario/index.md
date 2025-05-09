# Projeto intermediário

Neste semestre, o projeto intermediário da disciplina de Aprendizagem por Reforço terá dois tópicos possíveis:

1. **AWS DeepRacer**
2. **Uso de Aprendizagem por Reforço em problemas de Coverage Path Planning**

Ambos os tópicos terão suas entregas finais na primeira semana de maio de 2025, mas as regras e orientações para cada um deles são diferentes.

Abaixo é descrito o escopo de cada um dos tópicos.

## AWS DeepRacer

O AWS DeepRacer é uma plataforma de aprendizado por reforço que permite treinar e avaliar modelos de condução autônoma em um ambiente simulado. O objetivo do projeto é treinar um agente para dirigir um carro em uma pista, utilizando técnicas de aprendizado por reforço.

Este ambiente é utilizado em competições de aprendizado por reforço, onde os participantes podem treinar seus modelos e competir em corridas virtuais. Neste ano, no congresso da SBC, haverá uma competição de AWS DeepRacer, e o projeto intermediário será uma preparação para essa competição.

Mais informações sobre a competição podem ser encontradas no site oficial do evento: [AWS DeepRacer na SBC 2025](https://csbc.sbc.org.br/2025/aws-deepracer). 

Se o aluno optar por este tópico então ele deve se inscrever na competição e seguir as regras e orientações do evento. Neste caso, o projeto deverá ser individual pois esta é uma regra da competição.

Datas importantes:

* Workshop 1 – 28/02/2025 (sexta-feira) às 17h30;
* Workshop 2 – 28/03/2025 (sexta-feira) às 10h;
* Workshop 3 - 28/04/2025 (segunda-feira) às 15h;
* Corrida virtual de classificação – 5 a 9 de maio;
* Corridas físicas – 20 a 23 de julho.

## Uso de Aprendizagem por Reforço em problemas de Coverage Path Planning

Coverage Path Planning (CPP) é um problema de planejamento de trajetória em que um agente deve percorrer uma área de forma a cobrir completamente essa área. O objetivo do projeto é aplicar técnicas de aprendizado por reforço para resolver problemas de CPP, utilizando ambientes simulados.

O projeto pode ser realizado em grupos de até 2 alunos.

A equipe pode escolher entre os seguintes ambientes:

* [DSSE - coverage environment](https://pfeinsper.github.io/drone-swarm-search/Documentation/docsCoverage.html#about)
* Criar um [ambiente customizado](https://gymnasium.farama.org/introduction/create_custom_env/) para esta tarefa.
* Adaptar um ambiente já existente (https://github.com/zuoxingdong/mazelab).

O objetivo deste projeto é treinar um agente ou um grupo de agentes para resolver o problema de CPP em um ambiente simulado. O ambiente simulado deve ser um ambiente 2D com dimensões variadas. O agente deve ser capaz de aprender a percorrer a área de forma eficiente, cobrindo toda a área e evitando obstáculos.

Um exemplo de estudo é apresentado em artigo que está no blackboard da disciplina. 

## Prazo para definição do tema

O aluno deve escolher o tema do projeto até o dia 8 de abril de 2025. O aluno deve enviar um e-mail para o professor com o tema escolhido e a equipe (se houver) até essa data.

## Relatório

Para ambos os casos será necessário entregar um relatório técnico com o projeto finalizado. O relatório deve ter no máximo 2 páginas, em formato PDF, e deve ser enviado até 10 de maio de 2025, às 23h59. O relatório deve ser submetido via Github Classroom no link [https://classroom.github.com/a/7dqEOHcz](https://classroom.github.com/a/7dqEOHcz) com os demais artefatos, se for o caso.

O relatório deve conter os seguintes tópicos:

* Contexto e objetivo do projeto;
* Descrição do método utilizado, e;
* Resultados obtidos.

No dia 12 de maio de 2025 as equipes deverão fazer uma apresentação de 10 minutos sobre o projeto, com 5 minutos para perguntas. 

## Vídeo

Cada equipe deverá gravar um vídeo de até 10 minutos apresentando os resultados do projeto. O vídeo deve ser colocado em alguma plataforma de vídeo (YouTube, Vimeo, etc.) e o link deve ser enviado junto com o relatório no repositório do projeto. De preferência, colocar o link para o vídeo no README do repositório. O vídeo deve conter os seguintes tópicos:

* Contexto e objetivo do projeto;
* Descrição do método utilizado;
* Resultados obtidos;
* Demonstração do funcionamento do agente.


## Considerações para quem escolheu o tópico CPP

Existem dois caminhos para a execução deste projeto: 

1. fazer uso da biblioteca DSSE. Neste caso, sugiro fortemente testar a instalação desta biblioteca o mais rápido possível pois ela tem inúmeras dependências que podem dar problemas; 

2. utilizar um ambiente customizado. Neste caso, sugiro utilizar o roteiro disponível em [https://github.com/fbarth/gym_custom_env](https://github.com/fbarth/gym_custom_env). 