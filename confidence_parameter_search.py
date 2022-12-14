import itertools

import numpy as np
import xgboost as xgb
class confidence_auc_search():
    def __init__(self,feature,label):
        self.DTrain = xgb.DMatrix(feature,label)
    def grid_search(self,num_boost_round,**param):
        DTrain=self.DTrain
        dic=param
        #用于记录参数组合和分数以及达到最高的boost次数
        res_para=[]
        res_score=[]
        res_maxboost=[]
        #找到所有可能的参数组合
        l_value=[i for i in dic.values()]
        l_values=[]
        for i in itertools.product(*l_value):
            l_values.append([j for j in i])
        #需要计算多少次
        totle_counts=len(l_values)
        l_keys=[i for i in dic.keys()]
        counter=1
        print("一共需要计算{}组参数".format(totle_counts))
        print("全部搜寻完需要建模计算{}次".format(totle_counts*10*5))
        for i in range(len(l_values)):
            param=dict(zip(l_keys,l_values[i]))
            #准备5次随机确保可信
            score_ini=[]
            boost_ini=[]
            for j in range(5):
                res=xgb.cv(param,DTrain,metrics=["auc"],num_boost_round=num_boost_round,nfold=10\
                           ,shuffle=True,seed=np.random.choice(np.arange(1,1000,1)))
                score_ini.append(res["test-auc-mean"].max())
                boost_ini.append(res["test-auc-mean"].argmax())
            #记录这一组参数结果
            res_para.append(param)
            res_score.append(sum(score_ini)/len(score_ini))
            res_maxboost.append(sum(boost_ini)/len(boost_ini))
            print("搜寻进程：{}/{}".format(counter,totle_counts))
            counter+=1
        max_index=res_score.index(max(res_score))
        return (res_para[max_index],res_score[max_index],res_maxboost[max_index])

class auc_search():
    def __init__(self,feature,label):
        self.DTrain = xgb.DMatrix(feature,label)
    def grid_search(self,num_boost_round,**param):
        DTrain=self.DTrain
        dic=param
        #用于记录参数组合和分数以及达到最高的boost次数
        res_para=[]
        res_score=[]
        res_maxboost=[]
        #找到所有可能的参数组合
        l_value=[i for i in dic.values()]
        l_values=[]
        for i in itertools.product(*l_value):
            l_values.append([j for j in i])
        l_keys=[i for i in dic.keys()]
        # 需要计算多少次
        totle_counts = len(l_values)
        counter = 1
        print("一共需要计算{}组参数".format(totle_counts))
        print("全部搜寻完需要建模计算{}次".format(totle_counts * 10 * 5))
        for i in range(len(l_values)):
            param=dict(zip(l_keys,l_values[i]))
            print(param)
            res=xgb.cv(param,DTrain,metrics=["auc"],num_boost_round=num_boost_round,nfold=10)
            #记录这一组参数结果
            res_para.append(param)
            res_score.append(res["test-auc-mean"].max())
            res_maxboost.append(res["test-auc-mean"].argmax())
            print("搜寻进程：{}/{}".format(counter, totle_counts))
            counter += 1
        max_index=res_score.index(max(res_score))
        return (res_para[max_index],res_score[max_index],res_maxboost[max_index])

