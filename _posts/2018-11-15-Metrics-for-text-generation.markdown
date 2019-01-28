---
layout: post
title: Metrics for Text Generation Model Evaluations
date: 2018-11-15
excerpt : "An introduction to automatic evaluation metrics that are generally used in Natural Language Generation to meausure model quality."
<!-- comments: true -->
---

With the advent of deep learning and it's ubitquitous use in NLP tasks, a lot of previously unthought and impossible-seeming problems are now being attempted and solved (to some extent). A major area of research and industry application is text generation, formally known as Natural Language Generation(NLG). This includes various tasks, the most famous among these is Machine Translation : converting text of one language to another language like English to French. Other important and popular problems in the NLG domain are dialog systems, summarisation and question answering, to name a few.

I will discuss one of the basic requirements for modelling generation problems, one which is important for tackling any Machine Learning task - defining evaluation metrics for measuring the quality of outputs by a system. In the following part, I'll list some of the widely used metrics in NLG. For measuring a sytem, multiple of these can be used to report different aspects of model's abilities.

I will first talk about some common terms used in this post. Firstly, to check evalutions in NLG, Machine generated texts are usually evalutated against a target text(truth value). This target text is the final text that the model is expected to produce. Here on 'generated text' would mean the machine produced texts(output of the model) and 'target or reference text' would refer to the original text to be compared with. Some other basic terms are n-gram and bag of the words modelling which are basic nlp concepts/terms. You can read about them online if you are not averse with them.

### BLEU : Bilingual Evaluation Understudy Score 
BLEU and Rouge are the most popular evalutation metrics that are used to compare models in the NLG domain. Every NLG paper will surely report these metrics on the standard datasets, always. BLEU is a precision focused metric that calculates n-gram overlap of the reference and generated texts. This n-gram overlap means the evalution scheme is word-position independent apart from n-grams term associations. Also, in BLEU, there is a brevity penalty i.e. if the generated text is too small compared to the target text.

### Rouge : Recall Oriented Understudy for Gisting Evaluation
Rouge, as mentioned earlier, is another widely reported metric. It is a very common practice to report Rouge along with BLEU scores for standard tasks. It is very similar to BLEU definition, difference being that Rouge is recall focused whereas BLEU was precision focused. There are 3 types of Rouge : n-rouge, the most common rouge type which means n-gram overlap. eg.(2-rouge, 1-rouge). Second is l-rouge which checks for Longest Common Subsequence instead of n-gram overlap. Third is s-rouge which focuses on skip grams. Standard implementations of these can be found in most ML libraries, although only n-rouge is used primarily.

### Perplexity
Perplexity, another widely used metric, is used to give the highest Probability for a sentence to be produced by the model trained on a dataset. Lower the perplexity value, better the mdoel. Perplexity is normalised on the length of sentences.<br>
$l=\frac{1} {m} \sum_{i=1}^{m} log(p(Sentence_i))$ where m = number of words.<br>
$Perplexity = 2^{-l}$ <br>
If the model is completely dumb(worst possilbe), perplexity = |v| where v is the vocabulary.

### LSA : Latent Semantic Analysis
LSA is used to calculate the semantic similarity of two texts based on the words they both contain. It uses word co-occurrence counts from a large corpus. It uses bag of words method for doing it, which is word position independent. Unlike other metrics, it doesn't punish word choice variation.

### METEOR : Metric for Evaluation of Translation with Explicit Ordering
METEOR works on word alignments. It computes one to one mapping of words in generated and reference texts. Traditionally, It uses the wordnet or porter stemmer. Finally, it computes an F-score based on these mappings. Meteor is a relatively lesser used metric in NLG, specially since the introduction of deep learning models.

### TER : Translation Edit Rate 
TER works on the principle of conversion of the generated text to the target text. 
$TER = \frac{number-of-edits} {word-length-of-Reference-text}$
TER works upon exact word matching. It helps to understand the absolute similarity among the reference and generated texts.

<br>
<br>

These are all the commonly used metrics used for NLG evaluations. You can read up more about them online if you need a more comprehensive explanation. I have written a python file to compute these metrics which can be found <a href="https://github.com/divishdayal/divishdayal.github.io/blob/master/assests/codes/evaluation_metrics.py">here</a>.