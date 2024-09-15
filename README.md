# Tripartite Microbial Consortia

## Main Goal 1: Find the Stable Coculture Condition for Cyanobacteria and Heterotrophic Partners with Carbon Resource Sharing
#### Overview

The goal of this part of the project is to identify the conditions under which cyanobacteria and heterotrophic partners can coexist stably in a coculture environment. This stability is determined by the efficient sharing and utilization of carbon resources, specifically sucrose and glucose, produced by the cyanobacteria through photosynthesis. 

#### Key assumption

1. Cyanobacteria Photosynthesis and Sucrose Production:
    - Cyanobacteria harness light and carbon dioxide to produce sucrose via photosynthesis. This process is fundamental to the survival and growth of both cyanobacteria and their heterotrophic partners.
    - Sucrose production is influenced by environmental factors such as light intensity and CO₂ concentration.

2. Resource Allocation:
    - Sucrose produced by cyanobacteria is partly used for their own growth and maintenance, with the remaining portion available to heterotrophic partners.
    - Understanding the balance between cyanobacteria's own consumption and the amount of sucrose made available to heterotrophs is critical for maintaining stable populations.

3. Heterotrophic Metabolism:
    - Heterotrophic partners has divided metabolic strategies: public metabolizers, private metabolizers, and cheaters.
    - Public metabolizers produce and secrete enzymes that convert sucrose into glucose, which can then be utilized by all members of the community, including cyanobacteria and other heterotrophs.
    - Private metabolizers consume sucrose for their own growth without sharing the resulting glucose.
    - Cheaters exploit the public goods produced by public metabolizers without contributing to the production process.

### Main Goal 2: Use Evolutionary Game Theory to Analyze the Cost and Benefit of Enzyme Production in Heterotrophic Partners

#### Overview

This project aims to apply evolutionary game theory (EGT) to understand the metabolic strategies of heterotrophic partners in a coculture system with cyanobacteria. We focus on three types of strategies: public metabolizers, private metabolizers, and cheaters. By analyzing the costs and benefits of enzyme production, we can predict stable metabolic interactions and optimize resource sharing.

#### Metabolic Strategies

1. Public Metabolizers:
    - Produce enzymes to convert sucrose into glucose, which is shared with the community.
    - Incurs a production cost but benefits from the collective pool of glucose.

2. Private Metabolizers:
    - Consume sucrose directly without sharing glucose.
    - Avoid enzyme production costs but do not contribute to the communal glucose pool.

3. Cheaters:
    - Exploit glucose produced by public metabolizers without producing enzymes.
    - Benefit from public resources without incurring costs, risking communal resource depletion.

 

## Model discription

# lotka volterra

$$ \frac{dC}{dt}= r_c \cdot C - \alpha \cdot C\cdot D - \beta \cdot C \cdot P $$

   $$ \frac{dD}{dt}= \alpha C\cdot D - \nu \cdot D $$


   $$ \frac{dP}{dt}= r_p \cdot P - \eta P \cdot C $$ 

$r_c, r_p =$  natural growth rate of public and private in Monoculture.
Effect of P on C population = $\beta$,  Benefit shearing( Public to Cheater) = $\alpha$,  Effect of C on P  Population =$\eta$, and mortality rate of cheater Population  = $\nu$.


# lotka volterra with logistic growth

 $$
    \frac{dC}{dt}= r_c \cdot C - \alpha \cdot C\cdot D - \beta \cdot C \cdot P - \lambda \cdot C ^2
$$

$$
    \frac{dD}{dt}= \alpha C\cdot D - \nu \cdot D^2
$$

$$
    \frac{dP}{dt}= r_P \cdot P - \eta P \cdot C - \gamma \cdot P^2
$$







$r_c, r_p =$  natural growth rate of public and private in Monoculture.
Effect of P on C population = $\beta$,  Benefit shearing( Public to Cheater) = $\alpha$,  Effect of C on Q  Population =$\eta$, and Effect of other cheater Population  = $\nu$, Effect of other Public Population  = $\lambda$, Effect of other Private Population  = $\gamma$





###  Equilibrium Point:
$( \frac{\nu}{\alpha}, \frac{r_c - \frac{\beta}{\gamma} \cdot (r_P - \eta \cdot \frac{\nu}{\alpha}) - \lambda \cdot \frac{\nu}{\alpha}}{\alpha}, \frac{r_P - \eta \cdot \frac{\nu}{\alpha}}{\gamma})
$

This is the equilibrium point where all three populations coexist.


### the Jacobian Matrix
The Jacobian matrix is:
$$
J(C^*, D^*, P^*) = \begin{pmatrix}
r_c - \alpha D^* - \beta P^* - 2\lambda C^* & -\alpha C^* & -\beta C^* \\
\alpha D^* & \alpha C^* - \nu & 0 \\
-\eta P^* & 0 & r_P - \eta C^* - 2\gamma P^*
\end{pmatrix}
$$

# Dynamic Resource Model

Cyanobacteria are photosynthetic microorganisms that convert light energy and carbon dioxide (CO₂) into organic carbon in the form of sucrose through photosynthesis. The photosynthesis process can be described by Michaelis-Menten kinetics to incorporate the effects of light intensity $(L_i)$ and $CO₂$ concentration $(C_i)$. The photosynthesis rate $(P)$ for cyanobacteria can be modeled as:

  
  $$ P = f(L_o, C_r) = P_{max} \frac{L_o }{K_L + L_o} \cdot \frac{C_r}{K_C + C_r} $$
  
  where $ K_L $ and $ K_C $ are half-saturation constants for light and CO_2,  $ P_{\text{max}} $ is the maximum photosynthesis rate respectively.

\textbf{Sucrose Production Rule}: The sucrose production $P(t) $ is a fraction of the photosynthesis output, adjusted by the cell's energy needs and efficiency factors.
  
 
  $$ S(t) = k \cdot P \cdot C  $$
  
where $ k $ is the conversion efficiency of photosynthetic products to sucrose. 





The sucrose $S_c$ produced is partially consumed by cyanobacteria for growth and maintenance, and the rest is excreted into the environment, making it available to the heterotrophic partners. The equation for sucrose intake rate is as follows:

$$ S_c = L_0 \left( \frac{A_f}{V} \right) \epsilon\cdot C  $$

with $ I_0 $  being the intensity of incident light, $ A_f $ being the illuminated surface area of the reactor, $ V $ being the reactor's liquid volume,$ C $ total cyano biomass, $ ε $  Extinction Coefficient.


$$ S_h =  S(t) - S_c $$

where $ S_h $ is the sucrose concentration rate given to the heterotropic partner. 

The growth rate of cyanobacteria $ \mu_C $ depends on the available sucrose:

$$ \mu_C = \mu_{\text{max}} \frac{S_c}{K_s + S_c} $$
and their biomass change over time is given by:

$$ \frac{dC}{dt} = \mu_C \cdot C - \lambda \cdot C $$

where $ \mu_{\text{max}} $ is the maximum specific growth rate,$ K_s $ is the half-saturation constant for sucrose, $ \lambda $ is the mortality rate of cyanobacteria.

\textbf{3) Private, Public and Cheater Metabolizer(Competition and Mutualism )}

 \textbf{Private Metabolizer (Q)}: This partner produces private enzymes to convert sucrose (Sh) into glucose (G) for its use. The specific growth rate $\mu_P$ is:

$$ \mu_q =\frac{\mu_{\text{max}}  \cdot S_h}{k_q + S_h} $$

 Their biomass change over time is given by:

  $$ \frac{dQ}{dt} = \mu_q \cdot Q - \lambda \cdot Q - e_q \cdot Q $$
  
  where $ e_q $ represents the cost of producing private enzymes.

$$ \frac{dS_h}{dt} = S_h - \nu_p \cdot P - \nu_q \cdot Q  $$

\textbf{Public Metabolizer (P)}: This partner produces public enzymes that convert sucrose(Sh)into glucose (G). The specific growth rate $ \mu_P $ of the public metabolizer depends on the available glucose:

  $$ \mu_P = \mu_\text{max} \frac{G}{K_p + G } $$

  Their biomass change over time is given by:

  $$ \frac{dP}{dt} = \mu_P \cdot P - \lambda \cdot P - e_p\cdot P $$

  Where $ e_p $ represents the cost of producing public enzymes.


-\textbf{ Cheater (D):} This partner does not produce public enzymes and relies on the glucose (G) produced by the public metabolizer. The specific growth rate $ \mu_D $ of the cheater is:

  $$ \mu_d = \mu_{\text{max}} \frac{G}{K_D + G} $$

  Their biomass change over time is given by:

  $$ \frac{dD}{dt} = \mu_D \cdot D - \lambda \cdot D $$

The change in glucose concentration (G) over time is described by:

$$ \frac{dG}{dt} = e_p \cdot \nu_p\cdot P -   \frac{\mu_D}{Y_D} - \frac{\mu_p}{Y_P} $$

$e_P$ is the enzyme that produces the sucrose-to-glucose production rate.\\
