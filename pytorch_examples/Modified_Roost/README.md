## Modified Roost

This is an implementation of Roost model (https://www.nature.com/articles/s41467-020-19964-7, https://github.com/CompRhys/roost) in pytorch geometric. This code is more simple and contact which makes it easier to modify it further and use as a building block for more complicated models. 

Inititally this code was used for prediction of thermal conductivity from composition (for inorganic materials). The approach which was used is that the model was first trained on formation energy data, and then fine-tuned on themal conductivity data.
