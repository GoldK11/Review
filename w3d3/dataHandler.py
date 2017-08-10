from normalDist import *
import openpyxl


class dataHandler:
    evaluator = NormD()

# 엑셀 데이터 가져오기
    @classmethod
    def getData(cls,filename):
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        dic = {}
        g = ws.rows
        for name, score in g:
            dic[name.value]=score.value
        return dic

# 변수 초기화
    def __init__(self,filename,clsname):
        self.rawdata = dataHandler.getData(filename)
        self.clsname = clsname
        self.cache = {}


#점수 가져오기, 연산 ( 평균, 분산, 표준편차)
    def get_score(self):
        if 'scores' not in self.cache:
            scores = list(self.rawdata.values())
            self.cache['scores']=scores
        return self.cache['scores']

    def get_avrg(self):
        if 'avrg' not in self.cache:
            self.cache['avrg'] = self.evaluator.avrg(self.get_score())
        return self.cache['avrg']

    def get_var(self):
        if 'var' not in self.cache:
            self.cache['var'] = self.evaluator.var(self.get_avrg(),self.get_score())
        return self.cache['var']

    def get_std_dev(self):
        if 'stdev' not in self.cache:
            self.cache['stdev'] = self.evaluator.std_dev(self.get_var())
        return self.cache['stdev']


# 학생평가 (최고점수, 최하점수)

    def low(self):
        if 'low' not in self.cache:
            self.cache['low'] = self.rawdata[self.wholow()]
        return self.cache['low']
        
        
    def high(self):
        if 'high' not in self.cache:
            self.cache['high'] = self.rawdata[self.whohigh()]
        return self.cache['high']
    
    def whohigh(self):
        if 'whohigh' not in self.cache:
            whohigh = reduce ( lambda a,b :
                            a if self.rawdata.get(a)>self.rawdata.get(b)
                            else b,
                            self.rawdata.keys())
            self.cache['whohigh'] = whohigh
        return self.cache['whohigh']    
    
    def wholow(self):
        if 'wholow' not in self.cache:
            wholow = reduce ( lambda a,b :
                            b if self.rawdata.get(a)>self.rawdata.get(b)
                            else a,
                            self.rawdata.keys())
            self.cache['wholow'] = wholow
        return self.cache['wholow']   


#  반 평가 
    def __str__(self):
        return '{} : {}'.format(self.rawdata,self.clsname)


    def GetEvaluation(self, total_avrg):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print(
        "{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".format(
            self.clsname,
            self.get_avrg(),
            self.get_var(),
            self.get_std_dev()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass(total_avrg)

    def evaluateClass(self, total_avrg):
        avrg = self.get_avrg()
        std_dev = self.get_std_dev()
        
        if avrg <total_avrg and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > total_avrg and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < total_avrg and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > total_avrg and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
            






    


    
                  
    
