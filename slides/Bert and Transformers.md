# Bert and Transformers Presentation 

Hongjin Yu 47216615

## Table of contents

- [Bert and Transformers Presentation](#bert-and-transformers-presentation)
  - [Table of contents](#table-of-contents)
  - [What is the problem - sequential data](#what-is-the-problem---sequential-data)
  - [Past Methods](#past-methods)
  - [Markov Chain 1906 wiki](#markov-chain-1906-wiki)
    - [Example from reddit](#example-from-reddit)
  - [RNN 1986 - Recurrent Neural Network](#rnn-1986---recurrent-neural-network)
    - [Information loss from sequential pipeline](#information-loss-from-sequential-pipeline)
  - [LSTM 1997 - Long Short Term Memory](#lstm-1997---long-short-term-memory)
  - [GRU 2014 Gated Recurrent Unit](#gru-2014-gated-recurrent-unit)
  - [RNN + Attention 2014 Paper](#rnn--attention-2014-paper)
  - [Transformers 2017 Paper: Attention Is All You Need](#transformers-2017-paper-attention-is-all-you-need)
  - [BERT Paper: BERT Pre-training of Deep Bidirectional Transformers for Language Understanding 2018](#bert-paper-bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding-2018)
    - [Word Embedding](#word-embedding)
    - [Attention](#attention)
    - [Self Attention](#self-attention)
    - [Masked Self Attention](#masked-self-attention)
    - [Multi-Head Attention](#multi-head-attention)
  - [Example Use Cases](#example-use-cases)
  - [Timeline and size of models](#timeline-and-size-of-models)
  - [Code / Examples](#code--examples)
  - [Closing notes](#closing-notes)
    - [The Bitter Lesson](#the-bitter-lesson)
  - [References](#references)

## What is the problem - sequential data

We have a sequence of data and we want to predict the next data point

e.g.

Sentence completion, music composition, code generation, stock market, population dynamics, weather

## Past Methods

## Markov Chain 1906 [wiki][markov wiki]

![markov][markov chain img]

[Subreddit generated completely with Markov Chains][SubredditSimulator]

### Example from reddit

![reddit markov img][reddit markov img]

[source][reddit markov]

Pros:

- Simple to understand and implement
- Locally makes sense

Cons:

- Long sentences stop making sense
- Combinatorial explosion

## RNN 1986 - Recurrent Neural Network

![rnn][rnn img]
[source][rnn img]

Use case: Google translate

Pros:

- Better than Markov chain in long sequences

Cons:

- Long sequences still often don't make sense
- Vanishing gradients when training
- Forget the start of long sequences
- Hard to parallelize training
- Need large amounts of data
- Training bottleneck means diminishing returns

### Information loss from sequential pipeline

![back drawing][back drawing]
[source][back drawing url]

## LSTM 1997 - Long Short Term Memory

## GRU 2014 Gated Recurrent Unit

![lstm][lstm img]

[source][lstm img]

These are modified versions of RNNs with gates that can be set/reset

Pros:

- Forget and Remember gates can potentially have longer term memory
  
Cons:

- Still has most of the other cons of RNNs

## RNN + Attention 2014 [Paper][rnn attention]

![rnn attention img][rnn attention img]

[source][rnn attention img]

## Transformers 2017 [Paper: Attention Is All You Need][transformer paper]

## BERT [Paper: BERT Pre-training of Deep Bidirectional Transformers for Language Understanding 2018][bert paper]

![transformer][transformer architecture]

[source][transformer architecture]

### Word Embedding

![word embedding img][word embedding img]

[source][word embedding]

- Each word becomes a multidimensional vector (aka word vector)
- Similar words will be close together, useful for synonyms, antonyms
- Shifting along certain axis can give you related words, e.g. King - Queen, England - London
- Can be pre-generated (Word2Vec, GloVe) or learned during the training process
- Not unique to Transformers

### Attention

![attention][attention]

[source][transformer paper]

### Self Attention

`The animal didn't cross the street because it was too tired`

![self attention][self attention]

[source][self attention source]

### Masked Self Attention

![masked][masked]

[source][masked source]


### Multi-Head Attention

![multi head attention][multi head]

[source][self attention source]

Pros:

- Can parallelize training
- Unprecedented accuracy
- Transfer learning / Fine tuning / zero shot learning with pre-trained language models

Cons:

- Huge models
- Data hungry
- All the cons that come with DNNs: Black box, biases
- May take over the world

## Example Use Cases

[google search][google bert]

[complete the sentence][complete paris]

[dr. seuss (GPT-3)][dr seuss]

**Prompt: Here’s a poem by Dr. Seuss about Elon Musk launching rockets with SpaceX, building electric cars at Tesla, selling flame throwers, dating Grimes, fighting the SEC, crushing short sellers, building brain chips to fight AI, and colonizing mars, and tweeting at all hours of day and night. Musk wants to make humans interplanetary to prevent extinction. The poem rhymes every other line with an ABAB structure. The rhyme structure is typical of Dr. Seuss nursery rhymes.**

Elon Musk
By Dr. Seuss
Once there was a man
who really was a Musk.
He liked to build robots
and rocket ships and such.

He said, “I’m building a car
that’s electric and cool.
I’ll bet it outsells those
Gasoline-burning clunkers soon!”

They sell cool cars
that are electric and clean.
And then he wanted to go
even farther, you see.

The first Tesla, Roadster,
Was just the start of a bigger dream.
He said, “I’m building a plane
that’s electric and green.

That’s not all!
That man is also a Musk.
He likes electric cars,
flamethrowers, tunnels, and such.

But then he thought, “If we make
a very small, small chip,
We’ll implant it in our heads,
And then connect our minds to the Internet!”

But then, in his haste,
he got into a fight.
He had some emails that he sent
that weren’t quite polite.

The SEC said, “Musk,
your tweets are a blight.
They really could cost you your job,
if you don’t stop
all this tweeting at night.”

He replied, “Well, I do tweet
and it’s really quite neat.
and I’ll tweet in a while
and send you some sweet treats.”

But the SEC said, “Nay,
You can’t tweet anymore.
We’ll see you in court,
and you’ll pay a fine,
for the tweets that you wrote.”

Then Musk cried, “Why?
The tweets I wrote are not mean,
I don’t use all-caps
and I’m sure that my tweets are clean.”

“But your tweets can move markets
and that’s why we’re sore.
You may be a genius
and a billionaire,
but that doesn’t give you the right to be a bore!”

Then Elon Musk said,
“You’re not much fun.
And I don’t want to sue.
But I’ll tell you what I’ll do.
I’ll send my Mars Rovers
to red planet you.”

But then he thought, “But I don’t
want to start a fight.
Instead, I’ll just stick to building my cars
and launching rockets at night.”

And that’s what he did.
And the SEC said, “Fine.”
And Elon Musk said, “OK.
And the market was
A bit worried that day.
But the price of Tesla
Went up that same old way.

So you see,
Musk is just fine,
If you can ignore all the hype.
But if you trade Tesla,
The tweets might give you a fright.

But Tesla’s still going up
With each tweet and each post.
The shorts are getting so mad
That they’re going to burst!

And now Musk is building a spaceship
that can take us to Mars.
And he’ll soon be launching
some satellites to the stars.

And then we’ll really be
Interplanetary for sure.
And Musk’s tweets will continue
In space and on Earth.

[Improved subreddit using transformers][SubSimulatorGPT2]

![gtp2 reddit][gtp2 reddit]

[can do arithmetic][arithmetic]

[can code][can code]

## Timeline and size of models

![Turing-NLG][Turing-NLG]

[source][Turing-NLG]

![GPT3][GPT3]

[source][GPT3]

GPT3

- 175 billion parameters
- 12 million dollars to train

## Code / Examples

- Pre-trained model
- Choose your own adventure
- AI D&D Gamemaster

## Closing notes

### [The Bitter Lesson][bitter lesson]

- Rich Sutton
- March 13, 2019
- The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin.

## References

(References are in Bert and Transformers.md)

[markov wiki]: https://en.wikipedia.org/wiki/Markov_chain
[markov chain img]: https://miro.medium.com/max/519/1*3HSQl6UoNmnS1BgD5do_qg.png
[reddit markov img]: reddit_markov.PNG
[reddit markov]: https://www.reddit.com/r/SubredditSimulator/comments/hett6r/florida_man_refuses_to_pay_child_support_despite/

[SubredditSimulator]: https://www.reddit.com/r/SubredditSimulator/
[rnn img]: https://miro.medium.com/max/1739/1*iK8Wel75Ri55rSZfwAKHCA.jpeg
[lstm img]: https://upload.wikimedia.org/wikipedia/commons/5/5f/Gated_Recurrent_Unit.svg
[SubSimulatorGPT2]: https://www.reddit.com/r/SubSimulatorGPT2/
[gtp2 reddit]: gtp2_reddit.PNG
[transformer architecture]: https://miro.medium.com/max/3600/1*BHzGVskWGS_3jEcYYi6miQ.png

[rnn attention]: https://arxiv.org/abs/1409.0473
[rnn attention img]:https://miro.medium.com/max/700/1*wnXVyE8LXPfODvB_Z5vu8A.jpeg
[transformer paper]: https://arxiv.org/abs/1706.03762
[bert paper]: https://arxiv.org/abs/1810.04805

[bitter lesson]: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
[hugging face]: https://github.com/huggingface

[complete paris]: https://huggingface.co/bert-base-uncased?text=Paris+is+the+%5BMASK%5D+of+France
[Turing-NLG]: https://www.microsoft.com/en-us/research/uploads/prod/2020/02/TurningNGL_Model__1400x788.png
[GPT3]: https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4c9d108-0e5c-4a7f-83ed-beed232b0e65_1384x1264.png
[arithmetic]: https://medium.com/analytics-vidhya/a-simple-explanation-of-gpt-3-571aca61208c
[can code]: https://analyticsindiamag.com/open-ai-gpt-3-code-generator-app-building/
[dr seuss]: https://arr.am/2020/07/14/elon-musk-by-dr-seuss-gpt-3/

[back drawing]: back_drawing.png
[back drawing url]: https://www.youtube.com/watch?v=3hF0NnFbYP0

[word embedding img]: https://ruder.io/content/images/size/w2000/2016/04/word_embeddings_colah.png
[word embedding]: https://ruder.io/word-embeddings-1/

[self attention]: self_attention.png
[self attention source]: http://jalammar.github.io/illustrated-transformer/

[attention]: attention.png
[multi head]: multi_head_attention.png

[masked]: http://jalammar.github.io/images/gpt2/self-attention-and-masked-self-attention.png
[masked source]: http://jalammar.github.io/illustrated-gpt2/
[google bert]: https://www.searchenginejournal.com/google-bert-rolls-out-worldwide/339359/#close