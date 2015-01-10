import argparse
import random
import time
import math

from pythonosc import osc_message_builder
from pythonosc import udp_client

start_time = time.time()

def set_red_pulse():
  msg = osc_message_builder.OscMessageBuilder(address = "/dmx/universe/5000/7")
  v = time.time() - start_time
  v *= 30
  v /= 2*math.pi
  v = math.sin(v)
  v = math.fabs(v)
  msg.add_arg(v)
  msg = msg.build()
  client.send(msg)

def set_bulb_pulse():
   msg = osc_message_builder.OscMessageBuilder(address = "/dmx/universe/5000/15")
   v = time.time() - start_time
   v *= 100
   v /= 2*math.pi
   v = math.sin(v)
   v = math.fabs(v)
   msg.add_arg(v*0.25)
   msg = msg.build()
   client.send(msg)

def set_green_zero():
   msg = osc_message_builder.OscMessageBuilder(address = "/dmx/universe/5000/8")
   msg.add_arg(0)
   msg = msg.build()
   client.send(msg)

def set_blue_zero():
   msg = osc_message_builder.OscMessageBuilder(address = "/dmx/universe/5000/9")
   msg.add_arg(0)
   msg = msg.build()
   client.send(msg)

def send(receiver, v):
  msg = osc_message_builder.OscMessageBuilder(address = "/dmx/universe/5000/"+str(receiver))
  msg.add_arg(v)
  msg = msg.build()
  client.send(msg)

def set_bulb_noisy():
  base = 0.2
  factor = 0.1
  v = base
  v += (random.random()*factor)
  if random.random() > 0.99:
    v += 0.5
    send(1,v)
    time.sleep(0.15)
    send(1,0)
    send(2,v)
    time.sleep(0.15)
    send(2,0)
    send(3,v)
    time.sleep(0.15)
    send(3,0)
  else:
    send(1,v)
    v = base
    v += (random.random()*factor)
    time.sleep(0.01)
    send(2,v)
    v = base
    v += (random.random()*factor)
    time.sleep(0.01)
    send(3,v)




def set_neon():
  msg = osc_message_builder.OscMessageBuilder(address = "/dmx/universe/5000/4")
  v = 0
  flash = False
  if random.random() > 0.99:
    flash = True
    v+=0.8
  msg.add_arg(v)
  msg = msg.build()
  client.send(msg)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=7770,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.UDPClient(args.ip, args.port)

  start_time = time.time()

  while True:
    set_bulb_noisy()
    time.sleep(0.001)
    #set_neon()
    time.sleep(0.001)

    pass

