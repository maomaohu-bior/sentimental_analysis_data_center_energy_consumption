# Analyzing_public_sentiments_to_data_center_energy_consumption

## ⚠️ Important Notice ⚠️
__As the paper is under review, all contents in this repository are currently not permitted for reuse by anyone until this announcement is removed. Thank you for your understanding! 🙏__
## 0. Summary of supplemental materials
This table below shows all supplemental materials. All sheets in Tables S1 and S2 are arranged in the order shown in this table.

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/supplemental%20materials.png)

## 1. Introduction
### 1.1 Objective 
This repository aims at providing the codes and data regarding the paper entitled “……” for the public, and it is developed by XXX University of XXX in Singapore and XXX University in China.
### 1.2 Acknowledgements
We greatly appreciate the selfless spirits of these voluntary contributors of a series of open python libraries, including Ollama (https://github.com/ollama/ollama), meta-llama (https://github.com/meta-llama/llama), google-gemini (https://github.com/google-gemini/gemma-cookbook), Phi-3CookBook (https://github.com/microsoft/Phi-3CookBook), some base works (https://github.com/DAMO-NLP-SG/LLM-Sentiment, https://github.com/Data4Democracy/media-crawler, https://github.com/jeffreyxchan/Twitter-Crawler, https://fred.stlouisfed.org/series/APU000072610), and so on. Our work stands on the shoulders of these giants.
### 1.3 Copyright
As for anything regarding the copyright, please refer to the MIT License or contact the authors.


## 2 Reuse ths repository
### 2.1 Set environment
All code is developed in **Python 3.9** using **PyCharm IDE**. Below are the hardware specifications of the workstation used to run this code. These specifications are listed for reference only and do not represent the minimum requirements to run the project. Feel free to experiment with different setups! 🚀

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/work%20station.png)

↑↑↑ Set configuration of our workstation running this repository.


Before submitting these codes to Github, all of them have been tested to be well-performed (as shown in the screwshots). Even so, we are not able to guarantee their operation in other computing environments due to the differences in the python version, computer operating system, and adopted hardware.

### 2.2 Mine posts and comments from Twitter

![](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/d270ad282da2e573a99f8a4eb2556132a986f75c/Videos%20%26%20Figures/data%20mining%20from%20Twitter.gif)

↑↑↑ A .gif to showcase the data mining from Twitter, the whole HD video could be downloaded here ![video](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/data%20mining%20from%20Twitter%2C.mp4) all collected social media data could be found in Table S1.

### 2.3 Sentiment labeling by Gemma 2, Llama 3.2 & Phi 3
↓↓↓ A .gif to showcase the sentiment labeling process based on Llama 3.2. The whole HD wideo could be found here ![video](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/2637deb2460a9ca45a7f28ab0ff829ef13641563/Videos%20%26%20Figures/11%E6%9C%889%E6%97%A5(1).mp4)

![](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/d270ad282da2e573a99f8a4eb2556132a986f75c/Videos%20%26%20Figures/sentiment%20labeling.gif)

↓↓↓ All codes could be found below.

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/all%20codes%20could%20be%20found%20here.png)

### 2.4 Compare the performance of Gemma 2, Llama 3.2 & Phi 3 in sentiment labeling

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/8c38d7dfe22e8f97e372555947b5c115f97c2485/Videos%20%26%20Figures/all%20codes%20could%20be%20found%20here%20comparison.png)

↑↑↑ Codes for calculating the Precision, Recall and F1-score could be found above

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/b69a8c56a7c09a34a5c449d82c06855595c00aa0/Videos%20%26%20Figures/Screenshot%20of%20F1-score%20of%20gemma%202.png)
![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/b69a8c56a7c09a34a5c449d82c06855595c00aa0/Videos%20%26%20Figures/Screenshot%20of%20F1-score%20of%20llama%203.2.png)
![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/b69a8c56a7c09a34a5c449d82c06855595c00aa0/Videos%20%26%20Figures/Screenshot%20of%20F1-score%20of%20phi%203.png)


↑↑↑ Screenshots of the Precision, Recall, and F1-score of Gemma 2, Llama 3.2, and Phi 3.

### 2.5 Topic labeling by Gemma 2

#### 2.5.1 Topic prompts

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/positive%20topic%20prompts.png)

↑↑↑ Positive topic prompt for LLMs in topic classification.

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/negative%20topic%20prompts.png)


↑↑↑ Negative topic prompt for LLMs in topic classification.

#### 2.5.2 Topic labeling

↓↓↓ Codes for positive and negative topic labeling could be found below

![image](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/8c38d7dfe22e8f97e372555947b5c115f97c2485/Videos%20%26%20Figures/all%20codes%20could%20be%20found%20here%20topic.png)

![](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/positive%20topic.gif)

↑↑↑ A GIF to show positive topic classification based on Gemma2.

![](https://github.com/maomaohu-bior/sentimental_analysis_data_center_energy_consumption/blob/4a4b077949b19277ee992abc0f1dc36022c5a981/Videos%20%26%20Figures/negative%20topic.gif)

↑↑↑ A GIF to show negative topic classification based on Gemma2.




