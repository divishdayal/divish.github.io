---
layout: post
title: Convolutional Neural Networks (CNN) – Applications in NLP for Sentence Classification
date: 2017-08-27
excerpt : "How to use CNN, widely used in computer vision, for NLP tasks - what are the use cases and how to use it for sentence classification tasks like sentiment analysis, question answer selection, etc."
<!-- comments: true -->
---


Convolutional Neural Networks (CNN) are undoubtedly the most common networks used in deep learning today. It has extensive applications in Computer Vision (CV). There are hardly in CV networks which do not comprise of CNN as one of their components. Some examples are object detection and segmentation, classification of images, etc. These networks have been consistently used with variations and holds the state of the art results on ImageNet since it’s inception in 2012.

CNN have also found application in Natural Language Processing (NLP) tasks too. “Convolutional neural networks for sentence classification.” by Kim Yoon is one of the such widely popular paper which applies CNN for sentence classification. I will discuss about CNN and this paper with code in this post.

CNN’s are especially good on tasks involving recognition of particular signals in the  data samples. For eg. in images, it can be used to identify the presence of objects to classify them. In NLP tasks, CNN can be used to classify text on these location invariant identification of signals like sentiment analysis (positive vs. negetive), etc.

![CNN image]({{site.url}}/images/CNN-for-sentence-classification.png)

The CNN network can be divided into three broad architectural categories – convolution, max pooling and fully connected layer. The convolution layer is a small window that traverses the whole image to identify certain features. Out of these features identified in the convolution layer, max pooling layer extracts the most prominent features. It’s called max because it identifies the maximum value in the convolution layer arrays. There are other operations like average pooling which takes an average over several array cells, and also min pooling which takes the minimum values. Finally a fully connected layer is used to match all the features that are extracted, and use them to classify each input into specific classes based on those features.

For sentence classifications, these convolutions represent bi-grams, tri-grams, etc. The network will consider all these x-grams in the text, and the max pooling layer will extract the information from the prominent of these x-grams, prominent for the specific task we train the model on. The backpropagation learning shall update the weights in the convolutional layer to maximize, and identify these prominent x-grams. In the convolution layer, we can have multiple x-grams at once, for the model presented in this post, I used 3,4,5-grams simultaneously. Finally, there is a fully connected layer in the end to match the probability distributions from each of these convolution x-grams. For eg. if a bigram is very good, and a tri-gram is not very good, the model will learn to classify this joint probability to be in the negetive sentiment class for the task of +ve/-ve sentiment classification.

The code for the paper mentioned in the first paragraph can be found on my github here. It is coded on TensorFlow (v1.3) with regularisation techniques like dropout and batch normalisation implementations. Please comment if you have any suggestions on code/post organisation.
