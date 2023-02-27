from django.shortcuts import render
import banana_dev as banana
from django.http import JsonResponse
from django.conf import settings
from .utils import BloomzSnippetGenerator, GPTJSnippetGenerator


# Generate a headline or teaser depending on gen_type parameter with a given fulltext
def generate(request):
  model = request.GET.get('model')
  fulltext = request.GET.get('fulltext')
  gen_type = request.GET.get('gen_type')

  if model == "gptj":
    generator = GPTJSnippetGenerator()
    output = generator.generate(gen_type, fulltext)
  
  elif model == "bloomz":
    generator = BloomzSnippetGenerator()
    output = generator.generate(gen_type, fulltext)
  
  else:
    raise Exception(f"Sorry, model {model} is unknown")

  return JsonResponse({"output": output})