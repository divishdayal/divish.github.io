---
layout: post
title: Tensor2Tensor - Directory structure and Organisation. 
date: 2019-01-13
excerpt : "An opensource deep learning library in Tensorflow by Google. It contains implementations of commonly used models as well as advanced research models like Transformer, imaagenet, resnet, gan, etc."
<!-- comments: true -->
---

I have been working and playing around the tensor2tensor library to modify it for a task. Because of this, I have gained some practical knowledge about the structure and organisation of the library which I think would be valuable to share. When I was looking for resources on Tensor2tensor, I found no direct or indirect documentation guide about the code in the library. All you can find on the web is how to use Command Line Iterface of Tensor2tensor for various tasks, which is not helpful esp. when you are in research and development.

In the post, I'll focus on the file organisation of Tensor2Tensor. I'll discuss where to find which parts along with a bit of code organisation. In another post, I'll focus more deeply on the coding format and the style used for developing the tensorflow models. These two posts should help in understanding, like I did, about how to orgainise your tensorflow projects and some good practices to code. Atleast I'll try my best to explain this. :) If you want to learn the practical aspects of using the tensor2tensor library for training the transformer model, a very helpful resource is <a href="https://arxiv.org/pdf/1804.00247.pdf">*Training Tips for the Transformer model*</a> on arxiv. Also there are tensor2tensor library's tutorials for a good practical introduction to the library. I am going to discuss the deeper details about the library in this post.

For model codes, there are four main directories which contain the functions and definitions. These are in the tensor2tensor directory of the root directory. These are :
<ul>
	<li>_bin_ : like the usual, this directory contains the executable files for CLI commands that users generally use. You can browse in these if you want to play around with command line interactions and finding file source paths of these codes (can refer to functions being imported in these files and trace back). Otherwise, keeping model development and modifications in mind, bin directory is not much use and ignore it.  </li>
	<li>_layers_ : A very important directory containing all the different layers that are used in the models implementations. API's for layers like variants of attention for different models, usual stuff like fully connected layer, calculating cross entropy and other similar operations, lstm/gru cells, convolution layers, deconvolution layers and all other building blocks can be found in this directory. </li>
	<li>_utils_ : I believe, it's the most important directory of the tensor2tensor library. It has all the boilerplate code for the models, their training and testing/decoding environments.  </li>
	<li>_models_ : This directory contains model specific code for each of the models in tensor2tensor library. For each model, this model defines all the placeholder functions and parameters which go to the files in the utils directory for model execution and training. Apart from these, these files also define the pre-defined model parameters for training. So Transformer has parameters for transformer-tiny, transformer-small, transformer-big, etc.</li>
</ul>

The tensor2tensor library uses the Estimator API for it's code organisation structure. Estimator API is a high level tensorflow API that is meant to simplify and encapsulate operations such as training and evaluation. So, the utils directory defines the estimator API code chunks for the training and evaluation of any models defined in the models directory.