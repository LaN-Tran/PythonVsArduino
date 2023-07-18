# -*- coding: utf-8 -*-
import pyfirmata
import time

# Connect to the board
board = pyfirmata.Arduino('COM11')

#Start an infinite loop to read inputs of the Arduino
it = pyfirmata.util.Iterator(board)
it.start()

#Set variables correspond the board inputs/outputs
analog_input_left_right = board.analog[1]
analog_input_left_right.enable_reporting()

analog_input_up_down = board.analog[0]
analog_input_up_down.enable_reporting()



while True:
    # read-in the value of the joy stick:

    left_right_value = analog_input_left_right.read()
    
    if left_right_value is not None:
        print('left-right value: ', left_right_value * 5)
        #print('left-right value type: ', type(left_right_value))
        #print('integer type: ', type(6))
        #board.digital[13].write(1)
        time.sleep(1)
        #board.digital[13].write(0)
        #time.sleep(left_right_value+ 1)
    
    up_down_value = analog_input_up_down.read()
   
    if up_down_value is not None:
        print('up_down_value: ', up_down_value * 5)
        #board.digital[13].write(1)
        time.sleep(1)
        #board.digital[13].write(0)
        #time.sleep(up_down_value+ 1)
    
    
