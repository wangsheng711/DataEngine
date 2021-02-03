#课程作业3 对汽车质量数据进行统计

import pandas as pd
import numpy as np

carBrandProDType = np.dtype({'names': ['brand', 'typenum', 'pronum', 'ave'],
                                 'formats': ['U32', 'i', 'i', 'f']})
carModelProDType = np.dtype({'names': ['model', 'pronum'],
                                 'formats': ['U32', 'i']})
carBrandPro = []
carModelPro = []
carData = pd.read_csv("C:\Users\IMBAQ\Downloads\homework\L1\car_data_analyze/car_complain.csv")
carDataTmp = carData.set_index(['brand', 'car_model'])['problem'].str.rstrip(',').str.split(',', expand=True).stack().reset_index(-1, drop=True).reset_index(name="problem")
carBrand = carDataTmp.groupby('brand')

for brandName, brandData in carBrand:
    brandProNum = 0
    modelNum = 0
    carBrandModel = brandData.groupby('car_model')
    for modelName, modelData in carBrandModel:
        modeProNum = len(modelData)
        brandProNum += modeProNum
        modelNum += 1
        carModelPro.append((modelName, modeProNum))
    carBrandPro.append((brandName, modelNum, brandProNum, 0.))
carBrandProCal = np.array(carBrandPro, dtype=carBrandProDType)
carModelProCal = np.array(carModelPro, dtype=carModelProDType)
carBrandProCal['ave'] = np.divide(carBrandProCal['pronum'], carBrandProCal['typenum'])
print("品牌投诉总数：")
sortIdx = carBrandProCal['pronum'].argsort()
for idx in sortIdx:
    print(carBrandProCal[idx]['brand'], ': ', carBrandProCal[idx]['pronum'])
print("\n车型投诉总数：")
sortIdx = carModelProCal['pronum'].argsort()
for idx in sortIdx:
    print(carModelProCal[idx]['model'], ': ', carModelProCal[idx]['pronum'])
print("\n平均车型投诉数量：")
sortIdx = carBrandProCal['ave'].argsort()
for idx in sortIdx:
    print(carBrandProCal[idx]['brand'], ': ', carBrandProCal[idx]['ave'])
print(carBrandProCal[sortIdx[-1]]['brand'], ': ', carBrandProCal[sortIdx[-1]]['ave'])








