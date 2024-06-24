# CrabNet for multiproperty prediction

This is version of CrabNet was created for multiproperty prediction. The original CrabNet model can be found here (https://www.nature.com/articles/s41524-021-00545-1, https://github.com/anthony-wang/CrabNet)

The model CrabNet_for_Multiproperty is composed of a common encoder (Embedder+Attention Layers) 
and separate ResNet heads (one for each property). Properties used were Formation Energy, Energy Above Hull, Stability, Disorder (so two regression tasks and two classification tasks) the loss was taken as a sum of losses from all heads. Each material in train/test set should have at least one property. 
