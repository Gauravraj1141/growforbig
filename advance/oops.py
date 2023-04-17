class McaNew:
    def __init__(self,name,enroll_number,course_title,course_code,date):
        self.name = name
        self.enroll_number = enroll_number
        self.course_title = course_title
        self.course_code = course_code
        self.date = date

    def get_submit_receipt(self):
        return f"Thank You! {self.name} for submitting your Assignment . \n submission date : {self.date}" \
               f" \n your enrollment number is successfully" \
               f" update for your course {self.course_title} and course code is {self.course_code}"


mohan = McaNew('Mohan',23565656,'mca_new','mca-211','22/04/2023')
receipt = mohan.get_submit_receipt()
print(receipt)
print(mohan.course_code)