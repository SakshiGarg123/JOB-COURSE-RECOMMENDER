# JOB-COURSE-RECOMMENDER
The training and placement cell of NSUT allows each student sitting for placements to submit their resume on the portal. We take a resume as input and suggest suitable jobs to student in which they would be interested in applying candidature for, based on their skills.

**Input:** Resume as pdf files

**Output:** Job Recommendations

**Training Dataset:** Naukri.com

# Running the code
1) **Extracting data from naukri.com:** Run main_naukri.py to extract the recent jobs posted on the website. The extracted data is stored in example.log (It already contains some extracted jobs so you can skip this step if you want)
2) **Resume:** Save the resume in the pdf format in the code directory and name it resume.pdf
3) **Recommend Jobs:** Run read_logfile.py to generate job recommendations
