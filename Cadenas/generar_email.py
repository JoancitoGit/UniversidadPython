# Variables
nombre = 'Joan Manuel Alexander García Cedano'
empresa = 'Sistema Estatal de Seguridad Pública'
dominio = 'com.mx'

# Generar Email
email = nombre[:4] +'.'+ nombre[22:28] + '@' + empresa[0:1] + empresa[8:9] + empresa[19:20] + empresa[29:30] + '.' + dominio
print(email.lower())