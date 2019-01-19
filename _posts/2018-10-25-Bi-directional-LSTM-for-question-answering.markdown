---
layout: post
title: Bi-directional LSTM with attention for question answering (NLP)
date: 2018-10-25
excerpt : "description bla bla"
comments: true
---

# Bi-directional LSTM with attention for question answering (NLP)

In this post, I’ll present a model I am currently working on during the course of my Bachelor’s thesis. In this post, a model to select the top answer for a question in community question answering forums is presented. The model here is largely inspired from “Improved Representation Learning for Question Answer Matching.” – Tan, Ming, et al.  and “Teaching machines to read and comprehend.”-Hermann, Karl Moritz, et al.

Neural networks have consistently performed well on tasks which depend upon semantic information for optimum results. The presented model in this post comprises of Long Short Term Memory (LSTM) networks, which have been very famous in the past few years since the inception of sequence modeling using neural networks. LSTM were first proposed in 1997, though their practically powerful influence was only recognized recently with the improvement in processing capabilities, and the rise in use of GPU’s for running deep learning models.
Long Short Term Memory networks

Inspired by the way humans read and understand text, Recurrent Neural Networks (RNN) have a solution to resolve these dependencies of current information that go in the past. At any time state, the output is dependent on the current input as well as information of the previous inputs.There are variants of RNN like Long Short Term Memory (LSTM) and Gated Recurrent Units (GRU) that solve some of the problems of RNN like gradient vanishing and remembering longer sequences. This type of modeling has shown very good results on language modeling tasks.

An LSTM cell comprises of 3 gates to remember a part of inputs in the previous time steps.

![useful image]({{site.url}}/images/Bi-directional-LSTM-for-question-answering-1.jpg)

Input Gate
The input gate layer in the first equation below is a sigmoid layer to decide which values in the cell state would be updated. This results in i_t taking a value between 0 and 1, where a 0 means update no new information into the cell memory and vice versa for 1.

i_t = \sigma( W_i . [h_{t-1} , x_t] + b_i )

\widetilde{C_t} = tanh( W_c . [h_{t-1} , x_t] + b_c )

Then, in the equation above, we create a candidate new cell state content to be updated into the final cell state for the current time step.

Forget Gate
The forget gate has the function of deciding which information in the cell memory to keep, and which to forget.
f_t = \sigma( W_f . [h_{t-1} , x_t] + b_f )

It looks at h_{t-1} and x_t to output a number between 0 and 1. A 1 would mean to keep all of it, and a 0 would mean to forget everything.
C_t = f_t * C_{t-1} + i_t * \widetilde{C_t}

In the above equation, we update the cell contents to new contents. Here, the forget gate f_t decides on how much of the old information is to be removed, and the input gate i_t determines the scale of addition of new candidate contents \widetilde{C_t} into the cell state.

Output Gate
The output gate layer decides the output at each time step. The output of the LSTM cell uses a sigmoid layer on inputs x_t and h_{t-1}. Updated output h_t is dependent on the updated cell state in the current time step C_t as shown in following equations.

o_t = \sigma( W_o . [h_{t-1} , x_t] + b_o )

h_t = o_t * tanh(C_t)

This structure of an LSTM helps it model the dependencies of previous inputs efficiently.
Model Architecture – Components

Our proposed model for question answering task uses a variant of LSTM’s as discussed in the last section, as well as some mechanisms such as attention. Lets discuss about them in the following parts.

Bi-directional LSTM
Bi-directional LSTM’s were introduced in 1997 by Schuster and Paliwal. They are different from LSTM in the way that they model input in both directions, from beginning to end as well as from end to the beginning. Using such a structure, the outputs can resolve dependencies on the future and past informations. They have proved to improve results in a variety of tasks as compared to vanilla LSTM’s. They perform especially better on tasks where the context information is very important.

Attention
Attention mechanisms are a recent trend in deep learning. This mechanism is loosely related to the visual attention phenomenon experienced by humans. Attention has been very common in the Computer Vision domain, and recently has found applications in the Natural Language Processing (NLP) domain.

Structurally, in neural networks, attention is used to revisit the input to decode the current output. In Computer Vision, attention is popularly used in CNN’s for a variety of tasks such as image classification, visual question answering, image captioning, etc. In NLP, some information that models such as RNN and LSTM are not able to store because of various reasons, can be reused for better output generation (decoding). Attention has showed specially good results in machine translation, while showing better results in other tasks as well.

In our task, attention shall be used to construct the answer vector. When the LSTM gives it’s output for an answer sentence, at each time step for every word, attention on the whole question will scale the answer word vectors according to their importance. This will result in varying the importance of each answer word based on it’s respective question.

A short-coming of attention is that it increases the number of parameters in the model. This increase of parameters now needs more data to generalize to the task at hand, as compared to models without attention.
The proposed Model

The proposed model is shown in the following figure. As discussed above, the model uses Bi-directional LSTM to vectorize sentences. The input at each time step to the model is Glove 50-dimensional word embedding. The input sentences i.e. question and candidate answer posts are served as input to the model using these word embeddings.

![useful image]({{site.url}}/images/Bi-directional-LSTM-for-question-answering-2.jpg)

At each time step, the bi-directional LSTM gives 2 outputs – one from the forward moving LSTM cell and another from the backward moving LSTM cell. For the model proposed here, we concatenate the two vector outputs at each time step. For each output h_a(t) of the Answer encoding bi-directional LSTM, attention of the average-pooled question vector o_q is applied using the following equations :
m_{a,q}(t) = W_{am}h_a(t) + W_{qm}o_q
s_{a,q}(t) = exp(W_{m,s}^Ttanh(m_{a,q}(t)))
\tilde{h_a}(t) = h_a(t)s_{a,q}(t)

In the above equations, \tilde{h_a}(t) is the updated output vector for answer sentences at a particular time step after applying attention using the above equations. As shown in the figure, o_q is the average pooled question vector, and \tilde{h_a}(t) is average pooled to obtain o_a, the answer vector.

After obtaining the vectors for question and answer, we use cosine similarity measure to obtain the a value for a question answer pair. For training the model, cosine hinge loss function is used as shown below,

L = max(0, m - s_{a+} + s_{a-})

In the above equation, m is the margin which is a hyper-parameter to be set for the model, s_{a+} is the cosine similarity score for the question and the positive labeled answer for a question, and s_{a-} is the score with a negative labeled answer. Essentially, we want to train the model to be able to produce a score at-least more than the margin value. Hence, at each iteration, the model consumes a question, with a correct answer and a wrong answer to calculate loss and back-propagate the loss to respective trainable components of the model.

![useful image]({{site.url}}/images/Bi-directional-LSTM-for-question-answering-3.jpg)

For training the proposed model, we have used WikiQA dataset. The dataset has a total of 3047 questions with candidate answers. The source of this dataset is Bing query logs from the years 2010-11. For each question, our model forms a pair of wrong answer and correct answer to train the model. WikiQA has a variety of questions from no fixed domain, where each question has many candidate answers like the community question answering domain, thats why we chose this dataset. The questions in WikiQA have no particular domain, hence the proposed model learns the general features that ranks an answer for each question, which can later be transferred on our required domain of MOOC discussion fora.
Model Parameters and Training

The proposed model uses Glove embeddings for the words in the input sentence. The word embeddings are input to the bi-directional LSTM at each time step. The cell memory size of the bi-directional LSTM was kept at 128 with a dropout output probability of 0.5. The margin for the loss function was set at 0.3. The batch size for training was 16 at each training step, and the model was trained using Adam Optimizer  with a learning rate of 0.0001.

Using the above parameters, the model was trained on the WikiQA dataset giving very close results to the models proposed in 2016. In the year 2017, this model performs 2-3% points lower to the state-of-the-art.

You can find the github code for this post here. The model is coded on TensorFlow v1.3. Please let me know if you have any questions or suggestions regarding the material presented in this post.