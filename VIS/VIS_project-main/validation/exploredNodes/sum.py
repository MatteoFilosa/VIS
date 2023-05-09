sheet_5["A3"].value += count_mousemove_departure
sheet_5["B3"].value += count_mousemove_distance
sheet_5["C3"].value += count_mousemove_delay
sheet_5["D3"].value += count_mousemove_airtime
sheet_5["E3"].value += count_mousemove_arrival
sheet_5["F3"].value += count_mousemove_count
sheet_5["G3"].value += special_mousemove_count

sheet_5["A6"].value += count_mousedown_departure
sheet_5["B6"].value += count_mousedown_distance
sheet_5["C6"].value += count_mousedown_delay
sheet_5["D6"].value += count_mousedown_airtime
sheet_5["E6"].value += count_mousedown_arrival
sheet_5["F6"].value += count_mousedown_count

sheet_5["A10"].value += count_mousemove_brush_departure
sheet_5["B10"].value += count_mousemove_brush_distance
sheet_5["C10"].value += count_mousemove_brush_delay
sheet_5["D10"].value += count_mousemove_brush_airtime
sheet_5["E10"].value += count_mousemove_brush_arrival

sheet_5["A13"].value += count_mouseup_departure
sheet_5["B13"].value += count_mouseup_distance
sheet_5["C13"].value += count_mouseup_delay
sheet_5["D13"].value += count_mouseup_airtime
sheet_5["E13"].value += count_mouseup_arrival

sheet_5["A17"].value += count_click_departure
sheet_5["B17"].value += count_click_distance
sheet_5["C17"].value += count_click_delay
sheet_5["D17"].value += count_click_airtime
sheet_5["E17"].value += count_click_arrival
sheet_5["F17"].value += count_click_count
sheet_5["G17"].value += special_click_count

sheet_5["A21"].value += count_mouseout_departure
sheet_5["B21"].value += count_mouseout_distance
sheet_5["C21"].value += count_mouseout_delay
sheet_5["D21"].value += count_mouseout_airtime
sheet_5["E21"].value += count_mouseout_arrival
sheet_5["F21"].value += count_mouseout_count

sheet_5["A25"].value += special_mouseout_departure
sheet_5["B25"].value += special_mouseout_distance
sheet_5["C25"].value += special_mouseout_delay
sheet_5["D25"].value += special_mouseout_airtime
sheet_5["E25"].value += special_mouseout_arrival
sheet_5["F25"].value += special_mouseout_count

sheet_5["A29"].value += count_wheel_departure
sheet_5["B29"].value += count_wheel_distance
sheet_5["C29"].value += count_wheel_delay
sheet_5["D29"].value += count_wheel_airtime
sheet_5["E29"].value += count_wheel_arrival


sheet_5["A33"].value += special_wheel_departure
sheet_5["B33"].value += special_wheel_distance
sheet_5["C33"].value += special_wheel_delay
sheet_5["D33"].value += special_wheel_airtime
sheet_5["E33"].value += special_wheel_arrival

sheet_5["A37"].value += count_dblclick_departure
sheet_5["B37"].value += count_dblclick_distance
sheet_5["C37"].value += count_dblclick_delay
sheet_5["D37"].value += count_dblclick_airtime
sheet_5["E37"].value += count_dblclick_arrival
sheet_5["F37"].value += count_dblclick_count

wb_5.save(filename="count_path_5.xlsx")