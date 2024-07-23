# a='이음효율'
# b='적용 안전율'
# c='모드 계수'
# wight1=중량물 무게
# weight2=양중함 무게
# weight3=줄걸이 용구 무게
class Safety :
    def __init__(self,weight1,weight2,weight3, num_slings, sling_type, sling_method):
        self.weight1=weight1#중량물 무게
        self.weight2=weight2#양중함 무게
        self.weight3=weight3#줄걸이 용구 무게
        self.num_slings=num_slings#줄걸이 수
        self.sling_type=sling_type#줄걸이 종류
        self.sling_method=sling_method#줄걸이 방법
        safety_factor=1.5#안전 계수
    def type(self):
        if self.slings_type=='chain':
            a=100#이음효율
            b=5#적용 안전율
        elif self.slings_type=='wire_rope':
            a=75
            b=5
        elif self.slings_type=='nylon_sling':
            a=100
            b=1
        if self.sling_method=='1자걸이':
            c=1
        elif self.sling_method=='초크 걸이':
            c=0.8
        elif self.sling_method=='U자형 걸이':
            c=2
        weight = self.weight1 + self.weight2 + self.weight3

    def print(self):
        weight = self.weight1 + self.weight2 + self.weight3
        if weight<100:
            print('총 양중 무게:',weight,'작업 가능 여부: 가능')
        elif weight>=100:
            print('총 양중 무게:', weight, '작업 가능 여부: 불가능')

weight1=int(input('중량물 무게를 입력하세요:'))
weight2=int(input('양중함 무게를 입력하세요.'))
weight3=int(input('줄걸이 용구 무게를 입력하세요.'))
num=int(input('줄걸이 수를 입력하세요.'))
type1=input('줄걸이 종류를 입력하세요:')
method=input('줄걸이 방법을 입력하세요:')
my_info=Safety(weight1,weight2,weight3,num,type1,method)
my_info.print()

    # def f(self):
    #     safety_factor=1.5
    #     weight=self.weight1+self.weight2+self.weight3
    #     required_sling_capacity = (weight * safety_factor)
    #     required_shackle_capacity = required_sling_capacity

