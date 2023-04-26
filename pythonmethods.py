class time:
    def _init_(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

time_1 = time(5, 32, 00)
time_2 = time(23, 11, 11)
print(time_1)
print(time_2)
