# AF Discovery -- Segmenting Ultrasound (US) Images for Amniotic Fluid (AF) - An AI4GoodLab 2023 Project
This repository contains the code and documentation for the team **AF Discovery**, part of the **AI4GoodLab** 2023 initiative. Our team of five, along with our TA, completed this project within a three-week timeframe. The technical description is *"Machine Learning Pipeline for Segmenting Ultrasound (US) Images to Assess Amniotic Fluid (AF)"*.

![Picture8](https://github.com/SeidaAhmed/Ultrasound-Image-Segmentation-classification/assets/65707004/1d809528-dfa8-4fdb-b565-179bca13962b)

## Our Mission
We are **AF Discovery**, dedicated to enhancing patient care for expectant mothers by equipping clinicians with a machine learning solution that facilitates timely and confident decision-making.

## Importance of **AF Discovery**
Amniotic fluid surrounds a developing fetus and its volume is critical for fetal health. Both excessive and insufficient amniotic fluid levels can lead to serious complications requiring urgent medical intervention. 

For instance, low amniotic fluid volume (AFV) may necessitate time-sensitive decisions such as induced labor or cesarean delivery. With over 280 million women facing AFV-related complications annually, accurate and timely assessments are essential.

Currently, AFV calculations are performed manually by ultrasound technicians and physicians, which is time-consuming and subject to human error. In low-resource settings, the lack of time often leads to visual assessments rather than precise calculations.

Our solution leverages machine learning to segment fetal ultrasound images and determine AFV in real-time, thereby saving valuable time and resources for healthcare providers and empowering patients to make informed decisions.

## Development and Training Process
We have developed a supervised deep learning convolutional neural network model, known as U-NET, to segment 2D fetal ultrasound images and a regression model to predict outcomes.

Due to the unavailability of a labeled AFV ultrasound dataset, we utilized a similar dataset of fetal head ultrasound images. Our UNET model was trained on this dataset, which was divided into labeled training and test sets. The regression model was subsequently trained using clinical measures associated with the training images. This pipeline can be adapted for AFV datasets in the future.

The fetal head images were annotated for head circumference and preprocessed before being input into the UNET model. The regression model then utilized the UNET's segmentation predictions to estimate outcomes, specifically predicting fetal head circumference.

## Model Performance
While our model successfully segments fetal head ultrasound images, there is potential for improvement. Various similarity coefficients suggest that our prediction accuracy can be enhanced. Future steps will focus on refining our model and adapting it for AF datasets.

## Using the AF Discovery WebApp
Users can upload screenshots of their ultrasound images and receive predicted AFV results within moments. This functionality could be extended to live video feeds, enabling real-time segmentation of ultrasound features in the future.

## Team Contact Information
Our team at AF Discovery comprises highly skilled researchers with expertise in machine learning, computer science, and biology. We welcome any inquiries you may have!

- **Arfaa Rashid**
  - B.Sc. in Computer Science, University of Windsor
  - LinkedIn: [Arfaa's LinkedIn](https://www.linkedin.com/in/arfaa-rashid-6696-hbc/)
  - GitHub: [Arfaa's GitHub](https://github.com/arfaamr)

- **Ann-K Chou**
  - M.Sc. in Interactive Arts & Technology, Simon Fraser University
  - LinkedIn: [Ann-K Chou's LinkedIn](https://www.linkedin.com/in/annkchou/)
  - GitHub: [Ann-K Chou's GitHub](https://github.com/annkchou)

- **Huma Noor**
  - B.Sc. in Biochemical Biophysics and Bioethics, University of Toronto

- **Mehjabin Rahman**
  - M.Sc., Toronto Metropolitan University
  - LinkedIn: [Mehjabin's LinkedIn](https://www.linkedin.com/in/mehjabin-rahman)
  - GitHub: [Mehjabin's GitHub](https://github.com/mehjabin-rahman)

- **Seida Ahmed**
  - M.Sc., University of Toronto
  - GitHub: [Seida Ahmed's GitHub](https://github.com/SeidaAhmed)

- **Karissa Chan (Teaching Assistant)**
  - M.Sc., Toronto Metropolitan University
  - LinkedIn: [Karissa Chan's LinkedIn](https://www.linkedin.com/in/karissa-chan/)

---

## Presentation and Demo
Access the presentation and demo of our project [here](https://www.figma.com/proto/LetYxHdyqilbbD0F1KBtLf/AF-Discovery?type=design&node-id=2-2313&scaling=scale-down&page-id=0%3A1&starting-point-node-id=9%3A6275).

## Demo of HC Predictor (Gradio App) (Live until June 20, 2023)
![Demo of HC Predictor Screenshot](Img/Ann-HC-gradioapp.jpg)
Access the demo HC Predictor (Random Forest Regression) [here](https://9cc7148ac18b49fbb0.gradio.live/).

## Technologies Utilized
- Machine Learning Framework: TensorFlow
- GPU: Google Colab
- Development Environments: Colab, Jupyter, Spyder
- Code Sharing Platforms: Colab, Google Shared Drive, GitHub
- Serverless Architecture
- Mock-up Design: Figma
- Front-end Deployment: Gradio

## Dataset Acknowledgment
We acknowledge the dataset provided by Thomas L. A. van den Heuvel, Dagmar de Bruijn, Chris L. de Korte, and Bram van Ginneken in their publication titled "Automated Measurement of Fetal Head Circumference Using 2D Ultrasound Images" [Data set]. This dataset, available at Zenodo (http://doi.org/10.5281/zenodo.1322001), was instrumental in training our machine learning models.

## References
- Thomas L. A. van den Heuvel, Dagmar de Bruijn, Chris L. de Korte, and Bram van Ginneken. Automated measurement of fetal head circumference using 2D ultrasound images [Data set]. Zenodo. http://doi.org/10.5281/zenodo.1322001
- arXiv:2303.07852 [eess.IV] https://doi.org/10.48550/arXiv.2303.07852

## Acknowledgements
I (Ann K. Chou) would like to acknowledge AI4Good for their support and guidance throughout this project. Additionally, I would like to express my gratitude to the AI4Good lab for fully supporting my special needs as a person with a disability.

---

## Ann K Chou's Background as Relevant to AI4Good
As a soon-to-graduate Master of Science student in Interactive Arts and Technology at Simon Fraser University, my background is highly relevant to this health-related AI4Good project. With a background as a medical technologist and health informatics practitioner, I bring a unique perspective to the table. Additionally, I am severely hard of hearing and have recently been diagnosed with Autism Spectrum Disorder. These personal experiences have fueled my passion for using technology and AI for the greater good. Joining the AI4Good lab provides me with an opportunity to enhance my technical skills and stay up-to-date with the latest machine learning concepts. Through my own research in electronic health records, I have shifted my focus towards an art-oriented activist community approach and empathy-driven design. This change is partly influenced by the challenges in accessing clinical data and the shifting priorities in the clinical realm due to the impact of COVID-19. This project duration of 3 weeks strikes a good balance for me, allowing me to take care of myself and other obligations while still dedicating time to learning and working on the project.

## Ann K Chou's Individual Contribution
My main contributions to the project were focused on the downstream tasks of the UNet model. I worked on post-processing techniques to refine the output of my colleague's UNet model, which was in the form of a binary image. Additionally, I developed regression models to predict the head circumference based on the segmented ultrasound images. These efforts were crucial in providing accurate and meaningful outcomes for our machine learning solution. I am proud to have played a role in enhancing the performance and usability of our model.

Connect with me:
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Ann%20K%20Chou-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/annkchou/)
- [![Instagram](https://img.shields.io/badge/Instagram-annreflection-purple?style=flat&logo=instagram)](https://www.instagram.com/annreflection/)
- ![Hard of Hearing](Img/Assistive_Listening_Devices_2.png)

## Seida Ahmed's Individual Contribution 
My involvement in this project begins with the initiation of the idea, derived from my personal experience.. While pregnant with my first baby, I faced the challenge of low Amniotic Fluid Volume during the third trimester, leading to an elective Cesarian Section. The inconsistent results from various check-ups made it difficult for me to make an informed decision. This made me realize that many women worldwide may face similar problems. Moreover, the limited availability of physicians in Ethiopia further highlighted the need for automation in measuring amniotic fluid levels, allowing doctors to save more lives.

## Mehjabin and Arfaa Rashid's Individual Contribution 
- train unet, custom dataloader, similarity, working w dataset
- worked on preprocessing, background research
