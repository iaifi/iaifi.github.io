---
layout: article
title: 
---

<img src="images/summer-workshop-logo_2026.png" align="left" style="max-width:5990px;width:100%" hspace="10" vspace="10"> 


The IAIFI Summer Workshop brings together researchers from across Physics and AI for plenary talks, poster sessions, and networking to promote research at the intersection of Physics and AI. We will also accept submissions for contributed talks and/or posters.

**Registration is open for the 2026 IAIFI Summer Workshop.** [Register here](https://buy.stripe.com/bJebJ15xqfTu4H87ax7Vm0r) by July 31, 2026. 
{:.success}


* **The 2026 Summer Workshop will be held August 10–14, 2026**
* **Location: MIT, Cambridge, MA**

[Register](https://buy.stripe.com/bJebJ15xqfTu4H87ax7Vm0r){:.button.button--outline-primary.button--pill.button--lg} [Agenda](#agenda){:.button.button--outline-primary.button--pill.button--lg}  [Speakers](#plenary-speakers){:.button.button--outline-primary.button--pill.button--lg}   [Accommodations](#accommodations){:.button.button--outline-primary.button--pill.button--lg}[FAQ](#faq){:.button.button--outline-primary.button--pill.button--lg}  [Past Workshops](/past-workshops.html){:.button.button--outline-primary.button--pill.button--lg}

## About
The Institute for Artificial Intelligence and Fundamental Interactions (IAIFI) is enabling physics discoveries and advancing foundational AI through the development of novel AI approaches that incorporate first principles, best practices, and domain knowledge from fundamental physics. The goal of the Workshop is to serve as a meeting place to facilitate advances and connections across this growing interdisciplinary field.



## Agenda

*The schedule is subject to change. More details to be provided in the coming days.*

Regarding **IAIFI Industry Day Day on Friday, August 14**: This will be an excellent networking opportunity between Workshop attendees, IAIFI members, and industry partners. [See more about Industry Day here](https://iaifi.org/industry-day), including participating industry partners.

<img src="images/20260722_SummerWorkshop.png" align="left" style="max-width:2108px;width:100%" hspace="10" vspace="10">


### Monday, August 10, 2026
**9:00-9:15 am ET**

Welcome

**9:15–10:00 am ET**

*Statistical Mechanics approaches for Reinforcement learning and Generative Flow networks*

Rahul Kulkarni, University of Massachusetts Boston

<details>
<summary>Abstract</summary>
<em>Details to come.</em>
</details>

**10:00–10:45 am ET**

*Physics-Informed Machine Learning: from colliders to galaxies*

Sung Hak Lim, IBS CTPU-PTC

<details>
<summary>Abstract</summary>
<em>Details to come.</em>
</details>

**10:45-11:15 am ET**

Break

**11:15 am–12:00 pm ET**

*Dynamic Simulation-Based Inference: Extracting Insights from Complex Data and Simulations*

Christoph Weniger, University of Amsterdam

<details>
<summary>Abstract</summary>
<em>Much of our physical knowledge lives inside simulators: forward models that encode both established physics and the parameters we wish to infer, but whose likelihoods are often intractable — from gravitational waveforms to cosmological surveys. Simulation-based inference (SBI) turns these simulators into inference engines, training neural networks to estimate posteriors directly from simulated data. After introducing the foundations of modern SBI and amortization, we discuss dynamic SBI: an active learning scheme that continuously focuses costly simulations on the parameter regions that matter. We then present the FALCON framework for distributed dynamic SBI, which enables the simultaneous inference of a multitude of parameters in complex forward models. We demonstrate the approach on benchmark problems, ongoing LISA parameter estimation for massive black hole binaries, and discuss extensions towards field-level cosmological inference.</em>
</details>

**12:00–1:30 pm ET**

Lunch Break

**1:30–2:15 pm ET**

*Hierarchical Reinforcement Learning for Sparse-Reward Search in Commutative Algebra*

Giorgi Butbaia, Caltech

<details>
<summary>Abstract</summary>
<em>Applying machine learning techniques to solving long-standing mathematical conjectures can be particularly challenging due to their extreme reward sparsity. As an illustrative example, we consider Kalai's algebraic Hirsch conjecture and recast the construction of its counterexamples as a sparse-reward reinforcement learning problem on graphs. In this talk, we propose a constrained options-based HRL framework with an equivariant graph neural network policy, which allows us to learn useful temporal abstractions for this task. We evaluate our approach over a wide range of degrees and demonstrate that it consistently outperforms classical RL algorithms as well as greedy search. By exploiting the hierarchical structure of the problem, we effectively provide a first-of-its-kind application of HRL to a problem in commutative algebra.</em>
</details>

**2:15–3:00 pm ET**

*Generative Pretrained Neural Operators as Foundation Models for PDEs*

Zongyi Li, MIT

<details>
<summary>Abstract</summary>
<em>We present a generative neural operator for various partial differential equations. A single flow-matching transformer is trained jointly on 24 two-dimensional spatiotemporal systems spanning simulations, laboratory measurements, and global weather reanalysis. A canonical field representation with type-specific patchification maps different variables and resolutions into a shared token space, enabling one model and one compiled program across all systems. Through variable-length conditioning and masked generation, the same model supports forecasting, long rollouts, inverse prediction, missing-channel completion, super-resolution, and probabilistic ensembles without task-specific architectures. Joint training performs competitively with specialist models, improves transfer in data-limited settings, and continues to benefit from scaling up to 3.3 billion parameters. These results position generative modeling as a scalable and task-general foundation for learning PDE dynamics.</em>
</details>

**3:00–3:30 pm ET**

Break

**3:30–4:15 pm ET**

*Imaging at the Edge of Science: Integrating Scientific Knowledge and AI to Recover Hidden Structure*

Berthy Feng, MIT

<details>
<summary>Abstract</summary>
<em>Images play a central role in scientific discovery. Whether it’s astronomical, biological, or materials systems, bringing complex phenomena into view enables scientists to probe, model, and fundamentally understand them. However, many of the most important scientific questions lie at the edge of what can be directly observed.

<br><br>We can accomplish extreme imaging through computational methods, bringing the invisible into view by supplementing limited observable data with human-imposed assumptions, or priors. When imaging for science, the challenge is imposing just enough known assumptions to infer the unknown.

<br><br>I create principled methods for bringing advanced priors, such as scientific knowledge and AI, into computational imaging. Using astrophysics as a running example, this talk presents my vision for a framework in which scientists systematically explore different priors, understand their effects on imaging, and extract scientific insights.

<br><br>The talk is organized in three parts.
<br>1. First, we understand the importance of priors in extreme scientific imaging. I present my work on leveraging generative AI to flexibly tune a knob between different priors and understand their effects on imaging. Applied to black-hole imaging, my approach lets us infer physical features of a real black hole by identifying image features that are robust to prior assumptions.
<br>2. Second, we carefully balance scientific assumptions to solve an extreme imaging problem in astrophysics. I present Physics-informed Dynamic Emission Fields (PI-DEF), a method for imaging the dynamic 3D gas near a black hole. PI-DEF strikes a balance between known/unknown physics, imposing known physics as hard constraints on the solution while leaving room for learning unknown physics, such as the velocity field near the black hole.
<br>3. Third, we open an efficient route for bringing in known physics across imaging problems. I present Neural Approximate Mirror Maps (NAMMs), which learn to automatically impose any desired physics constraint onto any image. With NAMMs, we can easily incorporate known constraints (e.g., conservation laws) into generated and reconstructed images.

<br><br>The ideas of my talk naturally extend to many scientific domains, including biology, chemistry, and materials science.</em>
</details>

**4:15-5:00 pm ET**

*Simple yet predictive theories for how generative AI learns and imagines*

Surya Ganguli, Stanford

<details>
<summary>Abstract</summary>
<em>Details to come.</em>
</details>

**5:30–8:00 pm ET**

Poster Session and Reception

*Poster details to come.*

### Tuesday, August 11, 2026

**9:00–9:45 am ET**

*Accelerated forward modeling for cosmological simulations*

Shivam Pandey, University of Arizona

<details>
<summary>Abstract</summary>
<em>Developing fast and efficient methods for simulating our observable Universe is a key challenge in maximizing information extraction from cosmological datasets. The current simulations are too slow to scale to the volume necessary to analyze even decade-old observations. I will discuss different machine-learning-based approaches (e.g., using a multi-modal, transformer-based architecture) to learn the mapping from approximate and cheap dark matter-only simulations to galaxies in high-resolution and expensive simulations, achieving an orders-of-magnitude acceleration and the ability to cheaply scale to a large volume. I will discuss how these approaches enable the first analysis of large-volume observations of approximately a million galaxies using simulation-based inference techniques to place precise constraints on cosmological models. Finally, I will discuss the potential of these approaches in the context of ongoing and next-generation large-scale cosmological surveys.</em>
</details>

**9:45–10:30 am ET**

*The Era of Scientific Foundation Models*

Miles Cranmer, University of Cambridge

<details>
<summary>Abstract</summary>
<em>Why can't machine learning models generalize? Physical theories certainly can! General relativity predicted black holes and gravitational waves decades before any observational evidence. How can physics extrapolate so far beyond its data?

<br><br>I think the answer is induction. The physicist assumes a new model ought to accommodate old models. Yet the machine learner does not do this; instead, they ask their models to exist in isolation, and to bootstrap all knowledge from scratch. However, the past five years have seen this machine learning practice shift with the notion of generalist "foundation models" coming into vogue: models pretrained on massive diverse datasets which learn general representations (such as large language models).

<br><br>In this talk I will present new evidence that this strategy is starting to pay off for physics. Walrus, our 1.3B-parameter physics foundation model pretrained on 19 different PDEs in 2D and 3D, after finetuning on just three idealized simulations of the Rayleigh-Taylor instability, predicts real laboratory experiments zero-shot: it leaves the simulation regime and lands on the experimentally-measured mixing rate, without ever seeing a single experimental sample. This gives new data-driven evidence on a century-old discrepancy between simulation and experiment. I will use this result to introduce PolymathicAI, our research collaboration building large-scale multi-disciplinary scientific foundation models, and share some tricks we have found useful for building and adapting these models, such as tokeniser pretraining and probabilistic retrofitting. Finally, I will discuss what these models are actually learning, and how symbolic distillation via PySR and SymTorch can convert pieces of a neural network into interpretable, closed-form equations.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*These aren't the anomalies you're looking for*

Daniel Whiteson, UC Irvine

<details>
<summary>Abstract</summary>
<em>AI has sharpened our analysis and optimizes our pipelines. But it's also capable of creating entirely new pathways to discovery. I'll present examples of how AI allows us to search for objects which were once completely inaccessible, such as non-helical tracks, and describe how we can use it to search unexplored dimensions in our data, such as time-varying phenomena.</em>
</details>

**11:45 am–12:30 pm ET**

*ML-Enhanced LHC Simulations*

Tilman Plehn, Heidelberg University

<details>
<summary>Abstract</summary>
<em>Simulations are crucial for the precision-LHC program, and modern machine learning is transforming them rapidly. I will show how surrogates and generative models enhance LHC simulations and allow us to simulate LHC events with unprecedented speed and precision. To this end, we drive the development of uncertainty-aware precision networks for applications like ML-MadGraph, MLhad, and enhanced higher-order predictions.</em>
</details>

**12:30–2:00 pm ET**

Lunch Break

**2:00–3:30 pm ET**

*Parallel Session for Contributed Talks; details to come.*

**3:30–4:00 pm ET**

Break

**4:00–4:45 pm ET**

*Rethinking Discovery: Foundation Models for Particle Physics*

Gregor Kasieczka, University of Hamburg

<details>
<summary>Abstract</summary>
<em>Rethinking Discovery: Foundation Models for Particle Physics

Three distinctive strands of development are set to revolutionize the way data intensive sciences such as particle physics are carried out: i) anomaly detection and end-to-end tuning greatly increases the scope and sensitivity of individual searches; ii) foundation models unify the training of state-of-the-art models; and iii) agentic systems carry out increasingly complex data analysis chains. We will discuss the status, progress, and current limitations of these technologies in the context of discovering new physics at the LHC and future collider experiments.</em>
</details>

**4:45-5:30 pm ET**

*Machine Learning for Gravitational-Wave Searches*

Erik Katsavounidis, MIT

<details>
<summary>Abstract</summary>
<em>The continuing growth of the gravitational-wave detector network with their increased sensitivity and the resulting increased volume and complexity of their data present a significant computational challenge for the present and future running of the instruments. At the same time, real-time identification and characterization of sources is inextricably linked to discovery not only for gravitational-wave sources but for the wealth of multi-messenger prospects they may bring. We will review the role machine learning is posed to play in addressing these challenges for both real-time gravitational-wave searches but also in analyses of archival data. This includes end-to-end analysis pipelines and their deployment “in production”, ranging from noise regression, detector characterization, transient source detection and gravitational-wave source characterization.</em>
</details>

### Wednesday, August 12, 2026

*Today will have a later start, at 9:45am.*

**9:45–10:30 am ET**

*Title to come.*

Vicky Kalogera, Northwestern University

<details>
<summary>Abstract</summary>
<em>Details to come.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*AI for Scattering Amplitudes*

Lance Dixon, SLAC

<details>
<summary>Abstract</summary>
<em>Scattering amplitudes at high loop orders are remarkably difficult for humans to compute.  Can machines do any better?  Many scattering amplitudes can be mapped into a language-like representation using the symbol associated with multiple polylogarithms. For some special cases we know the symbol to eight loops, where it contains over a billion words (sequences of letters), each with an integer coefficient.  We trained a custom transformer-based model to predict the coefficients at lower loop orders, using many of the terms in the symbol.  Such models can also learn correlations between coefficients at different loop orders.  However, it is difficult to learn the next loop order from scratch in this way.  So we have used large-language models, as well as genetic algorithm models, in order to learn (more) patterns in the symbol that should hold to all loop orders.</em>
</details>

**11:45 am–12:30 pm ET**

*Graph reinforcement learning for exploring model spaces beyond the Standard Model*

Lisa Everett, University of Wisconsin-Madison

<details>
<summary>Abstract</summary>
<em>We describe a methodology for exploring beyond Standard Model (BSM) parameter spaces with reinforcement learning. This method allows for the exploration of new physics model spaces without the user specifying a fixed particle content, which can be applied to nearly any model space with a pre-specified gauge group. The procedure is based on the construction of a suitable graph grammar that represents a given BSM framework. The graph grammar is then used to create a reinforcement learning environment tasked with creating models that are consistent with given experimental constraints. As a proof of concept of this methodology, we carry out this procedure for a class of new physics theories with vector-like leptons that may or may not be charged under a dark U (1) group, inspired by portal matter extensions of the sub-GeV vector portal/kinetic mixing simplified dark matter model framework.</em>
</details>

**12:30–2:00 pm ET**

Lunch Break

**2:00–3:30 pm ET**

*Parallel Session for Contributed Talks; details to come.*

**3:30–4:00 pm ET**

Break

**4:00–5:00 pm ET**

Panel: AI's Impact on Career Paths in Industry and Academia

*Details to come*

**6:00–8:00 pm ET**

*Workshop Dinner*

MIT Samberg Conference Center

### Thursday, August 13, 2026

**9:00–9:45 am ET**

*Running Headlong the Vortex: The Intersection of Experimental Particle Physics, LLMs, Agentic Workflows, and Collaborations*

Gordon Watts, University of Washington

<details>
<summary>Abstract</summary>
<em>Large language models and agentic workflows are changing how software is written, analyses are developed, and expertise is accessed. For experimental particle physics, these technologies raise important questions about productivity, knowledge transfer, collaboration, and governance.  This talk will focus on three questions: Why should we care? Where are we today? And where might we be going? I will discuss AI-assisted analysis, workflow automation, and the implications for large scientific collaborations. I will discuss both current capabilities and limitations, as well as emerging challenges involving validation, reproducibility, training, authorship, and responsibility.  Rather than predicting the future, the goal is to explore how AI and automation may reshape the way particle physics is done and how collaborations operate—and how we can adapt while preserving the principles that underpin scientific discovery.</em>
</details>

**9:45–10:30 am ET**

*From pixels to particles: deep learning in accelerator neutrino experiments*

Saul Alonso Monsalve, ETH Zurich

<details>
<summary>Abstract</summary>
<em>Neutrino detectors do not see particles directly. They record sparse patterns of charge, light, or pixel hits, from which the underlying interaction must be reconstructed. This talk will follow that path from raw detector readout to particle-level information, using examples from accelerator neutrino experiments. I will discuss how deep learning can help identify and separate particle activity, reconstruct vertices and kinematics, and learn useful representations from large samples of unlabeled data. Particular attention will be given to the practical challenges that determine whether these methods work in real experiments: detector geometry, limited labels, simulation mismodelling, and transfer across detector technologies. I will close with recent ideas in which machine learning and detector design are developed together, rather than treated as separate problems.</em>
</details>

**10:30-11:00 am ET**

Break

**11:00–11:45 am ET**

*Generative Perception: Probabilistic Inference for 3D Vision and Autonomy*

Todd Zickler, Harvard SEAS

<details>
<summary>Abstract</summary>
<em>Recovering 3D shape and materials from 2D images is fundamentally ambiguous. While humans handle this with remarkable success, many computer vision systems produce a single "best-fit" reconstruction, which fails to capture the true underlying uncertainty. In this talk, I describe our group’s efforts to treat perception as a generative inference task. I begin by mathematically characterizing some of the 3D explanation spaces of visual data, illustrating why single-outcome systems are inherently fragile for downstream tasks like motion planning and manipulation. I then present Generative Perception, a framework that leverages generative models to produce diverse, physics-grounded samples of 3D geometry and material properties. I demonstrate how these models represent uncertainty in the face of ambiguity, and how they naturally collapse toward veridical explanations as temporal cues become available. Finally, I discuss implications for embodied AI, arguing that robust, uncertainty-aware perception is a prerequisite for safe and effective autonomous systems in unconstrained environments.</em>
</details>

**11:45 am–12:30 pm ET**

*Symmetry breaking in transformers and interpretable alignment*

Eva Silverstein, Stanford University

<details>
<summary>Abstract</summary>
<em>Details to come.</em>
</details>

**12:30–2:00 pm ET**

Lunch Break

**2:00–3:30 pm ET**

*Parallel Session for Contributed Talks; details to come.*

**3:30–4:00 pm ET**

Break

**4:00–4:45 pm ET**

*AI and Cosmology*

Benjamin Wandelt, Johns Hopkins University

<details>
<summary>Abstract</summary>
<em>Details to come.</em>
</details>

**4:45–5:30 pm ET**

*Building Intelligence through Energy Based Models*

Yilun Du, Harvard

<details>
<summary>Abstract</summary>
<em>Existing AI systems are very powerful, but often fail in unseen environments in unexpected ways. I'll talk a bit about how we can use energy-based models (EBMs) as a tool for building more robust AI systems.  I'll talk about how EBMs allow us to reason and use search to solve unseen tasks, as well as how we can compose multiple EBMs together to solve unseen problems. I'll illustrate some initial results on scene understanding, reasoning, and decision-making.</em>
</details>

**5:30–6:00 pm ET**

*Remarks from IAIFI Leadership*


### Friday, August 14, 2026

#### IAIFI Industry Day

All Industry Day events will take place at the MIT Samberg Conference Center. [See the full schedule here,](https://iaifi.org/industry-day) including the list of participating industry partners.

**11:00am–1:00pm ET**

*Flash talks from industry partners*

**1:00pm-2:15pm ET**

*Networking lunch*

**2:15pm-3:45pm**

*Industry Partner Expo and Reception*

## Plenary Speakers

<div class="card-columns">
  <!--<div class="row">-->

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-saul-alonso-monsalve.jpg" alt="Saúl Alonso-Monsalve" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://samprd.ethz.ch">Saúl Alonso-Monsalve</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> ETH Zurich </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/photo-giorgi-butbaia.jpg" alt="Giorgi Butbaia" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://scholar.google.com/citations?user=FNLypywAAAAJ&hl=en">Giorgi Butbaia</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Caltech </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-miles-cranmer.jpg" alt="Miles Cranmer" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.maths.cam.ac.uk/person/mc2473">Miles Cranmer</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Cambridge </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-lance-dixon.jpg" alt="Lance Dixon" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://faculty.slac.stanford.edu/person/lance-dixon">Lance Dixon</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> SLAC </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-yilun-du.jpg" alt="Yilun Du" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://yilundu.github.io">Yilun Du</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Harvard Kempner Institute </em> <br>
         </div>
         </div>
       </div>
       
    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-lisa-everett.jpg" alt="Lisa Everett" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.physics.wisc.edu/directory/everett-lisa-l/">Lisa Everett</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> University of Wisconsin-Madison </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-berthy-feng.jpg" alt="Berthy Feng" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.berthyfeng.com">Berthy Feng</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IAIFI Fellow &<br>Incoming NYU Assistant Professor starting September 2027 </em> <br>
         </div>
         </div>
       </div>

     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-surya-ganguli.jpg" alt="Surya Ganguli" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://ganguli-gang.stanford.edu/surya.html">Surya Ganguli</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Standford University </em> <br>
         </div>
         </div>
       </div>

        <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-vicky-kalogera.jpg" alt="Vicky Kalogera" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://physics.northwestern.edu/people/faculty/core-faculty/vicky-kalogera.html">Vicky Kalogera</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Northwestern University</em> <br>
         </div>
         </div>
       </div>
       
       <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-gregor-kasieczka.jpg" alt="Gregor Kasieczka" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.physik.uni-hamburg.de/en/iexp/gruppe-kasieczka/personen/kasieczka-gregor.html">Gregor Kasieczka</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Universitat Hamburg </em> <br>
         </div>
         </div>
       </div>

      <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-erik-katsavounidis.jpg" alt="Erik Katsavounidis" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://www.mit.edu/~kats/">Erik Katsavounidis</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MIT </em> <br>
         </div>
         </div>
       </div>
       
      <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-rahul-kulkarni.jpg" alt="Rahul Kulkarni" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://blogs.umb.edu/rahulkulkarni/">Rahul Kulkarni</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> UMass Boston </em> <br>
         </div>
         </div>
       </div>
       
       <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-zongyi-li.jpg" alt="Zongyi Li" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://zongyi-li.github.io">Zongyi Li</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> MIT </em> <br>
         </div>
         </div>
       </div>

      <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-sung-hak-lim..jpg" alt="Sung Hak Lim" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://inspirehep.net/authors/1309390">Sung Hak Lim</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> IBS, Daejeon, CTPU. hep-ex and hep-ph and astro-ph </em> <br>
         </div>
         </div>
       </div>

       <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-shivam-pandey.jpg" alt="Shivam Pandey" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://astro.arizona.edu/person/shivam-pandey">Shivam Pandey</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> The University of Arizona </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-tilman-plehn.jpg" alt="Tilman Plehn" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://inspirehep.net/authors/993181">Tilman Plehn</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Heidelberg University </em> <br>
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
         <em> Stanford University </em> <br>
         </div>
         </div>
       </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
     <img class="my-card-img-top" src="images/small-photo-ben-wandelt.jpg" alt="Ben Wandelt" height="210rem" style="object-fit: cover;">
     <div class="card-body d-flex flex-column">
     <div class="card-text" style="text-align: center; min-height: 2rem;">
     <a href="https://benwandelt.org/">Ben Wandelt</a>
     </div>
     <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
     <em> Johns Hopkins University </em> <br>
     </div>
     </div>
   </div>

    <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
     <img class="my-card-img-top" src="images/small-photo-gordon-watts-2026.jpg" alt="Gordon Watts" height="210rem" style="object-fit: cover;">
     <div class="card-body d-flex flex-column">
     <div class="card-text" style="text-align: center; min-height: 2rem;">
     <a href="https://phys.washington.edu/people/gordon-watts">Gordon Watts</a>
     </div>
     <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
     <em> University of Washington </em> <br>
     </div>
     </div>
   </div>
   
   <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
        <img class="my-card-img-top" src="images/small-photo-christoph-weniger.jpg" alt="Christoph Weniger" height="210rem" style="object-fit: cover;">
        <div class="card-body d-flex flex-column">
        <div class="card-text" style="text-align: center; min-height: 2rem;">
        <a href="https://www.christophweniger.com/">Christoph Weniger</a>
        </div>
        <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
        <em> University of Amsterdam </em> <br>
        </div>
        </div>
     </div>
     
     <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
        <img class="my-card-img-top" src="images/small-photo-daniel-whiteson.jpg" alt="Daniel Whiteson" height="210rem" style="object-fit: cover;">
        <div class="card-body d-flex flex-column">
        <div class="card-text" style="text-align: center; min-height: 2rem;">
        <a href="https://sites.uci.edu/daniel/">Daniel Whiteson</a>
        </div>
        <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
        <em> UC Irvine </em> <br>
        </div>
        </div>
     </div>
     
        <div class="card" style="width: 17rem; height: 20rem; justify-content: center;">
         <img class="my-card-img-top" src="images/small-photo-todd-zickler.jpg" alt="Todd Zickler" height="210rem" style="object-fit: cover;">
         <div class="card-body d-flex flex-column">
         <div class="card-text" style="text-align: center; min-height: 2rem;">
         <a href="https://seas.harvard.edu/person/todd-zickler">Todd Zickler</a>
         </div>
         <div class="card-text" style="text-align: center; min-height: 4rem; line-height: 140%">
         <em> Harvard University </em> <br>
         </div>
         </div>
       </div>
       
</div>
<br>

## Accommodations

Recommended hotels in the area include: 

- <b>Le Meridien</b>, 20 Sydney St, Cambridge, MA 02139. 

- <b>Boston Marriott Cambridge<b>, 50 Broadway, Cambridge, MA 02142.

- <b>Residence Inn by Marriott<b>, 120 Broadway, Cambridge, MA 02142.

<!--
* <b>Hyatt Regency<b>, 575 Memorial Drrive, Cambridge, Massachusetts, 02139-4896.
    
    $219 nightly rate
    
    Deadline to book; Friday, July 10, 2026

  [Book online](https://www.hyatt.com/events/en-US/group-booking/BOSRC/G-IAIF)

-->


## FAQ 
* *Who can attend the Summer Workshop?* Any researcher working at or interested in the intersection of physics and AI is encouraged to attend the Summer Workshop. 
* *What is the cost to attend the Summer Worskhop?* The registration fee for the Summer Workshop is 200 USD and includes a welcome dinner, as well as coffee breaks and snacks.
* *If I come to the Summer School, can I also attend the Workshop?* Yes! We encourage you to stay for the Workshop and you can stay in the dorms for both events if you choose (at your expense). 
* *Will the recordings of the talks be available?* We plan to share the talks on our [YouTube channel](https://www.youtube.com/channel/UCueoFcGm_15kSB-wDd4CBZA).

[Submit a question or comment](https://app.smartsheet.com/b/form/76c1d070d19d4688b65962c4ed190478){:.button.button--outline-primary.button--pill.button--sm}

## 2026 Organizing Committee 
* Will Detmold, Co-Chair (MIT)
* Bill Freeman, Co-Chair (MIT) 
* Akshunna Dogra (IAIFI Fellow)
* Berthy Feng (IAIFI Fellow)
* Mathis Gerdes (IAIFI Fellow)
* Juvenal Bassa (UPRM)
* Yize Dong (Harvard)
* Franc O (Northeastern)
* Sneh Pandya (Northeastern)
* Shelley Tong (MIT)
* Lana Xu (MIT)
* Xiaoyuan Zhang (MIT)
* Marisa LaFleur (IAIFI Managing Director)
* Thomas Bradford (IAIFI Project Coordinator)
