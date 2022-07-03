from utils import Dataset

# Open markup file
with open('chatbot-cont.md', 'r') as file:
    output = Dataset(file.read())
    output.removeComments()
