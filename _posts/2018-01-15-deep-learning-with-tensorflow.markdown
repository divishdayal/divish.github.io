---
layout: post
title: Getting started with deep learning on TensorFlow
date: 2018-01-15
excerpt : "How to get familiar with the recent trends in data science and machine learning."
comments: true
---

This post is about getting up to speed with the recent trends in data science. Deep learning has gained a lot of traction these days. It has showed remarkable improvements in almost every field – given the results do not need to be interpretable. The very reason deep learning works so good is that it can find features in the data automatically. But this also means that analysing these features that make the model work in a certain way is a difficult task.

Why is deep learning getting so popular ? Why should we use it ? 

Deep learning is a branch of Machine Learning. It’s one of many ways to train a model to perform some task after learning on a dataset. The advent and popularity of networks in the field of Machine Learning is not so recent, deep learning had been ideated way back in the 1980’s and 1990’s. There exist other probabilistic networks like Bayesian networks and other variants of it like Conditional Random Fields which were very popular until very recently. The reason why deep learning has been so famous is that it doesn’t require explicit feature engineering. It can automatically learn the features in the vector space, move featured objects around to form clusters in the multi-dimensional space by gradient calculations and backpropagation. This means, if you have the dataset, and you practically know the task you need to perform on the dataset, and a deep learning network that is feasible to perform that task, most of the work is done. It’s due to this ease, activation energy and knowledge needed to learn from the data has vastly reduced, and production timelines of simple models has greatly reduced. To create an analogy, in the Web world, many people started joining the web development industry once frameworks which were easy to use and implement were introduced. The learning curve and time to live were reduced for new people to join the industry. This is relatable to deep learning and data sciences field.

![CNN image]({{site.url}}/images/deep-learning-with-tensorflow.png)

Anyway, for novice programmers who are thinking of entering this recent fashion, I will give a few tips to work on the basics and gain momentum to move onto the more subtle parts of the field.

Firstly, I strongly feel that before learning anything about deep learning, it’s very important to know an overview of Machine Learning. It helps to gain insights on how and what problems are being solved by deep learning and what’s still not feasible. For starters, I think the Stanford course on ML taught by Andrew Ng shall be good enough. I would recommend the youtube lecture series over Coursera course, as the Coursera course is a somewhat mellowed down version of the actual classroom course on youtube.

For deep learning, a perfect start would be cs231n – Convolutional Neural Networks for Visual Recognition. This course is stream-lined for Computer Vision. For people not exactly interested in CV, this course is still a very good resource to learn the building blocks of all the basic networks that you’ll need for most purposes. Talking about courses, another good resource, but slightly more advanced than the previous one – cs224d – Deep learning for NLP. This course focuses on the Natural Language Processing side of things, and as you can see on the course website, the earlier course on Computer Vision is a recommended pre-requisite for this course.

I strongly believe that watching online videos is the best way to familiarize to a new area, in the shortest time and easiest route. Another good and engaging way to learn is through the videos of Siraj Raval on youtube. His videos are short and funny, informative and includes live coding to get up to speed. His videos are a very good resource to learn coding on TensorFlow. After getting started from there, one can follow official TensorFlow tutorials and try to code some other networks through guidance and support from github repositories.

For your first programs on TensorFlow, you can code networks for classification on MNIST dataset. This dataset is kinda ‘hello world’ of the deep learning networks. You can try all the different models and see your score improve on it. This gives a nice feeling, and gives you some good experience of running algos on datasets.

Another really nice resource that I find very useful to learn is – Marin Gorner’s tutorial video. For beginners, this video is a really nice introduction with very concise and wonderful explanations of various basic network architectures and practices in deep learning, with tips of code on TensorFlow simultaneously.

Once you get a acquainted with the basics and your confidence in the area improves, you can follow particular topics in the deep learning book. This is by far the best and most informative written resource on deep learning out there. This book is written by deep learning gurus and is followed as textbook by all the top courses on deep learning in the universities.

Thats about it. All these resources aren’t that time consuming once you step out of the initial ‘learning to walk’ zone. All the best. Do comment with any suggestions you have or resources that you feel that helped you and aren’t listed here.
