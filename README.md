# Analyzing_public_sentiments_to_data_center_energy_consumption

## ⚠️ Important Notice ⚠️
__As the paper is under review, all contents in this repository are currently not permitted for reuse by anyone until this announcement is removed. Thank you for your understanding! 🙏__
## 0. Summary of supplemental materials
This table below shows all supplemental materials. All sheets in Tables S1 and S2 are arranged in the order shown in this table.

![image](https://github.com/user-attachments/assets/7293fe61-24ba-4601-bb44-3ad4664ed01e)

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

![image](https://github.com/user-attachments/assets/8df90782-f33a-4bc9-abda-2b144687c5ad)

↑↑↑ Set configuration of our workstation running this repository.


Before submitting these codes to Github, all of them have been tested to be well-performed (as shown in the screwshots). Even so, we are not able to guarantee their operation in other computing environments due to the differences in the python version, computer operating system, and adopted hardware.

### 2.2 Mine posts and comments from Twitter

https://github.com/user-attachments/assets/b0bdbe0e-6b89-4528-925c-2dd4259719c3

↑↑↑ A video to showcase the data mining from Twitter, all collected social media data could be found in Table S1.


↓↓↓ All codes could be found below


### 2.3 Sentiment labeling by Gemma 2, Llama 3.2 & Phi 3
↓↓↓ A video to showcase the sentiment labeling process based on Llama 3.2.
 
https://github.com/user-attachments/assets/c1b962a8-b48f-4cad-81e0-ee718074758b

↓↓↓ All codes could be found below.

![image](https://github.com/user-attachments/assets/33d14148-2bc8-4650-8364-210fd6dff7ff)



### 2.4 Compare the performance of Gemma 2, Llama 3.2 & Phi 3 in sentiment labeling

![image](https://github.com/user-attachments/assets/acaaf867-c41f-4942-a1af-e37ee753e844)

↑↑↑ Codes for calculating the Precision, Recall and F1-score could be found above

![Screenshot of F1-score of gemma 2](https://github.com/user-attachments/assets/ac192995-18c5-40fa-b3c4-c11d09b5202e)
![Screenshot of F1-score of llama 3 2](https://github.com/user-attachments/assets/1d21091e-96da-44a0-89e8-2333e0c277be)
![Screenshot of F1-score of phi 3](https://github.com/user-attachments/assets/93a03eb5-349e-425d-9a97-86a33d813c2f)

↑↑↑ Screenshots of the Precision, Recall, and F1-score of Gemma 2, Llama 3.2, and Phi 3.

### 2.5 Topic labeling by Gemma 2

#### 2.5.1 Topic prompts

![image](https://github.com/user-attachments/assets/a06d2ce2-f0ac-4e5e-9049-3e7c4eaa99ce)

↑↑↑ Positive topic prompt for LLMs in topic classification.

![image](https://github.com/user-attachments/assets/3cd49eb7-4ff3-4a92-ad5c-61d4e3355d33)

↑↑↑ Negative topic prompt for LLMs in topic classification.

#### 2.5.2 Topic labeling

↓↓↓ Codes for positive and negative topic labeling could be found below

![image](https://github.com/user-attachments/assets/9c8139dc-07ca-49b9-974c-7b171c0f5c19)

![positive topic](https://github.com/user-attachments/assets/1f4cb64c-93f1-4295-b3bc-ea47f5db8876)

↑↑↑ A GIF to show positive topic classification based on Gemma2.

![11月9日 (1)](https://github.com/user-attachments/assets/1d0142a9-de5c-4891-8266-a053700bd105)

↑↑↑ A GIF to show negative topic classification based on Gemma2.




