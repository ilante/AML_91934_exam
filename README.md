# Computer Vision with Fashion-MNIST 

##### My First Machine Learning Project

## 88407 Appliend Machine Learning 
## And
## 91934 Appliend Machine Learning - ADVANCED

### International Master of Bioinformatics, University of Bologna


The ML methods developed are:

1. Artificial Neural Network (ANN)
2. Convolutional Neural Network (CNN)
2. Support Vector Machine (SVM)
3. k-nearest neighbors (k-NN)
4. Decision Tree (DT)
5. Random Forest (RF)


[View notebook in GitHub](https://github.com/ilante/AML_91934_exam/blob/main/Englander_AML_1_and_2.ipynb)

[Click here to open project in colab](https://colab.research.google.com/drive/1sfiID3MhXOyF_xI_Q4U80VecAwBIR6YX?usp=sharing)

Below an example of the input data: 

![](https://raw.githubusercontent.com/ilante/AML_91934_exam/main/fashion-mnist-example-img.png)

---
```
Wall clock time during last run: 1 hr and 20 min using:

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 495.44       Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  Off  | 00000000:00:04.0 Off |                    0 |
| N/A   43C    P0    28W / 250W |      0MiB / 16280MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
The obtained accuracies are outlined

| Method  | Accuracy | Wall Time |
|---------|----------|-----------|
| NN      | 88.63    | 44.63     |
| CNN 1   | 90.90    | 6.40      |
| CNN 2   | 92.64    | 20.68     |
| SVM PCA | 67.86    | 421.82    |
| SVM     | 88.04    | 388.39    |
| KNN bf  | 85.54    | 26.21     |
| KNN kd  | 85.54    | 25.92     |
| KNN bt  | 85.54    | 25.85     |
| DT      | 81.40    | 35.65     |
| RF      | 87.56    | 115.82    |
