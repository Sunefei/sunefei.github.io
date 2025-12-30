---
permalink: /
title: "Yifei Sun (孙逸飞)"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.google_scholar_repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.google_scholar_repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

I received my Ph.D. degree from the College of Computer Science and Technology at Zhejiang University in 2025, under the supervision of Prof. [Yang Yang](http://yangy.org/). 
Previously, I visited National University of Singapore (NUS) from Nov 2023 to Jun 2024. (working with Prof. [Bingsheng He](https://www.comp.nus.edu.sg/~hebs/), Prof. [Bryan Hooi](https://bhooi.github.io/) and Prof. [Zemin Liu](https://zemin-liu.github.io/)).

My research interests include **graph mining, foundation models for structured data, and reasoning and planning for LLMs**. I have published several papers in CCF-A tier venues, with <a href="https://scholar.google.com/citations?user=9mxdFawAAAAJ"><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> citations on Google Scholar. 

<!-- My current research interests lie primarily in the area of **Machine Learning and Data Mining on Graphs**, including but not limited to graph neural networks, graph pre-training, and real-world applications on graphs. Moreover, in the era of LLMs, I am also dedicated to leveraging graph structures to help LLMs achieve better performance in more challenging real-world scenarios. -->

<!-- ⭐️ The main goal of my Ph.D. research is to build generalizable graph models and frameworks, capable of learning from rich and complex graph data and enhancing their utility across diverse downstream tasks and datasets. -->


Ongoing Work
------

[☀️**Graph-Enhanced LLM Reasoning**] Enhancing in-context learning (ICL) with graph structure.

[☀️**Unified GraphRAG**] Building unified GraphRAG framework for both context and logic information.

[☀️**Planning for Agentic Systems**] Enabling dynamic and adaptive planning for agentic RAG and multi-turn dialogs.

<!-- - [🌏**Generalization at the Graph Principle Level**] Towards Graph Foundation Model across Domains. -->
<!-- - [💡**Generalization at the Graph Task Level**] Graph LLM for Zero-Shot Node Classification. -->
<!-- - [💡**Generalization at the Graph Task Level**] Tackling Multi-label Node Classification. (Under Review) -->
  
If interested, please drop me a message by email.

News
------

- [2025.11] Our paper "[Table as a modality for Large Language models](https://www.arxiv.org/abs/2512.00947)" is accepted by NeurIPS 2025.
- [2025.1] Our paper "[Multi-Label Node Classification with Label Influence Propagation](https://openreview.net/pdf?id=3X3LuwzZrl)" is accepted by ICLR 2025. Hope to see you in Singapore🇸🇬!!
- [2025.1] One co-authored paper accepted by WWW'25 (Oral)! Congrats to Yufei He! "[UniGraph2: Learning a Unified Embedding Space to Bind Multimodal Graphs](https://openreview.net/forum?id=lEQEKUpXt6#discussion)".
- [2024.11] Our paper "[Handling Feature Heterogeneity with Learnable Graph Patches](https://dl.acm.org/doi/10.1145/3690624.3709242)" is accepted by KDD 2025.
- [2024.10] Attended SMP'24 and received the [**Best Poster Award**](https://mp.weixin.qq.com/s/7z6ehuyRZJb2CkSUtOvMww)! Thank you all for the recognition!
- [2024.10] Our paper "[G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://arxiv.org/abs/2402.07630)" is accepted by NeurIPS 2024. Congrats to [Xiaoxin He](https://xiaoxinhe.github.io/)!
- [2024.5] Our paper "[Chromosomal Structural Abnormality Diagnosis by Homologous Similarity](https://arxiv.org/abs/2407.08204)" is accepted by KDD 2024 (ADS). Congrats to Juren Li!
- [2024.5] Our paper "[Exploring Correlations of Self-supervised Tasks for Graphs](https://arxiv.org/abs/2405.04245)" is accepted by ICML 2024. Congrats to Taoran Fang!

Selected Publications (Full version see [Google Scholar](https://scholar.google.com/citations?user=9mxdFawAAAAJ))
------

[💡**Generalization at the Graph Task Level**]

### TL;DR: Provide insights into multi-label node classification (MLNC) and model the propagation of label influences.

- **Yifei Sun**, Zemin Liu, Bryan Hooi, Yang Yang, Rizal Fathony, Jia Chen, Bingsheng He. [Multi-Label Node Classification with Label Influence Propagation](https://openreview.net/pdf?id=3X3LuwzZrl). Accepted by ICLR 2025.

[🌏**Generalization at the Graph Principle Level**]

### TL;DR: Generalized graph model that tackles feature heterogeneity to achieve cross-domain transferability.

- **Yifei Sun**, Yang Yang, Xiao Feng, Zijun Wang, haoyang zhong, Chunping Wang, Lei Chen.  [Handling Feature Heterogeneity with Learnable Graph Patches](http://yangy.org/works/gnn/KDD25_GraphPatches.pdf). Accepted by ACM KDD 2025.

[🎈**Generalization at the Graph Data Level**]

### TL;DR: Narrow the Gap between Graph Pre-training and Fine-tuning to enhance the generalization of graph models.

- **Yifei Sun**, Qi Zhu, Yang Yang, Chunping Wang, Tianyu Fan, Jiajun Zhu, Lei Chen. [Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns](https://arxiv.org/abs/2312.13583). In Proceedings of the 36th AAAI Conference on Artificial Intelligence (AAAI'24), 2024.

[🎈**Generalization at the Graph Data Level**]

### TL;DR: Break the limitations of GNNs by creating new message passing paradigm.

- **Yifei Sun**, Haoran Deng, Yang Yang, Chunping Wang, Jiarong Xu, Renhong Huang, Linfeng Cao, Yang Wang, and Lei Chen. [Beyond Homophily: Structure-aware Path Aggregation Graph Neural Network](https://www.ijcai.org/proceedings/2022/0310.pdf). In Proceedings of the 31st International Joint Conference on Artificial Intelligence (IJCAI'22), 2022.

Academic Activities
------

- [2024.10] Gave a talk on "Exploring the Generalization of Graph Models" at the Doctoral Forum of SMP 2024.
- [2024.5] Co-organized the full-day workshop on [Graph Foundation Models](https://www.www24gfm.com/) at the WebConf 2024.
