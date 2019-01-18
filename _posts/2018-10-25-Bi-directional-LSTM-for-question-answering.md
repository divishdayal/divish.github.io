---
layout: post
title: "Bi-directional LSTM with attention for question answering (NLP)"
date: 2016-03-18
description : "description bla bla"
comments: true
---

# Bi-directional LSTM with attention for question answering (NLP)

In this post, I’ll present a model I am currently working on during the course of my Bachelor’s thesis. In this post, a model to select the top answer for a question in community question answering forums is presented. The model here is largely inspired from “Improved Representation Learning for Question Answer Matching.” – Tan, Ming, et al.  and “Teaching machines to read and comprehend.”-Hermann, Karl Moritz, et al.

Neural networks have consistently performed well on tasks which depend upon semantic information for optimum results. The presented model in this post comprises of Long Short Term Memory (LSTM) networks, which have been very famous in the past few years since the inception of sequence modeling using neural networks. LSTM were first proposed in 1997, though their practically powerful influence was only recognized recently with the improvement in processing capabilities, and the rise in use of GPU’s for running deep learning models.