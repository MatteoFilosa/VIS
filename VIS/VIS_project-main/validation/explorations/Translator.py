import json
with open('evaluation_result.txt', 'r') as file:

    data = file.read()
    """ data = data.replace('"{"doesPathStart":"YES_chiudi_virgola_apri",','],[{')
    data = data.replace(',"doesPathEnd":"YES_chiudi_virgola"}",','}],[')
    data = data.replace('"{', '{')
    data = data.replace('}",', '},')
    data = data.replace(':', ': ')
    data = data.replace(',]', ']')
    
    
    data = data.replace('"coord_y":', "")
    data = data.replace('},"leadsToState"', '],"leadsToState"')
    
    data = data.replace('{"doesPathStart": "YES_apri",', '[{')
    data = data.replace(' ["start_brush_x":', '[[[')
    data = data.replace('"start_brush_y":', '')
    data = data.replace('}{"end_brush_x":','],[')
    data = data.replace('"end_brush_y":', '')
    data = data.replace('}chiudi_brush",', ']]],')
    data = data.replace(']]],"leadsToState": 0}],[', ']]]},')
    data = data.replace('"Prossima system question",' , '],[') """


    
    data = data.replace('"info": {"direction":', '"info": [')
    data = data.replace('"letter":', '[')
    data = data.replace('"x":', '')
    data = data.replace('"y": "', '')
    data = data.replace('"direction": ', '')
    data = data.replace('"Mquadra_aperta",', '"M",[')
    data = data.replace('quadra_chiusa"', ']]')
    data = data.replace('"start_brush_x":', '')
    data = data.replace('\\', '')
    data = data.replace('{"coord_x":', '[') 
    data = data.replace('"coord_y":', '') 
    data = data.replace('}, "leadsToState": 0}', ']}')
    data = data.replace('"{"start_brush_x":', '[[[')
    data = data.replace('null', '' )
    data = data.replace('"start_brush_y":', '')
    data = data.replace('}{"end_brush_x":','],[')
    data = data.replace('"end_brush_y":', '')
    data = data.replace('}chiudi_brush"', ']]]')
    data = data.replace('"Restore"', '],[')
    data = data.replace('"Back"', '],[')
    data = data.replace('"Prossima system question"', '],[')
    data = data.replace('{"pan_extent_x":', 'PAN,[[')
    data = data.replace('"pan_extent_y":', '')
    data = data.replace('"clicked_x":', '')
    data = data.replace('"clicked_y":', '')
    data = data.replace('"", null,' , '')
    data = data.replace('"pan_info":', '')
    data = data.replace(', ],[,', '],[' )
    data = data.replace('null', '' )
    data = data.replace('}, "info": [[[', ',0,0],[[0,0],[0,0]]] "info": [[[')
    data = data.replace('}, "info": [', ',0,0],[[0,0],[0,0]]] "info": [[[')
    data = data.replace('}}', ']}')
    data = data.replace('"",', '')
    data = data.replace(',  ,', ',')

    ####normal log###
    data = data.replace('"coord_x":', "")
    data = data.replace('"info": {', '"info": [')
    data = data.replace('"double!?!",', '')

    #data = data.replace('Pan on the brush performed in departure', 'Template per pan: ,[[-100,-100,205,105,0,0],[[0,0],[0,0]]]')
    
    #"info": "{\"start_brush_x\":376,\"start_brush_y\":50}{\"end_brush_x\":662,\"end_brush_y\":3
    

  
with open('exploration_falcon_7M.json', 'w') as file:
    file.write(data)

    
    ###########
    