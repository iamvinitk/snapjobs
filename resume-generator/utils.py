import os


def generate_tex_file(template, file_name="output.tex"):
    """
    This function generates a .tex file from the template.
    """
    with open("./tmp/" + file_name, "w") as f:
        f.write(template)


def tex2pdf(tex_file):
    """
    This function takes a .tex file as input and returns a .pdf file as output using the pdflatex command.
    """
    status = os.system(f"pdflatex -output-directory tmp {tex_file} -interaction=batchmode")

    if status != 0:
        raise Exception("Error occurred while generating the PDF file.")
    return tex_file[:-4] + ".pdf"


def get_resume_number(output_folder, skip_new_file=True):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # check if there are any files in the folder
    if os.listdir(output_folder):
        # get all folders in the output folder
        folders = os.listdir(output_folder)
        # The folders names are in the format "1", "2", etc.
        # find th the highest number and increment it by 1
        folders = list(filter(lambda x: x.isdigit(), folders))
        if not folders:
            resume_number = 1
        else:
            numbers = [int(folder) for folder in folders]
            resume_number = max(numbers) + 1
            if skip_new_file:
                resume_number -= 1

    else:
        resume_number = 1

    return resume_number
