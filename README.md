# MindCare
a model aim to help doctors detect alzheimer disease early by ptrdicting MCI-to-AD conversion with multi-modal deep learning, ADNI1 datasouce will be used for this proejct as considered a valble data soucre for our project by combining mri images in addtion to the clinical data for each patient 
the choseen data include:
 Longitudinal 1.5 MRI scans
 Cognitive and Clinical Assessments

 daata Preprocessing will include:
   MRI: Skull-strip, normalize, register longitudinally.
   Tabular: Normalize numerical, encode categorical.

possiple model workflow:
  3D/2D CNN-LSTM for MRI
  LSTM for cognitive
  
