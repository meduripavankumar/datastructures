My Name is Pavan,
I have a overall 6 years of experience in IT,with Python and AWS as my core tech expertise, 
my highesh qualification is a MBA degree in Business Analytics at Bits Pilani. and a BTech degree in Computer Science.
I'm currently working for Amazon and its been 2.5 years with Amazon, as a team lead.
My typical day starts with taking updates from the team.assigning tasks and checking on the progress.
Create reports on the tasks and the corresponding progress, keeping it ready for the weekly leadership call.
Once done, i will be involved in code,design reviews, infra justification meetings, then I will delve into my part of coding.
We have delivered 2 tools so far from the team.
My recent successful project is Search And Rescue Automation Tool.This tool is responsible to automate the validations
that were earlier performed maually by the operations Team.
Validations involve Denied Party check,GSI Check,Categorisation of websites as Ads or Non Ads,Check for Marketing Claims,Send Nudges.
And this is the workflow of the application.
On the Architecture part


/* we have used S3 for storing the files.App server is deployed on the Ec2 instance.
For security we have a VPC with subnet and API Gateway,Cognito user pool,
and a security group and auto scaling on the App server Filtering on inbound and outbound traffic on Security Groups.
and we have Route 53, SES paired with SNS and a cloud watch log monitors and AWS Wormail for sending emails to customers.
on Gen AI we have used services like AWS Comprehand,AWS Translate,AWS Textract. */

Architecture Overview
The tool is built on a robust AWS-based infrastructure to ensure scalability, security, and efficiency:

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
Tool first takes the input as company name,PNID,website,email address as input csv file.
Tool processes the company and checks if it is a denied party or not, then proceeding onto the GSI using the unique PNID
At this point we extract the content of the website, identify its language using Comprehand, translate if needed into english.
The translated text is then given to our custom designed LLM model to analyse the content extracted and categorise as Ads or Non-Ads,via an API.
The tool then checks for Marketing claims,
a marketing claim could sound something like I ABC Company can grow your sales from 1X to 10 X within one week time and we are official partners with Amazon.
To perform this check we used AWS comprehand service to analyse the content and get the sentiment of the content and check if the sentiment matches with the marketing keyword phrases
It then uses the SES connection and workmail to send the emails to the customers.
This sends the result file to the users mail address once it completes processing the file so that user can work on other products that are enrolled in this Tool.








