import os

'''
Plugin handler for the Earthworm export plugin.
'''
class SeedlinkPluginHandler:
  # Create defaults
  def __init__(self): pass

  def push(self, seedlink):
    # Check and set defaults
    try: hb_msg = seedlink.param('sources.ewexport_pasv.heartbeat.message')
    except:
        hb_msg = 'alive'
        seedlink.setParam('sources.ewexport_pasv.heartbeat.message', hb_msg)

    try: hb_rate = seedlink.param('sources.ewexport_pasv.heartbeat.rate')
    except:
        hb_rate = 120
        seedlink.setParam('sources.ewexport_pasv.heartbeat.rate', hb_rate)

    host = seedlink._get('sources.ewexport_pasv.address')
    port = seedlink._get('sources.ewexport_pasv.port')

    return host + ":" + port


  # Flush does nothing
  def flush(self, seedlink):
    pass
