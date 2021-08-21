from machine import Pin, Timer

led = Pin(25, Pin.OUT)
LED_STATE = True
timer = Timer()


def blink(timer) -> None:

    global led, LED_STATE
    LED_STATE = not LED_STATE
    led.value(LED_STATE)


timer.init(freq=2,
           mode=Timer.PERIODIC,
           callback=blink)
