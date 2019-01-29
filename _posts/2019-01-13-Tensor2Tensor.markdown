---
layout: post
title: Tensor2Tensor : Directory structure and Organisation. 
date: 2019-01-13
excerpt : "An opensource deep learning library in Tensorflow by Google. It contains implementations of commonly used models as well as advanced research models like Transformer."
<!-- comments: true -->
---

I have been working and playing around the tensor2tensor library to modify it for a task. Because of this, I have gained some practical knowledge about the structure and organisation of the library which I think would be valuable to share. When I was looking for resources on Tensor2tensor, I found no direct or indirect documentation guide about the code in the library. All you can find on the web is how to use Command Line Iterface of Tensor2tensor for various tasks, which is not helpful esp. when you are in research and development.

In the post, I'll focus on the file organisation of Tensor2Tensor. I'll discuss where to find which parts along with a bit of code organisation. In another post, I'll focus more deeply on the coding format and the style used for developing the tensorflow models. These two posts should help in understanding, like I did, about how to orgainise your tensorflow projects and some good practices to code. Atleast I'll try my best to explain this. :) If you want to learn the practical aspects of using the tensor2tensor library for training the transformer model, a very helpful resourse is <a href="https://arxiv.org/pdf/1804.00247.pdf">*Training Tips for the Transformer model*</a> on arxiv.