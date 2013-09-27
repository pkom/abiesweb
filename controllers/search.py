# coding: utf8
# intente algo como
def index(): return dict(message="Página principal de búsquedas")

def bytitle():
    response.flash = T('Searching by title...')
    #if not session.titulo:
    #    session.titulo = ''
    #if request.vars.keyword:
    #    session.titulo = request.vars.keyword  
    return dict(form=FORM(INPUT(_id='keyword', _name='keyword', _onkeyup="ajax('busca_titulos', ['keyword'], 'target');")), target_div=DIV(_id='target'))

def busca_titulos(): 
    if len(request.vars.keyword) < 4:
        return ""
    pattern = '%' + request.vars.keyword.lower() + '%'
    query = (db.Fondos.IdFondo == db.Ejemplares.IdFondo) & (db.Fondos.Titulo.lower().like(pattern))  
    fondos = db(query).select(orderby=db.Fondos.Titulo)
    items = [A(row.Fondos.Titulo, _href=URL('show_fondo', args=row.Fondos.IdFondo)) for row in fondos]
    #if not session.titulos:
    #    session.titulos = UL(*items).xml()
    return UL(*items).xml()
    #return session.titulos

def bytitle1():
    response.flash = T('Searching by title...')
    form = FORM(INPUT(_name='titulo', requires = IS_NOT_EMPTY(T('Enter a value'))), INPUT(_type='submit'))
    fondos = ''
    if form.accepts(request.vars, keepvalues = True):
        session.titulo = form.vars.titulo
        patron_titulo = '%'+form.vars.titulo.lower()+'%'
        query = (db.Fondos.IdFondo == db.Ejemplares.IdFondo) & (db.Fondos.Titulo.lower().like(patron_titulo))
        fondos = db(query).select(orderby=db.Fondos.Titulo)
    return dict(form = form, fondos = fondos)

def bytitle2():
    session.flash = T('Searching by title...')
    form = FORM(INPUT(_name='titulo', requires = IS_NOT_EMPTY(T('Enter a value'))), INPUT(_type='submit'))
    if form.accepts(request.vars, session, keepvalues = True):
        session.flash = T('Búsqueda realizada')
        redirect(URL(r = request, f = 'bytitle1'))
    else:
        response.flash = T('Hay errores')        
    #patron_titulo = '%'+form.vars.titulo.lower()+'%'      
    #query = (db.Fondos.IdFondo == db.Ejemplares.IdFondo) & (db.Fondos.Titulo.lower().like(patron_titulo))
    query = (db.Fondos.IdFondo == db.Ejemplares.IdFondo)
    fondos = db(query).select(orderby=db.Fondos.Titulo)
    return dict(form = form, fondos = fondos)


def show_fondo():
    this_fondo = db.Fondos(request.args(0)) or redirect(URL('index'))
    editorial = db(db.Editoriales.IdEditorial==this_fondo.IdEditorial).select().first()
    tipofondo = db(db.TiposFondo.IdTipoFondo==this_fondo.IdTipoFondo).select().first()
    fondoautores = db(db.Fondos_Autores.IdFondo==this_fondo.IdFondo).select()
    nautores = []
    for fondoautor in fondoautores:
        nautores += db(db.Autores.IdAutor==fondoautor.IdAutor).select(db.Autores.a,db.Autores.IdAutor)
    fondoejemplares = db(db.Ejemplares.IdFondo==this_fondo.IdFondo).select()
    #procesemos para cada ejemplar el tipo del ejemplar y sus ubicaciones
    ubicacionestipos = {}
    for ejemplar in fondoejemplares:
        tipoejemplar = db(db.TiposEjemplar.IdTipoEjemplar==ejemplar.IdTipoEjemplar).select().first()
        ubicacion = db(db.Ubicaciones.IdUbicacion==ejemplar.IdUbicacion).select().first()
        ubicacionestipos[ejemplar.IdEjemplar] = [ tipoejemplar.TipoEjemplar if tipoejemplar != None else "", ubicacion.Ubicacion if ubicacion != None else "" ]
       
    return dict(fondo=this_fondo, ejemplares=fondoejemplares, autores=nautores, editorial=editorial, tipofondo=tipofondo, ubicacionestipos=ubicacionestipos)

def byauthor(): 
    response.flash = T('Searching by author...')
    return dict(form=FORM(INPUT(_id='keyword', _name='keyword', _onkeyup="ajax('busca_autores', ['keyword'], 'target');")), target_div=DIV(_id='target'))
    
def busca_autores():
    if len(request.vars.keyword) < 4:
        return ""
    pattern = '%' + request.vars.keyword.lower() + '%'
    autores = db(db.Autores.a.lower().like(pattern)).select(orderby=db.Autores.a)
    items = [A(row.a, _href=URL('show_autor_fondos', args=row.IdAutor)) for row in autores]
    return UL(*items).xml()    

def show_autor_fondos():
    this_autor = db.Autores(request.args(0)) or redirect(URL('index'))
    #fondosautor = db(db.Fondos_Autores.IdAutor==this_autor.id).select()
    #fondos = []
    #for fondo in fondosautor:
    #    fondos += db(db.Fondos.IdFondo==fondo.IdFondo).select(db.Fondos.IdFondo, db.Fondos.Titulo, orderby=db.Fondos.Titulo)
    fondosautor = db((db.Fondos_Autores.IdAutor==this_autor.IdAutor) & (db.Fondos_Autores.IdFondo==db.Fondos.IdFondo)).select(db.Fondos.IdFondo, db.Fondos.Titulo, orderby=db.Fondos.Titulo)
    return dict(autor=this_autor, fondos=fondosautor)

def bypublisher():
    response.flash = T('Searching by publisher...')
    return dict(form=FORM(INPUT(_id='keyword', _name='keyword', _onkeyup="ajax('busca_editoriales', ['keyword'], 'target');")), target_div=DIV(_id='target'))

def busca_editoriales():
    pattern = '%' + request.vars.keyword.lower() + '%'
    editoriales = db(db.Editoriales.Editorial.lower().like(pattern)).select(orderby=db.Editoriales.Editorial)
    items = [A(row.Editorial, _href=URL('show_editorial_fondos', args=row.IdEditorial)) for row in editoriales]
    return UL(*items).xml()

def show_editorial_fondos():
    this_editorial = db.Editoriales(request.args(0)) or redirect(URL('index'))
    fondoseditorial = db(db.Fondos.IdEditorial==this_editorial.IdEditorial).select(orderby=db.Fondos.Titulo)
    return dict(editorial=this_editorial, fondos=fondoseditorial)
