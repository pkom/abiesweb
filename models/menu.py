# -*- coding: utf-8 -*- 

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = request.application
response.subtitle = T('Library of I.E.S. Maestro Juan Calero')
response.meta.author = 'Francisco Mora Sánchez'
response.meta.description = T('Consultations library foldings')
response.meta.keywords = 'biblioteca ies enseñanza secundaria maestro juan calero'

##########################################
## this is the main application menu
## add/remove items as required
##########################################

response.menu = [
    (T('Start'), False, URL(request.application,'default','index'), [])
    ]

response.menu+=[
    (T('Search books'), False, URL(request.application,'search','bytitle'),
     [
            (T('By Title'), False, URL(request.application, 'search', 'bytitle')), 
            (T('By Author'), False, URL(request.application, 'search', 'byauthor')),
            (T('By Publisher'), False, URL(request.application, 'search', 'bypublisher')),
            ]
   ),
  ]
  
response.menu+=[
    (T('Send suggestions'), False, URL(request.application,'suggestions','sendsuggestions'), [])
  ]

response.menu+=[
    (T('Terms of use'), False, URL(request.application,'use','showtermofuse'), [])
  ]
