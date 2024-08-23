from typing import List

from enums import Section

LATEX_TEMPLATE: str = r"""
\documentclass[a4paper, 11pt]{article}


\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}

\input{glyphtounicode}


\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.7in}
\addtolength{\evensidemargin}{-0.7in}
\addtolength{\textwidth}{1.32in}
\addtolength{\topmargin}{-0.75in}
\addtolength{\textheight}{1.35in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-8pt}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{black}\titlerule \vspace{0pt}]

% Ensure that generated pdf is machine readable/ATS parsable
\pdfgentounicode=1


\usepackage[lining]{sourcesanspro}
\usepackage[T1]{fontenc}

\newcommand{\resumeSubHeadingListStart}
{\begin{itemize}[leftmargin=0in, rightmargin=0in, label={}]}

\newcommand{\resumeSubHeadingListEnd}
{\end{itemize}}

\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

\newcommand{\resumeItem}[1]{
  \item\small{
    {#1} \vspace{-2pt}
  }
}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\begin{document}
!title

!section1
!section2
!section3
!section4
\end{document}
"""

RESUME_ITEM: str = r"""
\resumeItem{!item} \vspace{0pt}
"""

TITLE_SECTION: str = r"""
\begin{center}
    !full_name    
    !location
    !phone_number
    !email
    !linkedin
    !github
    !website
\end{center}
"""

EDUCATION_SECTION: str = r"""
\newcommand{\resumeSubheadingEducation}[4]{
    \item
    \begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textbf{\small{#2}} \\
        {#3} & {#4}
    \end{tabular*}\vspace{0pt}
}
\section{Education}
\resumeSubHeadingListStart
\vspace{-8pt}
!education_list
\resumeSubHeadingListEnd
"""

EDUCATION_TEMPLATE: str = r"""
\resumeSubheadingEducation{!degree}{!date}{!university}{!location}
\vspace{-4pt}
"""

EXPERIENCE_SECTION: str = r"""
\newcommand{\resumeSubheadingExperience}[4]{
    \item
    \begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1 $|$ #3} $|$ \small{#4} & \textbf{\small{#2}} 
    \end{tabular*}\vspace{-4pt}
}
\section{Experience}
\resumeSubHeadingListStart
\vspace{-8pt}
!experience_list
\resumeSubHeadingListEnd
"""

EXPERIENCE_TEMPLATE: str = r"""
\resumeSubheadingExperience{!title}{!date}{!company}{!location}
\resumeItemListStart
\vspace{-2pt}
!description
\resumeItemListEnd
"""

PROJECTS_SECTION: str = r"""
\newcommand{\resumeSubheadingProjects}[3]{
    \item
    \begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1}{ $|$ \footnotesize{#3}} & \textbf{\small{#2}} \\
    \end{tabular*}\vspace{-4pt}
}
\section{Projects}
\resumeSubHeadingListStart
\vspace{-8pt}
!projects_list
\resumeSubHeadingListEnd
"""

PROJECTS_TEMPLATE: str = r"""
\resumeSubheadingProjects{!title}{!date}{!tech_stack}
\resumeItemListStart
\vspace{-4pt}
!description
\resumeItemListEnd
"""

SKILLS_SECTION: str = r"""
\newcommand{\resumeSubheadingSkills}[2]{
    \textbf{#1:}{\small{\hspace{2mm}#2}}
}
\section{Technical Skills}
!skills_list
"""

SKILLS_TEMPLATE: str = r"""
\textbf{\small{!name:}} {\footnotesize{!value}}
"""

title_keys: List[str] = [
    "full_name",
    "location",
    "phone_number",
    "email",
    "linkedin_short_url",
    "linkedin_url",
    "github_short_url",
    "github_url",
    "website_short_url",
    "website_url",
]


def safe_latex_string(s: str) -> str:
    s = s.replace("&", r"\&")
    s = s.replace("%", r"\%")
    s = s.replace("$", r"\$")
    s = s.replace("#", r"\#")
    s = s.replace("_", r"\_")
    return s


def get_title_section(data) -> str:
    title = TITLE_SECTION
    for key in title_keys:
        if key in data:
            match key:
                case "full_name":
                    title = title.replace("!full_name", r"""\textbf{\LARGE \scshape """ + safe_latex_string(
                        data.get(key, "")) + r"""} \\ \vspace{4pt}""")
                case "location":
                    title = title.replace("!location", r"""\small {""" + safe_latex_string(data.get(key, "")) + r"""}""")
                case "phone_number":
                    title = title.replace("!phone_number", r"""$|$ \small\href{tel:""" + safe_latex_string(
                        data.get(key, "")) + r"""}{\raisebox{-0.1\height}\ \underline{\smash{""" + safe_latex_string(
                        data.get(key, "")) + r"""}}}""")
                case "email":
                    title = title.replace("!email", r"""$|$\small\href{mailto:""" + safe_latex_string(
                        data.get(key, "")) + r"""}{\underline{\smash{""" + safe_latex_string(
                        data.get(key, "")) + r"""}}}""")
        else:
            title = title.replace("!" + key, "")

    if "linkedin_url" in data and "linkedin_short_url" in data:
        title = title.replace("!linkedin",
                              r"""$|$\small\href{""" + safe_latex_string(
                                  data.get("linkedin_url",
                                           "")) + r"""}{\raisebox{-0.1\height}\ \underline{\smash{""" + safe_latex_string(
                                  data.get("linkedin_short_url", "")) + r"""}}}""")
    else:
        title = title.replace("!linkedin", "")

    if "github_url" in data and "github_short_url" in data:
        title = title.replace("!github",
                              r"""$|$\small\href{""" + safe_latex_string(
                                  data.get("github_url",
                                           "")) + r"""}{\raisebox{-0.1\height}\ \underline{\smash{""" + safe_latex_string(
                                  data.get("github_short_url", "")) + r"""}}}""")
    else:
        title = title.replace("!github", "")

    if "website_url" in data and "website_short_url" in data:
        title = title.replace("!website",
                              r"""$|$\small\href{""" + safe_latex_string(
                                  data.get("website_url",
                                           "")) + r"""}{\raisebox{-0.1\height}\ \underline{\smash{""" + safe_latex_string(
                                  data.get("website_short_url", "")) + r"""}}}""")
    else:
        title = title.replace("!website", "")
    return title


def get_education_section(data) -> str:
    education_section = EDUCATION_SECTION
    education_list = ""
    for education in data.get("education", []):
        education_list += EDUCATION_TEMPLATE
        for key in education:
            education_list = education_list.replace("!" + key, education.get(key, ""))

    if len(data.get("education", [])) == 0:
        education_section = education_section.replace("!education_list", r"""\item{}""")
    else:
        education_section = education_section.replace("!education_list", education_list)
    return education_section


def get_experience_section(data) -> str:
    experience_section = EXPERIENCE_SECTION
    experience_list = ""
    for experience in data.get("experience", []):
        experience_list += EXPERIENCE_TEMPLATE
        for k, v in experience.items():
            if k == "description":
                resume_item = ""
                for description in v:
                    resume_item += RESUME_ITEM
                    resume_item = resume_item.replace("!item", safe_latex_string(description))
                experience_list = experience_list.replace("!description", resume_item)

            else:
                experience_list = experience_list.replace("!" + k, v)

    if len(data.get("experience", [])) == 0:
        experience_section = experience_section.replace("!experience_list", r"""\item{}""")
    else:
        experience_section = experience_section.replace("!experience_list", experience_list)
    return experience_section


def get_projects_section(data) -> str:
    projects_section = PROJECTS_SECTION
    projects_list = ""
    for project in data.get("projects", []):
        projects_list += PROJECTS_TEMPLATE
        for k, v in project.items():
            if k == "description":
                resume_item = ""
                for description in v:
                    resume_item += RESUME_ITEM
                    resume_item = resume_item.replace("!item", safe_latex_string(description))
                projects_list = projects_list.replace("!description", resume_item)

            else:
                projects_list = projects_list.replace("!" + k, v)

    if len(data.get("projects", [])) == 0:
        projects_section = projects_section.replace("!projects_list", r"""\item{}""")
    else:
        projects_section = projects_section.replace("!projects_list", projects_list)
    return projects_section


def get_skills_section(data) -> str:
    skills_section = SKILLS_SECTION
    skills_list = ""
    for skill in data.get("skills", []):
        skills_list += SKILLS_TEMPLATE
        for k, v in skill.items():
            skills_list = skills_list.replace("!" + safe_latex_string(k), safe_latex_string(v))

    skills_section = skills_section.replace("!skills_list", skills_list)
    return skills_section


def get_section(data, section: Section) -> str:
    match section:
        case Section.EDUCATION:
            return get_education_section(data)
        case Section.EXPERIENCE:
            return get_experience_section(data)
        case Section.PROJECTS:
            return get_projects_section(data)
        case Section.SKILLS:
            return get_skills_section(data)
        case _:
            return ""
