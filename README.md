
# 🧠 Early Detection of Alzheimer’s Disease Using Multi-Modal Deep Learning

##  Project Objective

This project aims to assist clinicians in the **early detection of Alzheimer’s Disease (AD)** using a ** deep learning approach**. Accurate and early prediction can improve treatment planning, monitoring, and quality of life for patients at risk.

---

## 🗂 Data Source: ADNI1

The **Alzheimer’s Disease Neuroimaging Initiative (ADNI1)** dataset is a highly regarded and publicly available resource for neuroimaging research. It provides rich longitudinal data suitable for modeling disease progression.

For this project, we will use:

* ** 1.5T 3D structural MRI scans**

These data types will be **combined** to provide a more holistic view of patient trajectories, improving the model’s predictive power.

You can get permission to access the data from https://adni.loni.usc.edu/
---

##  Data Preprocessing

###  MRI Data:

* **Skull Stripping** using SynthStrip to isolate brain regions.
* **Bias Field Correction** (if required) using ANTs or SimpleITK.

* after downloading the data you can import the functions from FileArrangement.py file to organize and delete the unnecessary MRI pictures 


###  MRI Modality:

* **3D Convolutional Neural Networks (CNNs)** to extract spatial features.

---

##  Target Outcome

* **Binary classification**:  CN vs AD 
* **Evaluation Metrics**: Accuracy, AUC-ROC, Precision, Recall, F1-score.

---

##  Tools & Libraries

* **MRI Processing**: FSL, nibabel, SimpleITK, ANTs
* **Modeling**:  TensorFlow
* **Data Handling**: pandas, NumPy
* **Visualization**: matplotlib, seaborn, NiBabel viewers


