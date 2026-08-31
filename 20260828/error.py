온도 = [71.2, 68.5, 75.9, 80.1, 66.3, 72.4, 69.8, 95.6, 70.0, 73.1, 68.9, 71.5]


class sensor:
    def __init__(self, name, list):
        self.name = name
        self.list = list
        self.sum = 0
        self.ls = []

    def avgs(self):
        for i in self.list:
            self.ls.append(i)
            self.sum += i
        i_avg = round((self.sum / len(self.list)), 2)
        return i_avg

    def show(self):
        print(f"{self.name} 센서 / 측정 {len(self.ls)}회 / 평균 {self.avgs()}")


info = sensor("범용", 온도)
print(info.name, info.avgs())
info.show()
print()

print("문제 10. 상속")


class temp_sensor(sensor):
    def __init__(self, name, list, limit=90):
        super().__init__(name, list)
        self.limit = limit
        self.wrong_ls = []

    def wrong(self):
        for i in self.list:
            if i > self.limit:
                self.wrong_ls.append(i)
        return self.wrong_ls

    def wrong_cnt(self):
        print(f"{len(self.wrong())} {self.limit}")


ts = temp_sensor("온도", 온도)
ts.show()
ts.wrong_cnt()
print()

print("문제 11. 오버라이딩")


class vib_sensor(sensor):
    def __init__(self, name, list, limit=35):
        super().__init__(name, list)
        self.limit = limit

    def show(self):
        print(f"[진동] {self.name} / 평균 {self.avgs()} / 한계 {self.limit}")


vs = vib_sensor("진동", [30.1, 31.4, 41.2, 29.8])
vs.show()


def avgs(self):
    total = 0

    for value in self.list:
        total += value

    return round(total / len(self.list), 2)
