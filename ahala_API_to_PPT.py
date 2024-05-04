# Importing the necessary libraries
import json
import requests
from pptx import Presentation
from pptx.util import Inches, Pt
import pptx.util

def get_sheroes_ppt(abcd_id_list):

    # Getting the API and using json
    for id_number in abcd_id_list:
        response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={id_number}', headers={"User-Agent": "XY"})
        json_response = json.loads(response.text)

        # print(type(json_response))
        # print(json_response)
        desc = json_response['data']['description']
        dyk = json_response['data']['did_you_know']
        name = json_response['data']['name']
        text = 'Description: ' + desc + 'Did You Know: ' + dyk
        # print(text)
        # print('\n', total_text)
        # print(type(total_text))

        prs = Presentation()
        Layout = prs.slide_layouts[3]
        prs.slide_width = pptx.util.Inches(11)
        prs.slide_height = pptx.util.Inches(9)
        slide = prs.slides.add_slide(Layout)
        # slide = prs.slides[-1]

        # Build the Text Box
        slide.shapes.title.text = name
        slide.shapes.title.text_frame.paragraphs[0].font.size = Pt(40)
        slide.placeholders[1].text = text

        slide.placeholders[1].text_frame.paragraphs[0].font.size = Pt(13)
        slide.placeholders[1].text_frame.paragraphs[1].font.size = Pt(13)
        slide.placeholders[1].text_frame.paragraphs[2].font.size = Pt(13)
        slide.placeholders[1].text_frame.paragraphs[3].font.size = Pt(13)
        slide.placeholders[1].text_frame.paragraphs[4].font.size = Pt(13)
        # first_slide.placeholders[1].text_frame.paragraphs[5].font.size = Pt(13)
        # first_slide.placeholders[1].text_frame.paragraphs[6].font.size = Pt(13)
        # first_slide.placeholders[1].text_frame.paragraphs[5].font.size = Pt(13)
        # first_slide.placeholders[1].text_frame.paragraphs[6].font.size = Pt(13)
        # first_slide.placeholders[1].text_frame.paragraphs[7].font.size = Pt(13)

        img_path = 'C:/Users/ugant/OneDrive/Desktop/Python102/aishwarya manivannan.png'
        left_inch = Inches(5.00)
        top_inch = Inches(1.75)
        width_inch = Inches(5.5)
        height_inch = Inches(6.25)

        slide.shapes.add_picture(str(img_path), left_inch, top_inch, width_inch, height_inch)

# Saving the ppt
    # first_slide = first_slide+1
    prs.save("First_presentation.pptx")
    print("done")

# Calling the function

id_list = [733, 711]
get_sheroes_ppt(id_list)