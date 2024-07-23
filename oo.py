# a='이음효율'
# b='적용 안전율'
# c='모드 계수'
# wight1=중량물 무게
# weight2=양중함 무게
# weight3=줄걸이 용구 무게
class Safety :
    def __init__(self,weight1,weight2,weight3, num_slings, sling_type, sling_method):
        self.weight1=weight1
        self.weight2=weight2
        self.weight3=weight3
        self.num_slings=num_slings
        self.sling_type=sling_type
        self.sling_method=sling_method
    def a(self):
        if self.slings_type=='chain':
            a=100
            b=5
        elif self.slings_type=='wire_rope':
            a=75
            b=5
        elif self.slings_type=='nylon_sling':
            a=100
            b=1
    def b(self):
        if self.sling_method=='1자걸이':
            c=1
        elif self.sling_method=='초크 걸이':
            c=0.8
        elif self.sling_method=='U자형 걸이':
            c=2
    def f(self):
        weight=self.weight1+self.weight2+self.weight3
        if weight<15:
            print('작업 가능')
        else:
            print('작업 불가능')
