from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    500coin=math.Object(
        PARENT=networks.nets['500coin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='a41b235688585852'.decode('hex'),
        PREFIX='5623b62133665258'.decode('hex'),
        P2P_PORT=1121,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=1122,
        BOOTSTRAP_ADDRS='p2poolcoin.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-fhc',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade 500coin to >= 0.8.0.2!' if v < 80002 else None,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
