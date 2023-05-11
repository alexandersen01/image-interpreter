import openai

image = input('Is the image local or online? (local/online) ')
if image == 'local':
    image = input('Enter the path to the image: ')
    extention = input('Enter the extention of the image: ')
    image = open(image, 'rb')
else:
    image = input('Enter the URL of the image: ')
    #grab the characters after the last period in the url
    extention = image.split('.')[-1]
    image = openai.Image(image)

response = openai.Answer.create(
    search_model="ada",
    model="curie",
    question="What is the name of the image?",
    examples_context="This is a photo of a",
    examples=[["a cat", "Furry feline"], ["a dog", "Furry canine"], ["a person", "Human"]],
    documents=[image],
    file=f"{image}.{extention}",
    max_rerank=10,
    max_tokens=5,
    stop=["\n", ""]
)

print(response)


