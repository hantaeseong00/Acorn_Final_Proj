# :pushpin: GgulKkuk
>영양 불균형 문제 해결을 위한 CNN 기반 반찬 예측 및 메뉴 추천 서비스
>https://go-quality.dev  

## 1. 소스코드(Colab)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)
- [KaggleProject-COVID-19 Radiography.ipynb](https://colab.research.google.com/drive/1L6PIqXr90Z5dmQ6rOFfv8pmAqIsb8Zs5#scrollTo=YYHdRwx4S1Is)

</br>

## 2. MobileNet 기본 세팅
- weight: imagenet
- Dropout: 0.5
- optimizer: Adam

</br>

### 2.1. Basic
- Model Architecture: MobileNet - F - D(1024) - D(1024) - D(1024)
- Learning Rate: 2e-5
![](./Graph/1.png)
- Accuracy : 0.9488
- Learning Time : 26376814.830 ms
</br>

### 2.2. Change dense value to 2048
- Model Architecture: MobileNet - F - D(2048) - D(2048) - D(2048)
- Learning Rate: 2e-5
![](./Graph/2.png)
- Accuracy : 0.9520
- Learning Time : 25686338.559 ms

</br>

### 2.3. Change dense value to 4098
- Model Architecture: MobileNet - F - D(4098) - D(4098) - D(4098)
- Learning Rate: 2e-5
![](./Graph/3.png)
- Accuracy : 0.9523
- Learning Time : 25535377.915 ms

</br>

### 2.4. Change the number of hidden layers to 2
- Model Architecture: MobileNet - F - D(1024) - D(1024)
- Learning Rate: 2e-5
![](./Graph/4.png)
- Accuracy : 0.9520
- Learning Time : 20395924.553 ms

</br>

### 2.5. Change the number of hidden layers to 4
- Model Architecture: MobileNet - F - D(1024) - D(1024) - D(1024) - D(1024)
- Learning Rate: 2e-5
![](./Graph/5.png)
- Accuracy : 0.9365
- Learning Time : 20511320.952 ms

</br>

### 2.6. Change learning rate value to 5e-5
- Model Architecture: MobileNet - F - D(1024) - D(1024) - D(1024)
- Learning Rate: 5e-5
![](./graph/6.png)
- Accuracy : 0.9537
- Learning Time : 23425362.471 ms

</br>

### 2.7. Change learning rate value to 2e-4
- Model Architecture: MobileNet - F - D(1024) - D(1024) - D(1024)
- Learning Rate: 2e-4
![](./Graph/7.png)
- Accuracy : 0.9654
- Learning Time : 28082135.071 ms

</br>

## 3. The result of MobileNet fine-tuning

![](./Graph/The_result_of_MobileNet_fine_tuning.png)

| Model | Hidden Layer | Dense Count | Learning Rate | Accuracy | Learning Time(ms) | 
| :-- | :-: | :-: | :-: | :-: | :-: |
| **mn_resultset1** | 3 | 1024 | 2e-5 | 94.88% | 26376814 |
|  |  |  |  |  |  |
| **mn_resultset2** | 3 | 2048 | 2e-5 | 95.20% | 25686338 |
| **mn_resultset3** | 3 | **4096** | 2e-5 | 95.23% | 25535377 |
|  |  |  |  |  |  |
| **mn_resultset4** | **2** | 1024 | 2e-5 | 95.20% | 20395924 |
| **mn_resultset5** | **4** | 1024 | 2e-5 | **93.65%** | **20511320** |
|  |  |  |  |  |  |
| **mn_resultset6** | 3 | 1024 | 5e-5 | 95.37% | 23425362 |
| **mn_resultset7** | 3 | 1024 | **2e-4** | **96.54%** | **28082135** |


</br>
