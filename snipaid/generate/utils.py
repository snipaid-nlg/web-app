import banana_dev as banana
from django.conf import settings

class SnippetGenerator:

    def clean_headline(self, output):
        output = output.split('\n')[0]
        output = output.split('.')[0]
        output = output.split('?')[0]
        output = output.split('!')[0]
        return output
    
    def clean_text(self, output):
        output = ".".join(output.split('.')[:-1])
        output += '.'
        return output

class GPTJSnippetGenerator(SnippetGenerator):
    MODEL_KEY = settings.BANANA_MODEL_KEY_GPTJ
        
    # Instance method to generate a headline for a fulltext with gptj model.
    def generate_headline(self, fulltext):
        # define inputs
        model_inputs = {
            "prompt": f'[Text]:{fulltext}\n\n[Titel]:',
            "temperature": 1.0, 
            "top_p": 0.7,
            "num_beams": 1,
            "max_new_tokens": 60,
            "do_sample": True
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.split("[Titel]:")[1]
        output = self.clean_headline(output)
        return output

    # Instance method to generate a teaser for a fulltext with gptj model.
    def generate_teaser(self, fulltext):
        # define inputs
        model_inputs = {
            "prompt": f'[Text]:{fulltext}\n\n[Teaser]:',
            "temperature": 1.0, 
            "top_p": 0.7,
            "num_beams": 1,
            "max_new_tokens": 150,
            "do_sample": True
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.split("[Teaser]:")[1]
        output = self.clean_text(output)
        return output
    
    def generate(self, gen_type, fulltext):
        if gen_type == "headline":
            return self.generate_headline(fulltext)
        elif gen_type == "teaser":
            return self.generate_teaser(fulltext)
        else:
            raise Exception(f"Sorry, unknown gentype {gen_type} for gptj model.")
    
class BloomzSnippetGenerator(SnippetGenerator):
    MODEL_KEY = settings.BANANA_MODEL_KEY_BLOOMZ

    # Instance method to generate a headline for a fulltext with bloomz model.
    def generate_headline(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "\nWhat is the best title for this article? ",
            "params": {
                "min_new_tokens": 3,
                "max_new_tokens": 20,
                "length_penalty": 1.0,
                "no_repeat_ngram_size": 0,
                "repetition_penalty": 1.0,
                "diversity_penalty": 0.0,
                "num_beam_groups": 1,
                "do_sample": False,
                "temperature": 1.0,
                "early_stopping": False,
                "pad_token_id": 3,
                "eos_token_id": 2,
                "num_return_sequences": 1,
                "top_k": 50, 
                "top_p": 0.75
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = self.clean_headline(output)
        return output
    
    # Instance method to generate a teaser for a fulltext with bloomz model.
    def generate_teaser(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "\nWrite a one or two sentence news hook/teaser/lede/bait: ",
            "params": {
                "min_new_tokens": 30,
                "max_new_tokens": 60,
                "top_k": 50, 
                "top_p": 0.75,
                "no_repeat_ngram_size": 2,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up outputs
        output = self.clean_text(output)
        return output
    
    # Instance method to generate a summary for a fulltext with bloomz model.
    def generate_summary(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "\nSummary in two to three sentences: ",
            "params": {
                "min_new_tokens": 50,
                "max_new_tokens": 150,
                "top_k": 50, 
                "top_p": 0.75,
                "no_repeat_ngram_size": 2,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up outputs
        output = self.clean_text(output)
        return output
    
    # Instance method to generate a summary for a fulltext with bloomz model.
    def generate_keywords(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "\nKeywords: ",
            "params": {
                "min_new_tokens": 1,
                "max_new_tokens": 80,
                "repetition_penalty": 1.05,
                "top_k": 50, 
                "top_p": 0.75
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        return output
    
    def generate(self, gen_type, fulltext):
        if gen_type == "headline":
            return self.generate_headline(fulltext)
        elif gen_type == "teaser":
            return self.generate_teaser(fulltext)
        elif gen_type == "summary":
            return self.generate_summary(fulltext)
        elif gen_type == "keywords":
            return self.generate_keywords(fulltext)
        else:
            raise Exception(f"Sorry, unknown gentype {gen_type} for bloomz model.")
        
class IgelSnippetGenerator(SnippetGenerator):
    MODEL_KEY = settings.BANANA_MODEL_KEY_IGEL

    # Instance method to generate a headline for a fulltext with igel model.
    def generate_headline(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "Welche Überschrift passt am besten zum Inhalt des Artikels?",
            "params": {
                "min_new_tokens": 3,
                "max_new_tokens": 20,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.replace("<|endoftext|>", "")
        return output
    
    # Instance method to generate a teaser for a fulltext with igel model.
    def generate_teaser(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "Generiere einen Teaser zu folgendem Artikel.",
            "params": {
                "min_new_tokens": 30,
                "max_new_tokens": 60,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.replace("<|endoftext|>", "")
        return output
    
    # Instance method to generate a summary for a fulltext with igel model.
    def generate_summary(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "Fasse den folgenden Artikel in wenigen Sätzen zusammen.",
            "params": {
                "min_new_tokens": 50,
                "max_new_tokens": 150,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.replace("<|endoftext|>", "")
        return output
    
    # Instance method to generate a summary for a fulltext with igel model.
    def generate_keywords(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "Nenne die zehn wichtigsten Keywords aus dem Text.",
            "params": {
                "min_new_tokens": 50,
                "max_new_tokens": 150,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.replace("<|endoftext|>", "")
        return output
    
    # Instance method to generate a derp for a fulltext with igel model.
    def generate_serp(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "Wie könnten Title-Tag und Meta-Description auf der SERP zu diesem Artikel lauten?",
            "params": {
                "min_new_tokens": 50,
                "max_new_tokens": 90,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.replace("<|endoftext|>", "")
        return output
    
    # Instance method to generate a tweet for a fulltext with igel model.
    def generate_tweet(self, fulltext):
        # define inputs
        model_inputs = {
            "task_prefix": "",
            "document": fulltext,
            "prompt": "Schreibe einen Tweet über den Artikel.",
            "params": {
                "min_new_tokens": 50,
                "max_new_tokens": 150,
            }
        }
        # generate
        out = banana.run(settings.BANANA_API_KEY, self.MODEL_KEY, model_inputs)
        output = out['modelOutputs'][0]['output']
        # clean up output
        output = output.replace("<|endoftext|>", "")
        return output
    
    def generate(self, gen_type, fulltext):
        if gen_type == "headline":
            return self.generate_headline(fulltext)
        elif gen_type == "teaser":
            return self.generate_teaser(fulltext)
        elif gen_type == "summary":
            return self.generate_summary(fulltext)
        elif gen_type == "keywords":
            return self.generate_keywords(fulltext)
        elif gen_type == "serp":
            return self.generate_serp(fulltext)
        elif gen_type == "tweet":
            return self.generate_tweet(fulltext)
        else:
            raise Exception(f"Sorry, unknown gentype {gen_type} for igel model.")
    