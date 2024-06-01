strip = robotbit.rgb()
strip.set_brightness(32)
strip.show_rainbow(1, 300)

def on_forever():
    robotbit.servo(robotbit.Servos.S1, 90)
    robotbit.servo(robotbit.Servos.S2, 90)
    robotbit.servo(robotbit.Servos.S3, 90)
    robotbit.servo(robotbit.Servos.S4, 90)
basic.forever(on_forever)
