---
layout: article
title: Journal Club
aside:
  toc: true
---

The IAIFI Journal Club is open to IAIFI members and affiliates. 

[Sign up to lead a discussion!](https://forms.gle/zfpT4QQdXg8tu6VB7)


## Upcoming Journal Clubs

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.journal-club %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date > now %}
  {% if talk.type == "spring-2024" %}

* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
  {% endif %}
  {% endif %}
{% endfor %}

## Past Journal Clubs

### Spring 2024 Journal Clubs

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.journal-club %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "spring-2024" %}

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * [Slides]({{talk.slides-link}}) (for IAIFI members only)
{% else %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * Slides to come
  {% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

### Fall 2023 Journal Clubs

{% capture now %}{{'now' | date: '%s' | plus: 0 }}{% endcapture %}
{% assign talks = site.data.journal-club %}
{% for talk in talks %}
  {% capture date %}{{talk.talk-date | date: '%s' | plus: 0 }}{% endcapture %}
  {% if date < now %}
  {% if talk.type == "fall-2023" %}

{% if talk.slides-link %}
* **<a href="{{talk.speaker-website}}">{{talk.speaker-name}}</a>, {{talk.speaker-title}}, {{talk.speaker-affiliation}}**
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * [Slides]({{talk.slides-link}}) (for IAIFI members only)
{% else %}
    * **{{talk.talk-date-time}}, {{talk.talk-location}}**
    * *{{talk.talk-title}}*
    * {{talk.talk-abstract}}
    * Slides not available
  {% endif %}
  {% endif %}
  {% endif %}
{% endfor %}

### Spring 2023 Journal Clubs

* **Di Luo, IAIFI Fellow**
  * **April 25, 2023, 11:00am-12:00pm**
  * *Multi-legged Robot Locomotion via Spin Models Duality*
  * Contact planning is crucial in locomoting systems.Specifically, appropriate contact planning can enable versatile behaviors (e.g., sidewinding in limbless locomotors) and facilitate speed-dependent gait transitions (e.g., walk-trot-gallop in quadrupedal locomotors). The challenges of contact planning include determining not only the sequence by which contact is made and broken between the locomotor and the environments, but also the sequence of internal shape changes (e.g., body bending and limb shoulder joint oscillation). Most state-of-art contact planning algorithms focused on conventional robots (e.g.biped and quadruped) and conventional tasks (e.g. forward locomotion), and there is a lack of study on general contact planning in multi-legged robots. In this talk, I am going to discuss that using geometric mechanics framework, we can obtain the global optimal contact sequence given the internal shape changes sequence. Therefore, we simplify the contact planning problem to a graph optimization problem to identify the internal shape changes. Taking advantages of the spatio-temporal symmetry in locomotion, we map the graph optimization problem to special cases of spin models, which allows us to obtain the global optima in polynomial time. We apply our approach to develop new forward and sidewinding behaviors in a hexapod and a 12-legged centipede. We verify our predictions using numerical and robophysical models, and obtain novel and effective locomotion behaviors.
  * [Slides](https://drive.google.com/file/d/1l8uWeXrgZaZ5m44hrbwLUBurWqukAij0/view?usp=share_link) 
(For IAIFI members only)

* **Ziming Liu, Grad Student, MIT**
  * **April 25, 2023, 11:00am-12:00pm**
  * *Physics-inspired generative models*
  * It might be surprising and delightful to physicists that physics has been playing a huge role in diffusion models. In fact, the evolution of our physical world can be viewed as a generation process. In this journal club, I will first review diffusion models, the more recent PFGM/PFGM++ inspired from electrostatics, and then introduce the GenPhys framework which manages to convert even more physical processes to generative models.
  * [Slides](https://drive.google.com/file/d/1ya9nXg_oJX9wZYzB9AHtc0jBUVEifk6o/view?usp=share_link) 
(For IAIFI members only)

* **Asem Wardak, Research Fellow, Harvard**
  * **April 11, 2023, 11:00am-12:00pm**
  * *Extended Anderson Criticality in Heavy-Tailed Neural Networks*
  * This talk focuses on nonlinearly interacting systems with random, heavy-tailed connectivity. We show how heavy-tailed connectivity gives rise to an extended critical regime of spatially multifractal fluctuations between the quiescent and active phases. This phase differs from the edge of chaos in classical networks by the appearance of universal hallmarks of the Anderson transition in condensed matter physics over an extended region in phase space. We then investigate some consequences of the multifractal Anderson regime for performing persistent computations.
  * [Slides](https://drive.google.com/file/d/1yo-x-axFISmZSKefSFDuZg5UGMIPGkud/view?usp=share_link) 
(For IAIFI members only)

* **Joshua Villarreal, Grad Student, MIT**
  * **April 4, 2023, 11:00am-12:00pm**
  * *Surrogate Modeling of Particle Accelerators*
  * Abstract: The design, construction, and fine-tuning of particle accelerators has never been easy. Each is a technical challenge in and of itself, and the need to repeatedly run accurate, high-fidelity simulations of the beam traversing the device can slow development. This is especially true for many modern-day particle accelerators, whose beam dynamics tend to observe more nonlinear effects like those arising from space charge, making their simulation more computationally expensive. Thus, there is demand to develop machine learning and statistical learning models that can reproduce these beam dynamic simulations with orders-of-magnitude improvements in runtime.  In this talk, I present an overview of recent efforts to build such accelerator surrogate models, which can be used for the design optimization and real-time commissioning, tuning, and running of the accelerator they aim to replicate. As an example, I also present the status of IsoDAR’s work to build a surrogate model for a Radio-Frequency Quadrupole accelerator, a vital component to IsoDAR’s groundbreaking design. I outline challenges of these and other virtual accelerators, and present future plans to make these surrogate models ubiquitous in future development of accelerator experiments of all kinds.
  * [Slides](https://drive.google.com/file/d/1rumOzVCo6j8lFo1ZmS9mMmmM1w7bJ5qb/view?usp=share_link) 
(For IAIFI members only)

* **Daniel Murnane, Postdoc Researcher, Berkeley Lab**
  * **March 21, 2023, 11:00am-12:00pm**
  * *Multi-Tasking ML for Point Clouds at the LHC*
  * Abstract: The Large Hadron Collider is one of the world's most data-intensive experiments. Every second, millions of collisions are processed, each one resembling a jigsaw puzzle with thousands of pieces. With the upcoming upgrade to the High Luminosity LHC, this problem will only become more complex. To make sense of this data, deep learning techniques are increasingly being used. For example, graph neural networks and transformers have proven effective at handling point cloud tasks such as track reconstruction and jet tagging. In this talk, I will review the point cloud problems in collider physics and recent deep learning solutions investigated by the Exatrkx project - an initiative to implement innovative algorithms for HEP at exascale. These architectures can accurately perform tracking and tagging with low latency, even in the high luminosity regime. Additionally, I will explore how multi-tasking and multi-modal networks can combine several of these different tasks.  
  * [Slides](https://drive.google.com/file/d/1XiSb3X4NWcD5yf13MkAt7BvWMzYWziKc/view?usp=share_link) 
(For IAIFI members only)

* **Manuel Szewc, Postdoc, University of Cincinnati**
  * **March 14, 2023, 11:00am-12:00pm**
  * *Modeling Hadronization with Machine Learning*
  * Abstract: A fundamental part of event generation, hadronization is currently simulated with the help of fine-tuned empirical models. In this talk, I'll present MLHAD, a proposed alternative for hadronization where the empirical model is replaced by a surrogate Machine Learning-based model to be ultimately data-trainable. I'll detail the current stage of development and discuss possible ways forward.
  * [Slides](https://drive.google.com/file/d/1-fdoYOech0muQzE7JHXDavJwI76xtUoe/view?usp=share_link) 
(For IAIFI members only)

* **Max Tegmark, Professor, MIT**
  * **February 28, 2023, 11:00am-12:00pm**
  * *Mechanistic interpretability*
  * Abstract: Mechanistic interpretability aims to reverse-engineer trained neural networks to distill out the algorithms they have discovered for performing various tasks. Although such "artificial neuroscience" is hard and fun, it's easier than conventional neuroscience since you have complete knowledge of what every neuron and synapse is doing.
  * [Slides](https://drive.google.com/file/d/1gEDzE9zF3dWT6GnOe-m7a0rQ4PH_-fi2/view?usp=share_link) 
(For IAIFI members only)

* **Liping Liu, Assistant Professor, Tufts University**
  * **February 14, 2023, 11:00am-12:00pm**
  * *Address combinatorial graph problems with learning methods*
  * Abstract: There are plenty of hard combinatorial problems defined on graphs. Recently learning algorithms have been used to speed up the search for approximate solutions to these problems. This talk will start with an introduction to hard problems on graphs and traditional algorithms, then it will give an overview of learning algorithms for solving combinatorial problems on graphs. The second part of the talk will focus on two specific problems, graph matching and subgraph distance calculation, and discuss neural methods for these two problems. Finally, it will conclude with open questions: why and when can neural networks help to solve combinatorial problems? 
  * References:
    * [ Learning Combinatorial Optimization Algorithms over Graphs; Stochastic Iterative Graph Matching](https://proceedings.mlr.press/v139/liu21i/liu21i.pdf)
  * [Slides](https://drive.google.com/file/d/1jNBRcVDmMGiZDztMHmZ2Bo67klkrG0sd/view?usp=share_link) 
(For IAIFI members only)

### Fall 2022 Journal Clubs

* **Anna Golubeva, IAIFI Fellow and Matt Schwartz, Professor, Harvard**
  * **November 29, 2022, 11:00am-12:00pm**
  * *Should artificial intelligence be interpretable to humans?*
  * Resource:
    * [Should artificial intelligence be interpretable to humans?](https://www.nature.com/articles/s42254-022-00538-z.epdf?sharing_token=3J2X15FrSE4DX0-C4wy1WNRgN0jAjWel9jnR3ZoTv0OFWnX9fRT21Uquw1b6H6Uwdyiv6G2YbqpT_Vajh5RO07uuYzVKSwxqjGcOXKm1_MY4fr_liHzLlaBNHy4GXn2lUCIv0J8bXJTJ1_hqEzfrwjUZfC1BXzy8Su9RPY9xz5Y%3D)

* **Michael Toomey, PhD Student, Brown University**
  * **November 15, 2022, 11:00am-12:00pm**
  * *Deep Learning the Dark Sector*
  * Abstract: One of the most pressing questions in physics today is the microphysical origin of dark matter. While there have been numerous experimental programs aimed at detecting its interactions with the Standard Model, all efforts to-date have come up empty. An alternative method to constrain dark matter is purely based on its gravitational interactions. In particular, gravitational lensing can be very sensitive to the distribution and morphology of dark matter substructure which can vary appreciably between different models. However, the complexity of data sets, systematics, and large volumes of data make the dimensionality of this problem difficult to approach from more traditional methods. Thankfully, this is a task ideally suited for machine learning. In this talk we will demonstrate how machine learning will play a critical role in distinguishing between models of dark matter and constraining model parameters in lensing data. We will additionally discuss techniques unique to ML for transferring the knowledge accumulated by models in the controlled setting of simulation to real data sets utilizing unsupervised domain adaptation.
  * [Slides](https://drive.google.com/file/d/1hzKARxgLJ9QgcfB_X2CmLmFtb7B9qW3D/view?usp=share_link) (For IAIFI members only)

* **Ziming Liu, PhD Student, MIT**
  * **November 8, 2022, 11:00am-12:00pm**
  * *Toy Models of Superposition*
  * Abstract: It would be very convenient if the individual neurons of artificial neural networks corresponded to cleanly interpretable features of the input. For example, in an “ideal” ImageNet classifier, each neuron would fire only in the presence of a specific visual feature, such as the color red, a left-facing curve, or a dog snout. But it isn't always the case that features correspond so cleanly to neurons, especially in large language models where it actually seems rare for neurons to correspond to clean features. I will present a recent paper "Toy Models of Superposition" from Anthropic, aiming to answer these questions:  Why is it that neurons sometimes align with features and sometimes don't? Why do some models and tasks have many of these clean neurons, while they're vanishingly rare in others?
  * [Slides](https://drive.google.com/file/d/17LPLsDVGrr8ZD0yXJNFiVn-4sIgObGre/view?usp=share_link) (For IAIFI members only)

* **Sona Najafi, Researcher, IBM**
  * **October 25, 2022, 11:00am-12:00pm**
  * *Quantum machine learning from algorithms to hardware*
  * Abstract: The rapid progress of technology over the past few decades has led to the emergence of two powerful computational paradigms known as quantum computing and machine learning. While machine learning tries to learn the solutions from data, quantum computing harnesses the quantum laws for more powerful computation compared to classical computers. In this talk, I will discuss three domains of quantum machine learning, each harnessing a particular aspect of quantum computers and targeting specific problems. The first domain scrutinizes the power of quantum computers to work with high-dimensional data and speed-up algebra, but raises the caveat of input/output due to the quantum measurement rules. The second domain circumvents this problem by using a hybrid architecture, performing optimization on a classical computer while evaluating parameterized states on a quantum circuit, chosen based on a particular issue. Finally, the third domain is inspired by brain-like computation and uses a given quantum system's natural interaction and unitary dynamic as a source for learning

* **Kim Nicoli, Grad Student, Technical University of Berlin** 
  * **October 18, 2022, 11:00am-12:00pm**
  * Deep Learning approaches in lattice quantum field theory: recent advances and future challenges**
  * Abstract: Normalizing flows are deep generative models that leverage the change of variable formula to map simple base densities to arbitrary complex target distributions. Recent works have shown the potential of such methods in learning normalized Boltzmann densities in many fields ranging from condensed matter physics to molecular science to lattice field theory. Though sampling from a flow-based density comes with many advantages over standard MCMC sampling, it is known that these methods still suffer from several limitations. In my talk, I will start to give an overview on how to deploy deep generative models to learn Boltzmann densities in the context of a phi^4 lattice field theory. Specifically, I’ll focus on how these methods open up the possibility to estimate thermodynamic observables, i.e., physical observables which depend on the partition function and hence are not straightforward to estimate using standard MCMC methods. In the second part of my talk, I will present two ideas that have been proposed to mitigate the well-known problem of mode-collapse which often occurs when normalizing flows are trained to learn a multimodal target density.  More specifically I’ll talk about a novel “mode-dropping estimator” and path gradients. In the last part of my talk, I’ll present a new idea which aims at using flow-based methods to mitigate the sign problem.
  * [Slides](https://drive.google.com/file/d/10Xi0kKV0fyqbdtdZcJi2wSskyB1tyRJs/view?usp=share_link) (For IAIFI members only)

* **Adriana Dropulic, Grad Student, Princeton**
  * **October 4, 2022, 11:00am-12:00pm**
  * *Machine Learning the 6th Dimension: Stellar Radial Velocities from 5D Phase-Space Correlations*
  * Abstract: The Gaia satellite will observe the positions and velocities of over a billion Milky Way stars. In the early data releases, most observed stars do not have complete 6D phase-space information. We demonstrate the ability to infer the missing line-of-sight velocities until more spectroscopic observations become available. We utilize a novel neural network architecture that, after being trained on a subset of data with complete phase-space information, takes in a star's 5D astrometry (angular coordinates, proper motions, and parallax) and outputs a predicted line-of-sight velocity with an associated uncertainty. Working with a mock Gaia catalog, we show that the network can successfully recover the distributions and correlations of each velocity component for stars that fall within ~5 kpc of the Sun. We also demonstrate that the network can accurately reconstruct the velocity distribution of a kinematic substructure in the stellar halo that is spatially uniform, even when it comprises a small fraction of the total star count. We apply the neural network to real Gaia data and discuss how the inferred information augments our understanding of the Milky Way's formation history. 
  * [Slides](https://drive.google.com/file/d/1Y8zu457kF-_7RANQThgrqlm7IZzp-bFi/view?usp=share_link) (For IAIFI members only)

* **Iris Cong, Grad Student, Harvard**
  * **September 27, 2022, 11:00am-12:00pm**
  * *Quantum Convolutional Neural Networks*
  * Abstract: Convolutional neural networks (CNNs) have recently proven successful for many complex applications ranging from image recognition to precision medicine. In the first part of my talk, motivated by recent advances in realizing quantum information processors, I introduce and analyze a quantum circuit-based algorithm inspired by CNNs. Our quantum convolutional neural network (QCNN) uses only O(log(N)) variational parameters for input sizes of N qubits, allowing for its efficient training and implementation on realistic, near-term quantum devices. To explicitly illustrate its capabilities, I show that QCNN can accurately recognize quantum states associated with a one-dimensional symmetry-protected topological phase, with performance surpassing existing approaches. I further demonstrate that QCNN can be used to devise a quantum error correction (QEC) scheme optimized for a given, unknown error model that substantially outperforms known quantum codes of comparable complexity. The design of such error correction codes is particularly important for near-term experiments, whose error models may be different from those addressed by general-purpose QEC schemes. 
If time permits, I will also present our latest results on generalizing the QCNN framework to more accurately and efficiently identify two-dimensional topological phases of matter.
  * [Slides](https://docs.google.com/document/d/1W44NYu7-R8jfxp1DnJ7eW77IYt3fmxPGfPTRWxEbejg/edit?usp=share_link) (For IAIFI members only)

* **Miles Cranmer, Grad Student, Princeton**
  * **September 20, 2022, 11:00am–12:00pm**
  * *Interpretable Machine Learning for Physics*
  * Abstract: Would Kepler have discovered his laws if machine learning had been around in 1609? Or would he have been satisfied with the accuracy of some black box regression model, leaving Newton without the inspiration to find the law of gravitation? In this talk I will present a review of some industry-oriented machine learning algorithms, and discuss a major issue facing their use in the natural sciences: a lack of interpretability. I will then outline several approaches I have created with collaborators to help address these problems, based largely on a mix of structured deep learning and symbolic methods. This will include an introduction to the PySR software (https://astroautomata.com/PySR), a Python/Julia package for high-performance symbolic regression. I will conclude by demonstrating applications of such techniques and how we may gain new insights from such results.
  * Resources: [https://arxiv.org/abs/2207.12409](https://arxiv.org/abs/2207.12409); [https://arxiv.org/abs/2202.02306](https://arxiv.org/abs/2202.02306); [https://arxiv.org/abs/2006.11287](https://arxiv.org/abs/2006.11287)
  * [Slides](https://drive.google.com/file/d/176ynOd7WzIY2zCWYuFF3WfNGyHi0ptJv/view?usp=share_link) (For IAIFI members only)

* **Anindita Maiti, Grad Student, Northeastern**
  * **September 13, 2022, 11:00am-12:00pm**
  * *A Study of Neural Network Field Theories*
  * Abstract: I will present a systematic exploration of field theories arising in Neural Networks, using a dual framework given by Neural Network parameters. The infinite width limit of NN architectures, combined with i.i.d. parameters, lead to Gaussian Processes in Neural Networks by the Central Limit Theorem (CLT), corresponding to generalized free field theories. Small and large violations of the CLT respectively lead to weakly coupled and non-perturbative non-Lagrangian field theories in Neural Networks. Non-Gaussianity, locality (via cluster decomposition), and symmetries of Neural Network field theories are examined via NN parameter space, without necessitating the knowledge of field theoretic actions. Thus, Neural Network field theories, in conjunction to this duality via parameters, may have potential implications for Physics and Machine Learning both.
  * Resources: [https://arxiv.org/abs/2106.00694](https://arxiv.org/abs/2106.00694)
  * [Slides](https://drive.google.com/file/d/1QO5j9F6JM1cbDZa-dRawrdCyXR9TDxOl/view?usp=share_link) (For IAIFI members only)

### Spring 2022 Journal Clubs
* **Jessie Micallef, PhD Student, Michigan State University & Incoming IAIFI Fellow**
  * **March 10, 2022, 11:00am-12:00pm**
  * *"Adapting CNNs to Reconstruct Sparse, GeV-Scale IceCube Neutrino Events"*
  * Resources:
    * [Reconstructing Neutrino Energy using CNNs for GeV Scale IceCube Events](https://pos.sissa.it/395/1053/pdf)
    * [Direction Reconstruction using a CNN for GeV-Scale Neutrinos in IceCube](https://pos.sissa.it/395/1054/pdf)
  * [Slides](https://drive.google.com/file/d/1jDfgHtzJK6tstCXS22_l5mmKhbiZOWJN/view?usp=share_link) (For IAIFI members only)

* **Denis Boyda, Postdoctoral Appointee, Argonne National Laboratory & Incoming IAIFI Fellow**
  * **RESCHEDULED: March 17, 2022, 11:00am-12:00pm**
  * *"Overview of some popular Machine Learning frameworks for data parallelism"*
  * Resources: 
    * [S. Li et. al. PyTorch Distributed: Experiences on Accelerating Data Parallel Training. 2020.](https://arxiv.org/abs/2006.15704) arXiv:2006.15704
    * [A. Sergeev and Mike Del Balso. Horovod: fast and easy distributed deep learning in TensorFlow. 2018.](https://arxiv.org/abs/1802.05799) arXiv:1802.05799
    * [S. Rajbhandari et.al. ZeRO: Memory Optimizations Toward Training Trillion Parameter Models. 2020.](https://arxiv.org/abs/1910.02054) arXiv:1910.02054​
  * [Slides](https://drive.google.com/file/d/14x1xuW2iSsGbEvrrZB-xfc5Np6ID3Wnt/view?usp=share_link) (For IAIFI members only)

* **Yin Lin, Postdoctoral Researcher, MIT**
  * **April 7, 2022, 11:00am-12:00pm**
  * *"Accelerating Dirac equation solves in lattice QFT with neural-network preconditioners"*
  * Resources:
    * [An Introduction to the Conjugate Gradient Method Without the Agonizing Pain](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)
    * [Iterative Methods for Sparse Linear Systems](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf)
    * [Deep Learning of Preconditioners for Conjugate Gradient Solvers in Urban Water Related Problems](https://arxiv.org/abs/1906.06925)
    * [Learning to Optimize Non-Rigid Tracking](https://arxiv.org/abs/2003.12230)
  * [Slides](https://drive.google.com/file/d/1q9udj9V_LTJFY7ATFGU35sjwVzmpXinB/view?usp=share_link) (For IAIFI members only)

* **Anatoly Dymarsky, Associate Professor, University of Kentucky**
  * **April 14, 2022, 11:00am-12:00pm**
  * *Tensor network to learn the wave function of data*
  * Abstract: We use tensor network-based architecture to train a network which simultaneously accomplishes two tasks: image classification and image sampling. We argue that simultaneous performance of these tasks means our network has successfully learned the whole "manifold of data" (using the terminology from the literature) - namely all possible images of a particular kind. We use a black and white version of MNIST, hence our network learns all possible images depicting a particular digit. We access global properties of the "manifold of data" by calculating its size. Thus, we found there are 2^72 possible images of digit 3. We explain this number is robust and largely independent of the details of training process etc. 
  * Resources: 
    * [Tensor network to learn the wavefunction of data](https://arxiv.org/abs/2111.08014)
  * [Slides](https://drive.google.com/file/d/1zStOMyUi3aCk9a43zGxXkCEz_phd_Dmc/view?usp=share_link) (For IAIFI members only)

* **Carolina Cuesta, PhD Student, Durham University & Incoming IAIFI Fellow**
  * **April 21, 2022, 11:00am-12:00pm**
  * *Equivariant normalizing flows and their application to cosmology*
  * Resources:
    * [https://arxiv.org/abs/2202.05282](https://arxiv.org/abs/2202.05282)
    * [https://arxiv.org/abs/2105.09016](https://arxiv.org/abs/2105.09016)
  * [Slides](https://docs.google.com/document/d/1bU_ZsQkFuMsx00uCf3U_KeqLMF_NU6nW_qVvsdEoMlQ/edit?usp=share_link) (For IAIFI members only)

* **Benjamin Fuks, Professor, Sorbonne University**
  * **April 28, 2022, 11:00am-12:00pm**
  * *Precision simulations for new physics*
  * Resources:
    * [Precision simulations for new physics (JHEP 12 (2019) 008)](https://arxiv.org/abs/1907.04898)
    * [How precision allows us to design new variables to look for signals (Phys. Rev. D 100, 074010 (2019)](https://arxiv.org/abs/1901.09937)
    * [Trying to do better with boosted decision trees on the basis of tree-level simulations  (JHEP 04 (2022) 015)](https://arxiv.org/abs/2109.11815)

* **Dylan Hadfield, Assistant Professor, MIT** 
  * **May 5, 2022, 11:00am-12:00pm**
  * *Overoptimization, Incompleteness, and Goodhart's Law*
  * Resources:
    * [https://arxiv.org/abs/1611.08219](https://arxiv.org/abs/1611.08219)
    * [https://arxiv.org/abs/1705.09990](https://arxiv.org/abs/1705.09990)
    * [https://arxiv.org/abs/2102.03896](https://arxiv.org/abs/2102.03896)

* **Mark Hamilton, Graduate Student, MIT**
  * **May 12, 2022, 11:00am-12:00pm**
  * *Unsupervised Semantic Segmentation by Distilling Feature Correspondences*
  * Resources:
    * [Website](https://mhamilton.net/stego.html)
    * [Paper](https://arxiv.org/abs/2203.08414)
    * [Code](https://aka.ms/stego-code)
  * [Slides](https://drive.google.com/file/d/1LtKWMFvDBzRG774w12BSQmREqit0gw1-/view?usp=share_link) (For IAIFI members only)

* **Manami Kanemura, Undergraduate Student, Northeastern University (completed co-op with Bryan Ostdiek)**
  * **May 26, 2022, 11:00am-12:00pm**
  * *Using Soft-Introspection to improve anomaly detection at LHC*
  * Resources:
    * [Soft-IntroVAE: Analyzing and Improving the Introspective Variational Autoencoder](https://arxiv.org/abs/2012.13253)
    * [Challenges for Unsupervised Anomaly Detection in Particle Physics](https://arxiv.org/abs/2110.06948)
  * [Slides](https://drive.google.com/file/d/1A4oijQ-rRR3NhSTka0Mw5nD5yzULb-W-/view?usp=share_link) (For IAIFI members only)

### Fall 2021 Journal Clubs
  * **Michael Douglas**
    * **Thursday, September 23, 2021, 11:00am-12:00pm**
    * *"Solving Combinatorial Problems using AI/ML"*
    * Abstract/Resources: [Bright et al 1907.04408](https://arxiv.org/abs/1907.04408); [Heule et al 1905.10192](https://arxiv.org/abs/1905.10192); [Halverson et al 1903.11616](https://arxiv.org/abs/1903.11616); [McAleer et al 1805.07470](https://arxiv.org/abs/1805.07470); [Gukov et al 2010.16263](https://arxiv.org/abs/2010.16263); General sources on reinforcement learning: [Sutton and Bardo](https://www.davidsilver.uk/teaching), [The MathCheck SAT+CAS system](https://uwaterloo.ca/mathcheck)
  * [Slides](https://drive.google.com/file/d/18QpLIp1gwf1Qp8Qhjb4TUJnar-KFGSXC/view?usp=share_link) (For IAIFI members only)

  * **Ziming Liu**
    * **Thursday, October 7, 2021, 11:00am-12:00pm**
    * *"Dynamics in Modern Deep Learning Models"*
    * Abstract/Resources: [Transient Chaos in BERT](https://arxiv.org/pdf/2106.03181.pdf); [Memory and attention in deep learning](https://arxiv.org/pdf/2107.01390.pdf); [The Brownian motion in the transformer model](https://arxiv.org/pdf/2107.05264.pdf)
  * [Slides](https://drive.google.com/file/d/1Wirl7WS1Wg1i_b0hVDxv1El1PrbsZ-Zm/view?usp=share_link) (For IAIFI members only)

  * **Ge Yang**
    * **Thursday, October 21, 2021, 11:00am-12:00pm**
    * *"Learning and Generalization: Revisiting Neural Representations"*
    * Abstract/Resources: Understanding how deep neural networks learn and generalize has been a central pursuit of intelligence research. This is because we want to build agents that can learn quickly from a small amount of data, that also generalizes to a wider set of scenarios. In this talk, we take a systems approach by identifying key bottleneck components that limits learning and generalization. We will present two key results — overcoming the simplicity bias of neural value approximation via random Fourier features and going beyond the training distribution via invariance through inference.

  * **Eric Michaud, PhD Student, MIT**
    * **Thursday, November 18, 2021 11:00am-12:00pm**
    * *"Curious Properties of Neural Networks"*
    * Abstract/Resources: In this informal talk/discussion, I will highlight some facts about neural networks which I find to be particularly fun and surprising. Possible topics could include the Lottery Ticket Hypothesis (https://arxiv.org/abs/1803.03635), Double Descent (https://arxiv.org/abs/1912.02292), and “grokking” (https://mathai-iclr.github.io/papers/papers/MATHAI_29_paper.pdf). There will be time for discussion and for attendees to bring up their own favorite surprising facts about deep learning.

  * **Murphy Niu, Google Quantum AI**
    * **Thursday, December 3, 11:00am-12:00pm**
    * *"Entangling Quantum Generative Adversarial Networks using Tensorflow Quantum"*
    * Abstract/Resources: [https://arxiv.org/pdf/2105.00080.pdf](https://arxiv.org/pdf/2105.00080.pdf); [https://arxiv.org/pdf/2003.02989.pdf](https://arxiv.org/pdf/2003.02989.pdf)

### Spring 2021 Journal Clubs
  * **Anindita Maiti**
    * **Wednesday, February 17**
    * *"Neural Networks and Quantum Field Theory"*
    * Abstract/Resources: [https://arxiv.org/abs/2008.08601](https://arxiv.org/abs/2008.08601)

  * **Jacob Zavatone-Veth**
    * **Tuesday, March 2**
    * *"Non-Gaussian Processes and Neural Networks at Finite Widths"*
    * Abstract/Resources: [https://arxiv.org/abs/1910.00019](https://arxiv.org/abs/1910.00019)

  * **Di Luo**
    * **Tuesday, April 6**
    * *"Simulating Quantum Many-Body Physics with Neural Network Representation"*
    * Abstract/Resources: [https://arxiv.org/abs/1807.10770](https://arxiv.org/abs/1807.10770); [https://arxiv.org/pdf/1912.11052.pdf](https://arxiv.org/pdf/1912.11052.pdf); [https://arxiv.org/abs/2012.05232](https://arxiv.org/abs/2012.05232)

  * **Anna Golubeva**
    * **Tuesday, April 27**
    * *"Are Wider Nets Better Given the Same Number of Parameters?"*
    * Abstract/Resources: [https://arxiv.org/abs/2010.14495](https://arxiv.org/abs/2010.14495)

  * **Siddharth Mishra-Sharma**
    * **Tuesday, May 11**
    * *Simulation-Based Inference Focusing on Astrophysical Applications*
    * Abstract/Resources: [https://arxiv.org/abs/1911.01429](https://arxiv.org/abs/1911.01429); [https://arxiv.org/abs/1909.02005](https://arxiv.org/abs/1909.02005)

### Fall 2020 Journal Clubs
  * **Bhairav Mehta**
    * **Tuesday, October 20**
    * *"Learning Invariances"*
    * Abstract/Resources: [https://arxiv.org/abs/2009.00329](https://arxiv.org/abs/2009.00329)

  * **Andrew Tan**
    * **Wednesday, November 4**
    * *"Estimating Mutual Information"*
    * Abstract/Resources: [https://arxiv.org/abs/1905.06922](https://arxiv.org/abs/1905.06922)

  * **Ziming Liu**
    * **Wednesday, November 18**
    * *"Scaling Laws of Learning"*
    * Abstract/Resources: [https://arxiv.org/abs/2010.14701](https://arxiv.org/abs/2010.14701); [https://arxiv.org/abs/2004.10802](https://arxiv.org/abs/2004.10802); [https://arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361)

   * **Dan Roberts**
     * **Wednesday, December 2**
     * *"Effective Theory of Deep Learning"*

