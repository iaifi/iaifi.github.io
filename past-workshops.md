---
layout: article
title: Past IAIFI Summer Workshops
aside:
  toc: true
---

# 2025 Summer Workshop

<img src="images/summer-workshop-logo_2025.png" align="left" style="max-width:5990px;width:100%" hspace="10" vspace="10"> 

The IAIFI Summer Workshop brings together researchers from across Physics and AI for plenary talks, poster sessions, and networking to promote research at the intersection of Physics and AI. We are also accepting submissions for contributed talks and/or posters.

* **The 2025 Summer Workshop was held August 11–15, 2025**
* **Location: Harvard University Northwest Building (52 Oxford St, Cambridge, MA 02138), Room B103**

[Agenda](#agenda){:.button.button--outline-primary.button--pill.button--lg} [Speakers](#speakers){:.button.button--outline-primary.button--pill.button--lg} [FAQ](#faq){:.button.button--outline-primary.button--pill.button--lg}   [Accommodations](#accommodations){:.button.button--outline-primary.button--pill.button--lg}

## About
The Institute for Artificial Intelligence and Fundamental Interactions (IAIFI) is enabling physics discoveries and advancing foundational AI through the development of novel AI approaches that incorporate first principles, best practices, and domain knowledge from fundamental physics. The goal of the Workshop is to serve as a meeting place to facilitate advances and connections across this growing interdisciplinary field.

[View recordings from the 2025 Workshop](https://youtube.com/playlist?list=PLBY0ED2StbGYicBdodtC3QqVVnwhr758-&feature=shared)

**Many of the videos from the 2025 IAIFI Summer Workshop are now [posted on the IAIFI YouTube channel](https://youtube.com/playlist?list=PLBY0ED2StbGYicBdodtC3QqVVnwhr758-&feature=shared).**
{:.info} 

<!--
**Many of the speakers' slides from the 2025 IAIFI Summer Workshop are now [available online](https://drive.google.com/drive/folders/1lpw1hYCvnaUk00ta7sJMGpNVORR5Y8EC?usp=drive_link).** 
{:.info} 
-->


## Agenda

<img src="images/2025-summer-workshop.png" align="left" style="max-width:2108px;width:100%" hspace="10" vspace="10">

### Monday, August 11, 2025
**9:00-9:15 am ET**

Welcome

**9:15–10:00 am ET**

*AI in Astrophysics: Tackling Domain Shift, Model Robustness and Uncertainty*

Aleksandra Ciprijanovic, Fermilab

<details>
<summary>Abstract</summary>
<em>Artificial Intelligence is transforming astrophysics, from studying stars and galaxies to analyzing cosmic large-scale structures. However, a critical challenge arises when AI models trained on simulations or past observational data are applied to new observation— leading to domain shifts, reduced robustness, and increased uncertainty of model predictions. This talk will explore these issues, highlighting examples such as galaxy morphology classification and cosmological parameter inference, where AI struggles to adapt across different datasets. We will discuss domain adaptation as a strategy to improve model generalization and mitigate biases—essential for making AI-driven discoveries reliable. Notably, these challenges extend beyond astrophysics, affecting AI applications across physics and other scientific domains. Addressing them is essential for maximizing AI’s impact in advancing scientific research.</em>
</details>

**10:00–10:45 am ET**

*Theoretical foundations for language model self-improvement*

Dylan Foster, Microsoft Research

<details>
<summary>Abstract</summary>
<em>Language model post-training techniques based on reinforcement learning have led to breakthroughs in reasoning, but may fail to learn behaviors that are not already present in the pre-trained base model. Can we equip models with the ability to explore novel behaviors on their own, so that they can truly self-improve and solve open-ended problems? 

This talk will offer a theoretical perspective on this question. We will introduce a new framework for reinforcement learning with pre-trained language models, and show that (1) for a large class of existing algorithms, efficient exploration with language models is impossible (perhaps surprisingly, this is for computational reasons rather than statistical reasons); but (2) this can be sidestepped through new algorithmic interventions that combine multi-turn reinforcement learning with deliberate use of test-time compute, allowing efficient discovery of new behaviors beyond the base model.</em>
</details>

**10:45-11:15 am ET**

Break

**11:15 am–12:00 pm ET**

*Self-supervised Reinforcement Learning and Generative Models*

Amy Zhang, UT Austin

<details>
<summary>Abstract</summary>
<em>We explore the intersection of generative AI and reinforcement learning, demonstrating how generative models can be understood as RL agents and environments, and conversely, how RL can be viewed as generative modeling. We show how this perspective leads to new forms of self-supervised reinforcement learning algorithms that form new objectives for training generative models. We will discuss future directions and open problems, focusing on how RL can shape the future of foundation model training.</em>
</details>

**12:00–1:30 pm ET**

Lunch Break

**1:30–2:15 pm ET**

*Machine Learning for Time-Domain Astrophysics*

Alex Gagliano, IAIFI Fellow

<details>
<summary>Abstract</summary>
<em>The time-evolving night sky is alive with variable stars, supernovae, and merging neutron stars. Surveys that monitor this variability produce gappy, multi-modal observations that demand scalable, uncertainty-aware models for physical inference. In this talk, I’ll survey recent advances in time-domain astrophysics with machine learning, with a focus on representation learning and multi-modal architectures. I’ll introduce Minuet, a compact host-galaxy image encoder trained with diffusion; a categorical network that encodes light curves by their underlying power sources; and a mixture-of-experts model that fuses supernova light curves and spectra while preserving modality-specific information and yielding calibrated posteriors. I’ll conclude by outlining three topics at this intersection — better physical models, scalable population studies, and ML-guided survey optimization — with the greatest potential to drive discovery in the coming years.</em>
</details>

**2:15–3:00 pm ET**

*Emulating Dark Matter Halo Merger Trees with Generative Models*

Tri Nguyen, CIERA, Northwestern University

<details>
<summary>Abstract</summary>
<em>Merger trees track the hierarchical assembly of dark matter halos and are crucial for semi-analytic galaxy formation models. However, traditional methods rely on ad-hoc assumptions and struggle to incorporate environmental information. I present FLORAH-Tree, a generative model for merger trees by representing them as graph structures that capture the full branching hierarchy. I trained FLORAH-Tree on merger trees from the Very Small MultiDark Planck N-body simulation and validated it against simulation data and Extended Press-Schechter analytical trees. FLORAH-Tree accurately reproduces key merger tree statistics across mass and redshift ranges, outperforming analytical approaches. Applying the Santa Cruz semi-analytic model to generated trees shows that galaxy-halo scaling relations match expectations. FLORAH-Tree provides a computationally efficient method for generating merger trees while maintaining N-body simulation fidelity.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

*Multimodal Foundation Models for Scientific Data* 

Francois Lanusse, CNRS

<details>
<summary>Abstract</summary>
<em>Deep Learning has seen a recent shift in paradigm, from training specialized models on dedicated datasets, so-called Foundation Models, trained in a self-supervised manner on vast amounts of data and then adapted to solve specific tasks with state-of-the-art performance. This new paradigm has been exceptionally successful not only for large language models (LLMs) but in other domains such as vision models. In this talk I will discuss several methodologies that can be deployed in our scientific domains, in particular weakly-supervised cross-modal contrastive learning and multimodal self-supervised generative pretraining. I will show how these approaches can be used to build models flexible to very diverse and inhomogeneous observations (e.g. different types of measurements such as spectra, time-series, or images, but also different instruments, etc...) and how they can then be leveraged by the end-user for a variety of downstream applications (e.g. redshift estimation, morphology classification, physical parameter inference, searching for rare objects) with very simple machine learning methods and still reach near-optimal performance.</em>
</details>

**4:15-5:00 pm ET**

*Structured Learning for Astrophysical Data*

Peter Melchior, Princeton University

<details>
<summary>Abstract</summary>
<em>Astronomy and astrophysics are currently undergoing profound changes as the results of two developments: 1) the availability of vast quantities of data from surveys and simulations, and 2) the rapid progress in machine learning and AI. But how should we bridge the gap between data-driven and theoretical descriptions of the Universe? How do we actually learn new aspects of physical systems from data? I will show that introducing structure, usual reflecting causal relations, into deep learning architectures creates efficient, robust, useful, and highly interpretable models that respect known physics and reveal unknown phenomena. I will present results from my group on exoplanets, galaxy evolution, and cosmology to demonstrate what we can achieve already and discuss how this approach leads to future astrophysics and AI research.</em>
</details>

**5:30–8:00 pm ET**

Poster Session and Reception (Atrium, B101)

[View Poster Abstracts](https://docs.google.com/document/d/1sXSDDyGPuohhsxZGkj7nkvzMc_gCgwfzlUFxCnitSEY/edit?usp=sharing){:.button.button--outline-primary.button--pill.button--lg}

<details>
<summary>Details</summary>
<ul> <li> Differentiable Water Cherenkov Detector Simulation, Omar Alterkait (Tufts University / IAIFI) </li>
<li> End-to-end Optimization of Generative AI for Robust Background Estimation, Giada Badaracco (ETH Zurich) </li>
<li> Real-Time Compression of CMS Detector Data Using Conditional Autoencoders, Zachary Baldwin (Carnegie Mellon University) </li>
<li> Masked Autoencoder for Pretraining in Cosmic Ray Background Classification task, Vinicius Da Silva (Tufts University) </li>
<li> Mantis Shrimp: Exploring Photometric Band Utilization in Computer Vision Networks for Photometric Redshift Estimation, Andrew Engel (The Ohio State University) </li>
<li> Stress testing a Simulation Based Inference approach to Weak Lensing Galaxy Cluster Mass Inference, Akum Gill (Harvard University) </li>
<li> Task complexity shapes internal representations and robustness in neural networks, Robert Jankowski (University of Barcelona) </li>
<li> Generalization and robustness of neural ordinary differential equations for dynamical systems on graphs, Moritz Laber (Northeastern University) </li>
<li> Solvable Model of Pretrain-Test Task Alignment in In-Context Learning, Mary Letey (Harvard University) </li>
<li> Fast density functional theory for training machine learning interatomic potentials via large-scale atomistic sampling, Emmanuel Lujan (Massachusetts Institute of Technology) </li>
<li> Symbolic regression for precision LHC physics, Manuel Morales-Alvarado (INFN, Sezione di Trieste) </li>
<li> Generalized Parton Distributions from Symbolic Regression, Zaki Panjsheeri (University of Virginia) </li>
<li> A Breadth First Search Algorithm for Data Clustering based on Space-time Curvature, Ailun Shen (Interlake) </li>
<li> Analytical Theory of Spectral Effects in Sampling and Learning of Diffusion Model, Binxu Wang (Harvard University, Kempner Institute) </li>
<li> Investigating the Morphological Footprints of Cosmology in the Cosmic Web, Pragyan Yadav (University of Connecticut) </li></ul>
</details>


### Tuesday, August 12, 2025

**9:00–9:45 am ET**

*(Machine) Learning of Dark Matter*

Lina Necib, MIT

<details>
<summary>Abstract</summary>
<em>In this talk, I explore the impact of stellar kinematics on understanding the particle nature of Dark Matter, overviewing the correlations between stellar and Dark Matter phase space distributions in three separate locations: the solar neighborhood, the Galactic center, and dwarf galaxies. I will focus on the use of machine learning techniques applied to data from the Gaia mission to disentangle the local kinematics substructures, and the use of simulations to study the correlations between stars and Dark Matter. I will end by relating these empirical measurements to Dark Matter detection experiments.</em>
</details>

**9:45–10:30 am ET**

*Learning the Universe: Building a Scalable, Verifiable Emulation Pipeline for Astronomical Survey Science*

Matthew Ho, Columbia University

<details>
<summary>Abstract</summary>
<em>Learning the Universe is developing a large-scale, ML-accelerated pipeline for simulation-based inference in cosmology and astrophysics. By combining high-resolution physical models with fast emulators, we generate realistic training sets at the scale required for field-level inference from galaxy survey data. This enables us to constrain models of galaxy formation and cosmology from observations with unprecedented scale and precision. In designing this pipeline, we have also developed validation methodologies to assess emulator accuracy, identify sources of systematic error, and support blinded survey analysis. I will present results from its application to the SDSS BOSS CMASS spectroscopic galaxy sample and discuss how this approach is scaling to upcoming cosmological surveys.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*High-dimensional Bayesian Inference with Diffusion Models and Generative Flow Networks*

Alexandre Adam, Université de Montréal

<details>
<summary>Abstract</summary>
<em>The nature of dark matter is one of the greatest mystery in modern cosmology. Little is known about dark matter, other than it has a mass, thus gravitate, and interact with the electromagnetic field weakly, if none at all. Gravitational lensing is a natural phenomena which involves the trajectory of photons from distant galaxies bending by the gravity of massive object in our line of sight. As such, it is one of the most promising probe to study the nature of dark matter. This talk will discuss the problem of inferring the mass of the hypothetic dark matter particle from strong gravitational lens measurement, the challenges involved in such an inference from a Bayesien perspective and the potential solutions offered by modern deep learning framework such as diffusion models and generative flow networks.</em>
</details>

**11:45 am–12:30 pm ET**

*Bridging Legacy and Modern Inference: Practical SBI for Astrophysics*

Noemi Anau Montel, Max Planck Institute for Astrophysics

<details>
<summary>Abstract</summary>
<em>Simulation-based inference (SBI) has emerged as a transformative tool for astrophysical analysis, yet its widespread adoption still faces significant obstacles, including the integration with existing pipelines and establishing scientific trust. This talk addresses these challenges through three practical approaches demonstrated across different applications. In particular, I will discuss how to build effective simulators from explicit likelihood codes, allowing us to integrate legacy cosmological likelihoods, like the Planck CMB likelihood, with SBI frameworks. Second, I will present a robust SBI pipeline for complex Fermi-LAT gamma-ray observations that, while modeling background emission with greater realism, confirms source-count distributions consistent with traditional results and achieves $>98\%$ completeness relative to the standard catalog. Finally, I will introduce systematic tests for model misspecification by extending traditional goodness-of-fit concepts to simulation-based frameworks, showing an example of such tests on the GW150914 gravitational wave event.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–3:30 pm ET**

**Contributed Talks Session A: Generative Models**

*Room B101*

<details>
<summary>Conditional Generation of LArTPC Images Using Latent Diffusion, Zev Imani (Tufts University)</summary>
<em>Modern neutrino physics experiments utilize Liquid Argon Time Projection Chamber (LArTPC) technology to capture visual representations of particle interactions. Inspired by the success of denoising diffusion probabilistic models (DDPMs) in generating natural images, we have developed a method of conditionally generating 2D LArTPC images. By utilizing a modified latent diffusion model we have demonstrated the ability to generate single-particle events of a specified momentum with quality comparable to traditional simulation approaches.</em>
</details>

<details>
<summary>Leveraging LLM Agents for Optical Simulation and Design, Nikhil Mukund (MIT)</summary>
<em>High-fidelity simulations are integral to the design and debugging of sensitive optical experiments, ranging from tabletop setups to kilometer-scale interferometric systems, such as the Advanced LIGO detector. While several tools exist to model Gaussian beam propagation through complex optical layouts, generating executable code for these tools often demands substantial manual expertise and is prone to errors. In this work, we investigate the potential of utilizing large language model (LLM)-based agents to aid in optical system design and simulation. We highlight the challenges that arise when using off-the-shelf large language models (LLMs) with domain-specific software and investigate how augmenting these models with retrieval and feedback mechanisms can mitigate common failure modes. Through case studies involving widely used interferometer simulation tools, we illustrate the promise of this approach in reducing development time and enhancing reliability. Our findings suggest that this framework can be broadly extended to other simulation-based workflows, offering a general strategy for accelerating system modeling and analysis.</em>
</details>

<details>
<summary>MEMFlow - Computing matrix element method using neural importance sampling, Adrian-Antonio Petre (ETH Zurich / CMS Collaboration (CERN))</summary>
<em>The Matrix Element Method (MEM) is a well motivated multivariate technique to access the likelihood of an observed event given a hypothesis. It offers optimal statistical power for hypothesis testing in particle physics, but it is limited by the computation of the intensive multi-dimensional integrals required to model detector and theory effects. We present a novel approach that addresses this challenge by employing Transformers and generative machine learning (ML) models. Specifically, we utilize ML surrogates to efficiently sample the phasespace for different physics processes and to accurately encode the complex transfer functions describing detector reconstruction. Our goal is to efficiently use these sampled points in the context of neural importance sampling. We demonstrate this technique on the challenging ttH(bb) process in the semileptonic channel using the full CMS detector simulation. This advancement enables fully unbinned likelihood estimates of the Standard Model Effective Field Theory (EFT) couplings by using directly the experimental data, with the potential of significantly enhancing sensitivity to new physics.</em>
</details>

<details>
<summary>The Liquid Argon Dead Region Inference Project: ML Track Inference Between DUNE's Near Detector Prototype Modules, Hilary Utaegbulam (University of Rochester)</summary>
<em>The 2x2 Demonstrator is a prototype of ND-LAr, the liquid argon time-projection chamber of the Deep Underground Neutrino Experiment's Near Detector complex. Both the 2x2 Demonstrator and ND-LAr are modular detectors that will have pixelated charge readouts and inactive regions wherein there is no sensitivity to energy depositions in the liquid argon. In the 2x2, these inactive regions are located in between the active detector modules, which introduces the challenge of inferring what charge signals ought to look like in these regions. This study explores the use of a dual decoder sparse three-dimensional convolutional neural network to infer missing regions in charged particle tracks. Results indicate that this approach shows promise in predicting missing energy depositions in dead regions with good accuracy.</em>
</details>

<details>
<summary>Generative Mental World Explorer, Jieneng Chen (Johns Hopkins University)</summary>
<em>Understanding, navigating, and exploring the physical real world has long been a central challenge in the development of artificial intelligence. In this talk, I take a step toward this goal by introducing GenEx, a system capable of planning complex embodied world exploration, guided by its generative imagination that forms priors (expectations) about the surrounding environments. GenEx generates an entire 3D-consistent imaginative environment from as little as a single RGB image, bringing it to life through panoramic video streams. Powered by the generative imagination of the world, GPT-assisted agents are equipped to perform complex embodied tasks. These agents utilize predictive expectations regarding unseen parts of the physical world to refine their beliefs, simulate different outcomes based on potential decisions, and make more informed choices.</em>
</details>

<details>
<summary>Discovering group dynamics in coordinated time series via hierarchical recurrent switching-state models, Kaitlin Gili (Tufts University)</summary>
<em>Recent models that learn spatiotemporal patterns across individuals fail to incorporate explicit system-level collective behavior that can influence the trajectories of individual entities. To address this gap in the literature, we present a new hierarchical switching-state probabilistic generative model that can be trained in an unsupervised fashion to simultaneously learn both system-level and individual-level dynamics. We employ a latent system-level discrete state Markov chain that provides top-down influence on latent entity-level chains which in turn govern the emission of each observed time series. Recurrent feedback from the observations to the latent chains at both entity and system levels allows recent situational context to inform how dynamics unfold at all levels in bottom-up fashion. Our hierarchical switching recurrent dynamical model can be learned via closed-form variational coordinate ascent updates to all latent chains that scale linearly in the number of entities. This is asymptotically no more costly than fitting a separate model for each entity. Analysis of both synthetic data and real basketball team movements suggests our lean parametric model can achieve competitive forecasts compared to larger neural network models that require far more computational resources. Further experiments on soldier data as well as a synthetic marching band task with 64 cooperating entities show how our approach can yield interpretable insights about group dynamics over time.</em>
</details>

<details>
<summary>Analytical Theory of Spectral Effects in Sampling and Learning of Diffusion Model, Binxu Wang (Harvard University, Kempner Institute)</summary>
<em>Diffusion models generate complex data by estimating the score—the gradient of the log-density—across varying noise scales, but the relationship between the learned neural score and the true data score has remained unclear. Inspired by the “far-field” approximation in physics, we show that for moderate-to-high noise levels, the learned score is dominated by its linear (Gaussian) component, enabling a closed-form integration of the probability-flow ODE. This analytical solution predicts key sampling phenomena—namely, the early specification of coarse structures (e.g., scene layouts), the low dimensionality of sampling trajectories, and their sensitivity to perturbations—given the 1/f power spectrum of natural images. Practically, it permits an “analytical teleportation” that skips the first 15–30% of sampling steps, accelerating modern solvers (e.g., DPM-Solver-v3, UniPC) without degrading image quality (FID 1.93 on CIFAR-10).

Extending this perspective to learning, we derive exact solutions to the nested probability-flow and gradient-flow ODEs for linear denoisers in fully linear, deep linear, and convolutional networks. Our analysis reveals a universal inverse-variance spectral law (τ ∝ λ⁻¹): high-variance (coarse) modes converge much faster than low-variance (fine) modes. Weight sharing in convolutional architectures uniformly amplifies these rates, whereas local convolution dramatically reshapes mode-emergence dynamics by coupling Fourier modes. Empirical studies with MLP-based and U-Net diffusion models on Gaussian and natural-image datasets confirm these theoretical predictions. 

Together, our theory highlights the importance of spectral structure of data in determining sampling and training dynamics of diffusion models.</em>
</details>


**Contributed Talks Session B: Physics-Motivated Optimization**

*Room B103*

<details>
<summary>Feature Learning and Generalization in Deep Networks with Orthogonal Weights, Hannah Day (University of Illinois Urbana-Champaign)</summary>
<em>Signals propagating through a neural network can be thought of as a renormalization group flow where the marginal couplings are hyperparameters of the network tuned to criticality to prevent exponential growth or decay of signals. Using this formalism, we study the effect of initializing a network with weights sampled from an orthogonal matrix distribution and find several key features which indicate that networks with orthogonal initialization might perform better than those with Gaussian initialization throughout training.</em>
</details>

<details>
<summary>Self-supervised mapping of space-charge distortions in Liquid Argon TPCs, Jack Cleeve (Columbia University)</summary>
<em>We introduce an end-to-end, self-supervised neural workflow that learns the three-dimensional electric-field distortion in a Liquid Argon TPC directly from through-going cosmic muon tracks. The network uses geometric straightness and boundary conditions to generate its own target undistorted paths and iteratively refine them. In this talk, I will present the architecture of the model, detail the self-supervised training process and analyze its performance on SBND-scale simulations.</em>
</details>

<details>
<summary>Machine Learning Neutrino-Nucleus Cross Sections, Karla Tame-Narvaez (Fermilab)</summary>
<em>Neutrino-nucleus scattering cross sections are critical theoretical inputs for long-baseline neutrino oscillation experiments. However, robust modeling of these cross sections remains challenging. For a simple but physically motivated toy model of the DUNE experiment, we demonstrate that an accurate neural-network model of the cross section—leveraging Standard Model symmetries—can be learned from near-detector data. We then perform a neutrino oscillation analysis with simulated
far-detector events, finding that the modeled cross section achieves results consistent with what could be obtained if the true cross section were known exactly. This proof-of-principle study highlights the potential of future neutrino near-detector datasets and data-driven cross-section models.</em>
</details>

<details>
<summary>Data-Driven Methods for Quantum Many-Body Systems, Patrick Ledwith (Harvard)</summary>
<em>In this talk, we will discuss a general, modular scalar function that characterizes quantum phases with a ground-state degeneracy, given the spectrum of a many-body Hamiltonian. First, by interpreting it as a loss function, we show that it encodes the spectral distance to the target phase, thereby recasting quantum phase identification as a tractable optimization problem in Hamiltonian parameter space.  Applying this approach to the problem of fractional Chern insulators (FCIs), we uncover novel types of FCIs lying well beyond the Landau-level mimicry paradigm. Second, by instead interpreting the scalar function as the quality of a degenerate quantum phase, we apply Kolmogorov–Arnold Networks (KANs) to quantify to what extent the single-particle quantum geometry of a system is sufficient to predict the presence of a FCI ground state. Our work leverages gradient-based optimization and recent developments in symbolic regression for the targeted search and data-driven understanding of novel many-body phases.</em>
</details>

<details>
<summary>Using xLSTM in jet classification with the JetClass dataset, Daniel Eduardo Conde Villatoro (Universidad de Valencia)</summary>
<em>This work aims to use the novel xLSTM (extended Long Short-Term Memory) deep learning architecture for the jet classification task in the JetClass dataset. xLSTM is a recursive neural network that is an evolution of LSTM (Long Short-Term Memory), and it is meant to be competitive with other state-of-the-art architectures like transformers and attention. Previous works on jet classification had used LSTM to explore the relevance of constituent ordering for optimization during training, but classification on the JetClass dataset has mostly left LSTM behind in favour of the aforementioned tools. Our work revisits and builds upon the original motivation for using recursive architectures, using the xLSTM's ability to process ordered data effectively. We systematically compare the performance of different constituent ordering schemes during training.</em>
</details>

<details>
<summary>Transformers with Gauge Covariant Attention in Lattice QCD, Akio Tomiya (TWCU)</summary>
<em>We previously developed a Transformer neural network architecture for SU(2) lattice gauge theory and now present its straightforward extension to SU(3) lattice QCD. The model is gauge covariant and equivariant, respecting SU(3) gauge symmetry along with lattice rotations and translations. Its attention matrix is built from Frobenius inner products between link variables and covariantly transported staples, ensuring invariance under gauge transformations. Incorporated into a self learning HMC workflow, the SU(3) version shows better performance than existing gauge covariant networks, highlighting its potential to accelerate lattice QCD calculations.</em>
</details>

**3:30–4:00 pm ET**

Break

**4:00–4:45 pm ET**

*Kindness or Sycophancy? Understanding and Shaping Model Personality via Synthetic Games*

Hidenori Tanaka, Harvard University/NTT Research, Inc.

<details>
<summary>Abstract</summary>
<em>Abstract to come.</em>
</details>

**4:45-5:30 pm ET**

*Geometry of Neural Representations: Principles for Brains and Machines*

SueYeon Chung, Harvard University (starting Fall 2025), Flatiron Institute

<details>
<summary>Abstract</summary>
<em>Both brains and artificial neural networks operate in regimes of staggering complexity, yet their internal activity often lies on surprisingly low-dimensional, structured manifolds. The geometry of these manifolds constrains what computations are possible and how efficiently they can be implemented.
In this talk, I will present a theoretical framework that draws on statistical physics, geometry, and machine learning to link representational geometry to task performance across biological and artificial systems. I will highlight how geometric principles can be used to interpret neural data, diagnose learning in AI models, and design architectures that generalize efficiently.
By viewing neural computation through a geometric lens, we can identify shared organizing principles across scales and systems, and use these principles to guide the next generation of neuroscience-inspired AI.
</em>
</details>

### Wednesday, August 13, 2025

**9:00–9:45 am ET**

*From Neurons to Neutrons: An Intepretable AI model for Nuclear Physics*

Sokratis Trifinopoulos, MIT/CERN

<details>
<summary>Abstract</summary>
<em>Obtaining high-precision predictions of nuclear observables, such as nuclear binding energies $E_b$, charge radii etc., remains an important goal in nuclear-physics research. Recently, many AI-based tools have shown promising results on such tasks, some achieving a precision that surpasses the best physics models. However, the utility of these AI models remains in question given that predictions are only useful where measurements do not exist, which inherently requires extrapolation away from the training (and testing) samples. Since AI models are largely \textit{black boxes}, the reliability of such an extrapolation is difficult to assess. In this talk, I will present an AI model that not only achieves cutting-edge precision for nuclear observables, but does so in an interpretable manner. Focusing on the case of $E_b$, we find that the most important dimensions of its internal representation form a double helix, where the analog of the hydrogen bonds in DNA here link the number of protons and neutrons found in the most stable nucleus of each isotopic chain. Furthermore, I will show that the AI prediction of $E_b$ can be factorized and ordered hierarchically, with the most important terms corresponding to well-known symbolic models (such as the famous liquid drop). Remarkably, the improvement of the AI model over symbolic ones can almost entirely be attributed to an observation made by Jaffe in 1969. The end result is a data-driven model of nuclear masses that is fully interpretable.</em>
</details>

**9:45–10:30 am ET**

*Investigating Proton Spatial and Spin Structure with Interpretable AI*

Simonetta Liuti, University of Virginia

<details>
<summary>Abstract</summary>
<em>Abstract to come.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*Build Big or Build Smart - What’s the role of Domain Knowledge?*

Lukas Heinrich, Technical University Munich

<details>
<summary>Abstract</summary>
<em>Physics and Deep Learning have traditionally taken different routes to state of the art data processing. One is based on deep pipelines of manually designed algorithms that exploit the rich domain knowledge we have while the other relies on large-scale data and powerful learning algorithms. Both directions have recently seen new ideas come to the fore through Differentiable Programming and the rise of Foundation Modes. I will share recent work in both of these areas and discuss whether the famous “Bitter Lesson” will also catch up to fundamental physics.</em>
</details>

**11:45 am–12:30 pm ET**

*AI on the Edge: Decoding Particles, Brains, and Cosmic Collisions in Real Time*

Shih-Chieh Hsu, University of Washington

<details>
<summary>Abstract</summary>
<em>Artificial Intelligence is transforming scientific discovery at every scale-from the subatomic to the cosmic-by enabling real-time data analysis with unprecedented speed and precision. The A3D3 Institute leads this revolution, leveraging advanced hardware like FPGAs and GPUs, cutting-edge model compression, and specialized inference frameworks to accelerate breakthroughs in particle physics, neuroscience, and multi-messenger astrophysics. This talk highlights how A3D3’s innovations are powering instant detection of rare events, live decoding of brain signals, and rapid response to cosmic phenomena, ushering in a new era where AI turns massive data streams into actionable insights as they happen.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–3:30 pm ET**

**Contributed Talks Session A: Representation/Manifold Learning and Generative AI**

*Room B101*

<details>
<summary>Collapse-Proof Non-Contrastive Self-Supervised Learning, Emanuele Sansone (MIT)</summary>
<em>Self-supervised learning (SSL) has unlocked the potential of learning general-purpose representations from large amounts of unlabeled data. Despite its successes, important challenges remain, hindering the  
applicability and democratisation of SSL. One such challenge is the presence of failure modes occurring during the training of SSL models. In this talk, we aim to distill the essential principles to guarantee the avoidance of known collapses. We present a principled and simplified design of the projector and loss function for non-contrastive SSL based on hyperdimensional computing. We theoretically demonstrate that this design introduces an inductive bias that encourages representations to be simultaneously decorrelated and clustered, without explicitly enforcing these properties. This bias provably enhances generalization and suffices to avoid known training failure modes, such as representation, dimensional, cluster, and intracluster collapses. We validate our theoretical findings on image datasets, including SVHN, CIFAR-10, CIFAR-100, and ImageNet-100. Our approach effectively combines the strengths of feature decorrelation and cluster-based SSL methods, overcoming training failure modes while achieving strong generalization in clustering and linear classification tasks.</em>
</details>

<details>
<summary>Entropic Forces and Spontaneous Symmetry Breaking in Deep Learning, Liu Ziyin (MIT)</summary>
<em>Building on prior works on modified loss and parameter symmetry, we develop the theory of an effective landscape for understanding the stochastic and discrete-time learning behavior of neural networks. We show that together with symmetries in neural networks, these entropic forces lead to symmetry-breaking and phase-transition-like behaviors in the training of neural networks. We also show how elements of thermodynamics, such as the equipartition theorem, can emerge as a consequence of these entropic forces in the non-equilibrium learning dynamics.</em>
</details>

<details>
<summary>Using machine learning to emulate the atomic nucleus, Antoine Belley (MIT)</summary>
<em>Computing nuclear observables starting from the fundamental forces between the protons and neutrons in an atomic nucleus is an extremely computationally expensive task, due both to the poor scaling of the quantum many-body problem and the complicated nature of the strong force. This becomes especially prohibitive when one wants to assess the uncertainty of such a calculation coming from its many parameters. In this talk, I will present a novel emulator that allows to quickly predict results of costly calculations. By combining a transformer architecture, bayesian neural networks and a multi-fidelity approach in which coarser approximation can be used to train the model on top of the expensive high-precision calculations, state-of-the art emulation of nuclear properties can be achieve for multiple nuclei simultaneously, with a factor of 10^5 speed up. Moreover, the emulator is able to extrapolate to nuclei removed for the training data, allowing one to explore regions of the nuclear chart that are challenging to predict with conventional methods.</em>
</details>

<details>
<summary>Electron-nucleus cross sections from transfer learning, Krzysztof Graczyk (Institute of Theoretical Physics, University of Wroclaw, Poland)</summary>
<em>We present a deep learning approach to modeling inclusive electron–nucleus scattering cross sections using transfer learning, demonstrating how neural networks can effectively learn nuclear physical properties from limited experimental data. Initially trained on high-statistics electron–carbon scattering data, our model captures latent features that are transferable to other nuclei, such as lithium, oxygen, aluminum, calcium, and iron. This approach enables accurate predictions even in data-sparse regimes, revealing a robust internal representation of nuclear responses across different targets. Our results highlight the potential of representation learning to extract universal physical patterns and support data-driven modeling in nuclear and particle physics. The study illustrates how abstract, learned features can encapsulate domain knowledge, enabling generalization beyond the training distribution and reducing reliance on traditional theoretical models. To probe the method’s limitations, we applied it to the helium-3 target. The approach remained effective, although it required more extensive re-optimization. Finally, I will discuss the implications of this method for modeling neutrino-nucleus interactions. This talk is based mainly on the paper arXiv:2408.09936.</em>
</details>

<details>
<summary>A data-driven search for ancient asteroid families, Saverio Cambioni (Massachusetts Institute of Technology)</summary>
<em>A central goal of astrophysics is to understand how small bodies that coagulate from protoplanetary disks (planetesimals) assemble to form planets. In the solar system, some planetesimals escaped planet formation and populated the main-asteroid belt between the orbits of Mars and Jupiter, where we can observe them today. However, most of the planetesimals collided pairwise over time and formed families of asteroids. How can we distinguish the former from the latter? In this talk, I will present how collisional families can be identified by looking for clusters in the orbital properties of asteroids with unsupervised machine learning techniques. I will also show that dynamical effects lead to diffusion and destruction of clusters as families age. This process has prevented the identification of ancient families that formed at the dawn of the solar system. We seek collaborations with artificial-intelligence experts to determine alternative approaches for identifying ancient families. Once all families are found, the remainder are the primordial planetesimals whose size and composition will reveal the initial conditions of planet formation.</em>
</details>

<details>
<summary>Data-driven classification of metal-poor stars using machine learning based on nucleosynthesis calculations, Yilin Wang (TRIUMF / University of British Columbia)</summary>
<em>We present a first-time application of machine learning to classify metal-poor stars by the astrophysical processes that are responsible for enriching their stellar environments. The existing method categorizes stellar sites as having been enriched by the the rapid (r-), intermediate (i-), or slow (s-) neutron capture processes based on simple threshold values of abundance ratios from a very small and potentially restrictive set of elements. In this work, we develop data-driven classifiers trained on nucleosynthesis calculations from simulations of r- and s-process sites. We present the ML classification results, compare them to their conventional categorization using the existing method, and discuss the additional insights, and some challenges, revealed by this novel approach.</em>
</details>

<details>
<summary>Enforcing Hard Constraints in Generative Models for Mixed-Type tabular Data, Jose Munoz (Visa)</summary>
<em>While diffusion models are highly effective at generating high-fidelity synthetic data, their unconstrained nature often leads to outputs that violate fundamental principles or rules, making them unsuitable for scientific applications. We present a general, training-free framework that enforces hard constraints directly within the generative process of any pre-trained diffusion model. Our method works by applying a feasibility operator at each step of the reverse-diffusion chain, ensuring that generated samples remain on a valid manifold defined by known constraints. A novel aspect of our framework is its unified handling of constraints across mixed-type tabular data, simultaneously managing continuous and discrete variables within a single process. This approach guarantees 100% constraint compliance without requiring model retraining or inefficient post-hoc filtering. The primary benefit of generating strictly valid synthetic data is the significant improvement of downstream modeling tasks. By enabling the augmentation of scarce datasets with rule-compliant samples, our framework enhances the robustness, accuracy, and generalizability of predictive models. This method unlocks reliable data augmentation and scenario analysis in complex, rule-governed environments, establishing a foundation for more trustworthy AI systems.</em>
</details>


**Contributed Talks Session B: Uncertainty Quantification/Robust AI**

*Room B103*

<details>
<summary>SIDDA: SInkhorn Dynamic Domain Adaptation, Sneh Pandya (Northeastern)</summary>
<em>Modern neural networks (NNs) often do not generalize well in the presence of a "covariate shift"; that is, in situations where the training and test data distributions differ, but the conditional distribution of classification labels remains unchanged. In such cases, NN generalization can be reduced to a problem of learning more domain-invariant features. Domain adaptation (DA) methods include a range of techniques aimed at achieving this; however, these methods have struggled with the need for extensive hyperparameter tuning, which then incurs significant computational costs. In this work, we introduce SIDDA, an out-of-the-box DA training algorithm built upon the Sinkhorn divergence, that can achieve effective domain alignment with minimal hyperparameter tuning and computational overhead. We demonstrate the efficacy of our method on multiple simulated and real datasets of varying complexity, including simple shapes, handwritten digits, and real astronomical observations. SIDDA is compatible with a variety of NN architectures, and it works particularly well in improving classification accuracy and model calibration when paired with equivariant neural networks (ENNs). We find that SIDDA enhances the generalization capabilities of NNs, achieving up to a ≈40% improvement in classification accuracy on unlabeled target data.</em>
</details>

<details>
<summary>Frequentist Uncertainties on Neural Density Ratios with wifi Ensembles, Sean Benevedes (Massachusetts Institute of Technology)</summary>
<em>We propose wifi ensembles, a novel framework to obtain asymptotic frequentist uncertainties on density ratios in the context of neural ratio estimation. In the case where the density ratio of interest is a likelihood ratio conditioned on parameters, for example a likelihood ratio of collider events conditioned on parameters of nature, it can be used to perform simulation-based inference on those parameters. We show how uncertainties on a density ratio can be estimated with ensembles and propagated to determine the resultant uncertainty on the estimated parameters. We then turn to an application in quantum chromodynamics (QCD), using ensembles to estimate the likelihood ratio between generated quark and gluon jets. We use this learned likelihood ratio to estimate the quark fraction in a mixed quark/gluon sample, showing that the resultant uncertainties empirically satisfy the desired coverage properties.</em>
</details>

<details>
<summary>Uncertainty-Aware Discrimination of SMEFT Signatures in Embedding Spaces, Brandon Kriesten (Argonne National Laboratory)</summary>
<em>Representing hadronic parton distribution functions (PDFs) through flexible, high-fidelity parameterizations remains a long-standing goal of particle physics phenomenology. One crucial goal is to quantitatively connect experiments’ sensitivity to underlying theory assumptions, including a broad array of BSM and SMEFT scenarios, to the properties of the PDFs’ flavor and x-dependence. We explore this problem by encoding many SMEFT scenarios in contrastive embedding spaces generated from simulated QCD events. Within this space we apply evidence-based uncertainty quantification techniques to disentangle data (aleatoric) and knowledge (epistemic) uncertainty while identifying out of distribution samples. Equivalently important is the ability to exclude particular classes of theories, such as standard model-only physics scenarios, which we do through the identification of theory “superclasses.” I will present the latest progress in building these embedding spaces unifying dozens of SMEFT variants, demonstrating how model discrimination and anomaly detection naturally emerge alongside generation and classification tasks with uncertainty quantification.</em>
</details>

<details>
<summary>Detecting Model Misspecification in Cosmology with Scale-Dependent Normalizing Flows, Aizhan Akhmetzhanova (Harvard University)</summary>
<em>Current and upcoming cosmological experiments will provide massive amounts of high-dimensional data which require complex high-fidelity forward simulations to accurately model both physical processes and systematic effects which describe the data generation process. Assessing goodness-of-fit of these models on the observed datasets and identifying the degree of model misspecification present in the simulations in the high-dimensional data spaces is a challenging task. An additional challenge comes from choosing the appropriate representations of the data which, while reducing the dimensionality of the original dataset, retain all the relevant cosmological information and enable detection of model misspecification. 

Bayesian evidence provides one promising avenue to assess and quantify differences between simulated and observed datasets. In this work we develop a machine learning framework using normalizing flows to estimate the Bayesian evidence at the level of traditional and neural summary statistics of the data for a variety of astrophysical fields from the CAMELS simulations. A key focus of our work is training our models as a function of a smoothing scale applied to the data products from the simulations, which allows us to identify which scales are most affected by the differences in sub-grid physics models. By comparing Bayesian evidence between different suites of CAMELS simulations across a range of smoothing scales, we aim to provide a systematic way of detecting and evaluating the discrepancies between the different galaxy formation models, which could eventually help bridge the gap between the simulations and the observed data.</em>
</details>

<details>
<summary>Best of both worlds: integrating principled matched-filtering searches with AI/ML tools, Digvijay (Jay) Wadekar (Johns Hopkins University)</summary>
<em>In the infinite data and compute limit, machine learning (ML) methods can be optimal, however this idealistic situation is not often realized in practice. On the other hand, principled data-analysis methods are robust, but they make simplistic assumptions (e.g., the noise is roughly Gaussian). I will present how ML algorithms can enhance matched-filtering pipelines by: generating optimally compressed template banks and mitigating non-Gaussian noise. Incorporating these advancements in the IAS search pipeline, I will present detections of new heavy black holes in astrophysically significant regions of parameter space. I will also showcase how large language models (LLMs) can lower the entry barrier for non-specialists working with complex gravitational wave analysis frameworks.</em>
</details>

<details>
<summary>Robust Perception in AI: Temporal Uncertainty Quantification to Counter Hallucination in Multi-Object Tracking, Mohamed Nagy Mostafa (Khalifa University)</summary>
<em>AI perception systems often suffer from perception hallucinations, providing false perception information that can degrade decision-making. Nevertheless, identifying false perception information from correct information is challenging, particularly for problems that do not involve direct interaction with humans (such as automated systems). This talk will cover our recent research on introducing an automated mechanism based on temporal uncertainty, in which AI systems self-assess perceptual certainty using temporal uncertainty, filtering out hallucinated data while retaining valid environmental information that enhances multi-object tracking in self-driving cars.</em>
</details>

<details>
<summary>Generalization and robustness of neural ordinary differential equations for dynamical systems on graphs, Moritz Laber (Northeastern University)</summary>
<em>Complex systems from many domains, such as epidemiology, neuroscience, or population dynamics, can be modeled as a graph with node states evolving according to a system of ordinary differential equations (ODEs). Traditionally, these models are hand-crafted by domain experts based on prior knowledge about the system. More recently machine learning methods have been used to forecast complex dynamical systems based on observational data, potentially trading interpretability for predictive performance. Neural ODEs, machine learning models that extract an ODE's vector field from data, promise to combine the best of both worlds, as they allow incorporating prior knowledge into the architecture while learning details of a given system from empirical time series. While neural ODEs have become an important tool for data-driven modeling, questions of robustness, out-of-distribution generalization, and sample efficiency have only recently moved into the spotlight. Here, we study how incorporating prior knowledge about network dynamical systems into neural ODEs influences generalization to graphs of different sizes and different structural characteristics, as well as their robustness to noise and missing data. We focus on five dynamical systems from different domains and use random hyperbolic graphs as a flexible generative model of graphs with distinct structural characteristics. In this setup, we show empirically that generalization to larger graphs is possible in the case of low degree heterogeneity and exhibits low dependence on the graph's clustering coefficient. We also show that generalization is possible even for large degree heterogeneity for a limited class of dynamical systems. In addition, we show that generalization performance is mostly robust under noisy training data but degrades quickly when nodes in the graph are unobserved at inference time. While our results on size generalization may pave a route towards efficiency gains by training on smaller graphs, the brittleness to node-missingness serves as a reminder of the limitations of data-driven methods.</em>
</details>

**3:30–4:00 pm ET**

Break

**4:00–5:00 pm ET**

*Panel: Navigating Scientific Research with LLM Assistants*

* Alex Gagliano, IAIFI Fellow
* Mark Hamilton, Engineering Manager, Microsoft and Visiting Researcher, MIT
* Tamar Rott Shaham, Postdoc, MIT / Incoming Assistant Professor, Weizmann Institute of Science
* Moderator: Fabian Ruehle, Assistant Professor, Northeastern

**6:00–8:00 pm ET**

*Workshop Dinner*

Museum of Science

### Thursday, August 14, 2025

**9:00–9:45 am ET**

*Machine Learning inroads into the bootstrap programme*

Costis Papageorgakis, Queen Mary University of London

<details>
<summary>Abstract</summary>
<em>I will discuss the bootstrap philosophy and its numerical incarnations in Conformal Field Theory, in terms of the primal and dual formulations. After discussing the merits of the dual approach, I will outline how Machine Learning techniques (RL, PINNs) allow for directly attacking the primal problem with several concrete examples. </em>
</details>

**9:45–10:30 am ET**

*Towards Complete Automation in Particle Image Inference*

Francois Drielsma, SLAC

<details>
<summary>Abstract</summary>
<em>Particle imaging detectors have had a ubiquitous role in particle physics for over a century. The unrivaled level of detail they deliver has led to many discoveries and continues to make them an attractive choice in modern experiments. The liquid argon time projection chamber (LArTPC) technology – a dense, scalable realization of this detection paradigm – is the cornerstone of the US-based accelerator neutrino program. While the human brain can reliably recognize patterns in particle interaction images, automating this reconstruction process has been an ongoing challenge which could jeopardize the success of LArTPC experiments. Recent leaps in computer vision, made possible by machine learning (ML), have led to a remedy. We introduce an ML-based data reconstruction chain for particle imaging detectors: a multi-task network cascade which combines voxel-level feature extraction using Sparse Convolutional Neural Networks and particle superstructure formation using Graph Neural Networks. It provides a detailed description of an image and is currently used for state-of-the-art physics inference in three LArTPC experiments. Building on this success, we briefly inrtoduce the potential of leveraging self-supervised learning – the core concept of cutting-edge large language models – to learn the fundamental structure of detector data directly from a large corpus of raw, unlabeled data. This novel approach could address current shortcomings in signal processing and reduce the impact of data/simulation disagreements.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*Foundation Models for Detector Data: progress, potential, and challenges*

Michelle Kuchera, Davidson College

<details>
<summary>Abstract</summary>
<em>Building on recent successes in broader machine learning domains, physicists are now adapting large, pre-trained models to structured detector data. In this talk, I will survey the growing landscape of foundation model applications in nuclear and particle physics, with a focus on models designed for sparse or geometric data representations. I will discuss what we can learn from foundation model work in non-science machine learning research, how these ideas translate into physics contexts, and where domain-specific needs introduce new challenges. In addition to technical advances, I will also discuss the impact of culture in scientific disciplines which may affect logistics of deploying foundation models considering topics such as data ownership, reproducibility, and authorship.</em>
</details>

**11:45 am–12:30 pm ET**

*Deep(er) Reconstruction of Imaging Cherenkov Detectors: From Generative Towards Foundation Models*

Cristiano Fanelli, William & Mary

<details>
<summary>Abstract</summary>
<em>Imaging Cherenkov detectors are essential for charged particle identification (PID) in nuclear and particle physics experiments. This talk focuses on DIRC detectors, a particularly challenging class of imaging Cherenkov detectors that combine spatial and temporal information at the readout level. Their hit patterns are both sparse and topologically complex, making reconstruction especially demanding.  
Simulations present a major bottleneck. Traditional frameworks such as Geant4 are computationally expensive for Cherenkov detectors, where simulating optical photon transport through intricate geometries is essential for accurate reconstruction, calibration, and alignment. Thus, fast and high-fidelity simulations are critical. Flow-based generative models address this challenge by enabling high-fidelity fast simulation, reproducing Geant4-based photon hit distributions at only a fraction of the generation time.
 A second challenge lies in achieving PID that is not only fast but also highly accurate and valid across the full detector phase space and the kinematics of charged particles. Here, transformer-based architectures deliver enhanced PID with, effectively, orders-of-magnitude faster inference across the full phase space.  
Finally, we introduce a unified foundation model that integrates simulation, reconstruction, and other downstream tasks within a single framework.
An important byproduct of these approaches is the potential to open a new paradigm: learning detector responses directly from real data.  These developments mark a pathway toward next-generation, data-driven algorithms that support both reconstruction and simulation of Cherenkov detectors.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–3:30 pm ET**

**Contributed Talks Session A**

*Room B101*

Generative Models
<details>
<summary>Signal-Preserving Machine Learning for Polarized CMB Foreground Reconstruction, Helen Shao (University of Cambridge)</summary>
<em>Accurate measurement of Cosmic Microwave Background (CMB) B-mode polarization, a key probe of inflationary physics, is hindered by complex astrophysical foreground contamination. Standard foreground reconstruction techniques like the Internal Linear Combination (ILC) method can mitigate this problem while preserving the CMB signal. However, they are limited to second-order statistics, neglecting non-Gaussian information that dominates the foregrounds. This work presents a novel, signal-preserving machine learning framework for foreground reconstruction, designed to overcome these limitations using only single-frequency data. To achieve this, we leverage the statistical independence of primary CMB modes across angular scales, contrasted with the significant inter-scale correlations present in Galactic foregrounds. We train convolutional neural networks and conditional diffusion models to predict and subtract large-scale foreground features ($\ell < 200$) using only small-scale map information ($\ell > 200$) as a signal-free input. This approach preserves the cosmological signal by construction. We demonstrate the method's effectiveness using PySM3 simulations of Galactic dust emission, showing improved foreground removal compared to baseline methods. We validate the performance of the neural networks using correlation metrics in both pixel and harmonic space. We present this framework as a pathway towards simplified component separation for next-generation CMB experiments, with ongoing work to assess generalization across different foreground models and sky regions.</em>
</details>

<details>
<summary>Applying diffusion models to flavor physics: An example using S4′ modular flavor symmetry, Satsuki Nishimura (Kyushu University)</summary>
<em>We propose a numerical method for searching parameters in generic flavor models using a diffusion model, a type of generative artificial intelligence (generative AI). As a specific example, we consider the S4′ modular flavor model and construct a neural network that reproduces quark masses, the CKM matrix, and the Jarlskog invariant by treating the model’s free parameters as generation targets. By generating new parameters with the trained network, we find phenomenologically interesting regions of parameter space that are difficult to explore analytically. Furthermore, we confirm that spontaneous CP violation occurs in the S4′ model. The diffusion model enables an inverse-problem approach, allowing the machine to generate plausible sets of parameters from given experimental constraints. In addition, it can serve as a versatile analytical tool for extracting new physical predictions from flavor models. References are arXiv:2503.21432 [hep-ph] and arXiv:2504.00944 [hep-ph].</em>
</details>

<details>
<summary>AI-driven robotics for physics, Sachin Vaidya (Massachusetts Institute of Technology)</summary>
<em>AI-driven scientific discovery faces a key challenge: automating experiments to accelerate progress in laboratory settings. In this talk, I will discuss our work on automating optical experiments, a longstanding bottleneck in both research and industry. Tabletop optical setups are essential across disciplines—from photonics and materials science to biomedical imaging and semiconductor technology—yet they remain highly dependent on manual assembly and alignment. I will present our AI-driven robotic platform, which integrates LLM-based agents for optical design and code generation, a robotic arm, and computer vision for the assembly and fine alignment of optical setups.</em>
</details>

Interpretable AI / Deep Learning
<details>
<summary>Data-driven classification of structural nonlinearities using interpretable deep learning on time series, Bayan Abusalameh (National University of Singapore)</summary>
<em>This talk presents a novel time-domain approach for detecting and characterizing structural nonlinearities using deep learning and interpretable time-series analysis. We first generate a comprehensive synthetic dataset by solving single-degree-of-freedom system equations under various nonlinear conditions—including cubic stiffness (hardening and softening), clearance, Coulomb friction, and quadratic damping. This dataset serves as the foundation for training a deep learning model capable of classifying these nonlinear behaviors. Crucially, we integrate a post-hoc interpretability framework that highlights the specific regions of the input time series that influence the model's predictions. This transparency enables validation of the model’s reasoning against domain expert knowledge, addressing concerns surrounding the use of black-box methods in safety-critical domains such as aerospace and medicine. By removing the need for complex data preprocessing, our method offers a streamlined and scalable pipeline for structural diagnostics. The curated dataset also serves as a valuable benchmark for future research in nonlinear system identification.</em>
</details>

<details>
<summary>Symbolic regression for precision LHC physics, Manuel Morales-Alvarado (INFN, Sezione di Trieste)</summary>
<em>We study the potential of symbolic regression (SR) to derive compact and precise analytic expressions that can improve the accuracy and simplicity of phenomenological analyses at the Large Hadron Collider (LHC). 

As a benchmark, we apply SR to equation recovery in quantum electrodynamics (QED), where established analytical results from quantum field theory provide a reliable framework for evaluation. This benchmark serves to validate the performance and reliability of SR before extending its application to structure functions in the Drell-Yan process mediated by virtual photons, which lack analytic representations from first principles. Furthermore, we provide the first set of closed form equations for multidifferential angular coefficients in electroweak boson production. 

By combining the simplicity of analytic expressions with the predictive power of machine learning techniques, SR offers a useful tool for facilitating phenomenological analyses in high energy physics.</em>
</details>

Uncertainty Quantification/Robust AI
<details>
<summary>Debiasing Ultrafast Anomaly Detection with Posterior Agreement, Patrick Odagiu (ETH Zurich)</summary>
<em>The Level-1 Trigger system of the CMS experiment at CERN makes the final decision on which LHC collision data are stored to disk for later analysis. One algorithm used with this scope is an anomaly detection model based on an autoencoder architecture. This model is trained self-supervised on measured data, but its performance is typically evaluated on simulated datasets of potential anomalies. Since the true nature of anomalies in the real collision data is unknown, such a validation strategy inherently biases the model towards the characteristics of the simulated cases. We propose an alternative validation criterion: maximizing the mutual information between latent spaces produced by models that are obtained using different data sources. Thus, we explicitly quantify the bias introduced through the current model selection procedure by computing the mutual information between latent spaces of autoencoders in a cross-validation setting with different subsets of 25 simulated potential anomaly datasets. Additionally, we investigate how our metric can be used as a model selection criterion at training time, circumventing the reliance on simulated anomaly datasets. Therefore, using our method not only exposes the existing validation bias in the current level-1 anomaly detector, but also yields new models whose anomaly definitions are both robust and broadly informative, ensuring that the trigger remains sensitive to genuinely unexpected novel physics in LHC collisions.</em>
</details>

<details>
<summary>Machine Learning-Enhanced Planetary Atmospheric Simulations: Runtime-Integrated Surrogate Models for Global Circulation Models, Tara Tahseen (University College London)</summary>
<em>Atmospheric modeling across planetary science faces a fundamental computational challenge: a persistent trade-off between simulation resolution, physical complexity, and computational feasibility. This bottleneck limits scientific inference capabilities in Earth climate studies, climate studies of solar system bodies, and exoplanet atmospheric characterization. Our work addresses this challenge by integrating machine-learned surrogate models into global circulation models (GCMs), specifically within the OASIS GCM framework.

We present a novel approach that leverages Extreme Learning Machine algorithm to create adaptive radiative transfer surrogate models generated during simulation runtime. This methodology enables superior generalizability across diverse atmospheric conditions while dramatically reducing computational demands. Our implementation demonstrates remarkable efficacy, achieving >99% accuracy when modeling Venus's atmosphere while significantly accelerating simulation times, by a factor >5,000 for the Venus atmosphere.

This research exemplifies how physics-informed AI can transform computational planetary science by preserving physical first principles while overcoming traditional computational constraints. The approach opens new possibilities for high-resolution, physically sophisticated atmospheric simulations across the spectrum of planetary bodies, from Earth to distant exoplanets.</em>
</details>

**Contributed Talks Session B**

*Room B103*

Reinforcement Learning
<details>
<summary>Deep Reinforcement Learning Without Discounting, Jacob Adamczyk (University of Massachusetts Boston)</summary>
<em>Average-reward reinforcement learning (RL) offers a compelling approach to solving control problems by maximizing long-term average performance without discounting. This presentation will provide an overview and history of average-reward RL, contrasting it with the widely used discounted objective. The effectiveness of modern average-reward algorithms will be highlighted, featuring our group's latest work in this domain, which is based on connections to nonequilibrium statistical mechanics. Finally, open problems in the field, both theoretical and experimental, will be discussed.</em>
</details>

<details>
<summary>Learning Causal Representations for Efficient and Adaptive Decision-Making Agents in the Physical World, Fan Feng (University of California San Diego)</summary>
<em>Understanding the causality of the physical world, beyond raw perception, is essential for human cognition and reasoning. However, most decision-making agents, such as those trained with reinforcement learning, do not learn or reason in a causal manner. This lack of causal structure makes it difficult for agents to generalize effectively across tasks and environments. In this talk, we will explore how to equip agents with causal representations and reasoning capabilities by learning causal world models—latent structured models that uncover the hidden mechanisms of physical environments. These models not only capture latent causal factors but also enable agents to perform purposeful interventions and counterfactual reasoning, thereby supporting more robust and generalizable decision-making.

This talk will cover how to learn such models from observational and interactive data, how to use them to plan and act efficiently in complex physical environments, and how these representations and behaviors can be further used to refine causal understanding in new domains. Together, these ideas point toward the development of open-ended, generalist agents grounded in a causal understanding of the world. We will cover theoretical foundations, algorithmic design, and empirical applications in physical decision-making domains, such as robotic control and manipulation, and other long-horizon physical planning tasks, where understanding the underlying causal representation of the physical world is crucial.</em>
</details>

<details>
<summary>Autonomous Model Building with Reinforcement Learning: An Application with Lepton Flavor Symmetries, Jake Rudolph (UC Irvine)</summary>
<em>To build models of Beyond the Standard Model physics, a theorist has many choices to make in regards to new fields, internal symmetries, and charge assignments, collectively creating an enormous space of possible models. We describe the development and findings of an Autonomous Model Builder (AMBer), which uses Reinforcement Learning (RL) to efficiently find models satisfying specified discrete flavor symmetries and particle content. Aside from valiant efforts by theorists following their intuition, these theory spaces are not deeply explored due to the vast number of possibilities and the time-consuming nature of building and fitting a model for a given symmetry group and particle assignment. The lack of any guarantee of continuity or differentiability prevents the application of typical machine learning approaches. We describe an RL software pipeline that interfaces with newly optimized versions of physics software, and apply it to the task of neutrino model building. Our agent learns to find fruitful regions of theory space, uncovering new models in commonly analyzed symmetry groups, and exploring for the first time previously unexamined symmetries.</em>
</details>


Representation/Manifold Learning
<details>
<summary>Cell Reweighting Algorithms for Pathological Weight Mitigation Using Optimal Transport, Rishabh Jain (Brown University)</summary>
<em>As the accuracy of experimental results increase in high energy physics, so too must the precision of Monte Carlo simulations. Currently, event generation at next to leading order (NLO) accuracy and beyond results in a number of negative weighted events. Not only are these unphysical, but they also drive up the computational load and can be pathological when used in machine learning analyses. We develop a post hoc ‘cell reweighting’ scheme by imposing a metric in the multidimensional space of events so that nearby events on this manifold are reweighted together. We compare the performance of the algorithm with different choices of metric. We explicitly demonstrate the performance of the algorithm by implementing the reweighting scheme on simulated data of a Z boson and two jets produced at NLO accuracy.</em>
</details>

<details>
<summary>Lorentz Local Canonicalization: How to Make Any Network Lorentz-Equivariant, Jonas Spinner (Heidelberg University)</summary>
<em>Lorentz-equivariant neural networks are becoming the leading architectures for high-energy physics. Current implementations rely on specialized layers, limiting architectural choices. We introduce Lorentz Local Canonicalization (LLoCa), a general framework that renders any backbone network exactly Lorentz-equivariant. Using equivariantly predicted local reference frames, we construct LLoCa-transformers and graph networks. We adapt a recent approach to geometric message passing to the non-compact Lorentz group, allowing propagation of space-time tensorial features. Data augmentation emerges from LLoCa as a special choice of reference frame. Our models surpass state-of-the-art accuracy on relevant particle physics tasks, while being 4× faster and using 5-100× fewer FLOPs.</em>
</details>

<details>
<summary>Neural Networks and Quantum Mechanics, Christian Ferko (Northeastern University and IAIFI)</summary>
<em>Recent developments have suggested an emerging connection between neural networks and quantum field theories. In this talk, I will describe aspects of this relationship in the simplified setting of 1d QFTs, or models of quantum mechanics, where one has greater theoretical control. For instance, under mild assumptions, one can prove that any model of a quantum particle admits a representation as a neural network. Cherished features of quantum mechanics, such as uncertainty relations, emerge from specific architectural choices that are made to satisfy the axioms of quantum theory. Based on 2504.05462 with Jim Halverson.</em>
</details>

Other
<details>
<summary>The AI energy catastrophe, Trevor McCourt (Extropic)</summary>
<em>Have you ever done the napkin math on how much energy it would take to serve everyone in the country a useful AI assistant? At Extropic, we have, and the answer is "way too much". In my talk, I will introduce this energy crisis, explain why solving it is a challenging problem, and briefly discuss how Extropic intends to alleviate it.</em>
</details>

**3:30–4:00 pm ET**

Break

**4:00–4:45 pm ET**

*Theorem proving, AI and physics*

Michael Douglas, Harvard University

<details>
<summary>Abstract</summary>
<em>Interactive theorem proving (ITP) is a technology with which mathematical proofs can be expresssed in a formal language and automatically verified.  While effective, up to now formalization has been too laborious for regular use.  But thanks to advances in AI, especially language model coding assistants.and autoformalization, ITP could become easy to use within 1-3 years, facilitating large AI-human collaborations.  We will give an introduction and survey.of these developments.</em>
</details>

**4:45–5:30 pm ET**

*AI to tackle quantum gravity*

Sven Krippendorf, University of Cambridge

<details>
<summary>Abstract</summary>
<em>In this talk I report how modern numerical methods allow us to gain unprecedented insights into theories of quantum gravity. Focusing on the case of string theory, I report on which inverse problems are faced and how we can solve them using generative AI methods. I give an overview of how dedicated numerical pipelines had to be developed to enable numerical work on the model space of quantum gravity. These examples are then put into perspective to recent developments on automated scientific discoveries using agentic systems of LLMs and numerical tools.</em>
</details>


### Friday, August 15, 2025

**9:00–9:45 am ET**

*Generative quantum advantage for classical and quantum problems*

Hsin-Yuan (Robert) Huang, Caltech, Google

<details>
<summary>Abstract</summary>
<em>Recent breakthroughs in generative machine learning, powered by massive computational resources, have demonstrated unprecedented human-like capabilities. While beyond-classical quantum experiments have generated samples from classically intractable distributions, their complexity has, to-date, thwarted all efforts in efficient learning. This challenge has hindered demonstrations of generative quantum advantage: the ability for quantum computers to both learn and generate desired outputs substantially better than classical computers. We resolve this challenge by introducing a class of shallow quantum models that sample from universal classes of deep circuits. These models are hard to simulate classically, are efficiently trainable, have no barren plateaus or proliferating local minima, and can learn distributions that are provably out of reach for classical models. Using a 68 qubit superconducting quantum processor, we apply these models to two scenarios: learning classically intractable probability distributions and learning quantum circuits for accelerated physical simulation. Our results demonstrate that both learning and sampling are efficient in the current beyond-classical regime, opening new possibilities for quantum-enhanced generative models with provable classical hardness.</em>
</details>

**9:45–10:30 am ET**

*Artificial intelligence for quantum matter*

Liang Fu, MIT

<details>
<summary>Abstract</summary>
<em>Abstract to come.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*Understanding inference-time compute: Self-improvement and scaling*

Akshay Krishnamurthy, Microsoft Research

<details>
<summary>Abstract</summary>
<em>Inference-time compute has emerged as a new axis for scaling large language models, leading to breakthroughs in AI reasoning. Broadly speaking, inference-time compute methods involve allowing the language model to interact with a verifier to search for desirable, high-quality, or correct responses. While recent breakthroughs involve using a ground-truth verifier of correctness, it is also possible to invoke the language model itself or an otherwise learned model as verifiers. These latter protocols raise the possibility of self-improvement, whereby the AI system evaluates and refines its own generations to achieve higher performance.  This talk presents new understanding of and new algorithms for language model self-improvement. The first part of the talk focuses on a new perspective on self-improvement that we refer to as sharpening, whereby we "sharpen" the model toward one placing large probability mass on high-quality sequence, as measured by the language model itself. We show how the sharpening process can be done purely at inference time or amortized into the model via post-training, thereby avoiding expensive inference-time computation. In the second part of the talk, we consider the more general setting of a learned reward model, show that the performance of naive-but-widely-used inference-time compute strategies does not improve monotonically with compute, and develop a new compute-monotone algorithm with optimal statistical performance.  Based on joint works with Audrey Huang, Dhruv Rohatgi, Adam Block, Qinghua Liu, Jordan T. Ash, Cyril Zhang, Max Simchowitz, Dylan J. Foster and Nan Jiang.</em>
</details>

**11:45 am–12:30 pm ET**

*A Physics-informed Approach To Sensing*

Petros Boufounos, Mitsubishi Electric Research Laboratories

<details>
<summary>Abstract</summary>
<em>Physics-based models are experiencing a resurgence in signal processing applications. Thanks to developments in theory and computation it is now practical to incorporate models of dynamical systems within signal processing pipelines, learning algorithms and optimization loops. Advances in learning theory, such as Physics-Informed Neural Networks (PINNs) also allow for flexible and adaptive modeling of systems, even if the exact system model is not available at the algorithm design stage. In this talk we will explore how these new capabilities improve sensing systems and enable new capabilities is a variety of applications and modalities. We will discuss applications in underground imaging, fluid modeling and sensing, and airflow imaging, among others, and investigate different approaches to developing and using these models, their advantages and pitfalls.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–2:45 pm ET**

*State of AI Reasoning for Theoretical Physics - Insights from the TPBench Project*

Moritz Münchmeyer, University of Wisconsin-Madison

<details>
<summary>Abstract</summary>
<em>Large-language reasoning models are now powerful enough to perform mathematical reasoning in theoretical physics at graduate or even research level. In the mathematics community, data sets such as FrontierMath are being used to drive progress and evaluate models, but theoretical physics has so far received less attention. In this talk I will first present our dataset TPBench (arxiv:2502.15815, tpbench.org), which was constructed to benchmark and improve AI models specifically for theoretical physics. I will analyze both the strengths and remaining weaknesses of LLMs in theoretical physics reasoning, and discuss strategies to improve their performance. I will then show our new results (arxiv:2506.20729) comparing different test-time scaling techniques on TPBench, including sequential and parallel reasoning methods combined with symbolic verification to boost performance.</em>
</details>

**2:45–3:30 pm ET**

*Low latency machine learning at the LHCb experiment*

Eluned Smith, MIT

<details>
<summary>Abstract</summary>
<em>With an anticipated input rate of 200 Tb/s, the LHCb experiment demands real-time data reduction at the detector level to prevent irreversible loss of valuable physics information. This talk presents an overview of efforts to deploy machine learning inference directly on compact, radiation-tolerant FPGAs located near the detector readout—an environment that imposes stringent constraints on latency and resource utilization. As a concrete example, I highlight the use of Variational Autoencoders (VAEs) that can simultaneously compress waveforms and extract precise timestamps within the required latency budget. I also discuss other potential and ongoing machine learning applications within LHCb's front-end systems.</em>
</details>

**3:30–4:00 pm ET**

Closing


## Speakers
 
<div class="card-columns">
  <!--<div class="row">-->
    
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-alexandre-adam..jpg" alt="Alexandre Adam" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://github.com/AlexandreAdam">Alexandre Adam</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Montreal </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-noemi-anau-montel.jpg" alt="Noemi Anau Montel" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://noemiam.github.io/">Noemi Anau Montel</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Max-Planck Institute for Astrophysics </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-petros-boufounos.jpg" alt="Petros Boufounos" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://boufounos.com/">Petros Boufounos</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MERL </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sueyeon-chung.jpg" alt="SueYeon Chung" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://sites.google.com/site/sueyeonchung/">SueYeon Chung</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Harvard University </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-aleksandra-ciprijanovic.jpg" alt="Aleksandra Ciprijanovic" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.alexciprijanovic.com/">Aleksandra Ciprijanovic</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> FNAL </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-michael-douglas.jpg" alt="Michael Douglas" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://scgp.stonybrook.edu/people/faculty/bios/michael-r-douglas">Michael Douglas</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Harvard University </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-francois-drielsma.jpg" alt="Francois Drielsma" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://profiles.stanford.edu/francois-drielsma">Francois Drielsma</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> SLAC National Accelerator Laboratory </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-cristiano-fanelli.jpg" alt="Cristiano Fanelli" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://cristianofanelli.com/">Cristiano Fanelli</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> William & Mary </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-dylan-foster..jpg" alt="Dylan Foster" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://dylanfoster.net/">Dylan Foster</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Microsoft </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-liang-fu.jpg" alt="Liang Fu" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://physics.mit.edu/faculty/liang-fu/">Liang Fu</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MIT and IAIFI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-alex-gagliano.jpg" alt="Alexander Gagliano" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://alexandergagliano.github.io/">Alexander Gagliano</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IAIFI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-lukas-heinrich..jpg" alt="Lukas Heinrich" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.lukasheinrich.com/">Lukas Heinrich</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Technical University Munich </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-matthew-ho.jpg" alt="Matthew Ho" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://maho3.github.io/">Matthew Ho</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Columbia University </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-shih-chieh-hsu.jpg" alt="Shih-Chieh Hsu" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://faculty.washington.edu/schsu/">Shih-Chieh Hsu</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Washington </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-robert-huang.jpg" alt="Hsin-Yuan (Robert) Huang" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://hsinyuan-huang.github.io/">Hsin-Yuan (Robert) Huang</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Caltech and Google </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sven-krippendorf.jpg" alt="Sven Krippendorf" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://krippendorflab.github.io/">Sven Krippendorf</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Cambridge </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-akshay-krishnamurthy.jpg" alt="Akshay Krishnamurthy" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://people.cs.umass.edu/~akshay/">Akshay Krishnamurthy</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Microsoft </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-michelle-kuchera.jpg" alt="Michelle Kuchera" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://alpha-davidson.github.io/">Michelle Kuchera</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Davidson College </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-francois-lanusse.jpg" alt="Francois Lanusse" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://flanusse.net/">Francois Lanusse</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> CNRS </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-simonetta-liuti..jpg" alt="Simonetta Liuti" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://uva.theopenscholar.com/simonetta-liuti/">Simonetta Liuti</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Virginia </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-peter-melchior..jpg" alt="Peter Melchior" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://pmelchior.net/">Peter Melchior</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Princeton University </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-moritz-munchmeyer.jpg" alt="Moritz Münchmeyer" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.moritzmunchmeyer.com/">Moritz Münchmeyer</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Wisconsin-Madison </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-lina-necib.jpg" alt="Lina Necib" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://lnecib.com/">Lina Necib</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MIT and IAIFI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-tri-nguyen.jpg" alt="Tri Nguyen" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://trivnguyen.github.io/">Tri Nguyen</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Northwestern University and SkAI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-costis-papageorgakis.jpg" alt="Costis Papageorgakis" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.qmul.ac.uk/spcs/staff/academics/profiles/cpapageorgakis.html">Costis Papageorgakis</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Queen Mary University of London </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-eluned-smith.jpg" alt="Eluned Smith" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://physics.mit.edu/faculty/eluned-smith/">Eluned Smith</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MIT and IAIFI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-hidenori-tanaka.jpg" alt="Hidenori Tanaka" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://sites.google.com/view/htanaka/home">Hidenori Tanaka</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Harvard University and IAIFI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sokratis-trifinopoulos.jpg" alt="Sokratis Trifinopoulos" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://strifinopoulos.github.io/">Sokratis Trifinopoulos</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MIT and IAIFI </em> <br>
         </div>
         </div>
       </div>
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-amy-zhang.jpg" alt="Amy Zhang" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://amyzhang.github.io/">Amy Zhang</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> UT Austin </em> <br>
         </div>
         </div>
       </div>

</div>

<br>

## Accommodations
We have established discounted rates for August 10–August 16, 2025 at the following hotels:

* <b>Porter Square Hotel</b>, 1924 Massachusetts Avenue, Cambridge, MA 02142. 
    
    $235-275 nightly rate (1-2 people per room)
    
    Deadline to book: First come, first served

    To book, call 617-499-3399 and reference code 141315.
    
* <b>Hotel 1868</b>, 1868 Massachusetts Avenue, Cambridge, MA 02142. 
    
    $225-265 nightly rate (1-2 people per room)
    
    Deadline to book: First come, first served

    To book, call 617-499-3399 and reference code 141315.
    
Other area hotels include: 
* <b>[Charles Hotel](https://www.charleshotel.com)</b>
* <b>[Harvard Square Hotel](https://www.harvardsquarehotel.com)</b>
* <b>[Irving House at Harvard](https://www.irvinghouse.com)</b>
* <b>[Prentiss House](https://prentisshouse.com)</b>
    
Workshop attendees are also welcome to book dorms for a discounted rate at Harvard University: 
* <b>Harvard University Dorms, 36 Oxford Street, Cambridge, MA 02138</b>

    $110 nightly rate (1 person per room only) 

    **Note: Dorm booking is now closed.**


## FAQ 
* *Who can attend the Summer Workshop?* Any researcher working at or interested in the intersection of physics and AI is encouraged to attend the Summer Workshop. 
* *What is the cost to attend the Summer Worskhop?* The registration fee for the Summer Workshop is 200 USD and includes a welcome dinner, as well as coffee breaks and snacks.
* *If I come to the Summer School, can I also attend the Workshop?* Yes! We encourage you to stay for the Workshop and you can stay in the dorms for both events if you choose (at your expense). 
* *Will the recordings of the talks be available?* We plan to share the talks on our [YouTube channel](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA).

[Submit a question or comment](https://app.smartsheet.com/b/form/76c1d070d19d4688b65962c4ed190478){:.button.button--outline-primary.button--pill.button--sm}

## 2025 Organizing Committee 
* Fabian Ruehle, Chair (Northeastern University)
* Bill Freeman (MIT) 
* Cora Dvorkin (Harvard)
* Thomas Harvey (IAIFI Fellow)
* Sam Bright-Thonney (IAIFI Fellow)
* Sneh Pandya (Northeastern)
* Yidi Qi (Northeastern)
* Manos Theodosis (Harvard)
* Marshall Taylor (MIT)
* Marisa LaFleur (IAIFI Project Manager)
* Thomas Bradford (IAIFI Project Coordinator)


# 2024 Summer Workshop 

<img src="images/summer-workshop-logo_2024.png" align="left" style="max-width:5990px;width:100%" hspace="10" vspace="10"> 

The IAIFI Summer Workshop brings together researchers from across Physics and AI for plenary talks, poster sessions, and networking to promote research at the intersection of Physics and AI.

**Many of the videos from the 2024 IAIFI Summer Workshop are now [posted on the IAIFI YouTube channel](https://youtube.com/playlist?list=PLBY0ED2StbGZ-XaBaBu4IFgkRNyj54Ba9&feature=shared).**
{:.info} 

**Many of the speakers' slides from the 2024 IAIFI Summer Workshop are now [available online](https://drive.google.com/drive/folders/1oc50D5LE6BvAzHozT98VyLn1KoU1aN9d?usp=sharing).** 
{:.info} 

* **The 2024 Summer Workshop was held August 12–16, 2024**
* **Location: Bartos Theater, MIT List Visual Arts Center, Lower Level (20 Ames Street, Cambridge)**
* **Registration deadline: July 31, 2024** 

Here's what attendees at previous IAIFI Summer Workshops had to say about the experience: 

<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<iframe width="560" height="315" src="https://www.youtube.com/embed/QRfdc-3o01g?si=oHLv6eRpGUnpe__2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<!--
We have extended the deadline to [submit a poster](https://t.co/AmNkXRoWeg).  Submit by July 17, 2023 for full consideration!
{:.success}
-->

[Agenda](#agenda){:.button.button--outline-primary.button--pill.button--lg} [Speakers](#speakers){:.button.button--outline-primary.button--pill.button--lg}

## About
The Institute for Artificial Intelligence and Fundamental Interactions (IAIFI) is enabling physics discoveries and advancing foundational AI through the development of novel AI approaches that incorporate first principles, best practices, and domain knowledge from fundamental physics. The goal of the Workshop is to serve as a meeting place to facilitate advances and connections across this growing interdisciplinary field.

[View recommendations for meals and activities around MIT](https://docs.google.com/document/d/1Z2qX9Owxi7IV3D2q3xBIXns5y4r3rAps/edit#heading=h.gjdgxs)

## Agenda

<img src="images/2024-workshop-agenda.png" align="left" style="max-width:2108px;width:100%" hspace="10" vspace="10">

### Monday, August 12, 2024
**9:15-9:30 am ET**

Welcome

**9:30–10:15 am ET**

*10,000 Einsteins: AI and the future of theoretical physics*

Matt Schwartz, Harvard/IAIFI

<details>
<summary>Abstract</summary>
<em>AI has already proved revolutionary in many areas of physics, particularly those focused on data analysis. However, machines are also advancing rapidly in symbolic tasks. As much of what is done in theoretical physics is symbolic, there is tremendous potential for machines to transition from data analysis to formal theoretical work. This talk will discuss some initial progress in this direction and a vision for how machines and humans might collaborate in the future to solve some of the most challenging problems in fundamental physics.</em>
</details>

**10:15–11:00 am ET**

*Dynamic Models from Data*

Nathan Kutz, University of Washington

<details>
<summary>Abstract</summary>
<em>Physics based models and governing equations dominate science and engineering practice.  The advent of scientific computing has transformed every discipline as complex, high-dimensional and nonlinear systems could be easily simulated using numerical integration schemes whose accuracy and stability could be controlled.  With the advent of machine learning, a new paradigm has emerged in computing whereby we can build models directly from data.  In this work, integration strategies for leveraging the advantages of both traditional scientific computing and emerging machine learning techniques are discussed.  Using domain knowledge and physics-informed principles, new paradigms are available to aid in engineering understanding, design and control.</em>
</details>

**11:00-11:30 am ET**

Break

**11:30 am–12:15 pm ET**

*Accurate, efficient, and reliable learning of deep neural operators for multiphysics and multiscale problems*

Lu Lu, Yale University

<details>
<summary>Abstract</summary>
<em>It is widely known that neural networks (NNs) are universal approximators of functions. However, a less known but powerful result is that a NN can accurately approximate any nonlinear operator. This universal approximation theorem of operators is suggestive of the potential of deep neural networks (DNNs) in learning operators of complex systems. In this talk, I will present the deep operator network (DeepONet) to learn various operators that represent deterministic and stochastic differential equations. I will also present several extensions of DeepONet, such as DeepM&Mnet for multiphysics problems, DeepONet with proper orthogonal decomposition or Fourier decoder layers, MIONet for multiple-input operators, and multifidelity DeepONet. I will demonstrate the effectiveness of DeepONet and its extensions to diverse multiphysics and multiscale problems, such as bubble growth dynamics, high-speed boundary layers, electroconvection, hypersonics, geological carbon sequestration, and full waveform inversion. Deep learning models are usually limited to interpolation scenarios, and I will quantify the extrapolation complexity and develop a complete workflow to address the challenge of extrapolation for deep neural operators.</em>
</details>

**12:15–1:30 pm ET**

Lunch

**1:30–3:00 pm ET**

**Contributed Talks Session A - Representation/Manifold Learning**

Bartos Theater

<details>
<summary>Symmetries and neural tangent kernels: using physical principles to understand deep learning, Jan Gerken (Chalmers University of Technology)</summary>
<em>Despite its extraordinary success in applications, a thorough theoretical understanding of deep learning is still lacking, making progress depend largely on costly trial-and-error procedures. At the same time, theoretical physics has a long history of developing deep mathematical understanding of complex systems. In this talk, I will present some recent work on how techniques from theoretical physics can be used to deepen our understanding of deep learning and lead to practically relevant insights. In particular, symmetries, which are an established cornerstone of theoretical physics, have reached widespread popularity as a guiding principle in deep learning as well. In machine learning, symmetries feature most importantly in the form of data augmentation and equivariant neural networks. At the same time, neural tangent kernels, which are closely related to statistical field theory, have emerged as a powerful tool to understand neural networks both at initialization and during training. Combining these paradigms leads to practically relevant statements in deep learning. Furthermore, it opens the door towards further deepening the connecting between theoretical physics and our understanding of neural networks.</em>
</details>

<details>
<summary> Approximately-symmetric neural networks for quantum spin liquids, Dominik Kufel (Harvard University)</summary>
<em>We propose and analyze a family of approximately-symmetric neural networks for quantum spin liquid problems. These tailored architectures are parameter-efficient, scalable, and significantly out-perform existing symmetry-unaware neural network architectures. Utilizing the mixed-field toric code model, we demonstrate that our approach is competitive with the state-of-the-art tensor network and quantum Monte Carlo methods. Moreover, at the largest system sizes (N=480), our method allows us to explore Hamiltonians with sign problems beyond the reach of both quantum Monte Carlo and finite-size matrix-product states. The network comprises an exactly symmetric block following a non-symmetric block, which we argue learns a transformation of the ground state analogous to quasiadiabatic continuation. Our work paves the way toward investigating quantum spin liquid problems within interpretable neural network architectures.</em>
</details>

<details>
<summary>Title to come, Simonetta Liuti (The University of Virginia)</summary>
<em>Abstract to come</em>
</details>

<details>
<summary> A Neural Net Model for Distillation with Weights Explained, Berfin Simsek (NYU/Flatiron Institute)</summary>
<em>It is important to understand how large models represent knowledge to make them efficient and safe. We study a toy model of neural nets that exhibits non-linear dynamics and phase transition. Although the model is complex, it allows finding a family of the so-called "copy-average" critical points of the loss. The gradient flow initialized with random weights consistently converges to one such critical point for networks up to a certain width, which we proved to be optimal among all copy-average points. Moreover, we can explain every neuron of a trained neural network of any width. As the width grows, the network changes the compression strategy and exhibits a phase transition. We close by listing open questions calling for further mathematical analysis and extensions of the model considered here.</em>
</details>

**Physics-Motivated Optimization**
<details>
<summary>Beyond Closure Models: Estimating Long-term Statistics of Chaotic-Systems via Physics-Informed Neural Operators, Chuwei Wang (Caltech)</summary>
<em>Accurately predicting the long-term behavior of chaotic systems is important in many applications. This requires iterative computations on a dense spatiotemporal grid to account for the unstable nature of chaotic systems, which is expensive and impractical in many real-world scenarios. The alternative approach to such a full-resolved simulation is using a coarse grid and then correcting its errors through a 'closure model', which approximates the overall information from fine scales not captured in the coarse-grid simulation. Recently, ML approaches have been used for closure modeling, but they typically require a large number of training samples from expensive fully-resolved simulations (FRS). In this work, through the lens of Liouville flow in function spaces, we prove an even more fundamental limitation, viz., the standard approach to learning closure models suffers from a large approximation error for generic problems, no matter how large the model is, and it stems from the non-uniqueness of the mapping. We propose an alternative end-to-end learning approach using a physics-informed neural operator (PINO) that overcomes this limitation by not using a closure model or a coarse-grid solver.   We first train the PINO model on data from a coarse-grid solver and then fine-tune it with (a small amount of) FRS and physics-based losses on a fine grid. The discretization-free nature of neural operators means that they do not suffer from the restriction of a coarse grid that closure models face, and they can provably approximate the long-term statistics of chaotic systems. In our experiments on fluid dynamics, our PINO model achieves a 120x speedup compared to FRS with a relative error ~5%. In contrast, the closure model coupled with a coarse-grid solver is 58x slower than PINO while having a much higher error 205% when the closure model is trained on the same FRS dataset.</em>
</details>

<details>
<summary>Determining Heterogeneous Elastic Properties of Soft Materials using Physics-Informed Neural Networks, Wensi Wu (Children's Hospital of Philadelphia)</summary>
<em>The heterogeneous mechanical properties found in biological materials have profound implications for both engineering and medical applications. Within the engineering community, these properties are frequently studied to guide the design of mechanical devices such as artificial organs and soft robots. Concurrently, in the medical field, the mechanical properties of tissues play a crucial role in providing diagnostic information about various diseases and conditions. The significance of material mechanical properties across these diverse domains has driven a need to better understand the underlying mechanisms governing the microscopic properties of biological tissues and their associated functions, whether for improving material designs or disease diagnosis. In traditional engineering, identifying unknown material parameters requires iterative inverse finite element analyses and optimization of the constitutive parameters until the finite element model achieves an acceptable level of mechanical response, aligning with experimental data. While this method is efficient with homogeneous materials, optimizing the elasticity map of heterogeneous materials is challenging. In this work, we propose using physics-informed neural networks (PINNs) to identify the full-field elastic properties of highly nonlinear, hyperelastic materials. We applied our improved PINNs to six structurally complex materials and three constitutive material models (Neo-Hookean, Mooney-Rivlin, and Gent) to evaluate the accuracy of full-field elasticity maps estimated by PINNs. Our PINN model consistently produced highly accurate estimates of the full-field elastic properties, even when there was up to 10% noise present in the training data.</em>
</details>

**Contributed Talks Session B - Generative Models**

MIT Media Lab, Room 633

<details>
<summary>Machine learning phase transitions: A probabilistic perspective, Julian Arnold (University of Basel)</summary>
<em>The identification of phase transitions and the classification of different phases of matter from data are among the most popular applications of machine learning in physics. Neural network (NN)-based approaches have proven to be particularly powerful due to the ability of NNs to learn arbitrary functions. Many such approaches work by computing indicators of phase transitions from the output of NNs trained to solve specific classification problems. In this talk, I will derive the optimal solutions to these classification problems given by Bayes classifiers that take into account the probability distributions underlying the physical system under consideration [1]. This probabilistic viewpoint allows us to gain a deeper understanding of previous NN-based studies, highlighting the strengths and weaknesses of individual methods [1], enables us to root the methods in information theory [2], yields more efficient numerical routines based on the incorporation of readily available generative models [3], and widens the application domain of these methods to systems outside physics (such as diffusion models or transformers) [4,5]. 
[1] J. Arnold and F. Schäfer, PRX 12, 031044 (2022) [2] J. Arnold et al., arXiv:2311.10710 (2023) [3] J. Arnold et al., PRL 132, 207301 (2024) [4] J. Arnold et al., arXiv:2311.09128 (2023) [5] J. Arnold et al., arXiv:2405.17088 (2024)</em>
</details>

<details>
<summary>Accelerating Molecular Discovery with Machine Learning, Yuanqi Du (Cornell University)</summary>
<em>Recent advancements in machine learning have paved the way for groundbreaking opportunities in the realm of molecular discovery. At the forefront of this evolution are improved computational tools with proper inductive biases and efficient optimization. In this talk, I will delve into our efforts around these themes from a geometry, sampling and optimization perspective. I will first introduce how to encode symmetries in the design of neural networks and the balance of expressiveness and computational efficiency. Next, I will discuss how generative models enable a wide range of design and optimization tasks in molecular discovery. In the third part, I will talk about how the advancements in stochastic optimal control, sampling and optimal transport can be applied to find transition states in chemical reactions.</em>
</details>

<details>
<summary>Understanding Diffusion Models by Feynman's Path Integral, Yuji Hirono (Osaka University)</summary>
<em>Score-based diffusion models have proven effective in image generation and have gained widespread usage. We introduce a novel formulation of diffusion models using Feynman's path integral [1]. We find this formulation providing comprehensive descriptions of score-based generative models, and demonstrate the derivation of backward stochastic differential equations and loss functions.The formulation accommodates an interpolating parameter connecting stochastic and deterministic sampling schemes, and we identify this parameter as a counterpart of Planck's constant in quantum physics. This analogy enables us to apply the Wentzel-Kramers-Brillouin (WKB) expansion, a well-established technique in quantum physics, for evaluating the negative log-likelihood to assess the performance disparity between stochastic and deterministic sampling schemes.
Reference: [1] Yuji Hirono, Akinori Tanaka, Kenji Fukushima, accepted in ICML2024 [arXiv:2403.11262].</em>
</details>

<details>
<summary>Neural Entropy, Akhil Premkumar (University of Chicago)</summary>
<em>What is the smallest neural network that can do a particular task? To answer this question we need to understand the capacity of neural networks to encode and store information. In the context of generative diffusion models, we show that it is possible to identify the entropy of the network, which characterizes precisely its storage capacity.</em>
</details>

<details>
<summary>Predicting Missing Regions in Charged Particle Tracks Using a Sparse 3D Convolutional Neural Network, Hilary Utaegbulam (University of Rochester)</summary>
<em>The 2x2 Demonstrator is a prototype of ND-LAr, the liquid argon time-projection chamber of the Deep Underground Neutrino Experiment’s Near Detector complex. Both the 2x2 Demonstrator and ND-LAr are modular detectors that will have pixelated charge readouts and inactive regions wherein there is no sensitivity to charge deposition and light signals that arise from charged particle interactions with liquid argon. In the 2x2, these inactive regions are located in between the active detector modules, which introduces the challenge of inferring what charge signals ought to look like in these regions. This study explores the use of a Sparse 3D Convolutional Neural Network (ConvNet) to infer missing regions in charged particle tracks. Hits corresponding to energy depositions are voxelized into a three-dimensional grid for each track. Voxels that fall into predefined inactive regions are removed to simulate the lack of detector output. The model is trained to infer the topology of the missing track voxels, with the ultimate goal of inferring the missing charge or energy values in these voxels as well. Results indicate that this approach shows promise in prediction of missing track regions with some accuracy.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

*What Do Language Models Have To Say About Fundamental Physics?* 

Mariel Pettee, LBNL/Flatiron

<details>
<summary>Abstract</summary>
<em>The launch of ChatGPT in November 2022 ignited an ongoing worldwide conversation about the possible impacts of Large Language Models (LLMs) on the way we work. As scientists, however, the changes in our workflows since the advent of this technology have been relatively minor. Will this still be the case in 10 years? Could an analogous paradigm shift arise from a foundation model trained on a large amount of scientific data, transforming the way we conduct our research? If so, what can we learn from the development of other foundation models, particularly LLMs, in their evolution from specialists to (quasi-)generalists? In this talk, I will present some recent work exploring how language models could help form a foundation model of fundamental physics. I'll also share my perspective on how we should strive to shape such models to reflect our highest priorities as scientists.</em>
</details>

**4:15-5:00 pm ET**

*Solving the nuclear many-body problem with neural quantum state*

Alessandro Lovato, Argonne National Laboratory

<details>
<summary>Abstract</summary>
<em>Artificial neural networks can be employed to accurately and compactly represent quantum many-body states relevant to many applications, including nuclear physics, quantum chemistry, and condensed matter problems. I will argue that a variational Monte Carlo algorithm based on neural-network quantum states provides a systematically improvable solution to the nuclear Schrödinger equation with a polynomial cost in the number of nucleons. After presenting recent progress in describing atomic nuclei, neutron-star matter, and hypernuclei, I will illustrate an application to condensed-matter systems, specifically ultra-cold Fermi gases near the unitary limit. Detailed benchmarks with continuum Quantum Monte Carlo methods will be presented.</em>
</details>

**5:00–7:00 pm ET**

Poster Session

MIT Media Lab, 6th Floor

<details>
<summary>Details</summary>

<ul> <li> Data Compression and Inference in Cosmology with Self-Supervised Machine Learning, Aizhan Akhmetzhanova (Harvard University) </li>
<li> CNN and Transformer architecture for jets events classification, Juvenal Bassa (University of Puerto Rico - Mayaguez) </li> 
<li>Data-Driven Discovery of X-ray Transients with Machine Learning, Steven Dillmann (University of Cambridge)</li>
<li>Sampling Transition Dynamics with Machine Learning Approaches, Yuanqi Du (Cornell University)</li>
<li>Multi-Modal Generalized Class Discovery for Scalable Autonomous All-Sky Surveys, Sriram Elango (Harvard University)</li>
<li>Inverse Design of Complex Fluids with Fully-Differentiable Lagrangian Particle Dynamics, Kaylie Hausknecht (Harvard University and MIT)</li>
<li>Perfect Jet Classification Through Equivariant Regression, Timothy Hoffman (University of Chicago)</li>
<li>Flow-Based Generative Emulation of Grids of Stellar Evolutionary Models, Marc Hon (MIT Kavli Institute for Astrophysics and Space Research)</li>
<li>Enhancing Cosmological Simulations with Efficient and Interpretable Machine Learning in the Wavelet Basis, Cooper Jacobus (UC Berkeley: Dept. Astrophysics, Lawrence Berkeley National Lab: Computational Cosmology Center)</li>
<li>Training neural operators to preserve invariant measures of chaotic attractors, Ruoxi Jiang (University of Chicago)</li>
<li>Hidden Giants: Redefining QSO Classification and Outlier Detection with Redshift Invariant Autoencoders, Thaddaeus Kiker (Columbia University)</li>
<li>KAN: Kolmogorov-Arnold Networks, Ziming Liu (MIT, IAIFI)</li>
<li>Phase Transitions in the Output Distribution of Large Language Models, Niels Loerch (University of Basel)</li>
<li>Tackling reasoning problems with AI, Rishabh Mallik (Forschungszentrum Jülich)</li>
<li>Recurrent Features of Amplitudes in Planar N = 4 Super Yang-Mills Theory, Garrett Merz (University of Wisconsin-Madison)</li>
<li>Ultrafast Jet Classification using Geometric Learning, Patrick Odagiu (ETH Zurich)</li>
<li>Deep Stochastic Mechanics, Elena Orlova (The University of Chicago)</li>
<li>Differentiable and Distributional Cosmological Stasis, Sneh Pandya (Northeastern / IAIFI)</li>
<li>Exploring Astronomical Catalog Crossmatching with Machine Learning, Victor Samuel Perez Diaz (Center for Astrophysics | Harvard & Smithsonian, IAIFI)</li>
<li>Towards an AI-enabled astronomy system: natural language processing of Chandra data archive, Shivam Raval (Harvard University)</li>
<li>Auto-decoding Poisson Processes for Unsupervised X-ray Sources Learning, Yanke Song (Harvard University, Department of Statistics)</li>
<li>Development of photothermal techniques for the detection of cancer biomarkers, Ilhem Soyah (Higher school of sciences and technology of Hammam Sousse)</li>
<li>Multi-Modal Contrastive Training for Robust VQA, Mitra Tajrobehkar (Vertical Oceans)</li>
<li>Zero-Shot Classification of Astronomical Images with Large Multimodal Models, Dimitrios Tanoglidis (University of Pennsylvania)</li>
<li>Vertex finding and jet class classification using Wasserstein Neural Network, Diego F. Vasquez Plaza (Univesity Puerto rico Mayagüez)</li>
<li>Learning Group Invariant CY Metrics by Fundamental Domain Projections, Moritz Walden (Uppsala University)</li>
<li>Accelerating Energy Computation in Many-electron Systems with Forward Laplacian, Chuwei Wang (Caltech)</li>
<li>Emulating the Effects of Pile-Up on X-ray Spectra, Justina Yang (Harvard University)</li>
<li>A Variational Continuation Method for Periodic Orbits Using Autograd and Hessian Eigendecompositions, Leo Yao (MIT)</li>
<li>HyperTagging: Reconstruction of Full Decays using Transformers and Hyperbolic Embedding, Boyang Yu (LMU Munich, Germany)</li>
<li>Neural scaling laws from large-N field theory, Zhengkang Zhang (University of Utah)</li>
<li>Revealing the 3D Cosmic Web with Physics Constrained Neural Fields, Brandon Zhao (Caltech)</li> </ul>
</details>

**6:00–8:00 pm ET**

Welcome Reception

MIT Media Lab, 6th Floor

### Tuesday, August 13, 2024

**9:30–10:15 am ET**

*Trends in AI for particle accelerators*

Verena Kain, CERN

<details>
<summary>Abstract</summary>
<em>AI is without doubt radically transforming science with many successful applications in molecular biology, astrophysics, nuclear physics and particle physics. It has enabled significant technological advances for robotics that can particularly enhance a system’s perception, navigational and manipulation abilities and interaction. For control, it enables novel and faster learning/teaching of tasks, replacing or augmenting classical control techniques for hard problems such as real-time control of the non-linear dynamics of the plasma in a tokamak of a fusion reactor, or navigating drones with super-human performance. Given the success and types of use cases that can be solved with AI algorithms, accelerator physics and associated technologies have also picked up on AI in the last 5 to 10 years with the number of ML applications steadily rising  - and subsequently the number of ML related papers at the big particle accelerator conferences. This contribution will give a brief overview of the typical use cases for AI for particle accelerators, show recent trends and describe the potential and vision of AI for particle accelerators with the emphasis on control and optimisation of particle accelerators.</em>
</details>

**10:15–11:00 am ET**

*An introduction to neural ODEs in scientific machine learning*

Patrick Kidger, Cradle.bio

<details>
<summary>Abstract</summary>
<em>This is an introduction to neural ODEs for scientific applications. The goal is to (a) provide a modelling tool that enhances the expressivity of existing theory-driven approaches, (b) demonstrate that neural ODEs are easy to use via modern autodifferentiable software, and (c) give enough of the tips-and-tricks needed to make neural ODEs work in practice!</em>
</details>

**11:00-11:30 am ET**

Break

**11:30 am–12:15 pm ET**

*Automatic Symmetry Discovery from Data*

Rose Yu, UCSD

<details>
<summary>Abstract</summary>
<em>Despite the success of equivariant neural networks in scientific applications, they require knowing the symmetry group a priori. However, it may be difficult to know which symmetry to use as an inductive bias in practice. Enforcing the wrong symmetry could even hurt the performance. In this talk, I will discuss our effort in developing a deep learning framework that can automatically discover symmetry from data.  Our framework, LieGAN, represents symmetry as interpretable Lie algebra basis and uses a paradigm akin to generative adversarial training. We further generalized it LaLieGAN to discover non-linear symmetries from high-dimensional data.  Empirically, the learned symmetry can also be readily used in  existing equivariant neural networks to improve accuracy and generalization in prediction. It can also improve equation discovery and long-term forecasting for various dynamical systems.</em>
</details>

**12:15–1:30 pm ET**

Lunch

**1:30–3:00 pm ET**

**Contributed Talks - Session A - Foundational ML**

Bartos Theater

<details>
<summary>Diversity with Similarity as a Measure of Dataset Quality, Josiah Couch (Beth Israel Deaconess Medical Center)</summary>
<em>Dataset size and class balance are important measures in deep learning. Maximizing them is seen as a way to ensure that datasets contain diverse images, which models are thought to need in order to generalize well. Yet neither size nor class balance measure image diversity directly, raising the possibility that better measures of dataset quality might exist. To test this hypothesis, we turned to a comprehensive framework of diversity measures that generalizes familiar quantities like Shannon entropy by accounting for the similarities and differences among images. (Size and class balance emerge from this framework as special cases.) We created several thousand diverse datasets by subsampling a variety of large medical-image datasets representing a range of imaging modalities, trained classifiers on these subsets, and calculated the correlation between subset diversity and model accuracy using diversity measures from the framework.</em>
</details>

<details>
<summary>RG flow of the NTK dynamics at finite-width from Feynman diagrams, Max Guillen (Chalmers University of Technology)</summary>
<em>Deep Learning is nowadays a well-stablished method for different applications in science and technology. However, it has been unclear for a long time how the "learning process" actually occurs in different architectures, and how this knowledge could be used to optimize performance and efficiency. Recently, high-energy-physics-based ideas have been applied to the modelling of Deep Learning, thus translating the learning problem to an RG flow analysis in Quantum Field Theory (QFT). In this talk, I will explain how these quite complicated formulae describing such RG flows for different observables in neural networks at initialization, can be easily obtained from a few rules resembling Feynman rules in QFT. I will also comment on some work in progress which implements such rules for computing higher-order corrections to the frozen (infinite-width) NTK for particular activation functions, and how they evolve after a few steps of SGD.</em>
</details>

<details>
<summary>Supervised learning of infinitely-overparameterized DNNs through the lens of Wilsonian RG, Anindita Maiti (Perimeter Institute)</summary>
<em>The key to the performance of ML algorithms is an ability to segregate relevant features in input datasets from the irrelevant ones. In a setup where data features play the role of an energy scale, we develop a Wilsonian RG framework to integrate out unlearnable modes associated with the Neural Network Gaussian Process (NNGP) kernel, in the regression context. Such a framework in the case of Gaussian features leads to a universal flow of the ridge parameter, whereas, non-Gaussianities in data features result in rich input-dependent RG flows. This framework goes beyond the usual analogies between RG flows and learning dynamics, and offers potential improvements to our understanding of feature learning and universality classes of models.</em>
</details>

<details>
<summary>Input Space Mode Connectivity in Deep Neural Networks, Jakub Vrabel (CEITEC, Brno University of Technology)</summary>
<em>We extend the concept of loss landscape mode connectivity to the input space of deep neural networks. Mode connectivity was originally studied within parameter space, where it describes the existence of low-loss paths between different solutions (loss minimizers) obtained through gradient descent. We present theoretical and empirical evidence of its presence in the input space of deep networks, thereby highlighting the broader nature of the phenomenon. We observe that different input images with similar predictions are generally connected, and for trained models, the path tends to be simple, with only a small deviation from being a linear path. Our methodology utilizes real, interpolated, and synthetic inputs created using the input optimization technique for feature visualization. To prove the existence of general mode connectivity in high-dimensional input spaces, we employ percolation theory. We argue that the approximate linear mode connectivity post-training is a manifestation of some implicit bias. We exploit mode connectivity to obtain new insights about adversarial examples and demonstrate its potential for adversarial detection. Additionally, we discuss applications for the interpretability of deep networks.</em>
</details>

<details>
<summary>Neural scaling laws from large-N field theory, Zhengkang Zhang (University of Utah)</summary>
<em>Many machine learning models based on neural networks exhibit scaling laws: their performance scales as power laws with respect to the sizes of the model and training data set. We use large-N field theory methods to solve a model recently proposed by Maloney, Roberts and Sully which provides a simplified setting to study neural scaling laws. Our solution extends the result in this latter paper to general nonzero values of the ridge parameter, which are essential to regularize the behavior of the model. In addition to obtaining new and more precise scaling laws, we also uncover a duality transformation at the diagrams level which explains the symmetry between model and training data set sizes. The same duality underlies recent efforts to design neural networks to simulate quantum field theories.</em>
</details>

<details>
<summary>Fourier-enhanced deep operator network for geophysics with improved accuracy, efficiency, and generalizability, Min Zhu (Yale University)</summary>
<em>Full waveform inversion (FWI) and geologic carbon sequestration (GCS) are two significant topics in geophysics. FWI infers subsurface structure information from seismic waveform data by solving a non-convex optimization problem. On the other hand, solving multiphase flow in porous media is essential for CO2 migration and pressure fields in the subsurface associated with GCS. However, numerical simulations for both FWI and GCS are computationally challenging and expensive due to the highly nonlinear governing partial differential equations (PDEs). Here, we develop a Fourier-enhanced deep operator network (Fourier-DeepONet) to address this issue. For FWI, compared with existing data-driven FWI methods, Fourier-DeepONet achieves more accurate predictions of subsurface structures across a wide range of source parameters. Additionally, Fourier-DeepONet demonstrates superior robustness when handling data with Gaussian noise or missing traces. For GCS, compared to the state-of-the-art Fourier neural operator (FNO), Fourier-DeepONet offers superior computational efficiency, with 90% fewer unknown parameters, significantly reduced training time (approximately 3.5 times faster), and much lower GPU memory requirements (less than 35%). Furthermore, Fourier-DeepONet maintains good accuracy when predicting out-of-distribution (OOD) data. This excellent generalizability is enabled by its adherence to the physical principle that the solution to a PDE is continuous over time.</em>
</details>

**Contributed Talks Session B - Physics-Motivated Optimization**

MIT Media Lab, Room 633

<details>
<summary>Search for new physics using Event-based anomaly detection at the ATLAS detector of CERN and development of ADFilter tool, Wasikul Islam (University of Wisconsin-Madison)</summary>
<em>Searches for new resonances in two-body invariant mass distributions are performed using an unsupervised anomaly detection technique in events produced in proton-proton collisions at a center of mass energy of 13 TeV recorded by the ATLAS detector at the LHC. Studies are conducted in data containing at least one isolated lepton. An autoencoder network is trained with 1% randomly selected collision events and anomalous regions are then defined which contain events with high reconstruction losses from the decoder. Nine invariant mass distributions are inspected which contain pairs of one light jet (or one b-jet) and one lepton, photon, or a second light jet (b-jet). The 95% confidence level upper limits on contributions from generic Gaussian signals are reported for the studied invariant mass distributions. The obtained model-independent limits show strong potential to exclude generic heavy states with complex decays.</em>
</details>

<details>
<summary>Marginalize, Don't Subtract:  Spectral Component Separation for Faint Objects in DESI, Ana Sofia Uzsoy (Harvard University)</summary>
<em>Component separation is a critical step in disentangling multiple signals and in extracting useful information from spectra. In this talk, I present MADGICS (Marginalized Analytic Dataspace Gaussian Inference for Component Separation), a data-driven Bayesian component separation technique that can separate a spectrum into any number of Gaussian-distributed components. I then discuss the application of this technique for automatically determining redshifts for Lyman Alpha Emitter (LAE) galaxies observed with DESI while marginalizing over sky residuals to separate sky from target emission lines. We create a covariance matrix from visually inspected DESI LAE targets to provide physically motivated priors, and determine redshift by jointly inferring sky, LAE, and residual components for each individual spectrum. This component separation technique will allow us to create a high-quality catalog of LAE spectra and redshifts from DESI data and is also broadly generalizable to other spectral features of interest.</em>
</details>

<details>
<summary>A Variational Continuation Method for Periodic Orbits Using Autograd and Hessian Eigendecompositions, Leo Yao (MIT)</summary>
<em>We present a Hessian-based approach to numerically continue periodic orbits. Our method offers precise initializations of oscillations around unstable fixed points, an integrator-free variational continuation method, and efficient detection of orbit family intersections and subharmonic bifurcations. Leveraging autograd for computations, we present full continuations of periodic double pendulum oscillations from fixed points and examples of detected bifurcations along these orbit families.</em>
</details>

<details>
<summary>Revealing the 3D Cosmic Web with Physics Constrained Neural Fields, Brandon Zhao (Caltech)</summary>
<em>Weak gravitational lensing is the slight distortion of galaxy shapes by the gravitational effect of the large-scale structure. In our work, we seek to invert the weak lensing signal found in 2D telescope images to obtain a 3D reconstruction of the universe’s dark matter field. While typically this inversion is done in 2D to obtain a projection of the dark matter field, accurate 3D maps of the dark matter distribution are particularly useful as they allow us to detect and localize structures of interest such as galaxy clusters, as well as disambiguate them from intervening matter along the line of sight. This inversion is ill-posed for several reasons. First, images are only observed from a single viewing angle, which must be inverted into a 3D mass distribution. Second, the exact locations and shapes of unlensed galaxies is in general unknown, and can only be estimated with a degree of uncertainty. This introduces a large amount of noise to our measurement of the lensing signal.  We propose a novel methodology using a physics-constrained, coordinate-based neural field to model the underlying continuous matter distribution. We take an analysis-by-synthesis approach, optimizing the weights of the neural network through a fully differentiable physical forward model to reproduce the lensing signal present in image measurements. We showcase reconstruction results on simulated measurements of dark matter distributions from a low resolution N-Body particle simulation, and compare our approach with earlier 3D inversion methods.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

*KAN: Kolmogorov-Arnold Networks*

Ziming Liu, MIT/IAIFI

<details>
<summary>Abstract</summary>
<em>Inspired by the Kolmogorov-Arnold representation theorem, we propose Kolmogorov-Arnold Networks (KANs) as promising alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have fixed activation functions on nodes ("neurons"), KANs have learnable activation functions on edges ("weights"). KANs have no linear weights at all -- every weight parameter is replaced by a univariate function parametrized as a spline. We show that this seemingly simple change makes KANs outperform MLPs in terms of accuracy and interpretability. For accuracy, much smaller KANs can achieve comparable or better accuracy than much larger MLPs in data fitting and PDE solving. Theoretically and empirically, KANs possess faster neural scaling laws than MLPs. For interpretability, KANs can be intuitively visualized and can easily interact with human users. Through two examples in mathematics and physics, KANs are shown to be useful collaborators helping scientists (re)discover mathematical and physical laws. In summary, KANs are promising alternatives for MLPs, opening opportunities for further improving today's deep learning models which rely heavily on MLPs.</em>
</details>

**4:15-5:00 pm ET**

*A Pathway to Robotic Intelligence*

Pulkit Agrawal, MIT/IAIFI

<details>
<summary>Abstract</summary>
<em>Details to come</em>
</details>

### Wednesday, August 14, 2024

**9:30–10:15 am ET**

*Navigating Complex Models: Neural Networks for High-Dimensional Statistical Inference*

Christoph Weniger, University of Amsterdam

<details>
<summary>Abstract</summary>
<em>Details to come</em>
</details>

**10:15–11:00 am ET**

*Data-Driven High-Dimensional Inverse Problems: A Journey Through Strong Lensing Data Analysis*

Laurence Levasseur, University of Montreal

<details>
<summary>Abstract</summary>
<em>Details to come</em>
</details>

**11:00-11:30 am ET**

Break

**11:30 am–12:15 pm ET**

*Machine Learning and Physics: The Alliance of the Titans*

Ayan Paul, Northeastern

<details>
<summary>Abstract</summary>
<em>Leaps in our understanding of Physics have been concomitant with the adoption of new and increasingly powerful mathematical structures that shift our perspective of how we probe the dynamics of the universe and allow us to unravel complex concepts that were hitherto inaccessible to us. In the realm of data-driven science, where physics is firmly planted, machine learning is proving to be a long-awaited and much-needed mathematical structure that has showcased its worth in aiding landmark discoveries, understanding the underlying symmetries of theories that we propose, and connecting signals to kinematics interpretably, to mention a few. In this parable on the charm of machine learning in physics, we will discuss the nuances of some of these achievements and lay out what we can expect from the future.</em>
</details>

**12:15–1:30 pm ET**

Lunch

**1:30–2:15 pm ET**

*Geometric Machine Learning*

Melanie Weber, Harvard University

<details>
<summary>Abstract</summary>
<em>A recent surge of interest in exploiting geometric structure in data and models in machine learning has motivated the design of a range of geometric algorithms and architectures. This lecture will give an overview of this emerging research area and its mathematical foundation. We will cover topics at the intersection of Geometry and Machine Learning, including relevant tools from differential geometry and group theory, geometric representation learning, graph machine learning, and geometric deep learning.</em>
</details>

**2:15–3:00 pm ET**


*Machine Learning for LHC Theory*

Tilman Plehn, Heidelberg

<details>
<summary>Abstract</summary>
<em>Details to come</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

*Asteroseismic probes of far-ranging astrophysics with big data and machine learning*

Earl Bellinger, Yale University

<details>
<summary>Abstract</summary>
<em>Space telescopes like the NASA Kepler and TESS missions as well as the forthcoming PLATO mission are driving a data revolution in stellar astrophysics. The ultra-precise observations provided by these missions are challenging our best models of how stars evolve, and are in turn granting insights into the formation and evolution of planetary systems and the Galaxy as a whole. They furthermore present novel opportunities to probe far-ranging physics, such as dark matter and theories of gravity beyond general relativity. In this talk, I will give an overview of the data, models, challenges, and opportunities in asteroseismology, and highlight the role that machine learning is playing in advancing our knowledge across astrophysics.</em>
</details>

**4:15-5:00 pm ET**

*Big data cosmology meets AI*

Carol Cuesta-Lazaro, IAIFI Fellow

<details>
<summary>Abstract</summary>
<em>The upcoming era of cosmological surveys promises an unprecedented wealth of observational data that will transform our understanding of the universe. Surveys such as DESI, Euclid, and the Vera C. Rubin Observatory will provide extremely detailed maps of billions of galaxies out to high redshifts. Analyzing these massive datasets poses exciting challenges that machine learning is uniquely poised to help overcome. In this talk, I will highlight recent examples from my work on probabilistic machine learning for cosmology. First, I will explain how a point cloud diffusion model can be used both as a generative model for 3D maps of galaxy clustering and as a likelihood model for such datasets. Moreover, I will present a generative model developed to reconstruct the initial conditions of the Universe from spectroscopic survey observations. When combined with the wealth of data from upcoming surveys, these machine learning techniques have the potential to provide new insights into fundamental questions about the nature of the universe.</em>
</details>

**5:30-6:30 pm ET**

*Panel on Industry–Academia Collaboration*

* Moderator: Carol Cuesta-Lazaro, IAIFI Fellow

* Bill Freeman, Professor of EECS, MIT

* Marin Soljacic, Professor of Physics, MIT

* Partha Saha, Distinguished Engineer, Data and AI Platform, Visa

* Nima Dehmamy, Research Assistant Professor, IBM Research MIT-IBM Lab

### Thursday, August 15, 2024

**9:30–10:15 am ET**

*Uncertainty Quantification from Neural Network Correlation Functions*

Yonatan Kahn, University of Illinois Urbana-Champaign

<details>
<summary>Abstract</summary>
<em>Details to come</em>
</details>

**10:15–11:00 am ET**

*Transformers to transform Scattering Amplitudes Calculation*

Tianji Cai, SLAC

<details>
<summary>Abstract</summary>
<em>AI for fundamental physics is now a burgeoning field, with numerous efforts pushing the boundaries of experimental and theoretical physics. In this talk, I will introduce a recent innovative application of Natural Language Processing to state-of-the-art calculations for scattering amplitudes. Specifically, we use Transformers to predict the symbols at high loop orders of the three-gluon form factors in planar N=4 Super Yang-Mills theory. Our results have demonstrated great promises of Transformers for amplitude calculations, opening the door for an exciting new scientific paradigm where discoveries and human insights are inspired and aided by AI.</em>
</details>

**11:00-11:30 am ET**

Break

**11:30 am–12:15 pm ET**

*Neural ansatze for physics and physics of neural networks*

Nima Dehmamy, IBM Research MIT-IBM Lab 

<details>
<summary>Abstract</summary>
<em>I will discuss some of our recent works on using ML to solve physics problems and using physics to understand ML. For the former, I will talk about using a "neural ansatz" for physics simulations and our work on gauge equivariant networks. For the latter, I will discuss our work on parameter space symmetries and conservation laws, as well as some work in progress on transformers. </em>
</details>

**12:15–1:30 pm ET**

Lunch

**1:30–3:00 pm ET**

**Contributed Talks: Session A - Uncertainty Quantification/Robust AI**

Bartos Theater

<details>
<summary>Jolideco: A Hybrid ML-Statistical Approach for Robust Image Deconvolution in Sparse Poisson Regimes, Axel Donath (Center for Astrophysics | Harvard & Smithsonian)</summary>
<em>Machine learning for sparse image data reconstruction remains challenging, particularly in Astronomy where ground truth is often unavailable. While simulations and transfer learning offer partial solutions, high-dimensional parameter spaces can render these approaches computationally expensive or infeasible. Moreover, in low-count Poisson domains, quantifying uncertainties is crucial. We present Jolideco, a novel hybrid method for joint likelihood image deconvolution that synergizes machine learning with classical statistical modeling. This approach leverages a hand-crafted forward model for the imaging process, incorporating prior information such as telescope characteristics and noise distributions. Simultaneously, it employs an high-dimensional, patch-based image prior trained via ML on astronomical images from other wavelengths to regularize image structure. Jolideco demonstrates significantly improved reconstruction quality across diverse source scenarios and signal-to-noise regimes. Its closed statistical framework facilitates multi-telescope data integration and robust uncertainty quantification. We showcase Jolideco's effectiveness using example data from the Chandra X-ray Observatory and the Fermi-LAT Gamma-ray Space Telescope, illustrating its potential to advance astronomical image analysis in the Poisson regime.</em>
</details>

<details>
<summary>Towards Quantitatively Trustworthy AI, Nicholas Kersting (Visa, Inc.)</summary>
<em>Safe and effective application of AI to Science and Industry can only proceed through  measuring trustworthiness quantitatively such that we may track and report progress.  Traditional statistical metrics such as Precision, Recall, AUC, etc., no longer sufficient on their own, are supplemented with measures of reliability such as Explainable AI (XAI), most recently in Large Language Model Groundedness and Hallucination --- we report especially on progress in this latter in recent research and applications at Visa.</em>
</details>

<details>
<summary>Evidence-based Inverse Problem Solvers for QCD: Demystifying Uncertainty in Inverse Problem Solutions of Parton Distribution Functions, Brandon Kriesten (Argonne National Laboratory)</summary>
<em>Representing parton distribution functions (PDFs) of hadrons through robust, high-fidelity parameterizations has been a long-standing goal of particle physics phenomenology. Additionally, quantitatively connecting the underlying theory assumptions and chosen fitted datasets to the properties of the PDF’s flavor and x-dependence is a long-standing challenge. We use a variational autoencoder-based inverse mapper to find solutions to the inverse problem of decoding PDFs from experimental measurements / lattice QCD data while simultaneously dissecting patterns of learned correlations between the encoded data and reconstructed PDFs. Finally using evidence-based techniques, we seek to quantify the uncertainty of these models and separate data (aleatoric) and knowledge (epistemic) uncertainty while identifying out of distribution samples. I will show progress towards implementing these evidence-based inverse problem solvers for PDFs in an implementation that mirrors a phenomenological fit.</em>
</details>

<details>
<summary>Simulation Based Inference for FCC-ee, Lingfeng Li (Brown University)</summary>
<em>We apply machine-learning techniques to the effective-field-theory analysis of the e+e−→W+W− processes at future lepton colliders, and demonstrate their advantages in comparison with conventional methods, such as optimal observables. In particular, we show that machine-learning methods are more robust to detector effects and backgrounds, and could in principle produce unbiased results with sufficient Monte Carlo simulation samples that accurately describe experiments. This is crucial for the analyses at future lepton colliders given the outstanding precision of the e+e−→W+W− measurement (∼O(10−4) in terms of anomalous triple gauge couplings or even better) that can be reached. Our framework can be generalized to other effective-field-theory analyses, such as the one of e+e−→tt¯ or similar processes at muon colliders.</em>
</details>

<details>
<summary>Embed and Emulate: Contrastive representations for simulation-based inference, Peter Lu (University of Chicago)</summary>
<em>Scientific modeling and engineering applications rely heavily on parameter estimation methods to fit physical models and calibrate numerical simulations using real-world data. In the absence of an analytic statistical model, modern simulation-based inference (SBI) approaches first use a numerical simulator to generate a dataset consisting of parameters and corresponding model outputs, such as trajectories from a dynamical system. Then, given real experimental data, the system parameters can be inferred using a variety of SBI methods, some of which use machine learning emulators to accelerate data generation and inference. However, parameter estimation for dynamical systems, such as weather and climate, is still often difficult due to the high-dimensional nature of the data as well as the complexity of the physical models and simulations. We introduce Embed and Emulate (E&E): a new likelihood-free inference method for estimating arbitrary parameter posteriors based on contrastive learning. E&E learns a low-dimensional embedding for the data (i.e. a summary statistic) and a corresponding fast emulator in the embedding space, bypassing the need for running an expensive simulation or a high-dimensional emulator during inference. We validate our theoretical results on an synthetic toy experiment, which illustrates properties of the learned embedding as a contrastive representation, and then benchmark E&E on a realistic multimodal parameter estimation task using the high-dimensional, chaotic Lorenz 96 system.</em>
</details>

<details>
<summary>Going beyond the jet tagging frontier using knowledge distillation, Yuanchen Zhou (Brown University)</summary>
<em>Classifying jets for proton-proton collisions is a challenging problem, and several Artificial Intelligence / Machine Learning classifiers have been introduced to help handle the task. Different classifiers have tradeoffs in terms of their accuracy, model dependency, processing time, etc. We study these tradeoffs for different model architectures, and explore techniques to improve their overall performance. In particular, we study the technique of Knowledge Distillation, which distills knowledge from a complex model with high accuracy to a simpler model with faster processing time and potentially less model-dependence to see if it is possible to increase the accuracy of the simpler model while maintaining its other advantages.</em>
</details>

**Contributed Talks Session B - Representation/Manifold Learning**

MIT Media Lab, Room 633

<details>
<summary>Multi-modal generalized class discovery for scalable autonomous all-sky surveys, Laura Domine (Center for Astrophysics, Harvard University)</summary>
<em>The Galileo Project is a systematic scientific research program focused on understanding the origins and nature of Unidentified Aerial Phenomena (UAP). To date there is very little data on UAP whose properties and kinematics purportedly reside outside the performance envelope of known phenomena. We are in the process of designing, building and commissioning a multi-modal, multi-spectral detector to continuously monitor the sky and collect UAP data through a rigorous aerial census of natural and human-made phenomena. This open-world setting is a major challenge for artificial intelligence (AI) techniques which need to both (i) accurately detect and classify objects from known classes and (ii) cluster unknown, out-of-distribution objects. Using a commissioning dataset, which includes several months of videos from an all-sky array of eight long wave-infrared cameras and audible recordings, I will discuss our work developing a multi-modal generalized class discovery method to automatically identify new classes of objects in unlabeled data in addition to known classes. It opens the door to an autonomous aerial census where categorization relies less on our prior expectations.</em>
</details>

<details>
<summary>SPECTER: Efficient Evaluation of the Spectral EMD, Rikab Gambhir (MIT)</summary>
<em>The Energy Mover’s Distance (EMD) has seen use in collider physics as a metric between events and as a geometric method of defining infrared and collinear safe observables. Recently, the spectral Energy Mover’s Distance (SEMD) has been proposed as a more analytically tractable alternative to the EMD. In this work, we obtain a closed-form expression for the Riemannian-like p = 2 SEMD metric between events, eliminating the need to numerically solve an optimal transport problem. Additionally, we show how the SEMD can be used to define event and jet shape observables by minimizing the metric between event and parameterized energy flows (similar to the EMD), and we obtain closed-form expressions for several of these observables. We also present the SPECTER framework, an efficient and highly parallelized implementation of the SEMD metric and SEMD-derived shape observables. We demonstrate that the SEMD and SPECTER provide nearly thousand-fold compute time improvements over evaluation of the EMD.</em>
</details>

<details>
<summary>Hybrid Physics-AI for efficient bias-aware state estimation, Stiven Briand God Massala Moussounda (NTU Singapore,  ENS Paris-Saclay)</summary>
<em>We consider the problem of optimal recovery of an element $u$ of a Hilbert space \mathcal{H} from noisy measurements $\ell_i(u)$. Specifically, $u$ is solution of a biased parametric partial differential equation \(\mathcal{P}( u, \mu) \) and measurements $\ell_i(u)$ are linear functionals on \mathcal{H}. We propose a bias-aware Hybrid-AI approach to solve the optimal recovery by combining the Parameterized Background Data-Weak(PBDW) with the deep neural operator (Deeponet) \cite{lulu}. PBDW combines the model \(\mathcal{P}\) and the measurement in a weak form and estimate the state and the model's bias as a  combination of anticipated(Knowledge) and unanticipated(Ignorance) uncertainty. The anticipated uncertainty belongs to a background space $\mathcal{Z}_N$ built from a reduced model of a best-knowledge manifold \(\mathcal{M}^{\mathrm{bk}} =\{u(\mu), \for \mu \in \mathcal{D} \}\), while the unanticipated uncertainty modeled by a Deeponet belongs to $\mathcal{Z}_{N}^{\perp}$. By integrating Deeponet in the PBDW sate estimate, Deeponet lies inside the kernel of the anticipated physics thus strictly accommodates the deficient physics by locally learning the model bias. The local information comes from an optimal sensor selection strategy. To showcase its potential for solving complex physical systems, we apply this method on a 2D Helmoltz equation defined on the physical domain $\Omega$ with various model's bias from the source, boundary conditions or both.
</em>
</details>

<details>
<summary>Parameter Symmetry and Formation of Latent Representations, Liu Ziyin (MIT, NTT Research)</summary>
<em>Symmetries exist abundantly in the loss function of neural networks. We characterize the learning dynamics of stochastic gradient descent (SGD) when exponential symmetries, a broad subclass of continuous symmetries, exist in the loss function. We establish that when gradient noises do not balance, SGD has the tendency to move the model parameters toward a point where noises from different directions are balanced. Here, a special type of fixed point in the constant directions of the loss function emerges as a candidate for solutions for SGD. As the main theoretical result, we prove that every parameter connects without loss function barrier to a unique noise-balanced fixed point. Lastly, we discuss how the theory can be leveraged to understand common phenomena in deep learning, such as progressive sharpening and flattening and the formation of latent representations.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

*Applications of Neural Networks to Mitigate Unique Challenges in Neutrino Experiments*

Jessie Micallef, IAIFI Fellow

<details>
<summary>Abstract</summary>
<em>Details to come</em>
</details>

**4:15-5:00 pm ET**

*Equivariant Convolutional Networks & Group Steerable Kernels*

Maurice Weiler, MIT

<details>
<summary>Abstract</summary>
<em>Equivariance imposes symmetry constraints on the connectivity of neural networks. This talk investigates the case of equivariant networks for feature vector fields or point clouds, which generally requires 1) spatial (convolutional) weight sharing, and 2) G-steerability constraints on the shared weights themselves. It gives an intuition for steerable convolution kernels, discusses how they can be implemented directly via harmonic bases or implicitly via equivariant MLPs, and clarifies the relation to typical message passing operations in equivariant MPNNs. A gauge theoretic formulation of equivariant CNNs and MPNNs shows that these models are not only equivariant under global transformations, but under more general local gauge transformations as well.</em>
</details>

**5:00-5:30 pm ET**

Break

**5:30-7:30 pm ET**

Workshop Dinner, MIT Schwarzman College of Computing (51 Vassar St, Cambridge), 8th Floor

### Friday, August 16, 2024

**9:30–10:15 am ET**

*Neural Networks and Conformal Field Theory*

Jim Halverson, Northeastern/IAIFI

<details>
<summary>Abstract</summary>
<em>I'll present an essential result in ML theory, explain how it motivates a new approach to field theory, and present some key findings. Next, I'll discuss new work, explaining a result of Dirac on the relationship between Lorentz invariance and conformal invariance, and how this can be applied in neural networks for constructing new conformal field theories.</em>
</details>

**10:15–11:00 am ET**

*How good is your model — Goodness-of-fit by Neyman-Pearson testing*

Gaia Grosso, IAIFI Fellow

<details>
<summary>Abstract</summary>
<em>The Neyman-Pearson strategy for hypothesis testing can be employed for goodness-of-fit if the alternative hypothesis is selected from data by exploring a rich parametrised family of models. The New Physics Learning Machine (NPLM) methodology has been developed as a concrete implementation of this idea, to target the detection of new physical effects in multidimensional and unbinned collider data. The applications of the Neyman-Pearson test as a goodness-of-fit method extend beyond new physics discovery, to problems of data quality monitoring and, crucially, generative models validation. In this talk I will discuss the main challenges behind the practical use of the Neyman-Pearson strategy in real setups, such as model selection, uncertainty quantification and scalability, and I will present recent solutions and future prospect to tackle them.</em>
</details>

**11:00-11:30 am ET**

Break

**11:30 am–12:15 pm ET**

*Generative AI and the natural sciences: Governance strategies and historical perspectives*

David Kaiser, MIT

<details>
<summary>Abstract</summary>
<em>Generative AI techniques offer many exciting opportunities for researchers across the natural sciences and beyond. Like any new technologies, however, these tools can also lead to unanticipated problems. Therefore it is imperative to identify — and work to avoid or ameliorate — potential harms. Doing so requires coordination among the research community as well as with individuals and groups who are not themselves scientists. Recent history provides several examples of how once-new technologies have been managed by wide-ranging constituencies to advance the greater good. This talk will conclude by describing guidance for protecting scientific integrity in an age of generative AI, which was recently developed by a working group of the US National Academy of Sciences.</em>
</details>

**12:15–1:30 pm ET**

Lunch

**1:30–2:15 pm ET**

*Compiling Learning onto Physical Systems*

Dirk Englund, MIT

<details>
<summary>Abstract</summary>
<em>The hardware limitations of conventional electronics in deep learning applications have spurred exploration into physical architectures fundamentally different from today’s computers. This talk covers the scalability and performance metrics—such as throughput, energy consumption, and latency—of emerging optical and opto-electronic architectures, with a focus on recently developed hardware error correction techniques, in-situ training methods and initial field trials, as well as methods leveraging quantum information science to perform learning and inference in ways not currently possible. 
</em>
</details>

**2:15–3:00 pm ET**

*ML-based modeling and control to enable new capabilities in beam customization and control at particle accelerator scientific user facilities*

Auralee Edelen, SLAC

<details>
<summary>Abstract</summary>
<em>Particle accelerators are incredibly complicated machines that are used for numerous applications in science, industry, and medicine. At scientific user facilities driven by particle accelerators, it is often the case that custom particle beams must be generated on demand. Simultaneously, increasingly tight tolerances and difficult-to-achieve beam characteristics are needed to meet the needs of future applications of accelerators and unlock new experimental capabilities. This is a highly complicated, nonlinear control problem that involves precise shaping of the beam in 6D position-momentum phase space. In this talk I will discuss how ML based modeling and control is beginning to transform how beam control is conducted at accelerator facilities that require highly flexible beam customization. This includes the development of digital twins for accelerator systems, improving accelerator system models using differentiable simulations and other hybrid ML and physics approaches, physics-informed Bayesian optimization, reinforcement learning, and ML enhanced beam diagnostics. The talk will focus on examples from LCLS, LCLS-II, FACET-II, and MeV-UED at SLAC, and the APS and AWA at Argonne National Lab, all major scientific user facilities.
</em>
</details>

**3:00–3:30 pm ET**

Closing

## Speakers
 
<div class="card-columns">
  <!--<div class="row">-->
    
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-pulkit-agrawal.jpg" alt="Pulkit Agrawal" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://people.csail.mit.edu/pulkitag/">Pulkit Agrawal</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, EECS, MIT </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-earl-bellinger.jpg" alt="Earl Bellinger" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://earlbellinger.com/">Earl Bellinger</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Department of Astronomy, Yale University </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-tianji-cai.jpg" alt="Earl Bellinger" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://profiles.stanford.edu/tianji-cai">Tianji Cai</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Research Associate, SLAC National Accelerator Laboratory </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-carolina-cuesta.jpg" alt="Carolina Cuesta-Lazaro" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://iaifi.org/current-fellows.html#carolina-cuesta">Carolina Cuesta-Lazaro</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IAIFI Fellow, IAIFI </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-nima-dehmamy.jpg" alt="Nima Dehmamy" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://nimadehmamy.com/">Nima Dehmamy</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Research Staff Member, IBM Research </em> <br>
         </div>
         </div>
       </div>
   
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-auralee-edelen.jpg" alt="Auralee Edelen" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://scholar.google.com/citations?user=dFg7SC0AAAAJ&hl=en">Auralee Edelen</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Scientist, SLAC National Accelerator Laboratory </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-dirk-englund.jpg" alt="Dirk Englund" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.eecs.mit.edu/people/dirk-r-englund/">Dirk Englund</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Professor, MIT </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-gaia-grosso.jpg" alt="Gaia Grosso" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://iaifi.org/current-fellows.html#gaia-grosso">Gaia Grosso</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IAIFI Fellow </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-jim-halverson.jpg" alt="Jim Halverson" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://www.jimhalverson.com/">Jim Halverson</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Professor, Physics, Northeastern </em> <br>
         </div>
         </div>
       </div>

        <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-yonatan-kahn.jpg" alt="Yonatan Kahn" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://yfkahn.web.illinois.edu/">Yonatan Kahn</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Theoretical Physicist, UIUC </em> <br>
         </div>
         </div>
       </div>
    
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-verena-kain.jpg" alt="Verena Kain" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://sparks.cern/index.php/kain-verena/">Verena Kain</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Scientist, CERN </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-david-kaiser.jpg" alt="David Kaiser" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://web.mit.edu/dikaiser/www/">David Kaiser</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, History of Science/Physics, MIT </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-patrick-kidger.jpg" alt="Patrick Kidger" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://kidger.site/">Patrick Kidger</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Mathematician and Machine Learning Researcher, Cradle.bio </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/photo-j-nathan-kutz.jpg" alt="J. Nathan Kutz" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://amath.washington.edu/people/j-nathan-kutz">J. Nathan Kutz</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, University of Washington </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-laurence-levasseur.jpg" alt="Laurence Levasseur" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://mila.quebec/en/person/laurence-perreault-levasseur/">Laurence Levasseur</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, University of Montreal </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-ziming-liu.jpg" alt="Ziming Liu" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://kindxiaoming.github.io/">Ziming Liu</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Grad Student, MIT </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-alessandro-lovato.jpg" alt="Alessandro Lovato" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.anl.gov/profile/alessandro-lovato">Alessandro Lovato</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Physicist, Argonne National Laboratory </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-lu-lu.jpg" alt="Lu Lu" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://lugroup.yale.edu/">Lu Lu</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Yale University </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-jessie-micallef.jpg" alt="Jessie Micallef" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://github.com/jessimic">Jessie Micallef</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IAIFI Fellow, IAIFI </em> <br>
         </div>
         </div>
       </div>
        
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-ayan-paul.jpg" alt="Ayan Paul" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://ai.northeastern.edu/our-people/ayan-paul">Ayan Paul</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Research Scientist, The Institute for Experiential AI - Northeastern University </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-mariel-pettee.jpg" alt="Mariel Pettee" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://marielpettee.com//">Mariel Pettee</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Chamberlain Postdoctoral Research Fellow, Lawrence Berkeley National Lab </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-tilman-plehn.jpg" alt="Tilman Plehn" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.thphys.uni-heidelberg.de/~plehn/">Tilman Plehn</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, ITP - Heidelberg University </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-matt-schwartz.jpg" alt="Matt Schwartz" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://scholar.harvard.edu/schwartz">Matt Schwartz</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, Harvard </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-melanie-weber.jpg" alt="Melanie Weber" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://melanie-weber.com/">Melanie Weber</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor of Applied Mathematics and of Computer Science, Harvard </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-maurice-weiler.jpg" alt="Maurice Weiler" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://maurice-weiler.gitlab.io/">Maurice Weiler</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Deep Learning Researcher, University of Amsterdam </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-christoph-weniger.jpg" alt="Christoph Weniger" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.christophweniger.com">Christoph Weniger</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Professor, University of Amsterdam </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-rose-yu.jpg" alt="Rose Yu" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://roseyu.com//">Rose Yu</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, UC San Diego department of Computer Science and Engineering. </em> <br>
         </div>
         </div>
       </div>
       
    <!--
    </div>
<br> -->
</div>

<br>

## 2024 Organizing Committee 
* Fabian Ruehle, Chair (Northeastern University)
* Demba Ba (Harvard)
* Alex Gagliano (IAIFI Fellow)
* Di Luo (IAIFI Fellow)
* Polina Abratenko (Tufts)
* Owen Dugan (MIT)
* Sneh Pandya (Northeastern)
* Yidi Qi (Northeastern)
* Manos Theodosis (Harvard)
* Sokratis Trifinopoulos (MIT)

# 2023 Summer Workshop 

<img src="images/2023-summer-workshop-logo.png" align="left" style="max-width:5990px;width:100%" hspace="10" vspace="10"> 

The 2023 IAIFI Summer Workshop brought together researchers from across Physics and AI for two days (August 14–18, 2023) of plenary talks, poster sessions, and networking to promote research at the intersection of Physics and AI. The Workshop followed the [IAIFI Summer School](/past-summer-schools.html).

* The 2023 Summer Workshop was held **August 14–18, 2023**
* **Northeastern University, Interdisciplinary Science and Engineering Complex**

Here's what attendees at the 2023 Summer Workshop had to say about the experience: 

<style>
.responsive-wrap iframe{ max-width: 100%;}
</style>
<div class="responsive-wrap">
<iframe width="560" height="315" src="https://www.youtube.com/embed/QRfdc-3o01g?si=oHLv6eRpGUnpe__2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Videos of the plenary talks from the 2023 IAIFI Summer Workshop are [now available on YouTube](https://www.youtube.com/playlist?list=PLBY0ED2StbGalYxIbUNEK6ADuEv35W6ig).
{:.success}

## Agenda

<img src="images/2023-workshop-agenda.png" align="left" style="max-width:2108px;width:100%" hspace="10" vspace="10"> 

### Monday, August 14, 2023
**8:30–9:00 am ET**

Welcome/Introduction

**9:00 am–9:45 am ET**

Intuition for the Data Types and Interactions in Euclidean Neural Networks, Tess Smidt (MIT/IAIFI)

<details>
<summary>Abstract</summary>
<em>3D Euclidean symmetry-equivariant neural networks (E(3)NNs) are emerging as an effective machine learning paradigm in molecular modeling, protein design, computer graphics, and beyond. In this talk, I'll discuss the fundamental building blocks of E(3)NNs and how these pieces are combined to create the growing zoo of E(3)NNs available today.</em>
</details>

**9:45–10:30 am ET**

Uncertainty and Interpretability in Machine Learning Models, Joshua Speagle (University of Toronto)

<details>
<summary>Abstract</summary>
<em>In science, we are often concerned with not just whether our ML model performs well, but on understanding how robust our results are, how to interpret them, and what we might be learning in the presence of observational uncertainties. I will provide an overview of various approaches to help address these challenges in both specific and general settings.</em>
</details>

**10:30–11:00 am ET**

Break

**11:00–11:45 am ET**


Stochastic Collapse: How Gradient Noise Attracts SGD Dynamics Towards Simpler Subnetworks, Daniel Kunin (Stanford University)

<details>
<summary>Abstract</summary>
<em>In this work, we reveal a strong implicit bias of stochastic gradient descent (SGD) that drives overly expressive networks to much simpler subnetworks, thereby dramatically reducing the number of independent parameters, and improving generalization. To reveal this bias, we identify invariant sets, or subsets of parameter space that remain unmodified by SGD. We focus on two classes of invariant sets that correspond to simpler subnetworks and commonly appear in modern architectures. Our analysis uncovers that SGD exhibits a property of stochastic attractivity towards these simpler invariant sets. We establish a sufficient condition for stochastic attractivity based on a competition between the loss landscape's curvature around the invariant set and the noise introduced by stochastic gradients. Remarkably, we find that an increased level of noise strengthens attractivity, leading to the emergence of attractive invariant sets associated with saddle-points or local maxima of the train loss. We observe empirically the existence of attractive invariant sets in trained deep neural networks, implying that SGD dynamics often collapses to simple subnetworks with either vanishing or redundant neurons. We further demonstrate how this simplifying process of stochastic collapse benefits generalization in a linear teacher-student framework. Finally, through this analysis, we mechanistically explain why early training with large learning rates for extended periods benefits subsequent generalization.</em>
</details>


**11:45 am–12:30 pm ET**

Some Benefits of Machine Learning with Invariances, Stefanie Jegelka (MIT)

<details>
<summary>Abstract</summary>
<em>In many applications, especially in the sciences, data and tasks have known invariances. Encoding such invariances directly into a machine learning model can improve learning outcomes, while it also poses challenges on efficient model design.
In the first part of the talk, we will focus on the invariances relevant to eigenvectors and eigenspaces being inputs to a neural network. Such inputs are important, for instance, for graph representation learning. We will discuss targeted architectures that can universally express functions with the relevant invariances - sign flips and changes of basis - and their theoretical and empirical benefits. Second, we will take a broader, theoretical perspective. Empirically, it is known that encoding invariances into the machine learning model can reduce sample complexity. For the simplified setting of kernel ridge regression or random features, we will discuss new bounds that illustrate two ways in which invariances can reduce sample complexity. Our results hold for learning on manifolds and for invariances to (almost) any group action.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–3:00 pm ET**

**Parallel Session A: Theoretical ML I (Auditorium)**

<details>
<summary>Nu Tangent Kernels, Akshunna S. Dogra (Imperial College London)</summary>
<em>The approximation and generalization capacity of deep learning models has been profitably leveraged across a staggeringly wide variety of tasks. In particular, appropriately initialized Neural Networks sampled from suitable functional spaces invariably find stages of exponential (or near-exponential) learning. We introduce $\nu$ - Tangent Kernels ($\nu$TKs), functional analytic objects partly inspired from the Neural Tangent Kernel (NTK), to build a generic theory for Neural Network optimization and generalization. Specifically, we prove that for a large category of well-posed and semi-well-posed problems, Neural Network based models are capable of exponentially learning the tasks at hand. Notably, these results are showcased for a much wider class of loss functions/architectures than the standard mean squared error/large width regime that is usually the focus of conventional NTK analysis, and apply to diverse practical problems solved using real networks such as differential equation solvers, shape recognition, classification, feature extraction, etc. We end by exemplifying the power of the $\nu$TK perspective by comparing expected vs empirically observed optimization profiles across different regimes.</em>
</details>

<details>
<summary>A Solvable Model of Neural Scaling Laws, Alexander Maloney (McGill University)</summary>
<em>Large language models with a huge number of parameters, when trained on near internet-sized number of tokens, have been empirically shown to obey neural scaling laws: specifically, their performance behaves predictably as a power law in either parameters or dataset size until bottlenecked by the other resource. To understand this better, we first identify the necessary properties allowing such scaling laws to arise and then propose a statistical model -- a joint generative data model and random feature model -- that captures this neural scaling phenomenology. By solving this model in the dual limit of large training set size and large number of parameters, we gain insight into (i) the statistical structure of datasets and tasks that lead to scaling laws, (ii) the way nonlinear feature maps, such as those provided by neural networks, enable scaling laws when trained on these datasets, (iii) the optimality of the equiparameterization scaling of training sets and parameters, and (iv) whether such scaling laws can break down and how they behave when they do. Key findings are the manner in which the power laws that occur in the statistics of natural datasets are extended by nonlinear random feature maps and then translated into power-law scalings of the test loss and how the finite extent of the data's spectral power law causes the model's performance to plateau.</em>
</details>

<details>
<summary>Grokking: a playground for feature learning, Darshil Doshi (University of Maryland)</summary>
<em>Grokking in machine learning is the phenomenon of delayed generalization; wherein the network memorizes the training data quickly, but takes a much longer training time to learn useful features and generalize. Grokking offers a unique playground to gain insight into feature learning and generalization. In my talk, I will present a minimal framework that recreates Grokking: training a 2-layer Fully-Connected Network on Modular Arithmetic data. In this setup, it is possible to write down an analytical solution that generalizes to a 100% accuracy. More excitingly, a network trained with gradient descent finds the same solution! I will discuss these special solutions and the corresponding features. Furthermore, I will describe grokking "transitions" with training time, training dataset size and model size. I will end the talk with some interesting open questions on the topic and our ongoing work.</em>
</details>

**Parallel Session B: HEP-TH x ML (Room 138)**

<details>
<summary>$λφ^4$ Scalar Neural Network Field Theory, Anindita Maiti (Harvard University)</summary>
<em>Neural Network (NN) architectures at initialization define field theories. Certain large width limits of architectures result in free field theories due to Central Limit Theorem (CLT); deviations from CLT via finite width, and correlated, dissimilar NN parameters turn on field interactions. Edgeworth method provides a way to construct NN field theory actions using connected Feynman diagrams, where internal vertices correspond to connected correlators of NN field theories. Further, specific interacting field theories can be engineered via the NN parameter framework, where non-Gaussianities due to statistical independence breaking of NN parameters tune the action deformations. As an example, I will present the construction of $λφ^4$ scalar field theory in infinite width NNs.</em>
</details>

<details>
<summary>Applying the Variational Principle to Quantum Field Theory with Neural-Networks, John Martyn (MIT)</summary>
<em>Physicists dating back to Feynman have lamented the difficulties of applying the variational principle to quantum field theories. In non-relativistic quantum field theories, the challenge is to parameterize and optimize over the infinitely many n-particle wave functions comprising the state's Fock space representation. Here we approach this problem by introducing neural-network quantum field states, a deep learning ansatz that enables application of the variational principle to non-relativistic quantum field theories in the continuum. Our ansatz uses the Deep Sets neural network architecture to simultaneously parameterize all of the n-particle wave functions comprising a quantum field state. We employ our ansatz to approximate ground states of various field theories, including an inhomogeneous system and a system with long-range interactions, thus demonstrating a powerful new tool for probing quantum field theories.</em>
</details>

<details>
<summary>Structures of Neural Network Effective Theories, Zhengkang Zhang (University of Utah)</summary>
<em>We develop a diagrammatic approach to effective field theories (EFTs) corresponding to deep neural networks at initialization, which dramatically simplifies computations of finite-width corrections to neuron statistics. The structures of EFT calculations make it transparent that a single condition governs criticality of all connected correlators of neuron preactivations. Understanding of such EFTs may facilitate progress in both deep learning and field theory simulations.</em>
</details>

<details>
<summary>Normalizing Flows for Effective String Theory, Elia Cellini (University of Turin / INFN Turin)</summary>
<em>Effective String Theory (EST) is a non-perturbative framework used to describe confinement in Yang-Mills theory through the modeling of the interquark potential in terms of vibrating strings. An efficient numerical method to simulate such theories where analytical studies are not possible is still lacking. However, in recent years a new class of deep generative models called Normalizing Flows (NFs) has been proposed to sample lattice field theories more efficiently than traditional Monte Carlo methods. In this talk, we show a proof of concept of the application of NFs to EST regularized on the lattice. Namely, we use as case study the Nambu-Goto string in order to use the well-known analytical results of this theory as a benchmark for our methods.</em>
</details>


**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

Machine Learning at the Edge of Particle Physics, Javier Duarte (UCSD)

<details>
<summary>Abstract</summary>
<em>Ten years ago, the discovery of the Higgs boson confirmed the existence of a new kind of field, the Higgs field, which fills the universe. Measuring the interactions of the Higgs boson is necessary to confirm the standard model of particle physics, and any deviations from our expectations may give a critical hint for new laws of physics. At the CERN LHC, we collide protons at nearly the speed of light and analyze the debris from the collisions to learn about elementary particles like the Higgs boson. In this presentation, I will explain how we are developing machine learning methods to confront two major, and related, challenges at the LHC: (1) searching for the elusive Higgs boson self-interaction and (2) quickly filtering millions of collisions per second on field-programmable gate arrays (FPGAs) in pursuit of new physics.</em>
</details>

**4:15–5:30 pm ET**

Poster Session

<details>
<summary>Details</summary>
<em>Details to come.</em>
</details>

**6:00–8:00 pm ET**
Welcome Dinner


### Tuesday, August 15, 2023

**9:00 am–9:45 am ET**

Deep learning theory beyond the static kernel limit, Cengiz Pehlevan (Harvard/IAIFI)

<details>
<summary>Abstract</summary>
<em>Learning dynamics of deep neural networks is complex. While previous approaches made advances in mathematical analysis of the dynamics of two-layer neural networks, addressing deeper networks have been challenging. In this talk, I will present a mean field theory of the learning dynamics of deep networks and discuss its implications.</em>
</details>

**9:45–10:30 am ET**

Effective Theory of Transformers, Sho Yaida (Meta)

<details>
<summary>Abstract</summary>
<em>Large neural networks perform extremely well in practice, providing the backbone of modern machine learning. Theoretical analyses of these large models suggest particular scaling strategies, specifically for initialization and training hyperparameters. This talk walks through these suggestions for the concrete case of Transformers and mentions some of its practical implications.</em>
</details>

**10:30–11:00 am ET**

Break

**11:00–11:45 am ET**

Variational Monte Carlo with Large Patched Transformers, Stef Czischek (University of Ottawa)

<details>
<summary>Abstract</summary>
<em>Large language models, like transformers, have recently demonstrated immense powers in text and image generation. This success is driven by the ability to capture long-range correlations between elements in a sequence. The same feature makes the transformer a powerful wavefunction ansatz that addresses the challenge of describing correlations in simulations of qubit systems. In this talk I consider two-dimensional Rydberg atom arrays to demonstrate that transformers reach higher accuracies than conventional recurrent neural networks for variational ground state searches. I further introduce large, patched transformer models, which consider a sequence of large atom patches, and show that this architecture significantly accelerates the simulations.</em>
</details>

**11:45 am–12:30 pm ET**

Learned optimizers: why they're the future, why they’re hard, and what they can do now, Jascha Sohl-Dickstein (Google Brain)

<details>
<summary>Abstract</summary>
<em>The success of deep learning has hinged on learned functions dramatically outperforming hand-designed functions for many tasks. However, we still train models using hand designed optimizers acting on hand designed loss functions. I will argue that these hand designed components are typically mismatched to the desired behavior, and that we can expect meta-learned optimizers to perform much better. I will discuss the challenges and pathologies that make meta-training learned optimizers difficult. These include: chaotic and high variance meta-loss landscapes; extreme computational costs for meta-training; lack of comprehensive meta-training datasets; challenges designing learned optimizers with the right inductive biases; challenges interpreting the method of action of learned optimizers. I will share solutions to some of these challenges. I will show experimental results where learned optimizers outperform hand-designed optimizers in many contexts, and I will discuss novel capabilities that are enabled by meta-training learned optimizers.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–3:00 pm ET**

**Parallel Session A: HEP-EX x ML (Room 136)**

<details>
<summary>Is infrared-collinear safe information all you need for jet classification?, Dimitrios Athanasakos (YITP, Stony Brook)</summary>
<em>Machine learning-based jet classifiers are able to achieve impressive tagging performance in a variety of applications in high energy and nuclear physics. However, it remains unclear in many cases which aspects of jets give rise to this discriminating power, and whether jet observables that are tractable in perturbative QCD such as those obeying infrared-collinear (IRC) safety serve as sufficient inputs. In this article, we introduce a new classifier, Jet Flow Networks (JFNs), in an effort to address the question of whether IRC unsafe information provides additional discriminating power in jet classification. JFNs are permutation-invariant neural networks (deep sets) that take as input the kinematic information of reconstructed subjets. The subjet radius serves as a tunable hyperparameter, enabling the sensitivity to soft emissions and nonperturbative effects to be gradually increased as the subjet radius is decreased. We demonstrate the performance of JFNs for quark vs. gluon and QCD vs.  � Z jet tagging. For small subjet radii, the performance of JFNs is equivalent to the IRC-unsafe Particle Flow Networks (PFNs), demonstrating that infrared-collinear unsafe information is not necessary to achieve strong discrimination for both cases. As the subjet radius is increased, the performance of the JFNs remains essentially unchanged until physical thresholds that we identify are crossed. For relatively large subjet radii, we show that the JFNs may offer an increased model independence with a modest tradeoff in performance compared to classifiers that use the full particle information of the jet. These results shed new light onto how machines learn patterns in high-energy physics data.</em>
</details>

<details>
<summary>Machine Learning the Top Mass, Katherine Fraser (Harvard University)</summary>
<em>Measurements in particle colliders are often done by fitting data to simulation, which depends on many parameters. For the top quark mass in particular, these physical and unphysical parameters generate a source of error that must be profiled when fitting. In this talk, we discuss several methods for reducing this source of error, including the machine-learning method DCTR and a dense linearly-activated neural network. We also compare to histogram fits commonly used in experiment.</em>
</details>

<details>
<summary>Data-Driven Light Model for the MicroBooNE Experiment, Polina Abratenko (Tufts University)</summary>
<em>MicroBooNE is a short baseline neutrino oscillation experiment that employs Liquid Argon Time Projection Chamber (LArTPC) technology together with an array of Photomultiplier Tubes (PMTs), which detect scintillation light. This light detection is necessary for providing a means to reject cosmic ray background and trigger on beam-related interactions. Thus, accurate modeling of the expected optical detector signal is critical. Previous light models used on MicroBooNE have been simulation-based, which limits accuracy related to certain regions of the detector as well as different data conditions during runs. We present the status of a data-driven light model that uses a neural network to map the light yield in the MicroBooNE detector, allowing for specific conditioning based on MicroBooNE data.</em>
</details>

<details>
<summary>Using Machine Learning to Consolidate Input for DUNE’s 2x2 Prototype Near Detector, Jessie Micallef (IAIFI Fellow)</summary>
<em>The Deep Underground Neutrino Experiment (DUNE) aims to measure neutrino properties by detecting neutrinos as they travel 1300 km from Fermilab to Sanford Underground Research Facility (SURF). Understanding the composition of the neutrino beam at Fermilab is vital to make precision measurements at SURF, and thus a prototype of the near detector will soon begin testing. The state-of-the-art near detector prototype has some challenges for reconstructing particles, such as gaps between submodules inside the prototype detector and inputs from differently designed endcap detectors. This talk will discuss work to use machine learning methods that could generate the missing signatures between submodules and detectors, along with leveraging information from the endcap detectors’ despite their different geometry and structure.</em>
</details>

**Parallel Session B: Astro x ML I (Room 140)**

<details>
<summary>LenSiam: Self-Supervised Learning on Strong Gravitational Lens Images, Joshua Yao-Yu Lin (Prescient Design/Genentech)</summary>
<em>Self-supervised learning has been known for learning good representations from data without annotated labels. We explore the simple siamese (SimSiam) architecture for representation learn- ing on strong gravitational lens images. Com- monly used image augmentations tend to change lens properties; for example, zoom-in would af- fect the Einstein radius. To create image pairs representing the same underlying lens model, we introduce a lens augmentation method to preserve lens properties by fixing the lens model while varying the source galaxies. Our research demon- strates this lens augmentation works well with SimSiam for learning the lens image representa- tion without labels, so we name it LenSiam. We also show that a pre-trained LenSiam model can benefit downstream tasks. We plan to open-source our code and datasets.</em>
</details>

<details>
<summary>Leveraging Machine Learning for Retrieving Exoplanet Atmosphere Parameters from Low-Resolution Spectra, Cecilia Garraffo (AstroAI - CfA Harvard & Smithsonian)</summary>
<em>The study of exoplanet atmospheres plays a vital role in understanding their composition. However, extracting accurate atmospheric parameters from transmission spectra poses significant challenges. Bayesian sampling algorithms, although effective, can be time-consuming and laborious. As an alternative, machine learning techniques offer promising avenues to expedite and enhance this process.  At the AstroAI group, Center for Astrophysics | Harvard & Smithsonian, we focus on developing AI-based solutions to address astrophysics challenges.  In this presentation I will discuss a new model to retrieve the atmospheric parameters of Earth-sized rocky exoplanets observed with the JWST NIRSpec instrument using machine learning techniques. To tackle this task, we put together an interdisciplinary team of experts in Machine Learning, Astronomy, Molecular Spectroscopy, and Exoplanetary Research. In addition, I will discuss our results in the ARIEL data challenge organized by the European Space Agency (ESA), which paves the way for analyzing data from the upcoming ARIEL space telescope.  I will show the results of two different AI techniques: semi-supervised autoencoders and normalising flows. With the first we retrieve credible atmospheric parameters while simultaneously providing a fast estimator of radiative transfer. The second allows us to generate probability distributions of the parameters for each observed spectrum, and thus gain valuable insights into the plausible compositions for each specific spectrum.   Through this interdisciplinary approach that merges astrophysics and machine learning, we aim to advance our understanding of exoplanet atmospheres. Our research showcases the capabilities of AI tools to revolutionize the analysis of exoplanetary data, preparing the ground for more efficient and accurate characterization of exoplanets in the future.</em>
</details>

<details>
<summary>Generating images of the M87* black hole using GANs, Arya Mohan (AstroAI - Univ.AI)</summary>
<em>Recently, AstroAI has been developing imaging computer vision algorithms to accomplish a series of tasks, including direct inference on the physical parameters of Black Holes, in collaboration with the Event Horizon Telescope (EHT).  In this talk I will present a novel data augmentation methodology based on Conditional Progressive Generative Adversarial Networks (CPGAN) to generate diverse black hole (BH) images, accounting for variations in spin and electron temperature prescriptions. These generated images are valuable resources for training deep learning algorithms to accurately estimate black hole parameters from observational data. Our model can generate BH images for any spin value within the range of [-1, 1], given an electron temperature distribution. To validate the effectiveness of our approach, we employ a convolutional neural network to predict the BH spin using both the GRMHD images and the images generated by our proposed model. Our results demonstrate a significant performance improvement when training is conducted with the augmented dataset while testing is performed using GRMHD simulated data, as indicated by the high $R^2$ score. In this talk, I will discuss how employing GANs as cost-effective models for black hole image generation can reliably augment training datasets for other parameterization algorithms.</em>
</details>

<details>
<summary>Applications of Autoencoders to Spectral and Timing Data for Black-Hole X-ray Binary Systems, Thaddeus Kiker(AstroAI - Columbia University)</summary>
<em>Astronomy is undergoing significant advancements in the application of machine learning techniques to analyze varied datasets. I will discuss our pioneering work utilizing machine learning techniques to predict the presence and characteristics of transient quasi-periodic oscillations (QPOs) in the time domain (manifest in the power-density spectra of X-ray binary systems) using data and features derived solely from the energy spectrum.   We have employed an abundance of data from the NICER and RXTE archives and applied our approach to low-frequency QPOs in black hole low-mass X-ray binary systems GRS 1915+105 and MAXI J1535-571.  This work establishes a non-traditional foundation for using machine learning to reveal hidden patterns between energy and time domains and offers unique insight contributing to the ongoing challenge of discerning  the nature and origin of QPOs.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

From inference to discovery with AI in the physical sciences, Ben Wandelt (Sorbonne University/Flatiron Institute)

<details>
<summary>Abstract</summary>
<em>I will discuss machine learning approaches to Bayesian Inference and model comparison that are transforming the way we study the universe and its initial conditions with computational models.</em>
</details>

**4:15–5:00 pm ET**

Architecture Selection and Initialization for Graph Neural Networks, Boris Hanin (Princeton)

<details>
<summary>Abstract</summary>
<em>Graph neural networks (GNNs) are an important class of machine learning models designed for learning from graph-structured datasets, such as those from high energy physics, chemistry, genomics/genetics, and so on. In this talk, I will discuss recent work, joint with Gage DeZoort, in which we theoretically derive and empirically validate principles for architecture selection and initialization schemes in GNNs that provably avoid a range of common failure modes early in training.</em>
</details>

### Wednesday, August 16, 2023

**9:00 am–9:45 am ET**

The Strengths and Limitations of Equivariant Neural Networks, Robin Walters (Northeastern)

<details>
<summary>Abstract</summary>
<em>Despite the success of deep learning, there remain challenges to progress including dataset size, generalization, and lack of guarantees.  Incorporating symmetry into neural networks gives equivariant neural networks (ENN) which have helped address these challenges. I will discuss several dynamics applications, such as trajectory prediction, ocean currents, and robotics. However, there are also limits to the effectiveness of ENNs. In many applications where symmetry is only approximate or does apply across the entire input distribution, equivariance may hurt model performance.  I will discuss recent work characterizing errors resulting from mismatched symmetry biases which can be used for model selection.</em>
</details>

**9:45–10:30 am ET**

Generative Diffusion Models: From Foundations to Applications in Digital Content Creation, Karsten Kreis (NVIDIA)

<details>
<summary>Abstract</summary>
<em>Denoising diffusion-based generative models, rooted in physics, have led to multiple breakthroughs in deep generative learning. In this talk, I will provide an overview over recent works by NVIDIA on diffusion models and their applications for image, video, and 3D content creation. I will start with a short introduction to diffusion models and discuss large-scale text-to-image generation. I will also highlight different efforts on 3D generative modeling as well as high-resolution video generation with video latent diffusion models. Moreover, I will discuss techniques for smoother and faster diffusion, inspired by ideas in physics, for accelerated and high-performance generation.</em>
</details>

**10:30–11:00 am ET**

Break

**11:00–11:45 am ET**

Diffusion Generative Models in Collider Physics, Vinicius Mikuni (NERSC)

<details>
<summary>Abstract</summary>
<em>Generative models are are used in collider physics for a multitude of different tasks, including fast surrogate models for detector simulation, anomaly detection of new physics processes, and full event interpretation. In particular, diffusion models are becoming popular for different physics tasks due to high fidelity generation and flexible architecture design. In this talk, I will introduce different applications of diffusion models in collider physics and how physics knowledge is incorporated to create more performant models.</em>
</details>


**11:45 am–12:30 pm ET**

Generative models for first-principles theoretical physics calculations, Phiala Shanahan(MIT/IAIFI)

<details>
<summary>Abstract</summary>
<em>In the context of lattice quantum field theory calculations in particle and nuclear physics, I will describe avenues to accelerate sampling from known probability distributions using machine learning. I will focus in particular on flow-based generative models, and describe how guarantees of exactness and the incorporation of complex symmetries into model architectures can be achieved. I will show the results of proof-of-principle studies that demonstrate that sampling from generative models can be orders of magnitude more efficient than traditional sampling approaches such as Hamiltonian/hybrid Monte Carlo in this context, and discuss the potential impacts of these approaches in nuclear and particle physics.</em>
</details>

**12:30–2:15 pm ET**

Mixer Lunch
*Lunch provided by IAIFI on site*

**2:15–3:00 pm ET**

RG-Guided Denoising Diffusion Models, Miranda Cheng (University of Amsterdam)

<details>
<summary>Abstract</summary>
<em>In machine learning, score-based generative models have seen successes in recent years. In physics, the theory of renormalization group flows has been the backbone of the basic tools in the study of a wide range of physical phenomena. I will first point out their similarities, and discuss how the analogy inspires a systematica analysis of and explicit guideline for the design choices in denoising diffusion models.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

Renormalizing Diffusion Models, Semon Rezchikov (Princeton)

<details>
<summary>Abstract</summary>
<em>We present a method for learning the renormalization group flow of lattice field theories in the context of flow-based approaches to sampling. The exact renormalization group is associated to a stochastic differential equation on the space of fields. Using this observation, one can design ML models of conventional form as those used in generative modeling for images, but for the learned flow, and in some cases the learned network parameters themselves, have a physical interpretation. We will discuss theory and numerical experiments, as well as potential applications. Based on joint work with Jordan Cotler.</em>
</details>

**4:15–5:00 pm ET**

Renormalisation and Inference, David Berman (Queen Mary University/Cambridge Consultants)

<details>
<summary>Abstract</summary>
<em>This talk will describe the link between exact renormalisation group flow and statistical inference. The basic idea being that inference incorporates data into a model while renormalisation throws information away.</em>
</details>

**6:00 pm ET**

Informal Meetup for IAIFI Summer Workshop Attendees at Owl's Nest (Night Shift) on the Esplanade

*Cost of food and drink not covered*

### Thursday, August 17, 2023

**9:00 am–9:45 am ET**

Towards a phenomenological understanding of neural networks, Sven Krippendorf (Ludwig-Maximillian University)

<details>
<summary>Abstract</summary>
<em>A comprehensive, yet simple framework to describe neural network dynamics holds the key to transform the way we design and train neural networks. In this talk I describe our vision for such a framework where neural network dynamics are described by effective field theories.
By reducing the neural network dynamics to few emergent, collective variables this approach promises a simple and interpretable framework to understand their non-linear dynamics.
I demonstrate that these dynamics are comparable to those of known EFTs in physics, in particular to those arising in cosmology. I show that these collective variables can be used for improved data selection with improved generalization behaviour. Further, I discuss that this framework naturally offers a way on how to optimize gradient descent, connecting with existing modifications such as natural gradient descent. </em>
</details>

**9:45–10:30 am ET**

Machine learning Calabi Yau metrics, Magdalena Larfors (Uppsala University)

<details>
<summary>Abstract</summary>
<em>Calabi Yau (CY) manifolds are used ubiquitously in research on string theory. Since decades, these spaces have provided the main avenue to connect string theory with observable physics. A stumbling block in these constructions is the lack of an analytical expression for the CY metrics. In this talk I will review recent work on obtaining numerical approximations of CY metrics using machine learning, and the prospects such metrics may have in furthering string theory research.</em>
</details>

**10:30–11:00 am ET**

Break

**11:00–11:45 am ET**

Learning BPS spectra, Sergei Gukov (California Institute of Technology)

<details>
<summary>Abstract</summary>
<em>Spectra of states and operators are the key data of quantum field theories in any dimension and with any amount of supersymmetry. In this talk, we will consider an infinite family of strongly coupled 3d supersymmetric theories labeled by graphs that at present time do not admit a UV Lagrangian description. Spectra of supersymmetric (BPS) states in such theories relate to equally mysterious modular properties of the corresponding generating functions. We shall see how machine learning can help us unveil some of these mysteries. Based on joint work with Rak-Kyeong Seong.</em>
</details>


**11:45 am–12:30 pm ET**

Learning from Topology: Cosmological Parameter Inference from the Large-scale Structure, Gary Shiu (University of Wisconsin-Madison)

<details>
<summary>Abstract</summary>
<em>A challenge common to different scientific areas is to effectively infer from big, complex, higher-dimensional datasets the underlying theory. Persistent homology is a tool in computational topology developed for recognizing the ``shape” of data. Such topological measures have the advantages that 1) they are stable against experimental noise, 2) they probe multiscale, non-local characteristics of a dataset, 3) they provide interpretable statistics that encode information of all higher-point correlations. In this talk, I will focus on the applications of persistent homology (with and without machine learning) to inference of cosmological parameters and primordial non-Gaussianity.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–3:00 pm ET**

**Parallel Session A: Astro x ML II (Room 136)**

<details>
<summary>Using Neural Networks to detect Dark Star Candidates in the Early Universe, Sayed Shafaat Mahmud (Colgate University)</summary>
<em>Dark Stars, hypothesized to have formed during the cosmic dawn era,  are unique stellar objects that utilize dark matter annihilation as their primary source of energy against gravitational collapse. These stars can reach immense sizes, growing to millions of times the mass of our Sun, and possess luminosities on the order of trillion times that of the Sun. Dark Stars, powered by dark matter, have limited lifespans and may ultimately evolve into supermassive black holes. As such, Supermassive Dark Stars can be the precursors to the many observed supermassive black holes at high redshift, which remains an open question, many years after their discovery.  With the advent of the James Webb Space Telescope (JWST), we are now observing photometric data of too many, too massive, galaxy candidates too early in the universe. Motivated by recent findings by Ilie, Paulin, and Freese 2023 (PNAS submitted), who identified the first three Supermassive Dark Star candidates, our study aims to identify many more such candidates in the JWST data. To accomplish this, we will use a ‘two-step’ Neural network approach that trains using ~100,000 TLUSTY simulated spectra and identifies dark star candidates based on publicly available photometric data of high redshift objects found with JWST. As a validation of our method, we independently re-identified JADES-GS-z13-0, JADES-GS-z12-0, and JADES-GS-z11-0 as Dark Star candidates, as those found via a different approach in Ilie, Paulin, and Freese 2023.    Our study presents a novel application of neural networks in the detection of Dark Star candidates. The results from our analysis demonstrate the potential of neural networks in accurately predicting the crucial parameters associated with Dark Stars. This study contributes to our understanding of early universe astrophysics and aids in the identification of elusive Dark Star objects, shedding light on the complex interplay between dark matter and stellar evolution.</em>
</details>

<details>
<summary>Mapping Dark Matter in the Milky Way using Normalizing Flows and Gaia DR3, Sung Has Lim (Rutgers University)</summary>
<em>We present a novel, data-driven analysis of Galactic dynamics, using unsupervised machine learning -- in the form of density estimation with normalizing flows -- to learn the underlying phase space distribution of 6 million nearby stars from the Gaia DR3 catalog. Solving the collisionless Boltzmann equation with the assumption of approximate equilibrium, we calculate -- for the first time ever -- a model-free, unbinned, fully 3D map of the local acceleration and mass density fields within a 3 kpc sphere around the Sun. As our approach makes no assumptions about symmetries, we can test for signs of disequilibrium in our results. We find our results are consistent with equilibrium at the 10% level, limited by the current precision of the normalizing flows. After subtracting the known contribution of stars and gas from the calculated mass density, we find clear evidence for dark matter throughout the analyzed volume. Assuming spherical symmetry and averaging mass density measurements, we find a local dark matter density of 0.47±0.05GeV/cm3. We fit our results to a generalized NFW, and find a profile broadly consistent with other recent analyses.</em>
</details>

<details>
<summary>GHDNet: A Physics-Informed Neural Network for solving hydrodynamical systems in the presence of Self-gravity, Ramit Dey (Western University, Perimeter Institute)</summary>
<em>We propose GHDNet, a PINN-based architecture to model/solve a 3D self-gravitating hydrodynamical system. In computational astrophysics, cosmology and planetary science, such systems are of fundamental importance and the non-linear interaction of fluid dynamics with gravity makes them complicated. Compared to traditional approaches such as Finite Difference (FD), we show that PINNs being mesh-free, is a promising alternative, circumventing various limitations of the FD method. We present case studies where PINNs can trace the exponential growth of density due to gravitational instability in an efficient way while providing a more flexible, adaptable and scalable framework. We observe that for the 3D hydrodynamic simulations the runtime is ~10 times less compared to FD. Interestingly, GHDNet can predict accurate solutions well beyond the training domain.  Further, the accuracy of the model, both in terms of training loss as well as the deviation from the FD solution is analysed for a wide range of model parameters and a possible scaling law for PINNs is speculated.</em>
</details>

**Parallel Session B: Theoretical ML II (Room 140)**

<details>
<summary>Noisy dynamical systems evolve error correcting codes and modularity, Trevor McCourt (MIT/IAIFI)</summary>
<em>Noise is a ubiquitous feature of the physical world. As a result, the first prerequisite of life is fault tolerance: maintaining integrity of state despite external bombardment. Recent experimental advances have revealed that biological systems achieve fault tolerance by implementing mathematically intricate error-correcting codes and by organizing in a modular fashion that physically separates functionally distinct subsystems. These elaborate structures represent a vanishing volume in the massive genetic configuration space. How is it possible that the primitive process of evolution, by which all biological systems evolved, achieved such unusual results? In this work, through experiments in Boolean networks, we show that the simultaneous presence of error correction and modularity in biological systems is no coincidence. Rather, it is a typical co-occurrence in noisy dynamic systems undergoing evolution. From this, we deduce the principle of error correction enhanced evolvability: systems possessing error-correcting codes are more effectively improved by evolution than those without.</em>
</details>

<details>
<summary>Multi-modal Contrastive Learning for Robust Text Representation Classification, Mitra Tajrobehkar (vertical oceans pte ltd)</summary>
<em>Contrastive representation learning has emerged as a powerful technique in both Computer Vision (CV) and Natural Language Processing (NLP) domains, enabling the acquisition of practical and meaningful representations from text data. This talk will explore the captivating realm of contrastive representation learning in NLP, investigating its underlying principles and applications in tasks such as question answering. We will delve into the remarkable success of contrastive learning in enhancing language understanding, transfer learning, and domain adaptation in NLP tasks. Additionally, we will address the challenges associated with training language models, including limitations arising from data scarcity and bias. Join us to discover the potential of contrastive representation learning in advancing the capabilities of pre-trained language models.</em>
</details>

<details>
<summary>High-Dimensional Asymptotics of Feature Learning in the Early Phase of Neural Network Training, Zhichao Wang (UC San Diego)</summary>
<em>In this talk, I will present a recent application of random matrix theory in deep learning theory. We aim to show the benefit of feature learning due to gradient descent training of the first-layer parameters in a two-layer neural network where all the weight matrices are randomly initialized, and the training objective is the empirical MSE loss. We consider the ``early phase'' of learning in the proportional asymptotic limit, where all the dimensions go to infinity proportionally, and the number of gradient steps remains finite. In an idealized student-teacher setting, we show that gradient updates in the early phase result in a spiked random matrix model, which leads to an alignment between the first-layer weights and the teacher model. To quantify the impact of this alignment, we compute the asymptotic prediction risk of ridge regression on the trained features, which is determined by the Stieltjes transform of the limiting spectrum of the certain kernel random matrix. For a small learning rate, we establish a Gaussian equivalence property for the trained feature map and prove that the trained feature improves upon the initial random features model, but cannot defeat the best linear model on the input after finitely many gradient steps. Whereas for a sufficiently large learning rate, I will show that even after one gradient step, the same ridge estimator on trained features can go beyond this ``linear regime''. The talk is based on joint work with Jimmy Ba, Murat A. Erdogdu, Taiji Suzuki, Denny Wu,  and Greg Yang (arXiv:2205.01445).</em>
</details>

<details>
<summary>Adaptive active Brownian particles searching for targets of unknown positions, Harpreet Kaur (University of Innsbruck)</summary>
<em>Developing behavioral policies designed to efficiently solve target-search problems is a crucial issue both in nature and in the nanotechnology of the 21st century. Here, we characterize the target-search strategies of simple microswimmers in a homogeneous environment containing sparse targets of unknown positions. The microswimmers are capable of controlling their dynamics by switching between Brownian motion and an active Brownian particle and by selecting the time duration of each of the two phases. The specific conduct of a single microswimmer depends on an internal decision-making process determined by a simple neural network associated with the agent itself. Starting from a population of individuals with random behavior, we exploit the genetic algorithm NeuroEvolution of Augmenting Topologies to show how an evolutionary pressure based on the target-search performances of single individuals helps to find the optimal duration of the two different phases. Our findings reveal that the optimal policy strongly depends on the magnitude of the particle’s self-propulsion during the active phase and that a broad spectrum of network topology solutions exists, differing in the number of connections and hidden nodes.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

Machine Learning for Fundamental Physics: From the Smallest to the Largest Scales, David Shih (Rutgers University)

<details>
<summary>Abstract</summary>
<em>What new particles and interactions exist beyond the Standard Model? What is the nature of dark matter? What is the origin of the universe? Essential questions of fundamental physics such as these are being confronted with an unprecedented amount of high quality data from the LHC and astronomical surveys. Powerful and cross-cutting machine learning techniques such as generative modeling, density estimation and anomaly detection are increasingly being applied to these datasets, vastly enhancing their discovery potential. In my talk, I will showcase some highlights from this ongoing machine learning revolution that span the range from the smallest scales (LHC data) to the largest scales (astronomical data). I will describe how new techniques developed for model-independent new physics searches and fast simulation at the LHC can also be applied to data from the Gaia space telescope to map out the Milky Way dark matter density, discover new stellar streams, and upsample galaxy simulations.</em>
</details>

**4:15–5:00 pm ET**

Improving Energy Conserving Descent Optimization: Theory to Practice, Eva Silverstein (Stanford)

<details>
<summary>Abstract</summary>
<em>Standard gradient-based optimization and sampling methods employ frictional and/or thermal dynamics on the loss landscape. We develop a novel framework based on energy-conserving chaotic Hamiltonian dynamics.  Using the formulas derived from energy conservation for phase space measure and speed, we engineer separable Hamiltonians whose measure on the target (parameter) space reproduces the desired sampling or optimization objective.    This predicts nontrivial functional relations among hyper-parameters, greatly reducing their tuning.  Empirically, the sampler MCHMC/MCLMC outperforms HMC on various benchmarks (and recent CMB analyses by others).  ECD optimization matches or improves upon the better of Adam(W) and SGD on varied benchmarks, with new theoretical calculations driving stronger systematic improvements.</em>
</details>


### Friday, August 18, 2023

**9:00 am–9:45 am ET**

AstroAI: A New Initiative for Artificial Intelligence in Astrophysics, Rafael Martinez-Galarza (Harvard & Smithsonian Center for Astrophysics)

<details>
<summary>Abstract</summary>
<em>AstroAI is a new initiative dedicated to the design and development of machine learning (ML) and artificial intelligence (AI) algorithms that advance the field of Astrophysics. AstroAI was launched at the Center for Astrophysics | Harvard & Smithsonian (CfA) in November 2022,  after an imperative need was recognized both within and outside of the CfA for reliable and interpretable models in scientific research, especially in Astrophysics. AstroAI is committed to designing AI-based models targeted to drive new scientific discovery in Astrophysics, using a model that prioritizes a multi-disciplinary approach and a diverse group of researchers. In this talk I will discuss AstroAI's journey and remarkable growth since its inception, along with a selection of the projects our team has undertaken. Further exploration of our projects and their transformative potential in astrophysical research will be showcased across various posters.</em>
</details>

**9:45–10:30 am ET**

Facets of Responsible Machine Learning, Flavio du Pin Calmon (Harvard)

<details>
<summary>Abstract</summary>
<em>This talk overviews recent results in two aspects of fair machine learning. First, we introduce a post-processing technique, "FairProjection," designed to ensure group fairness in prediction and classification. This method applies to any classifier without requiring retraining and attains state-of-the-art performance in both accuracy and group fairness assurance in probabilistic classification. We also present converse results based on Blackwell's "comparison of experiments" theorem that capture the limits of group-fairness assurance in classification. Second, we overview the concept of predictive multiplicity in machine learning. Predictive multiplicity arises when different classifiers achieve similar average performance for a specific learning task, yet produce conflicting predictions for individual samples.</em>
</details>

**10:30–11:00 am ET**

Break

**11:00–11:45 am ET**

AI-assisted sensing & control at gravitational wave observatories, Nikhil Mukund (MIT/IAIFI)

<details>
<summary>Abstract</summary>
<em>Gravitational waves (GWs) from astrophysical events merging black holes and neutron stars cause tiny perturbations in our spacetime fabric and can be detected using sensitive detectors like Advanced LIGO. Our ability to detect these elusive signals, especially the fainter ones from the earlier universe, depends on optimal sensing and control of GW interferometers. These observatories strive to find the proper equilibrium between maintaining a stable operating point for optimal sensitivity and continuously innovating to expand their astrophysical reach. The cross-coupled nature of the sub-systems involved in such optomechanical experiments, combined with the non-stationary nature of the ambient environment, often makes the task daunting. In this talk, I will discuss the potential of using deep neural systems for improved sensing and control at these observatories. I will highlight our recent successes in deploying deep reinforcement learning-based decision-making systems and discuss embedded machine learning for high bandwidth MIMO control. I will mention the challenges we encounter in deploying neural systems for temporarily varying complex systems and why tackling these issues would be crucial for next-generation GW detectors like Cosmic Explorer and Einstein Telescope.
</em>
</details>


**11:45 am–12:30 pm ET**

Many body physics meets artificial intelligence, Di Luo (IAIFI Fellow)

<details>
<summary>Abstract</summary>
<em>In this talk, we will discuss the interaction between many-body physics and artificial intelligence. The advancement of artificial intelligence provides powerful tools for simulating many-body physics systems, ranging from high energy physics, condensed matter physics to quantum chemistry. Meanwhile, the many-body physics principles also inspire the development of AI and robotics, including generative models and robot planning.</em>
</details>

**12:30–2:00 pm ET**

Lunch

**2:00–2:45 pm ET**

Symbolic Distillation of Neural Networks for New Physics Discovery, Miles Cranmer (University of Cambridge)

<details>
<summary>Abstract</summary>
<em>Would Kepler have discovered his laws if machine learning had been around in 1609? Or would he have been satisfied with the accuracy of some black box regression model, leaving Newton without the inspiration to find the law of gravitation? In this talk we will consider the incompatibility between physical interpretation and black box machine learning. I will present a technique termed "symbolic distillation" that promises to bridge the divide, using symbolic regression as a tool for "translating" concepts to a mathematical language. I will also review various applications of this technique, from cosmology, to turbulence, to even economics.</em>
</details>

**2:45–3:30 pm ET**

From Pixels to Neutrinos, Taritree Wongjirad (Tufts/IAIFI)

<details>
<summary>Abstract</summary>
<em>Abstract to come</em>
</details>

**3:30–4:00 pm ET**

Closing

## Speakers

e following speakers have accepted invitations to give plenary talks at this year's workshop. We will continue to add to the list as speakers accept. 

<div class="card-columns">
  <!--<div class="row">-->

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-david-berman.jpg" alt="David Berman" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.qmul.ac.uk/spcs/staff/academics/profiles/dsberman.html">David Berman</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, Queen Mary University; Head of AI, Cambridge Consultants </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-miranda-cheng.jpg" alt="Miranda Cheng" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.uva.nl/en/profile/c/h/c.n.cheng/c.n.cheng.html">Miranda Cheng</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Professor, University of Amsterdam; Research Scientist, Academia Sinica, Taiwan </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-miles-cranmer.jpg" alt="Miles Cranmer" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://astroautomata.com">Miles Cranmer</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor of Data Intensive Science, University of Cambridge </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-stefanie-czischek.jpg" alt="Stefanie Czischek" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.uottawa.ca/faculty-science/professors/stefanie-czischek">Stefanie Czischek</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, University of Ottawa </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-flavio-du-pin-calmon.jpg" alt="Flavio du Pin Calmon" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://people.seas.harvard.edu/~flavio/">Flavio du Pin Calmon</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Harvard </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-javier-duarte.jpg" alt="Javier Duarte" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www-physics.ucsd.edu/Directory/Person/552">Javier Duarte</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, University of California, San Diego </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sergei-gukov.jpg" alt="Sergei Gukov" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://theory.caltech.edu/~gukov/">Sergei Gukov</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, California Institute of Technology </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-boris-hanin.jpg" alt="Boris Hanin" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://boris-hanin.github.io">Boris Hanin</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Princeton </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-stefanie-jegelka.jpg" alt="Stefanie Jegelka" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://people.csail.mit.edu/stefje/">Stefanie Jegelka</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Professor, MIT </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-karsten-kreis.jpg" alt="Karsten Kreis" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://karstenkreis.github.io">Karsten Kreis</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Senior Research Scientist, NVIDIA </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sven-krippendorf.jpg" alt="Sven Krippendorf" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://krippendorflab.github.io">Sven Krippendorf</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Senior Researcher, Ludwig-Maximilian University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/photo-daniel-kunin.png" alt="Daniel Kunin" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://daniel-kunin.com">Daniel Kunin</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> PhD Student, Stanford University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-magdalena-larfors.jpg" alt="Magdalena Larfors" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.katalog.uu.se/profile/?id=N3-1163">Magdalena Larfors</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Senior Lecturer/Associate Professor, Uppsala University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-di-luo.jpg" alt="Di Luo" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://scholar.google.com/citations?user=OxZytTQAAAAJ">Di Luo</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IAIFI Fellow </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/photo-rafael-martinez.jpg" alt="Rafael Martinez-Galarza" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://lweb.cfa.harvard.edu/~jmartine/Welcome.html">Rafael Martinez-Galarza</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Astrophysicist, Harvard & Smithsonian Center for Astrophysics </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-vinicius-mikuni.jpg" alt="Vinicius Mikuni" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.nersc.gov/about/nersc-staff/nesap-postdocs/vinicius-mikuni/">Vinicius Mikuni</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Postdoctoral Fellow, NERSC </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-nikhil-mukund.jpg" alt="Nikhil Mukund" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://space.mit.edu/people/mukund-nikhil/">Nikhil Mukund</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Postdoctoral Scholar, MIT Kavli Institute </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-cengiz-pehlevan.jpg" alt="Cengiz Pehlevan" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://pehlevan.seas.harvard.edu/">Cengiz Pehlevan</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Harvard </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-semon-rezchikov.jpg" alt="Semon Rezchikov" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.rezchikov.me">Semon Rezchikov</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Research Instructor and NSF Postdoctoral Fellow, Princeton University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-phiala-shanahan.jpg" alt="Phiala Shanahan" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://physics.mit.edu/faculty/phiala-shanahan/">Phiala Shanahan</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Associate Professor, MIT </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-david-shih.jpg" alt="David Shih" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://physics.rutgers.edu/people/faculty-list/faculty-profile/shih-david">David Shih</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, Rutgers University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-gary-shiu.jpg" alt="Gary Shiu" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.physics.wisc.edu/directory/shiu-gary/">Gary Shiu</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, University of Wisconsin-Madison </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-eva-silverstein.jpg" alt="Eva Silverstein" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://sitp.stanford.edu/people/eva-silverstein">Eva Silverstein</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, Stanford University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-tess-smidt.jpg" alt="Tess Smidt" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.eecs.mit.edu/people/tess-smidt/">Tess Smidt</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, MIT </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-jascha-sohl-dickstein.jpg" alt="Jascha Sohl-Dickstein" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="http://www.sohldickstein.com">Jascha Sohl-Dickstein</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Senior Staff Research Scientist, Google Brain </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-joshua-speagle.jpg" alt="Joshua Speagle" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://joshspeagle.com/">Joshua Speagle</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 3rem; line-height: 140%">
         <em> Assistant Professor of Astrostatistics, University of Toronto </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-robin-walters.jpg" alt="Robin Walters" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.khoury.northeastern.edu/people/robin-walters/">Robin Walters</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Khoury College of Computer Sciences, Northeastern University </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-ben-wandelt-workshop.jpg" alt="Ben Wandelt" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://benwandelt.org">Ben Wandelt</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Professor, Sorbonne University and Senior Research Scientist, Flatiron Institute </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-taritree-wongjirad.jpg" alt="Taritree Wongjirad" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://as.tufts.edu/physics/people/faculty/taritree-wongjirad">Taritree Wongjirad</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Assistant Professor, Tufts </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sho-yaida.jpg" alt="Sho Yaida" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.shoyaida.com">Sho Yaida</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Research Scientist, Meta </em> <br>
         </div>
         </div>
       </div>
  <!--
  </div>
<br> -->
</div>

<br>

## 2023 Organizing Committee 
* Jim Halverson, Chair (Northeastern University)
* Shuchin Aeron (Tufts)
* Denis Boyda (IAIFI Fellow)
* Anna Golubeva (IAIFI Fellow)
* Ouail Kitouni (MIT)
* Nayantara Mudur (Harvard)
* Marisa LaFleur (IAIFI Project Manger)

# 2022 Summer Workshop

<img src="images/phd-summer-school-logo-7.png" align="right" style="max-width:5990px;width:50%" hspace="50" vspace="10"> 


The 2022 IAIFI Summer Workshop brought together researchers from across Physics and AI for two days (August 8–9, 2022) of plenary talks, poster sessions, and networking to promote research at the intersection of Physics and AI. The Workshop followed the [IAIFI Summer School](/past-summer-schools.html).

The first annual Summer Workshop was held hybrid with ~110 in-person attendees from 10 different countries. The Workshop included 82% of the Summer School students who stayed to partake in the Workshop activities. 

<img src="images/workshop-2022-collage.png" align="center" style="max-width:3752px;width:75%" hspace="20" vspace="20">

### Workshop Agenda

[Download PDF of agenda](images/2022-workshop-agenda.pdf)

### Plenary Speakers 2022
**IAIFI Investigators/Affiliates in bold**

* [Siamak Ravanbakhsh](https://www.siamak.page), Assistant Professor, School of Computer Science, McGill University
* [Greg Yang](https://www.microsoft.com/en-us/research/people/gregyang/), Senior Researcher, Microsoft Research
* **[Phil Harris](https://physics.mit.edu/faculty/philip-harris/)**, Assistant Professor of Physics, MIT
* [Kazuhiro Terao](https://www.codingkazu.com), Staff Scientist, Stanford University
* [Claudius Krause](https://claudius-krause.gitlab.io), Postdoctoral Associate, Rutgers University
* **[Fabian Ruehle](https://cos.northeastern.edu/people/fabian-ruehle/)**, Assistant Professor, Northeastern University
* [Yi-Zhuang You](https://physics.ucsd.edu/Directory/Person/536), Assistant Professor, University of California, San Diego
* [Jennifer Ngadiuba](https://inspirehep.net/authors/1244433), Wilson Fellow, Fermilab
* **[Shuchin Aeron](http://www.ece.tufts.edu/~shuchin/)**, Associate Professor, Tufts University
* **[Cora Dvorkin](https://dvorkin.physics.harvard.edu)**, Associate Professor, Harvard University
* [Sébastien Racanière](https://scholar.google.com/citations?user=o-h0vrQAAAAJ&hl=en), Staff Research Engineer, DeepMind
* **[Anna Golubeva](https://annagolubeva.github.io)**, IAIFI Fellow

### 2022 Organizing Committee
* Jim Halverson, Chair (Northeastern University)
* Tess Smidt (MIT)
* Taritree Wongjirad (Tufts)
* Anna Golubeva (IAIFI Fellow)
* Dylan Rankin (MIT)
* Jeffrey Lazar (Harvard)
* Peter Lu (MIT)
