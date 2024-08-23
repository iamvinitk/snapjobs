import os
import uuid
from time import sleep

from enums import Section
from latex_template import LATEX_TEMPLATE, get_section, get_title_section
from utils import generate_tex_file, get_resume_number, tex2pdf
from typing import Dict


def generate_resume(data: Dict, ordering: Dict[Section, int]):
    # generate tmp folder if it does not exist
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    temp_file_id = str(uuid.uuid4())
    temp_file_name = f"{temp_file_id}.tex"

    print(str(id))
    print(ordering)
    template = LATEX_TEMPLATE.replace("!title", get_title_section(data))

    # iterate through ordering and replace the placeholders with the respective sections
    for section, order in ordering.items():
        template = template.replace(f"!section{order}", get_section(data, section))

    generate_tex_file(template, file_name=temp_file_name)
    tex2pdf(temp_file_name)
    #
    # OUTPUT_FOLDER = f"{COMPANY_NAME}/"
    # NAME = "Ayushi_Garg"
    # SKIP_NEW_FILE = True
    #
    # resume_number = get_resume_number(OUTPUT_FOLDER, SKIP_NEW_FILE)
    # # create a directory if it does not exist
    # if not os.path.exists(f"{OUTPUT_FOLDER}{resume_number}/"):
    #     os.makedirs(f"{OUTPUT_FOLDER}{resume_number}/")
    #
    # output_file = f"{OUTPUT_FOLDER}{resume_number}/{NAME}_Resume.pdf"
    #
    # os.rename("output.pdf", output_file)
    # delete all files in the tmp folder starting with the uuid
    for file in os.listdir("tmp"):
        print(file, file.startswith(str(temp_file_id)) and not file.endswith(".pdf"))
        if file.startswith(str(temp_file_id)) and not file.endswith(".pdf"):
            os.remove(f"tmp/{file}")

    return f"{temp_file_id}.pdf"


# generate_resume("output.tex", {"full_name": "Vinit Kanani"}, {
#     Section.EDUCATION: 2,
#     Section.EXPERIENCE: 1,
#     Section.PROJECTS: 3,
#     Section.SKILLS: 4
# })
