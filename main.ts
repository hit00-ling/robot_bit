let strip = robotbit.rgb()
strip.setBrightness(32)
strip.showRainbow(1, 300)
basic.forever(function () {
    robotbit.Servo(robotbit.Servos.S1, 90)
    robotbit.Servo(robotbit.Servos.S2, 90)
    robotbit.Servo(robotbit.Servos.S3, 90)
    robotbit.Servo(robotbit.Servos.S4, 90)
})
