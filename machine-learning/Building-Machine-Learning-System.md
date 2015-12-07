Topic: Coursera-Machine-Learning-Course-Note
date: 2015-12-05

# Week 6. Machine Learning System Design

## Brain Strom

在设计和研究一个项目时，尝试把所能想到的所有实现方法写下来，做一个对比，而不是头脑发热，心血来潮想做那一步就做哪一步

## Make it work

Andrew Ng说，在他设计和研究一个机器学习相关的问题的时候，最多先用一天的时间把项目实现起来，尽管它是一个简单而不完美的系统。这种做法的好处在于

1. 避免"过早优化",在一些不必要的问题上浪费时间和精力

2. 有指导性的知道自己下一步要做的是什么。因为很多时候初学者不知道自己下一步要做什么。

这让我想起了一位计算机科学家曾经说过的一句话

>Make it work, Make it right, Make it faster.

快速实现一个心中的想法，确实是成功开展工作的重要一步。

这里可以扩展开来的是，先从 **简单算法** 开始，先从 **小数据集** 开始
用我自己的话说，就是"快速实现原型"。

## Recommended Approach

Andrew推荐的Machine Learning System Design的通用方法

>1. Start with a simple algorithms that you can implement qucikly.Implement it and test it in your cross-validation data.
>2. Plot learning curves to decide if more data, more features, etc. are likely to help.
>3. Error analysis: Manually examine the examples(in cross-validation set)that your algorithms made errors on.See if you spot any systematic trend in what type of examples it is makeing errors on.

Notes:

1. Error analysis并不总能指导我们下一步要做什么，此时比较常见的做法是尝试一些新的算法并观察一下效果。

2. 使用数字来评估算法的效果。比如使用5%来表示错误率。这种定量的方式比定性的方式有时来得更直观

## others
[推荐系统TopN推荐评测指标-Precision&Recall](http://bookshadow.com/weblog/2014/06/10/precision-recall-f-measure/)