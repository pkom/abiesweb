# -*- coding: utf-8 -*- 

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
#########################################################################

if request.env.web2py_runtime_gae:            # if running on Google App Engine
    db = DAL('gae')                           # connect to Google BigTable
    session.connect(request, response, db = db) # and store sessions and tickets there
    ### or use the following lines to store sessions in Memcache
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
else:                                         # else use a normal relational database
    import MySQLdb
    from gluon.dal import MySQLAdapter
    MySQLAdapter.adapter = MySQLdb

    db = DAL('mysql://abies:abies@web/abies',pool_size=10)       # if not, use SQLite or other DB
## if no need for session
#session.forget()

#########################################################################
## Here is sample code if you need for 
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import *
mail = Mail()                                  # mailer
#auth = Auth(globals(),db)                      # authentication/authorization
crud = Crud(globals(),db)                      # for CRUD helpers using auth
service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()

mail.settings.server = 'smtp.gmail.com:587'  # your SMTP server
#mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'francisco.mora.sanchez@gmail.com'         # your email
mail.settings.login = 'francisco.mora.sanchez:danielmora'      # your credentials or None

#auth.settings.hmac_key = 'sha512:58b98219-4430-458b-8fcd-7083707423c3'   # before define_tables()
#auth.define_tables()                           # creates all needed tables
#auth.settings.mailer = mail                    # for user email verification
#auth.settings.registration_requires_verification = False
#auth.settings.registration_requires_approval = False
#auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s to verify your email'
#auth.settings.reset_password_requires_verification = True
#auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL(r=request,c='default',f='user',args=['reset_password'])+'/%(key)s to reset your password'

#########################################################################
## If you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, uncomment and customize following
# from gluon.contrib.login_methods.rpx_account import RPXAccount
# auth.settings.actions_disabled=['register','change_password','request_reset_password']
# auth.settings.login_form = RPXAccount(request, api_key='...',domain='...',
#    url = "http://localhost:8000/%s/default/user/login" % request.application)
## other login methods are in gluon/contrib/login_methods
#########################################################################

crud.settings.auth = None                      # =auth to enforce authorization on crud

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
db.define_table("TiposFondo",
      Field("IdTipoFondo", "id"),
      Field("TipoFondo"),
      migrate=False)
      
db.define_table("Paises",
      Field("IdPais", "id"),
      Field("Pais"),
      migrate=False)      

db.define_table("Lenguas",
      Field("IdLengua", "id"),
      Field("Lengua"),
      migrate=False)      
     
db.define_table("Autores",
      Field("IdAutor", "id"),
      Field("a"),
      Field("b"),
      Field("c"),
      Field("d"),
      Field("e"),
      Field("n"),
      migrate=False)       

db.define_table("Editoriales",
      Field("IdEditorial", "id"),
      Field("Editorial"),
      migrate=False)

db.define_table("TiposEjemplar",
      Field("IdTipoEjemplar", "id"),
      Field("TipoEjemplar"),
      migrate=False)
      
db.define_table("Ubicaciones",
      Field("IdUbicacion", "id"),
      Field("Ubicacion"),
      migrate=False)         
      
db.define_table("Fondos_Autores",
      Field("IdFondo"),
      Field("IdAutor"),
      primarykey=["IdFondo", "IdAutor"],
      migrate=False)             
      
db.define_table("Fondos",
      Field("IdFondo", "id"),
      Field("IdTipoFondo"),
      Field("IdAutor"),      
      Field("IdEditorial"),
      Field("IdLenguaInfo"),
      Field("IdPaisInfo"),     
      Field("Fecha1Info"),
      Field("Fecha2Info"),
      Field("DepositoLegal"),
      Field("ISBN"),
      Field("ISBN2"),
      Field("Titulo"),
      Field("Subtitulo"),
      Field("RestoPortada"),
      Field("Edicion"),
      Field("LugarEdicion"),
      Field("AnoEdicion"),
      Field("Extension"),
      Field("CaracteristicasFisicas"),
      Field("Dimensiones"),
      Field("Serie"),
      Field("NumeroSerie"),
      Field("Notas"),
      migrate=False)
      
db.define_table("Ejemplares",
      Field("IdEjemplar", "id"),
      Field("IdTipoEjemplar", db.TiposEjemplar),
      Field("IdFondo", db.Fondos),
      Field("CodigoEjemplar"),
      Field("ISBN"),
      Field("IdUbicacion", db.Ubicaciones),
      Field("NumRegistro"),
      Field("FechaAlta", "datetime"),
      Field("Importe"),
      Field("Moneda"),
      Field("Notas"),
      Field("Sig1"),
      Field("Sig2"),
      Field("Sig3"),
      Field("Prestado"),
      migrate=False)
