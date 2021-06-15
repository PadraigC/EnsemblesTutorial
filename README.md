# EnsemblesTutorial
Python notebooks to accompany the paper `A Tutorial on Ensembles in Machine Learningwith Python Examples`.  
The notebooks are as follows:  
1. `Ensembles-Preliminaries`: Code demonstrating the impact of ensemble size and diversity on accuracy.
2. `Ensembles-Bagging`: Code for bagging and random subspace ensembles.
3. `Ensembles-RandomF`: Using random forest to generate feature importance scores and OOB estimates of generalisation accuracy.
4. `Ensembles-Boosting`: A simple AdaBoost example to illustrate the internal workings.
5. `Ensembles=GBoost`: Gradient Boosting compared with other ensemble methods. 
6. `Ensembles-Hetero`: A heterogeneous ensemble with 7 estimators complared with a bagging ensemble.
7. `Ensemble-Stacking`: A comparison of a heterogeneous with some stacking alternatives.

`ensemble_functions.py`: Some helper functions for ensembles.

### Data files
1. `wine.csv`: The wine dataset from the UCI repository.
2. `HotelRevHelpfulness.csv`: The hotel review dataset - see: https://researchrepository.ucd.ie/handle/10197/1894
3. `AthleteSelection.csv`: A toy dataset with just two predictive features.
