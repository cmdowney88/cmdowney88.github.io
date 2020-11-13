var cv = [
    {
        "type": "education",
        "title": "University of Washington",
        "city": "Seattle",
        "level": "PhD",
        "field": "Computational Linguistics",
        "gpa": 3.95,
        "start_date": "September 2018",
        "end_date": "present",
        "advisors": ["Gina-Anne Levow"]
    },
    {
        "type": "education",
        "title": "Tulane University",
        "city": "New Orleans",
        "level": "BS",
        "field": "Linguistics and Russian",
        "gpa": 3.99,
        "start_date": "August 2014",
        "end_date": "May 2018",
        "advisors": ["Charles Mignot", "Judith Maxwell"]
    },
    {
        "type": "research_position",
        "title": "University of Washington FLAS Fellowship",
        "position": "Fellow",
        "description": "Foreign Language and Area Studies funded fellowship to study Inuktitut",
        "start_date": "September 2019",
        "end_date": "June 2020",
        "supervisors": ["Nadine Fabbi"]
    },
    {
        "type": "research_position",
        "title": "Low Resource Languages for Emergent Incidents (LORELEI)",
        "position": "Research Assistant",
        "description": "DARPA project for rapid machine translation of low-resource languages",
        "start_date": "August 2019",
        "end_date": "October 2019",
        "supervisors": ["Gina-Anne Levow"]
    },
    {
        "type": "research_position",
        "title": "Newberry Research Library Summer Institute",
        "position": "Fellow",
        "description": "Research on digital methods for language revitalization as well as ethics in Indigenous linguistics",
        "start_date": "July 2019",
        "end_date": "August 2019",
        "supervisors": ["Jenny Davis"]
    },
    {
        "type": "employment",
        "title": "University of Washington: Department of Linguistics",
        "position": "Teaching/Research Assistant",
        "start_date": "September 2018",
        "end_date": "present",
        "supervisors": ["Richard Wright"]
    },
    {
        "type": "employment",
        "title": "Apple: Siri Web Answers",
        "position": "AI|ML Intern",
        "start_date": "June 2020",
        "end_date": "September 2020",
        "supervisors": ["Chris DuBois"]
    },
    {
        "type": "invited_talk",
        "title": "Subword Segmentation for Morphologically Complex Languages",
        "event": "UW NLP Retreat",
        "location": "Lake Chelan, Washington",
        "date": "September 28 2019"
    },
    {
        "type": "invited_talk",
        "title": "Dependency vs Phrase-Structure Trees",
        "event": "UW Linguistics Syntax Roundtable",
        "location": "Seattle, Washington",
        "date": "October 4 2019"
    },
    {
        "type": "invited_talk",
        "title": "Archival Work and Language Revitalization at the NCAIS Summer Institute",
        "event": "UW Linguistics Field Reports",
        "location": "Seattle, Washington",
        "date": "December 13 2019"
    },
    {
        "type": "teaching",
        "title": "LING 566: Introduction to Syntax for Computational Linguistics",
        "position": "Teaching Assistant",
        "year": "2020",
        "term": "Fall",
        "supervisors": ["Emily M. Bender"]
    },
    {
        "type": "teaching",
        "title": "LING 200: Introduction to Linguistic Thought",
        "position": "Teaching Assistant",
        "year": "2019",
        "term": "Spring",
        "supervisors": ["Richard Wright"]
    },
    {
        "type": "teaching",
        "title": "LING 200: Introduction to Linguistic Thought",
        "position": "Teaching Assistant",
        "year": "2018",
        "term": "Fall",
        "supervisors": ["Laura McGarrity"]
    },
    {
        "type": "teaching",
        "title": "LING 406: Introduction to Syntax",
        "position": "Grader",
        "year": "2018",
        "term": "Fall",
        "supervisors": ["Kirby Conrod"]
    },
    {
        "type": "teaching",
        "title": "ASL 305: Introduction to American Deaf Culture",
        "position": "Grader",
        "year": "2019",
        "term": "Spring",
        "supervisors": ["Lance Forshay"]
    },
    {
        "type": "guest_lecture",
        "title": "Computational Linguistics and Language Revitalization",
        "date": "January 27 2020",
        "course": "ENGL 4717 (NAIS Capstone Seminar)",
        "school": "University of Colorado at Boulder",
        "instructor": "Penelope Kelsey"
    },
    {
        "type": "guest_lecture",
        "title": "Computational Linguistics and Language Revitalization",
        "date": "May 4 2020",
        "course": "LING 234 (Langauge and Diversity)",
        "school": "University of Washington",
        "instructor": "Lorna Rozelle"
    }
]

var people = [
    {
        "name": "Nadine Fabbi",
        "site": "https://jsis.washington.edu/canada/people/nadine-fabbi",
    },
    {
        "name": "Gina-Anne Levow",
        "site": "https://linguistics.washington.edu/people/gina-anne-levow"
    },
    {
        "name": "Jenny Davis",
        "site": "https://ais.illinois.edu/directory/profile/loksi"
    },
    {
        "name": "Richard Wright",
        "site": "https://linguistics.washington.edu/people/richard-wright"
    },
    {
        "name": "Lance Forshay",
        "site": "https://linguistics.washington.edu/people/lance-forshay"
    },
    {
        "name": "Fei Xia",
        "site": "https://linguistics.washington.edu/people/fei-xia"
    },
    {
        "name": "Laura McGarrity",
        "site": "https://linguistics.washington.edu/people/laura-mcgarrity"
    },
    {
        "name": "Kirby Conrod",
        "site": "https://kconrod.herokuapp.com"
    },
    {
        "name": "Chris DuBois",
        "site": "http://chrisdubois.org"
    },
    {
        "name": "Emily M. Bender",
        "site": "https://linguistics.washington.edu/people/emily-m-bender"
    }
]

const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

const terms = ["Winter", "Spring", "Summer", "Fall"]

function getEndYear(item) {
    if ("end_date" in item) {
        date = item.end_date
    }
    else {
        date = item.date
    }
    return parseInt(date.split(" ").slice(-1)[0])
}

function getEndMonth(item) {
    if ("end_date" in item) {
        date = item.end_date
    }
    else {
        date = item.date
    }
    return months.indexOf(date.split(" ")[0])
}

function getEndDay(item) {
    if ("end_date" in item) {
        date = item.end_date
    }
    else {
        date = item.date
    }
    return parseInt(date.split(" ")[1])
}

function getYear(item) {
    return parseInt(item.year)
}

function compareDates(a, b) {
    if (a.end_date === "present") return -1;
    else if (b.end_date === "present") return 1;
    else if (getEndYear(a) > getEndYear(b)) return -1;
    else if (getEndYear(a) < getEndYear(b)) return 1;
    else if (getEndMonth(a) > getEndMonth(b)) return -1;
    else if (getEndMonth(a) < getEndMonth(b)) return 1;
    else if (getEndDay(a) > getEndDay(b)) return -1;
    else if (getEndDay(a) < getEndDay(b)) return 1;
    else return -1;
}

function compareTerms(a, b) {
    if (getYear(a) > getYear(b)) return -1;
    else if (getYear(a) < getYear(b)) return 1;
    else return terms.indexOf(b.term) - terms.indexOf(a.term)
}

function findPerson(name) {
    link = ""
    for (y=0; y<people.length; y++) {
        if (people[y].name == name) {
            link = people[y].site
        }
    }
    return link
}

function educationSecondary(item) {
    text = item.level + " " + item.field + ", GPA " + item.gpa + ": Advised by "
    text_node = document.createTextNode(text)
    secondary_node = document.createElement("p")
    //secondary_node.className = "cv_subtitle"
    secondary_node.appendChild(text_node)
    advisors = item.advisors
    for (x=0; x<advisors.length; x++) {
        advisor = advisors[x]
        advisor_node = document.createTextNode(advisors[x])
        advisor_link = findPerson(advisor)
        if (advisor_link != "") {
            link_node = document.createElement("a")
            link_node.href = advisor_link
            link_node.appendChild(advisor_node)
            secondary_node.appendChild(link_node)
        }
        else {
            secondary_node.appendChild(advisor_node)
        }
        if (x < (advisors.length-1)) {
            secondary_node.append(", ")
        }
    }
    return secondary_node
}

function positionSecondary(item) {
    text = item.position + ": Supervised by "
    text_node = document.createTextNode(text)
    secondary_node = document.createElement("p")
    //secondary_node.className = "cv_subtitle"
    secondary_node.appendChild(text_node)
    supervisors = item.supervisors
    for (x=0; x<supervisors.length; x++) {
        supervisor = supervisors[x]
        supervisor_node = document.createTextNode(supervisors[x])
        supervisor_link = findPerson(supervisor)
        if (supervisor_link != "") {
            link_node = document.createElement("a")
            link_node.href = supervisor_link
            link_node.appendChild(supervisor_node)
            secondary_node.appendChild(link_node)
        }
        else {
            secondary_node.appendChild(supervisor_node)
        }
        if (x < (supervisors.length-1)) {
            secondary_node.append(", ")
        }
    }
    return secondary_node
}

function talkSecondary(item) {
    text = item.event + ": " + item.location
    text_node = document.createTextNode(text)
    secondary_node = document.createElement("p")
    //secondary_node.className = "cv_subtitle"
    secondary_node.appendChild(text_node)
    supervisors = item.supervisors
    return secondary_node
}

function lectureSecondary(item) {
    text = "as part of " + item.course + ", " + item.school + ": Instructed by "
    text_node = document.createTextNode(text)
    secondary_node = document.createElement("p")
    //secondary_node.className = "cv_subtitle"
    secondary_node.appendChild(text_node)
    instructor_node = document.createTextNode(item.instructor)
    instructor_link = findPerson(item.instructor)
    if (instructor_link != "") {
        link_node = document.createElement("a")
        link_node.href = instructor_link
        link_node.appendChild(instructor_node)
        secondary_node.appendChild(link_node)
    }
    else {
        secondary_node.appendChild(instructor_node)
    }
    return secondary_node
}

function createSection(items, secondaries, section_id) {
    section_ul = document.getElementById(section_id)
    for (x=0; x<items.length; x++) {
        item = items[x]

        title = document.createTextNode(item.title)
        title_node = document.createElement("h5")
        //title_node.className = "cv_title"
        title_node.appendChild(title)

        if ("start_date" in item && "end_date" in item) {
            dates = document.createTextNode(item.start_date + " - " + item.end_date)
        }
        else if ("date" in item) {
            dates = document.createTextNode(item.date)
        }
        else if ("year" in item) {
            if ("term" in item) {
                dates = document.createTextNode(item.term + " " + item.year)
            }
            else {
                dates = document.createTextNode(item.year)
            }
        }
        else {
            dates = document.createTextNode("n/a")
        }
        date_node = document.createElement("em")
        date_node.className = "float-right"
        date_node.appendChild(dates)

        primary_node = document.createElement("div")
        primary_node.appendChild(title_node)
        primary_node.appendChild(date_node)

        secondary_node = secondaries[x]

        section_li = document.createElement("li")
        section_li.appendChild(primary_node)
        section_li.appendChild(secondary_node)

        section_ul.appendChild(section_li)
    }
}

education = []
research_positions = []
publications = []
teaching = []
employment = []
talks = []
lectures = []

for (i=0; i<cv.length; i++) {
    item = cv[i]
    switch (item.type) {
        case "education":
            education.push(item)
            break
        case "research_position":
            research_positions.push(item)
            break
        case "publication":
            publications.push(item)
            break
        case "teaching":
            teaching.push(item)
            break
        case "employment":
            employment.push(item)
            break
        case "invited_talk":
            talks.push(item)
            break
        case "guest_lecture":
            lectures.push(item)
            break
    }
}

//education_secondaries = []
//for (i=0; i<education.length; i++) {
//    education_secondaries.push(educationSecondary(education[i]))
//}
//createSection(education, education_secondaries, "education")

research_positions.sort(compareDates)
research_secondaries = []
for (i=0; i<research_positions.length; i++) {
    research_secondaries.push(positionSecondary(research_positions[i]))
}
createSection(research_positions, research_secondaries, "research_ul")

employment.sort(compareDates)
employment_secondaries = []
for (i=0; i<employment.length; i++) {
    employment_secondaries.push(positionSecondary(employment[i]))
}
createSection(employment, employment_secondaries, "employment_ul")

talks.sort(compareDates)
talks_secondaries = []
for (i=0; i<talks.length; i++) {
    talks_secondaries.push(talkSecondary(talks[i]))
}
createSection(talks, talks_secondaries, "talks_ul")

teaching.sort(compareTerms)
teaching_secondaries = []
for (i=0; i<teaching.length; i++) {
    teaching_secondaries.push(positionSecondary(teaching[i]))
}
createSection(teaching, teaching_secondaries, "teaching_ul")

lectures.sort(compareDates)
lectures_secondaries = []
for (i=0; i<lectures.length; i++) {
    lectures_secondaries.push(lectureSecondary(lectures[i]))
}
createSection(lectures, lectures_secondaries, "lectures_ul")
