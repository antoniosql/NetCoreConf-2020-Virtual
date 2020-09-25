class BaseConfig(object):
    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    # RFM PowerBI
    WORKSPACE_ID = '8f61e6bb-a5ea-4f27-b804-b8d68c3b60ae'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '445048c7-0211-443b-b65e-9abfbec06e46'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '35069d74-1489-4194-80c7-3a81385ead5b'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'cd86bd27-a7bf-488d-911d-fd76f3029643'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'D-G.Mv8A8~4Itiqw665~OpalNoS8N-Z~PY'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    #POWER_BI_USER = 'asoto@solidq.com'
    
    # Master user email password. Required only for MasterUser authentication mode.
    #POWER_BI_PASS = ''