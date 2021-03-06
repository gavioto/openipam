from openipam.utilities.perms import Perms

# SSL
ssl_enabled = True
ssl_cert = None
ssl_key = None

# NETWORK BINDINGS
bind_port = 8443        # Port the frontend will listen on
bind_host = '0.0.0.0'   # Address the frontend will bind to

# WEBSERVICE
# The host and port settings of the backend webservice
xmlrpc_ssl_enabled = False
xmlrpc_port = 8080
xmlrpc_host = '127.0.0.1'

# WEB STATIC FILES (CSS, JavaScript, images, etc.)
static_dir='/usr/local/openipam/openIPAM/openipam/web'
styles_dir = None
scripts_dir = None
images_dir = None

# SESSIONS
session_storage = "file"
session_dir = "/var/lib/openipam/sessions/web"
session_timeout = 60

# PROXY SETTINGS
proxied = False # Are requests coming through a proxy?
proxy_base = None
proxy_client_ip_header = None

# Placed underneath the header on the My Access tab ... good for describing your procedures for obtaining more access
my_access_text = "<p>If you need additional access, please contact your local network administrator.</p>"
email_required_html = "<p>Your user does not have an email address set, please contact your local network administrator.</p>"

# LOGGING
log_dir = "/var/log/openipam/web"
log_access = None
log_error = None
log_stdout = None
log_stderr = None

# GROUPS
# Permissions selected by default when adding users to groups 
# FIXME: make this 'ADD' instead of permission bits, and rename this to be more intuitive
db_default_group_permissions = '00000010'

enable_gul = False

default_dns_records_limit = 100

# NOTICE: Defaults that can be overridden should go above this line
from openipam_config.frontend import *

if not styles_dir: styles_dir = "%s/styles" % static_dir
if not scripts_dir: scripts_dir = "%s/scripts" % static_dir
if not images_dir: images_dir = "%s/images" % static_dir

if not log_access: log_access = "%s/access" % log_dir
if not log_error: log_error = "%s/error" % log_dir
if not log_stdout: log_stdout = "%s/stdout" % log_dir
if not log_stderr: log_stderr = "%s/stderr" % log_dir

# FIXME: these should come from the backend
allow_dynamic_ip = True
db_service_group_id = 3

# FIXME: make this come from the DB
class PermObj( object ):
	pass
perms = PermObj()
perms.ADD=Perms('00000010')
perms.READ=Perms('00000100')
perms.DELETE=Perms('00001000')
perms.ADMIN=Perms('00000001')
perms.MODIFY=Perms('00001110')
perms.OWNER=Perms('00001111')
perms.DEITY=Perms('11111111')

