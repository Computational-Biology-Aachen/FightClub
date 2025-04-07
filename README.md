# 🧪 Fight Club: the war for resources

## Tripartite Microbial Dynamics

This project contains a theoretical framework to model **microbial population dynamics** involving three metabolic strategies competing for one shared nutrient.

---

## 📖 Overview

In microbial communities, shared nutrient use can lead to complex dynamics shaped by cooperation and competition. This project explores how three distinct microbial strategies co-exist and interact in a well-mixed batch culture on one carbon source (e.g., sucrose):

  - **Public Metabolizers** (P): Secrete invertase to externalize resource production.
  - **Cheaters** (C): Exploit the shared glucose without contributing enzymes.
  - **Private Metabolizers** (M): Internally cleave sucrose, bypassing communal sharing.

We explore both implement a system of non-linear ODEs in a Lotka–Volterra-inspired framework to study the dynamics. The model captures growth, cooperation, and competition dynamics among the populations.

---

## 📂 Repository Structure
This repository contains the code, models, and documentation for our theoretical study on microbial interactions and population dynamics. 

```
FightClub/
│
├── 📁 model/            # All code related to simulations 
│   ├── dynamic.py       # Model based on differential equations
│   ├── evolutionary.py  # Model based on evolutionary game theory
│   └── utils.py         # Helper functions (e.g., for fitting, plotting)
│
├── 📁 analysis/         # Post-processing and figure generation
│   ├── populationdynamics.ipynb  # Bifurcation analysis notebook
│   ├── casestudy.ipynb  # Case study showcasing applicability of teh general ODE model for race for iron
│   └── figures/         # Output plots used in manuscript
│
├── 📁 data/             # Experimental data (if shared)
│   ├── monoculture.csv    
│   └── coculture.csv      
│
├── 📁 docs/             # Documentation and (in future) manuscript figures
│   └── model_schematic.pdf
    └── manuscript.pdf   # We can consider pushing the latex source
│
├── LICENSE
├── README.md
├── requirements.txt       # Python dependencies or pixi, whatever you use
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
