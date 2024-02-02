# Reinforcement Learning 

This repository has the Reinforcement Learning subject material. 

## Offerings

* 2024/1 - Fabrício Barth
* 2023/1 - Fabrício Barth
* 2022/2 - Fabrício Barth

## How to setup the environment

```bash
python3.7 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## How to compile slides using Markdown with beamer

```bash
pandoc -t beamer slides.md -o slides.pdf
```

## How to compile slides using only LaTeX

There are some slides in this project that I made using only LaTeX with Beamer. In this case, I use the TexStudio editor to edit and compile it. 

## How to deploy the web page

```bash
mkdocs gh-deploy
```

## How to run the web server locally

```bash
mkdocs serve
```

## How to publish the lessons plan

```bash
python publish_lessons_plan.py
```


