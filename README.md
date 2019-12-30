# resume_parser
The point of this project is to make a working resume parser that can crawl through resumes and extract important information.

This parser should be able to
1. Pull out a list of skills of the applicant
2. Pull out previous employment and the start and quit times of thos opportunities
3. Pull out education and years of education
4. Make a guess of where the applicant lives (geo coordinates)
5. guess personality traits of applicant

Steps to achieve these objectives will be
1. import resume in any pdf or doc format and convert to text
2. Find education this will just be a dictionary containing
	name of college
	state
	degree type
	years at school
	GPA
	list of achievements or awards
3. previous employment
	list of previous employment contataining a dictionary of
		job title
		job type
		time at job
		time between thsi job and previous job
		state
		(verify company exists with website fancy but would be cool)
4. SKill sof applicant
	Get a list of skills that the applicant knows
5. Personality traits
	based on papers or something link personality traits to resume

