
class Time():
    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new, m_new, s_new)

        return result

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new, m_new, s_new)

        return result

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.second -= 1

    def second_to_time(self, s2):
        if 60 < self.second < 3600:
            h_new = 0
            m_new = self.second // 60
            s_new = self.second % 60

            output = Time(h_new, m_new, s_new)

            return output

        elif self.second > 3600:
            h_new = self.second // 3600
            self.second -= 3600
            m_new = self.second // 60
            s_new = self.second % 60
            output = Time(h_new, m_new, s_new)

            return output

        if 60 < s2.second < 3600:
            h_new1 = 0
            m_new1 = s2.second // 60
            s_new1 = s2.second % 60
            output1 = Time(h_new1, m_new1, s_new1)

            return output1

        elif s2.second > 3600:
            h_new1 = s2.second // 3600
            self.second -= 3600
            m_new1 = s2.second // 60
            s_new1 = s2.second % 60
            output1 = Time(h_new1, m_new1, s_new1)

            return output1

    def time_to_second(self, s2):
        s = self.hour * 3600
        s_new = self.second + s
        s = self.minute * 60
        s_new = self.second + s
        output = Time(0, 0, s_new)

        return output

    def gmt_tehran(self, s2):
        tehran_time = Time(3, 30, 00)
        result = self.sum(tehran_time)

        return result


t1 = Time(3, 46, 27)
t2 = Time(7, 19, 51)
s1 = Time(0, 0, 1200)
s2 = Time(0, 0, 3700)

t3 = t1.sum(t2)
t3.show()

t4 = t1.sub(t2)
t4.show()

t5 = s1.second_to_time(s2)
t5.show()

t6 = t1.time_to_second(t2)
t6.show()

t7 = t1.gmt_tehran(t2)
t7.show()
