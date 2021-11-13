from mininet.topo import SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import OVSController
from mininet.cli import CLI
import time

def singletest():

  topo = SingleSwitchTopo(k=6)
  
  net = Mininet(topo=topo, controller=OVSController,cleanup = True)
 
  net.start()
  net.pingAll()
  
  h1 = net.get('h1')
  h2 = net.get('h2')
  h3 = net.get('h3')
  h4 = net.get('h4')
  h5 = net.get('h5')
  h6 = net.get('h6')
  
  h1.cmdPrint('sudo python3 server_fork_mininet.py &')
  time.sleep(10)
  h2.cmdPrint('sudo python3 client_fork_mininet.py ')
  h3.cmdPrint('sudo python3 client_fork_mininet.py ')
  h4.cmdPrint('sudo python3 client_fork_mininet.py ')
  h5.cmdPrint('sudo python3 client_fork_mininet.py ')
  h6.cmdPrint('sudo python3 client_fork_mininet.py ')
  
  CLI(net)
  net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    singletest()
