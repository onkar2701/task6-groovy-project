# task6-groovy-project
Jenkins is an amazing tool for DevOps that allows us to execute clean and consistent builds. But creating the jobs within Jenkins to do this work can be labor intensive, manually updating those jobs is often error-prone, and tracking changes to those jobs is tedious at best.

Here is a solution for the same. This issue can be resolved with help of Jenkin’s Job DSL Plugin.

Lets's start our journey!

First of all, we need to create container image that has pre-installed jenkins. Whenever we launch this docker image, it will automatically start the jenkins server as well as kubernetes services.

Please refer the following article for the same.


For creating jobs automatically in jenkins, we need to install plugin called job DSL plugin.

No alt text provided for this image
Create a seed job which will generate jobs automatically. This job will pull the Github repo automatically when some developers push repo to Github.

No alt text provided for this image
No alt text provided for this image
No alt text provided for this image
For the jenkins file code go through the following Github Link:


Whenever developer commits code the seed job built using poll scm. It will fetch DSL script from the github and execute the DSL script. This script will generate 3 jobs as well as pipeline view for this jobs automatically.

No alt text provided for this image
Seed Job Output:

No alt text provided for this image
Job 1:

No alt text provided for this image
No alt text provided for this image
The first job created by DSL script is triggered by the seed job and will create a local if its not already created and copy web code from github to this folder.

Groovy Job 1 - Output:

No alt text provided for this image
Job 2:

No alt text provided for this image
This job will trigger whenever previous first job created by groovy build successfully. By looking at the code or program file, Jenkins will automatically start the respective language interpreter installed image container to deploy code on the top of Kubernetes. As well as the pod is exposed so that testing team can test the website and work accordingly.

Groovy Job 2 - Output:

No alt text provided for this image


Job 3:

No alt text provided for this image
This code is checked by the testing team.if app is not working , then send email to developer with error messages and redeploy the application after code is being edited by the developer.

failure_mail.py

import smtplib
sender_email = 'mail_id'
receiver = 'mail_id'
password = 'Gmail Password'
message = "The Website is not running properly."
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,receiver,message)
print("Email has been sent to ", receiver)
Job 3 - Output:

No alt text provided for this image
CPipeline Output:

No alt text provided for this image
Thus the CI-CD Pipeline on the top of kubernetes with the help of Jenkins File Approach done successfully!!
