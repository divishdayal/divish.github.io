
# coding: utf-8

# In[20]:


'''
Dependencies for this file:
    -> install pyter(https://github.com/aflc/pyter), using the following commands :
        git clone git://github.com/aflc/pyter.git
        cd pyter
        pip install -e .
        
        if the above command fails on linux: try installing pyter's dependency separately by : easy_install distribute
    -> nltk library : pip3 install nltk
    -> itertools (generally pre-installed in python)
'''


# In[12]:


from nltk.translate.bleu_score import SmoothingFunction, corpus_bleu, sentence_bleu


def bleu(ref, gen):
    ''' 
    calculate pair wise bleu score. uses nltk implementation
    Args:
        references : a list of reference sentences 
        candidates : a list of candidate(generated) sentences
    Returns:
        bleu score(float)
    '''
    ref_bleu = []
    gen_bleu = []
    for l in gen:
        gen_bleu.append(l.split())
    for i,l in enumerate(ref):
        ref_bleu.append([l.split()])
    cc = SmoothingFunction()
    score_bleu = corpus_bleu(ref_bleu, gen_bleu, weights=(0, 1, 0, 0), smoothing_function=cc.method4)
    return score_bleu


# In[14]:


#rouge scores for a reference/generated sentence pair
#source google seq2seq source code.

import itertools

#supporting function
def _split_into_words(sentences):
  """Splits multiple sentences into words and flattens the result"""
  return list(itertools.chain(*[_.split(" ") for _ in sentences]))

#supporting function
def _get_word_ngrams(n, sentences):
  """Calculates word n-grams for multiple sentences.
  """
  assert len(sentences) > 0
  assert n > 0

  words = _split_into_words(sentences)
  return _get_ngrams(n, words)

#supporting function
def _get_ngrams(n, text):
  """Calcualtes n-grams.
  Args:
    n: which n-grams to calculate
    text: An array of tokens
  Returns:
    A set of n-grams
  """
  ngram_set = set()
  text_length = len(text)
  max_index_ngram_start = text_length - n
  for i in range(max_index_ngram_start + 1):
    ngram_set.add(tuple(text[i:i + n]))
  return ngram_set

def rouge_n(reference_sentences, evaluated_sentences, n=2):
  """
  Computes ROUGE-N of two text collections of sentences.
  Sourece: http://research.microsoft.com/en-us/um/people/cyl/download/
  papers/rouge-working-note-v1.3.1.pdf
  Args:
    evaluated_sentences: The sentences that have been picked by the summarizer
    reference_sentences: The sentences from the referene set
    n: Size of ngram.  Defaults to 2.
  Returns:
    recall rouge score(float)
  Raises:
    ValueError: raises exception if a param has len <= 0
  """
  if len(evaluated_sentences) <= 0 or len(reference_sentences) <= 0:
    raise ValueError("Collections must contain at least 1 sentence.")

  evaluated_ngrams = _get_word_ngrams(n, evaluated_sentences)
  reference_ngrams = _get_word_ngrams(n, reference_sentences)
  reference_count = len(reference_ngrams)
  evaluated_count = len(evaluated_ngrams)

  # Gets the overlapping ngrams between evaluated and reference
  overlapping_ngrams = evaluated_ngrams.intersection(reference_ngrams)
  overlapping_count = len(overlapping_ngrams)

  # Handle edge case. This isn't mathematically correct, but it's good enough
  if evaluated_count == 0:
    precision = 0.0
  else:
    precision = overlapping_count / evaluated_count

  if reference_count == 0:
    recall = 0.0
  else:
    recall = overlapping_count / reference_count

  f1_score = 2.0 * ((precision * recall) / (precision + recall + 1e-8))

  #just returning recall count in rouge, useful for our purpose
  return recall



# In[15]:


import pyter

def ter(ref, gen):
    '''
    Args:
        ref - reference sentences - in a list
        gen - generated sentences - in a list
    Returns:
        averaged TER score over all sentence pairs
    '''
    if len(ref) == 1:
        total_score =  pyter.ter(gen[0].split(), ref[0].split())
    else:
        total_score = 0
        for i in range(len(gen)):
            total_score = total_score + pyter.ter(gen[i].split(), ref[i].split())
        total_score = total_score/len(gen)
    return total_score


# In[16]:


import os
import subprocess


def meteor_score_from_files(ref, hyp, scores_file=None, meteor_path = None):
    """
        Source: https://www.cs.cmu.edu/~alavie/METEOR/examples.html
        Java -jar command: java -Xmx2G -jar meteor-*.jar [hyp.txt] [ref.txt] -norm -f system1 > test.txt
        Command to obtain more results:
            'java -Xmx2G -jar meteor-*.jar example/xray/system1.hyp example/xray/reference -norm -writeAlignments -f system1'
    :param ref: file containing reference text
    :param hyp: file containing hypotheses text
    :param scores_file: file to store METEOR score
    :param meteor_path : specify the path of downloaded Meteor jar file. default is 'meteor-*/meteor-*.jar'
    
    :return : Meteor score for sentences
    """

    if scores_file is None:
        scores_file = 'results/test_meteor.txt'
    if meteor_path is None:
        meteor_path = "meteor-*/meteor-*.jar"
    p = subprocess.Popen('java -Xmx2G -jar {meteor_path_here} {hyp_file} {ref_file} -norm -q'.
        format(hyp_file=hyp, ref_file=ref, scores_file=scores_file, meteor_path_here = meteor_path), stdout = subprocess.PIPE, shell=True) 
    (output,error) = p.communicate()
    p_status = p.wait()
    output.rstrip()
    output = float(output)
    return output


# In[18]:


'''
read from files - 
ref.txt : reference texts
gen.txt : generated texts (from model)
these files should be in the same directory
'''



def evaluation_metrics(ref_file_path, gen_file_path, n_for_rouge = 2):
    '''
    Args:
        ref_file_path (string) : reference file path -> file containing the reference sentences on each line
        gen_file_path (string) : model generated file path -> containing corresponding generated sentences(to reference sentences) on each line
    
    Returns:
        A list containing [bleu, rouge, meteor, ter]
    '''
    file_ref = open(ref_file_path, 'r')
    ref = file_ref.readlines()

    file_gen = open(gen_file_path, 'r')
    gen = file_gen.readlines()

    for i,l in enumerate(gen):
        gen[i] = l.strip()

    for i,l in enumerate(ref):
        ref[i] = l.strip()
    
    meteor_score = meteor_score_from_files("ref.txt", "gen.txt")
    ter_score = ter(ref, gen)
    bleu_score = bleu(ref, gen)
    rouge_score = rouge_n(ref, gen, n=n_for_rouge)
    return [bleu_score, rouge_score, meteor_score, ter_score]

