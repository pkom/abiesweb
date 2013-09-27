# coding: utf8
# intente algo como
def sendsuggestions():  
    form = SQLFORM.factory(
             Field('correo', requires=IS_EMAIL(error_message=T('Invalid email'))),
             Field('texto', 'text', requires=IS_NOT_EMPTY(error_message=T('Introduce algún dato'))))
    if form.accepts(request.vars, session):
        session.correo = form.vars.correo
        session.texto =form.vars.texto
        if mail.send('afernandez@edu.juntaextremadura.net',
            'Sugerencia biblioteca',
            'Enviado por '+request.vars.correo+' desde '+request.env.remote_addr+' a las '+request.now.ctime()+' '+request.vars.texto):
            response.flash = T('Message is sent...')
        else:
            response.flash = T('Trouble sending message...')                       
    elif form.errors:
        response.flash = T('Form has errors...')
    else:
        session.ip = request.env.remote_addr
        session.hora = request.now.ctime()
        response.flash = T('Please fill the form')
    return dict(form=form)
