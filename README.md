
# 🧠 Early Detection of Alzheimer’s Disease Using Multi-Modal Deep Learning

##  Project Objective

This project aims to assist clinicians in the **early detection of Alzheimer’s Disease (AD)** by predicting the **conversion from Mild Cognitive Impairment (MCI) to AD** using a **multi-modal deep learning approach**. Accurate and early prediction can improve treatment planning, monitoring, and quality of life for patients at risk.

---

## 🗂 Data Source: ADNI1

The **Alzheimer’s Disease Neuroimaging Initiative (ADNI1)** dataset is a highly regarded and publicly available resource for neuroimaging research. It provides rich longitudinal data suitable for modeling disease progression.

For this project, we will use:

* **Longitudinal 1.5T structural MRI scans**


These data types will be **combined** to provide a more holistic view of patient trajectories, improving the model’s predictive power.

---

##  Data Preprocessing

###  MRI Data:

* **Skull Stripping** using SynthStrip to isolate brain regions.
* **Bias Field Correction** (if required) using ANTs or SimpleITK.



##  Proposed Model Architecture

The model will adopt a **multi-modal, temporal-aware architecture** that integrates imaging and clinical data.

###  MRI Modality:

* **2D/3D Convolutional Neural Networks (CNNs)** to extract spatial features.
* **LSTM (Long Short-Term Memory)** layers to model temporal progression across multiple visits.




---

##  Target Outcome

* **Binary classification**: Convert from MCI to AD vs. remain stable.
* **Evaluation Metrics**: Accuracy, AUC-ROC, Precision, Recall, F1-score.

---

##  Tools & Libraries

* **MRI Processing**: FSL, nibabel, SimpleITK, ANTs
* **Modeling**: PyTorch / TensorFlow
* **Data Handling**: pandas, NumPy
* **Visualization**: matplotlib, seaborn, NiBabel viewers


