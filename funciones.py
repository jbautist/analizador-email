import db_connection as sql


def comprobar_email(email):
    '''Verifica que el email sea válido.

    Args:
        email (str): email a verificar.

    Returns:
        bool: False si en "email" no se encuentran los caracteres "@" y ".".
    '''    
    if '@' not in email or '.' not in email: return False


#Devuelve el resultado de la consulta de la base de datos si esta dío un resultado, sino, devuelve "None".
almacenar_entidad = lambda resultado_consulta : resultado_consulta[0][0] if bool(resultado_consulta) == True else None


def analizar_email(email):
    '''1) Descompone las diferentes partes de la dirección de email.
    2) Verifica cómo está compuesto el dominio.
    3) Muestra sus partes y su significado.

    Args:
        email (str): email a analizar.
    '''    
    usuario, dominio = email.split('@')
    partes_dominio = dominio.split('.')
    host = partes_dominio[0]
    gTLD = ccTLD = None

    if len(partes_dominio) == 3:
        gTLD = '.' + partes_dominio[1]
        gTLD_entity = sql.dql('top_level_domains.db', f'SELECT entity FROM gTLDs WHERE name = "{gTLD}";')
        ccTLD = '.' + partes_dominio[2]
        ccTLD_entity = sql.dql('top_level_domains.db', f'SELECT entity FROM ccTLDs WHERE name = "{ccTLD}";')
    elif len(partes_dominio[1]) >= 3:
        gTLD = '.' + partes_dominio[1]
        gTLD_entity = sql.dql('top_level_domains.db', f'SELECT entity FROM gTLDs WHERE name = "{gTLD}";')
    else:
        ccTLD = '.' + partes_dominio[1]
        ccTLD_entity = sql.dql('top_level_domains.db', f'SELECT entity FROM ccTLDs WHERE name = "{ccTLD}";')

    if gTLD != None and ccTLD != None:
        gTLD_entity = almacenar_entidad(gTLD_entity)
        ccTLD_entity = almacenar_entidad(ccTLD_entity)

        print(f'''EMAIL: {email}

        USUARIO: {usuario}
        DOMINIO: {dominio}
        HOST: {host}
        DOMINIO DE NIVEL SUPERIOR GENÉRICO: {gTLD} ({gTLD_entity})
        DOMINIO DE NIVEL SUPERIOR GEOGRÁFICO: {ccTLD} ({ccTLD_entity})
        ''')
    elif gTLD != None and ccTLD == None:
        gTLD_entity = almacenar_entidad(gTLD_entity)

        print(f'''EMAIL: {email}

        USUARIO: {usuario}
        DOMINIO: {dominio}
        HOST: {host}
        DOMINIO DE NIVEL SUPERIOR GENÉRICO: {gTLD} ({gTLD_entity})
        ''')
    else:
        ccTLD_entity = almacenar_entidad(ccTLD_entity)

        print(f'''EMAIL: {email}
        
        USUARIO: {usuario}
        DOMINIO: {dominio}
        HOST: {host}
        DOMINIO DE NIVEL SUPERIOR GEOGRÁFICO: {ccTLD} ({ccTLD_entity})
        ''')