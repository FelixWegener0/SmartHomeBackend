import my_time as my_time


def info(message):
    f = open("/home/pi/project/SmartHomeBackend/log.txt", "a")
    f.write(my_time.getCurrentTime() + "    " + message + "\n")
    f.close()
