## Web App
### How to get started

1. Folllow the instructions in the [model-server](https://github.com/snipaid-nlg/gptj-title-teaser-10k) repository to setup the model server.
2. Clone this repository.
```
git clone https://github.com/snipaid-nlg/demo.git
```
3. Change directory to project directory.
```
cd demo
```
4. Create a file with the name ".env".
5. Insert the following content into the ".env" file. Replace Your-Personal-Banana-Api-Key, Your-Personal-Banana-Model-Key and Your-Strong-Secret-Key-For-Django with your own secret keys.
```
# Secret key for Django (at least 6 characters)
SECRET_KEY=Your-Strong-Secret-Key-For-Django

# API Key for Banana (copy from Banana)
BANANA_API_KEY=Your-Personal-Banana-Api-Key

# API Key for Model (copy from Banana)
BANANA_MODEL_KEY=Your-Personal-Banana-Model-Key
```
6. Build and run with docker.
```
docker compose up --build
```
7. Visit http://localhost:8000 to see if SnipAId is running.
8. Copy a text and generate some titles and teasers!

### Snippet Quality

SnipAId is build on GPT-J, an Open Source Model from the GPT family. The core functionality of GPT models is taking a string of text and predicting the next token. When generating text with SnipAId please keep in mind, that the statistically most likely next token is often not the token that produces the most "accurate" text. Never depend upon those models to produce factually accurate output!

**We recommend having a human curate or filter the outputs before releasing them, \
both to censor undesirable content and to improve the quality of the results.**

See also [limitations and biases](https://huggingface.co/EleutherAI/gpt-j-6B#limitations-and-biases) of GPT-J.
