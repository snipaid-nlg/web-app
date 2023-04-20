from django.shortcuts import render
import banana_dev as banana
from django.http import JsonResponse
from .utils import BloomzSnippetGenerator, GPTJSnippetGenerator, IgelSnippetGenerator


# Generate a headline or teaser depending on gen_type parameter with a given fulltext
def generate(request):
  model = request.GET.get('model')
  fulltext = request.GET.get('fulltext')
  gen_type = request.GET.get('gen_type')

  if model == "gptj":
    generator = GPTJSnippetGenerator()
  
  elif model == "bloomz":
    generator = BloomzSnippetGenerator()

  elif model == "snip-igel":
    generator = IgelSnippetGenerator()
  
  else:
    raise Exception(f"Sorry, model {model} is unknown")
  
  output = generator.generate(gen_type, fulltext)
  return JsonResponse({"output": output})