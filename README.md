# Tensorflow Question Answer Web App
<img style="width: 100%;" src="screenshot.png">

## Introduction
Tensorflow QA is a Text-to-Text Transfer Transformer web app built using Tensorflow 2.0 and Django using the  (<a href="https://github.com/google-research/text-to-text-transfer-transformer">T5 Pretrained Models</a>).

## Features
<ul>
    <li>Train your own model or use the pretrained model (link below)</li>
    <li>Beautiful UI to interact with the app</li>
    <li>Uses Tensorflow 2.0</li>
</ul>

## Setup
Setup everything using the requirements.txt file. 
Just run ``` python3 -r requirements.txt ```

## Usage
If you have everything installed (including Tensorflow and Django) you just need to run:
``` python3 manage.py runserver ``` 
Then wait for it to process the dataset and load the model. 
Then all you need is to open 127.0.0.1:8000 and interact with the chatbot.

## Pretrained Models
You can find all the pretrained models and weights <a target="_blank" href="https://github.com/google-research/text-to-text-transfer-transformer#released-model-checkpoints">here.</a>