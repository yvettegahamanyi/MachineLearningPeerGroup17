# 📊 alumathPeerGroup17: Formative 2 - Principle Component Analysis

This project explores assigned coursework. It includes **Principal Component Analysis (PCA)** analysis on a dataset, PDF to show deeper understanding of finding eigenvalues and eigenvectors of the given matrix and a python library that performs different actions on two matrices.

---

## 📁 Project Structure

alumathPeerGroup17/
├── content/ # Contains the raw dataset used for PCA
├── eigen-values and vectors/ # Screenshots and PCA computation results
├── MatrixComputationLib/ # codes for the library codes
└── PCA_colab_notebook.ipynb # Main Google Colab file used for PCA

---

## 📌 Project Objectives

- Understand the core steps of PCA (centering, covariance, eigendecomposition)
- Apply PCA to a real dataset
- Visualize the results using screenshots and notebook outputs
- create a library that performs different actions on two matrices

---

## 🧪 Tools Used

- Python
- Google Colab
- NumPy & pandas
- matplotlib (for plotting)
- SymPy (for symbolic math, if used)
- Dataset (stored in `/content/`)

---

## 🚀 How to Use

### PCA_colab_notebook

1. Open the file `PCA_colab_notebook.ipynb` in Google Colab or Jupyter Notebook.
2. Run each cell to:
   - Load and explore the dataset
   - Normalize and center the data
   - Compute the covariance matrix
   - Extract eigenvalues and eigenvectors
   - Select top principal components based on explained variance
   - Project the data onto lower dimensions

### Eigenvectors and Eigenvalues Calculations

1. open the pdf file using your browser or other pdf readers to be able to read our calculations

### Python Library

1. To perform multiplication
## alumathpeergroup17

alumathpeergroup17 is  lightweight Python library for basic matrix computations (addition, subtraction, multiplication) with dimension checks.
1. To perform multiplicatio
## Install

```bash
pip install alumathpeergroup17
```
## Import the library  and perform your operations
```
from alumathpeergroup17 import matrix_multiplication

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

print(matrix_multiplication(a, b))
```
## Output
```
[[19, 22], [43, 50]]
```
---


## 🖼 Screenshots

Visual results (such as eigenvalue plots, covariance matrices, and projections) can be found in:
eigen-values and vectors/

---

## 👩‍💻 Contributors

- [Yvette Gahamanyi](https://github.com/yvettegahamanyi)
- Group 17 Members (Alumath Peer Program)

---

## 📜 License

This project is for academic purposes only and does not carry a software license.
