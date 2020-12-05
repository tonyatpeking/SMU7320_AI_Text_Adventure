# %%
import torch
from transformers import pipeline, set_seed, AutoTokenizer
import random
import os
import sys
from config import (STARTING_TEXT_SPACE,
                    STARTING_TEXT_FANTASY,
                    STARTING_TEXT_MORNING,
                    TEXT_SEGMENTS_TO_CONSIDER,
                    TEXT_TO_GENERNERATE)

# %%
# check if cuda is available
print(torch.cuda.is_available())

# %%

MODEL = 'gpt2'

tokenizer = AutoTokenizer.from_pretrained(MODEL)

random.seed()
set_seed(random.randrange(99999))

text_generator = pipeline('text-generation', model=MODEL)


def clear_screen():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def get_text_to_consider():
    text_to_consider = ' '.join(all_text[-TEXT_SEGMENTS_TO_CONSIDER:])
    return text_to_consider


def get_all_text_as_str():
    text = ' '.join(all_text)
    return text

# %%


all_text = None
clear_screen()

init_input = input(
    'Choose a start: \n1: Space Opera \n2: Fantasy Adventure \n3: Normal Morning \nOr just type your own prompt \n>>>')
if init_input == '1':
    all_text = STARTING_TEXT_SPACE
elif init_input == '2':
    all_text = STARTING_TEXT_FANTASY
elif init_input == '3':
    all_text = STARTING_TEXT_MORNING
else:
    all_text = [init_input]

while(True):

    set_seed(random.randrange(99999))

    text_to_consider = get_text_to_consider()

    prompt_tokens = tokenizer.tokenize(text_to_consider)

    max_length = len(prompt_tokens) + TEXT_TO_GENERNERATE

    text_samples = text_generator(text_to_consider,
                                  do_sample=True,
                                  max_length=max_length,
                                  top_k=50,
                                  top_p=0.95,
                                  num_return_sequences=3)
    clear_screen()
    print('>>> The story so far <<<\n')
    print(get_all_text_as_str())

    text_samples = [sample['generated_text'][len(text_to_consider):]
                    for sample in text_samples]

    print('\n>>> Choose what happens next or type in custom text <<<\n')
    for i, sample in enumerate(text_samples):
        print('[{i}]: {sample}\n'.format(i=i, sample=sample))

    new_text = None

    user_input = input('>>>')

    if user_input == 'exit':
        file = open(r'exported_text.txt', 'w+')
        file.write(get_all_text_as_str())
        file.close()
        sys.exit()

    valid_options = list(range(len(text_samples)))
    if len(user_input) == 1 and user_input.isdigit() and (int(user_input) in valid_options):
        new_text = text_samples[int(user_input)]
    else:
        new_text = user_input

    all_text.append(new_text)


# %%
