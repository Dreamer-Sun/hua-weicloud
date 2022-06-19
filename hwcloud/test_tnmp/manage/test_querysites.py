import threading

from tnmp.manage.querysites import *


if __name__ == '__main__':
    # QuerySites()
    # QueryMapSites()
    QuerySitesdData()
    # QueryResultByQuerySitesdData()
    ############################
    # test = ['测试', '是个列表']
    # testdict = {'test': test}
    # print(testdict.get('test')[0])
    ############################
    # try:
    #     t1 = threading.Thread(target=QuerySitesdData)
    #     t2 = threading.Thread(target=QueryResultByQuerySitesdData)
    #     t1.start()
    #     t2.start()
    #
    #
    # except:
    #     print("无法启动线程")
#

