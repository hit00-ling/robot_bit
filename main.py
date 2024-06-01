strip = robotbit.rgb()
strip.set_brightness(32)
strip.show_rainbow(1, 300)

def on_forever():
    basic.show_number(0)
    basic.pause(1000)
basic.forever(on_forever)
