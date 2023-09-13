import pandas as pd
import DCaseMonitor as dcaseCom
import time

# CSVファイルを読み込む
df = pd.read_csv("resources/esmini-sim/full_log.csv")

# dcaseID = "9symYSQ_kDSS4hyR_QE4IQrBu6k2pSP2facoSqedXe8_"
# partsID = "Parts_n4punhpj"
dcaseID = "_gHvlTSHMSJMHenDsYhWsMVqMQU8yJ5DZqe9LQTHR8g_"
partsID = "Parts_8kdmb3ha"
url = "https://www.matsulab.org/dcase/editor.html?dcaseID=_gHvlTSHMSJMHenDsYhWsMVqMQU8yJ5DZqe9LQTHR8g_"


dcase = dcaseCom.DCaseMonitor(dcaseID, partsID, sslIgnore=True)
for i in range(10):
    n = random.randint(120, 130)
    result = False
    if n >= 124:
        result = True
    data = [{"Key": "単位数", "Value": n}, {"Key": "卒業", "Value": result}]
    ret = dcase.uploadNodeState(
        partsID, state=True, detail="卒業シミュレーター", kind=dcase.Evidence
    )
    apiPartsID = ret["partsID"]
    ret = dcase.uploadData(data, partsID=apiPartsID)
    ret = dcase.uploadBolderStyle(partsID=apiPartsID, color="#00FF00", thick=5)
    time.sleep(2)
ret = dcase.uploadBolderStyle(partsID=apiPartsID, color="#0000AA", thick=1)
