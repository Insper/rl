# Comments about the Frozen Lake implementations 

In the table below there are some results from the Frozen Lake implementations done last week. 

| Feature	| André	| Beatriz |	Carlos Dip | Diogo | Eduardo	| Felipe | 	Henrique | 	Letícia	| Lucas	 | Matheus |	Nívea |
|:----------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|**algorithm**|	Sarsa	|Sarsa	|Sarsa	|Q-Learning	|Q-Learning	|Q-Learning	|Q Learning	|Sarsa	|Sarsa	|Sarsa	|Sarsa|
|**alpha**|	0.1	| 0.098 |	0.09	| 0.1 |	0.2 |	0.1 |	0.1 |	0.03 |	0.2 |	0.05 |	0.12|
|**gamma**|	0.99	|0.98	|0.9	|0.99	|0.999	|0.99	|0.9	|0.98	|1	|0.95|	0.99|
|**epsilon**|	1	|1	| 0.75 |	0.999 |	0.9	| 0.9999 |	1	| 0.98 |	1 |	0.95 |	0.9|
|**epsilon_dec**|	0.9999	|0.9999	|0.05	|0.9999	|0.9999	|0.99996	|0.9999	|0.9999	|0.99|	0.9999 |	0.9999|
|**epsilon_min**|	0.05	|0.05|	0.99|	0.0001|	0.001|	0.0001|	0.1	|0.0001|	0.5|	0.0001|	0.0001|
|**# episodes**|50000	| 35000 |	10000 |	30000 |	30000 |	100000 |	10000 |	18000 |	500000 |	20000 |	30000 |
|**% of sucess**|	91%|	89%|	99%|	96%|	100%|	99%|	91%|	86%|	97%|	81%|	94%|

*Important notes*: 

* Carlos Dip changed the reward values to emphasize negative rewards and speed up the training using Sarsa.
* Felipe did a very good evaluation of the epsilon decay impact. This evaluation is available [here](https://github.com/insper-classroom/frozen-lake-felipeschiavinato/blob/main/README.md).
* How did Eduardo's implementations get a 100% rate of success?   