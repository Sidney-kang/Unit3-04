# Created by : Sidney Kang
# Created on : 13 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-04
# This program determines whether a given year is a leap year

import ui

def check_leap_year_touch_up_inside(sender):
    # This checks whether the inputed year is a leap year
    
    # input
    year_entered = int(view['user_input_textbox'].text)

    # process
    if year_entered % 4 != 0:
       # output
       view['check_if_leap_year_label'].text = "It is not a leap year."
    elif year_entered % 4 == 0 and year_entered % 100 != 0:
       # output
       view['check_if_leap_year_label'].text = "It is a leap year."
    elif year_entered % 4 == 0 and year_entered % 100 == 0:
    # output
       view['check_if_leap_year_label'].text = "It is a leap year."

view = ui.load_view()
view.present('sheet')
