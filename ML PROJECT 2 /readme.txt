Within the main folder, there are different files:

1) proyect2_PDEexplicit.py: file with the code to program euler explicit for the PDE with Dirichlet BCs. It's a Python Code done in Spyder.

2) PDEexplicit_Neumann.py: same tas previous with the exception that it's for PDE with Neumann BCs.

3) Machine Learning.pdf: The pdf of the report. 

4)Article_reference.pdf: One of the articles we follow to solve PDE with Neumann BCs through NNs. 

5) Neural_Networks_Script.ipynb: Jupyter file with the code for NN implementation with different GD methods. More explanations are below: 



The results are found within the Imagenes (in spanish, sorry! ) folder, inside the SGD, MGD and AM and Comparison folders.
Stand for:

SGD: Stochastic Gradient Descents,
MGD: Gradient Descent With Momentum and
AM: Adam Method


In each folder there are subfolders named lambda_{X}: the X represents different numbers. These numbers represent different learning rates.

In the Comparison folder there are results related to the performance of each Method.

Finally, in the AM_SECOND_EQUATION folder are the results of the same differential equation but with different boundary conditions (Neumann Conditions, conditions on the derivative) and a different initial condition: u(x,0)= cos(pi*x).