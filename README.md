# 🧪 Fight Club: the war for resources

## Tripartite Microbial Dynamics

This project contains a theoretical framework to model **microbial population dynamics** involving three metabolic strategies competing for one shared nutrient.

---

## 📖 Overview

In microbial communities, shared nutrient use can lead to complex dynamics shaped by cooperation and competition. This project explores how three distinct microbial strategies co-exist and interact in a well-mixed batch culture on one carbon source (e.g., sucrose):

  - **Public Metabolizers** (P): Secrete invertase to externalize resource production.
  - **Cheaters** (C): Exploit the shared glucose without contributing enzymes.
  - **Private Metabolizers** (M): Internally cleave sucrose, bypassing communal sharing.

We explore both implemention of the system  in a Generalized Lotka–Volterra-inspired framework and Evalutionary Game Theory to study the dynamics. The model captures growth, cooperation, and competition dynamics among the populations.

---

## 📂 Repository Structure
This repository contains the code, models, and documentation for our theoretical study on microbial interactions and population dynamics. 

```
FightClub/
│
├── 📁 model/            # All code related to simulations 
│   ├── dynamic.py       # Model based on differential equations
│   ├── evolutionary.py  # Model based on evolutionary game theory
│   └── parameters.py     # parameters used for analysis
│
├── 📁 analysis/         # Post-processing and figure generation
│   ├── main.ipynb  # All analysis notebook
│   ├── casestudy 1.ipynb  # Case study showcasing applicability of teh general ODE model for parameterization from experimental data
│   └── simplex-code.ipynb  # Evalutionary Game Theory 
    └── output  
│  
│
├── 📁 docs/             
│   └── model_schematic.pdf # Community  Schematic 
    └── manuscript.pdf   # main manuscript file
│
├── LICENSE
├── README.md
├── requirements.txt       # Python dependencies
```



## 🔧 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Computational-Biology-Aachen/FightClub.git
cd FightClub
pip install -r requirements.txt
```

Python 3.8+ is recommended.

## 📚 Citation

If you use this code or model in your work, please cite:

```bibtex
@misc{TripartiteMicrobialDynamics2025,
  author       = {Hassan, Tanvir and Matuszy\'nska, Anna},
  title        = {Tripartite Microbial Dynamics: A Theoretical Framework for Three-Way Nutrient Competition},
  year         = {2025},
  howpublished = {\url{https://github.com/Computational-Biology-Aachen/FightClub}},
  note         = {Version 1.0, accessed April 2025}
}
```

This project is licensed under the MIT License. See [LICENSE](./LICENSE.md) for details.
