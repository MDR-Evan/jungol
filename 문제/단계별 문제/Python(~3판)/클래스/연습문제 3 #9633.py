class Score:
    kor, eng = 0, 0

    def __init__(self, data):
        self.data = data

    def cal(self):
        for i in range(len(self.data)):
            Score.kor += int(self.data[i][1])
            Score.eng += int(self.data[i][2])

    def out_info(self):
        for i in range(len(self.data)):
            print(*self.data[i])
        print("합계 %d %d" % (Score.kor, Score.eng))

data = []
for i in range(2):
    data.append(input().split())

score = Score(data)
score.cal()
score.out_info()