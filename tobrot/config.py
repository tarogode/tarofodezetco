from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "1345947891:AAG43FPuOCwrv2c89oJhXVbJGoJhL678slw"
    APP_ID = 2105857
    API_HASH = "c8aacc9417551dc98e2b2f61fbfb8387"
    OWNER_ID = 1480779663
    AUTH_CHANNEL = [-1001396933879]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\n
client_id = 510098154856-2e1hp85tcoh7e37ubufepmqmn76holti.apps.googleusercontent.com\n
client_secret = x9x47NGfJlkQfVtZP9uQ_v6k
scope = drive\n
token = {"access_token":"ya29.a0AfH6SMCA97PSbVnmQGcDS_JhHXcOw0CySDGxjzZyWjmrgWHDf9A1n-Rmdg4sVnUDxV9Y5_5tAdbhfpW6_xbF1O9ALAeBj1xmKFQtMubDyGfYB_i1LltJA_e_zJawP-peIK4yzoYrZTvdfP02U2PHfqHiV6WmX5RCUPmXOqHlMG4","token_type":"Bearer","refresh_token":"1//0guQVZQz65RjnCgYIARAAGBASNwF-L9IrWy7b2vaAF3Qyh-UjCszb0xVSG83KYCi4X9taiSfr_9EhDO13oqWNTuoVGris4xENImo","expiry":"2020-12-03T13:41:27.382397538Z"}\n
team_drive = 0AGXuqNLwr3ISUk9PVA"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
