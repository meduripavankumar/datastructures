Hi -----,

First of all, thank you for taking your time to interview me.

Let me give you a brief about my growth journey.

I have completed my **B.Tech** from **SITAMS** and an **Executive MBA** with **BITS Pilani**.

I started as an **Associate Engineer** at **Unisys**, with **Java** as the technology. Within 9 months into my first company, I lost my job due to COVID layoffs.

Unsure what to do next, we started a **coaching center** at my friend’s place, and began teaching **AWS** there — meanwhile, I constantly kept myself updated and secured a few certifications in **Java, AWS, and Azure**.

Then I got an opportunity with **Cimpress** for a **contractual position as a Trainee Software Engineer**, and this is where I was first introduced to **Python**.

The entire application was in Python. It was so kind of my manager to say I could complete my module in any language — but I took it as a challenge and did it in **Python** itself, successfully contributing to a seamless integration.

It was a small module that called an API and stored logs in an **S3 bucket**.

Then with **Deloitte** and **Amazon**, I worked extensively with Python — exploring various challenges, finding the best-suited libraries, and optimizing the codebase.

It was with **Amazon** that I gained exposure to **Generative AI**.

I’ve worked with Amazon for almost **3 years now** and have delivered several successful projects — among which **Search And Rescue Automation Tool (SARA)** and **Tesseract** stand out as users’ favorites.

---

### 🧩 Project 1: Search And Rescue Automation Tool (SARA)

The intention of **SARA** is to act as a **scrutinizer** when a new applicant requests access to the **Amazon Ads API**.

It performs various checks — including **Denied Party**, **Good Standing Indicator**, etc. — along with **Generative AI** capabilities like classifying websites (whether they actually provide ad services or not) and detecting potential **marketing claims** that could mislead users.

All these observations are then sent to the reviewer handling the ticket.

---

### 🧩 Project 2: Tesseract

**Tesseract** performs similar actions but also includes sending emails based on the current status of approved applicants.

It checks whether a user has an **active directory**, verifies if the user has **published any ads**, ensures **licenses or certificates haven’t expired**, and sends automated **nudges accordingly** — globally — keeping them **compliant and active**.

---

This is a brief part of my **growth journey**.

---

### 👨‍💻 About Me

My name is **Pavan**.

I have an overall **6 years of experience in IT**, with **Python** and **AWS** as my core technical expertise.

My highest qualification is an **MBA in Business Analytics (BITS Pilani)** and a **B.Tech in Computer Science**.

I’m currently working at **Amazon**, and it’s been **2.5 years** as a **Team Lead**.

---

### 🧠 My Typical Workday

My typical day starts with taking updates from the team, assigning tasks, creating progress reports, and preparing for leadership calls.

Once done, I’m involved in **code**, **design**, and **infrastructure meetings** — followed by diving into my own coding work.

Our team has delivered **two tools** so far, with **SARA** being the most impactful.

---

### ⚙️ Project: Search And Rescue Automation Tool

This tool automates validations that were earlier performed manually by the operations team.

Validations involve:

* **Denied Party Check**
* **GSI Check**
* **Website Categorization (Ads vs Non-Ads)**
* **Marketing Claims Detection**
* **Automated Email Notifications (Nudges)**

---

### 🏗️ Architecture Overview

**Storage & Compute:**

* **S3** for storing input and processed files
* **EC2** instance for application deployment
* **Auto Scaling** to handle variable workloads

**Security & Networking:**

* **VPC** with subnet isolation for secure deployment
* **API Gateway** and **Cognito** for authentication and API management
* **Security Groups** & **Routing Rules** for traffic control

**Monitoring & Notifications:**

* **CloudWatch Logs** for real-time monitoring
* **Route 53** for domain management
* **SES** & **SNS** for automated email notifications

**AI & Generative AI Services:**

* **Textract** for extracting text from websites
* **Comprehend** for language detection and sentiment analysis
* **Translate** for multilingual text processing
* **Custom LLM Integration** for website categorization and marketing claim detection

---

### ⚙️ Functional Workflow

* Tool takes **input CSV** with company name, PNID, website, and email.
* It checks if the company is a **Denied Party** and verifies **GSI** using the PNID.
* The tool **extracts website content**, identifies its language using **Comprehend**, and translates to English if needed.
* The translated text is sent to a **custom LLM API** for **Ads vs Non-Ads classification**.
* It checks for **Marketing Claims** using sentiment and keyword analysis.
* It uses **SES** and **WorkMail** to send processed results to users automatically.
* Once processing is complete, the **result file** is emailed so users can continue working on other enrolled products.

---

Would you like me to make this more **formal and ready-to-send** as a follow-up “thank-you email” to the interviewer (with subject line, polished tone, and closing statement)? It would read very professional while keeping your story authentic.






Hi -----,
First of all thank you for taking your time to interview me.
let me give you a brief about my growth journey.
I have completed my BTech from SITAMS and an executive MBA with Bits Pilani.
and started as a Assoc Engineer at Unisys, with java as the technology.Within 9 months into my first company
i lost my job for covid layoffs. Unsure what to do next we started a coaching center at my firend's place,
and started teaching AWS and cloud there. meanwhile constantly keeping my self updated and secured a few certifications 
on java,aws and azure.
Then i got an opportunity with cimpress for a contracutal position as trainee software engineer, and here is where im first introduced to python
the entire application was in python, its so kind of my manager to say compelte my module in any language. but i took it as a challenge and have done it python itself, and contributed for a seamless integration. However it is a small module that calls the API and keeps the logs in an S3 bucket.
Then with Deloitte and Amazon i worked on python exploring various challenges, finding best suited libraries etc.
it is with Amazon i got my exposure towards Gen AI.

I worked with Amazon for almost 3 years now and have delivered successful projects amongst which Search And Rescue Automation Tool and Tesseract stands out to be users favourite.

The intention of SARA is to act as scrutiniser when a new applicant asks for Amazon Ads API access.
This performs various checks that involve denied party,good standing indicator etc, along with Gen AI capacities like classifying the website 
whether the website is actually providing ad services or not. and check if there are any potential market claims, that could mislead.
and all these observations will be sent to the reviewer who is reviweing this ticket.

and Tesseract does also performs similar kind of actions but it also includes sending emails as per the current status of the approved applicants. Where it checks if the user has an active directory if yes, it checks if user has published any ads,checks whether the user license or certificates expired  etc.. and sends the nudges accordigly worldwide, keeping them compliant and active.

This is a brief part of my growth journey.



My Name is Pavan,
I have a overall 6 years of experience in IT,with Python and AWS as my core tech expertise, 
my highesh qualification is a MBA degree in Business Analytics at Bits Pilani. and a BTech degree in Computer Science.
I'm currently working for Amazon and its been 2.5 years with Amazon, as a team lead.

My typical day starts with taking updates from the team.assigning tasks creating reports on the tasks and progress, keeping it ready for the leadership call.
Once done, i will be involved in code,design and infra meetings, then I will delve into my part of coding.

We have delivered 2 tools so far from the team.
My recent successful project is Search And Rescue Automation Tool.This tool is responsible to automate the validations
that were earlier performed maually by the operations Team.
Validations involve Denied Party check,GSI Check,Categorisation of websites as Ads or Non Ads,Check for Marketing Claims,Send Nudges.
And this is the workflow of the application.


On the Architecture part

Storage & Compute:
S3 for storing input and processed files.
EC2 instance for deploying the application.
Auto-scaling to handle varying workloads.

Security & Networking:
VPC with subnet isolation for secure deployment.
API Gateway & Cognito for authentication and API management.
Security Groups & Routing Rules for filtering inbound/outbound traffic.

Monitoring & Notifications:
CloudWatch Logs for real-time monitoring.
AWS Route 53 for domain management.
Amazon SES & SNS for automated email notifications.

AI & Generative AI Services:
AWS Textract for extracting text from websites.
AWS Comprehend for detecting language and analyzing sentiment.
AWS Translate for multilingual text processing.
Custom LLM Model Integration for website categorization and marketing claims detection.

On the functionality part.
In short we have used S3 for storing the files.App server is deployed on the Ec2 instance.
For security we have a VPC with subnet and API Gateway,Cognito user pool,
and a security group and auto scaling on the App server Filtering on inbound and outbound traffic on Security Groups.
and we have Route 53, SES paired with SNS and a cloud watch log monitors and AWS Wormail for sending emails to customers.
on Gen AI we have used services like AWS Comprehand,AWS Translate,AWS Textract.

Tool first takes the input as company name,PNID,website,email address as input csv file.
Tool processes the company and checks if it is a denied party or not, then proceeding onto the GSI using the unique PNID
At this point we extract the content of the website, identify its language using Comprehand, translate if needed into english.
The translated text is then given to our custom designed LLM model to analyse the content extracted and categorise as Ads or Non-Ads,via an API.
The tool then checks for Marketing claims,
a marketing claim could sound something like I ABC Company can grow your sales from 1X to 10 X within one week time and we are official partners with Amazon.
To perform this check we used AWS comprehand service to analyse the content and get the sentiment of the content and check if the sentiment matches with the marketing keyword phrases
It then uses the SES connection and workmail to send the emails to the customers.
This sends the result file to the users mail address once it completes processing the file so that user can work on other products that are enrolled in this Tool.








