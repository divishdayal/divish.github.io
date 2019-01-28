---
layout: post
title: Metrics for Text Generation Model Evaluations
date: 2018-01-15
excerpt : "An introduction to automatic evaluation metrics that are generally used in Natural Language Generation to meausure model quality."
<!-- comments: true -->
---

With the advent of deep learning and it's ubitquitous use in NLP tasks, a lot of previously unthought and impossible-seeming tasks are now being attempted and solved (to some extent). A major area of research is text generation, formally known as Natural Language Generation(NLG). This includes various tasks and problems, most famous among these is Machine Translation : converting text of one language to another language like English to French and so on. Other important and popular problems in the NLG domain are dialog systems, summarisation and question answering, to name a few.

I will discuss one of the basic requirement for modelling generation problems, one which is important for tackling any Machine Learning task - defining evaluation metrics for measuring the quality of outputs by a system. In the following part, I'll list some of the widely used metrics in NLG. For measuring a sytem, multiple of these can be used to report different aspects of model's abilities.

I will first talk about some common terms occuring in the rest of the post. Firstly, to check evalutions in NLG, Machine generated texts are usually evalutated against some target text(truth value), so 'generated text' means the machine produced texts(output of the model) and 'target or reference text' would mean the original text to be compared with.

<ul>
	<li>BLEU : Bilingual Evaluation Understudy Score </li>
	BLEU and Rouge, are the most popular evalutation metrics used to compare models in the NLG domain. Every NLG paper will report these metrics on the standard datasets, always. BLEU is a precision focused metric that calculates n-gram overlap of the reference and generated texts. This n-gram overlap means the evalution scheme is word-position independent apart from n-grams term associations. Also, in BLEU, there is a brevity penalty i.e. if the generated text is too small compared to the target text.
	<li>Rouge : Recall Oriented Understudy for Gisting Evaluation</li>
	Rouge, as mentioned earlier, is another widely reported metric. It is very common to be reported along with BLEU scores for standard tasks. It is almost same to BLEU definition, difference being Rouge is Recall focused whereas BLEU was precision focused. There are 3 types of Rouge : n-rouge, the most common rouge type which means n-gram overlap. eg.(2-rouge, 1-rouge). Second is l-rouge which checks for Longest Common Subsequence instead of n-gram overlap. Third is s-rouge which focuses on skip grams. Standard implementations of these can be found in most ML libraries.
	<li>Perplexity</li>
	<li>LSA : Latent Semantic Analysis</li>
	<li>METEOR : Metric for Evaluation of Translation with Explicit Ordering</li>
	<li>TER : Translation Edit Rate </li>
	TER checks for the absolute conversion of the generated text to target text. 
	$TER = \frac({number of edits} {word length of Reference text})$