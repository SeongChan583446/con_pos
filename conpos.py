import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작1
rowNum = 0
#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝1

class POS(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #메인 메뉴
        self.adminSalesButton = QPushButton('매출관리',self)
        self.adminSalesButton.move(0,0)
        self.adminSalesButton.resize(270,40)
        self.adminSalesButton.clicked.connect(self.clickAdminSalesButton)

        self.adminInventoryButton = QPushButton('재고관리',self)
        self.adminInventoryButton.move(270,0)
        self.adminInventoryButton.resize(270,40)
        self.adminInventoryButton.clicked.connect(self.clickAdminInventoryButton)

        self.calcuButton = QPushButton('계산',self)
        self.calcuButton.move(540,0)
        self.calcuButton.resize(270,40)
        self.calcuButton.clicked.connect(self.clickCalcuButton)

        self.adminEmpButton = QPushButton('직원관리',self)
        self.adminEmpButton.move(810,0)
        self.adminEmpButton.resize(270,40)
        self.adminEmpButton.clicked.connect(self.clickAdminEmpButton)

        #매출관리 레이아웃
        self.salesInfoButton = QPushButton('매출 정보',self)
        self.salesInfoButton.move(0,60)
        self.salesInfoButton.resize(540,40)
        self.salesInfoButton.clicked.connect(self.clickSalesInfoButton)
        self.salesInfoButton.hide()

        self.salesRecordButton = QPushButton('판매 기록',self)
        self.salesRecordButton.move(540,60)
        self.salesRecordButton.resize(540,40)
        self.salesRecordButton.clicked.connect(self.clickSalesRecordButton)
        self.salesRecordButton.hide()

            #매출 정보
        self.daySalesInfoButton = QPushButton('일일매출정보',self)
        self.daySalesInfoButton.move(0,120)
        self.daySalesInfoButton.resize(240,40)
        self.daySalesInfoButton.clicked.connect(self.clickDaySalesInfoButton)
        self.daySalesInfoButton.hide()

        self.monthSalesInfoButton = QPushButton('월별매출정보',self)
        self.monthSalesInfoButton.move(0,160)
        self.monthSalesInfoButton.resize(240,40)
        self.monthSalesInfoButton.clicked.connect(self.clcikMonthSalesInfoButton)
        self.monthSalesInfoButton.hide()

                #일일 매출 정보
        self.daySalesInfoTable = QTableWidget(self)
        self.daySalesInfoTable.resize(840, 580)
        self.daySalesInfoTable.move(240, 120)

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작2
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select sdate, total_price from sale order by sdate asc;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = 0
        dtimeInfo = ["1999년 1월 1일"]
        for i in range(len(rows)):
            dtime = rows[i].get('sdate')
            temp = repr(dtime.year)+"년 "+repr(dtime.month)+"월 "+repr(dtime.day)+"일"
            for j in range(len(dtimeInfo)):
                if dtimeInfo[j] == temp:
                    break
                else:
                    if j == len(dtimeInfo)-1:
                        dtimeInfo.append(temp)
                        rowCount += 1                        
        conn.close()
     
        self.daySalesInfoTable.setRowCount(rowCount)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝2
        
        self.daySalesInfoTable.setColumnCount(2)
        tmp = ['날짜','매출']
        self.daySalesInfoTable.setHorizontalHeaderLabels(tmp)
        self.daySalesInfoTable.hide()

                #월별 매출 정보
        self.monthSalesInfoTable = QTableWidget(self)
        self.monthSalesInfoTable.resize(840,580)
        self.monthSalesInfoTable.move(240,120)
        
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작3
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select sdate, total_price from sale order by sdate asc;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = 0
        dtimeInfo = ["1999년 1월"]
        for i in range(len(rows)):
            dtime = rows[i].get('sdate')
            temp = repr(dtime.year)+"년 "+repr(dtime.month)+"월"
            for j in range(len(dtimeInfo)):
                if dtimeInfo[j] == temp:
                    break
                else:
                    if j == len(dtimeInfo)-1:
                        dtimeInfo.append(temp)
                        rowCount += 1                        
        conn.close()
        
        self.monthSalesInfoTable.setRowCount(rowCount)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝3
        
        self.monthSalesInfoTable.setColumnCount(2)
        self.monthSalesInfoTable.setHorizontalHeaderLabels(tmp)
        self.monthSalesInfoTable.hide()

            #판매기록
        self.refundButton = QPushButton('환불 처리',self)
        self.refundButton.move(0,120)
        self.refundButton.resize(240,40)
        self.refundButton.hide()
        
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작4
        self.refundButton.clicked.connect(self.clickRefundButton)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝4

        self.salesRecordTable = QTableWidget(self)
        self.salesRecordTable.resize(840,580)
        self.salesRecordTable.move(240,120)
        
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작5
        self.salesRecordTable.cellClicked.connect(self.getDataFromCell)

        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select count(sno) as scount from sale;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = int(rows[0].get('scount'))
        conn.close()
        
        self.salesRecordTable.setRowCount(rowCount)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝5
        
        self.salesRecordTable.setColumnCount(3)
        tmp = ['판매 시각','판매 물품','총 가격']
        self.salesRecordTable.setHorizontalHeaderLabels(tmp)
        self.salesRecordTable.hide()
        
        #재고 관리
            #재고 테이블
        self.inventoryTable = QTableWidget(self)
        self.inventoryTable.resize(1080,500)
        self.inventoryTable.move(0,80)
        
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작6
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select count(pno) as pcount from product;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = int(rows[0].get('pcount'))
        conn.close()

        self.inventoryTable.setRowCount(rowCount)
        self.inventoryTable.cellClicked.connect(self.getDataFromCell)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝6
        
        self.inventoryTable.setColumnCount(4)
        tmp = ['상품 번호', '상품 이름', '상품 가격', '재고 개수']
        self.inventoryTable.setHorizontalHeaderLabels(tmp)
        self.inventoryTable.hide()
        
        
            #상품 입고 처리 -이름,가격,개수,버튼
        self.inventoryEnterName = QLineEdit(self)
        self.inventoryEnterName.setPlaceholderText('상품 이름')
        self.inventoryEnterName.resize(250,40)
        self.inventoryEnterName.move(10,640)
        self.inventoryEnterName.hide()

        self.inventoryEnterPrice = QLineEdit(self)
        self.inventoryEnterPrice.setPlaceholderText('상품 가격')
        self.inventoryEnterPrice.resize(250, 40)
        self.inventoryEnterPrice.move(280,640)
        self.inventoryEnterPrice.hide()

        self.inventoryEnterNum = QLineEdit(self)
        self.inventoryEnterNum.setPlaceholderText('입고 개수')
        self.inventoryEnterNum.resize(250,40)
        self.inventoryEnterNum.move(550,640)
        self.inventoryEnterNum.hide()

        self.inventoryEnterButton = QPushButton('입고 하기',self)
        self.inventoryEnterButton.resize(270,40)
        self.inventoryEnterButton.move(810,640)
        self.inventoryEnterButton.hide()

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작7
        self.inventoryEnterButton.clicked.connect(self.inventoryEnter)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝7
        
            #상품 폐기 처리 -폐기개수, 버튼
        self.inventoryDiscardNum = QLineEdit(self)
        self.inventoryDiscardNum.setPlaceholderText('상품 개수')
        self.inventoryDiscardNum.resize(520,40)
        self.inventoryDiscardNum.move(10,680)
        self.inventoryDiscardNum.hide()

        self.inventoryDiscardButton = QPushButton('폐기 하기',self)
        self.inventoryDiscardButton.resize(540,40)
        self.inventoryDiscardButton.move(540,680)
        self.inventoryDiscardButton.hide()

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작8
        self.inventoryDiscardButton.clicked.connect(self.clickInventoryDiscardButton)
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝8

        #계산
        self.searchProductCode = QLineEdit(self)
        self.searchProductCode.setPlaceholderText('상품코드를 입력하세요')
        self.searchProductCode.resize(270,40)
        self.searchProductCode.move(540,60)
        self.searchProductCode.hide()

        self.searchProductButton = QPushButton('상품 검색',self)
        self.searchProductButton.resize(270, 40)
        self.searchProductButton.move(810,60)
        self.searchProductButton.hide()

        self.calcuTable = QTableWidget(self)
        self.calcuTable.resize(1080,500)
        self.calcuTable.move(0,120)
        self.calcuTable.setRowCount(10)
        self.calcuTable.setColumnCount(4)
        tmp = ['상품 코드','상품 이름','상품 수량', '상품 가격']
        self.calcuTable.setHorizontalHeaderLabels(tmp)
        self.calcuTable.hide()

        self.cardCalcuButton = QPushButton('카드계산',self)
        self.cardCalcuButton.resize(270,40)
        self.cardCalcuButton.move(810,630)
        self.cardCalcuButton.hide()

        self.cashCalcuButton = QPushButton('현급계산',self)
        self.cashCalcuButton.resize(270,40)
        self.cashCalcuButton.move(540,630)
        self.cashCalcuButton.hide()

        self.refundRightPreviosButton = QPushButton('직전 환불 버튼',self)
        self.refundRightPreviosButton.resize(270,40)
        self.refundRightPreviosButton.move(270,630)
        self.refundRightPreviosButton.hide()

        #직원 관리
        self.hireEmpLine = QLineEdit(self)
        self.hireEmpLine.setPlaceholderText('고용할 직원의 이름을 입력하세요.')
        self.hireEmpLine.resize(250,40)
        self.hireEmpLine.move(280,60)
        self.hireEmpLine.hide()

        self.empTel = QLineEdit(self)
        self.empTel.setPlaceholderText('핸드폰 번호를 입력하세요')
        self.empTel.resize(250,40)
        self.empTel.move(550,60)
        self.empTel.hide()
        
        self.hireEmpButton = QPushButton('직원 고용',self)
        self.hireEmpButton.resize(270,40)
        self.hireEmpButton.move(810,60)
        self.hireEmpButton.hide()

        self.empTable = QTableWidget(self)
        self.empTable.resize(1080,500)
        self.empTable.move(0,120)
        self.empTable.setRowCount(10)
        self.empTable.setColumnCount(4)
        tmp = ['직원 번호','직원 이름','직원 폰번', '고용 상태']
        self.empTable.setHorizontalHeaderLabels(tmp)
        self.empTable.hide()

        self.empCommute = QPushButton('출근',self)
        self.empCommute.resize(360,40)
        self.empCommute.move(0,620)
        self.empCommute.hide()

        self.empLeave = QPushButton('퇴근',self)
        self.empLeave.resize(360,40)
        self.empLeave.move(360,620)
        self.empLeave.hide()

        self.empRemove = QPushButton('직원 해임',self)
        self.empRemove.resize(360,40)
        self.empRemove.move(720,620)
        self.empRemove.hide()

        self.hireEmpLine.hide()
        self.empTel.hide()
        self.hireEmpButton.hide()
        self.empTable.hide()
        self.empCommute.hide()
        self.empLeave.hide()
        self.empRemove.hide()
        
        

        #layout set
        self.setWindowTitle('편의점 포스기')
        self.setGeometry(300, 300, 300, 200)
        self.resize(1080,740)
        self.show()


#메인 메뉴 버튼 클릭
    def clickAdminSalesButton(self):
        self.salesInfoButton.show()
        self.salesRecordButton.show()
        self.daySalesInfoButton.show()
        self.monthSalesInfoButton.show()
        self.daySalesInfoTable.show()
        self.inventoryTable.hide()
        self.inventoryEnterName.hide()
        self.inventoryEnterPrice.hide()
        self.inventoryEnterNum.hide()
        self.inventoryEnterButton.hide()
        self.inventoryDiscardNum.hide()
        self.inventoryDiscardButton.hide()
        self.searchProductCode.hide()
        self.searchProductButton.hide()
        self.calcuTable.hide()
        self.cardCalcuButton.hide()
        self.cashCalcuButton.hide()
        self.refundRightPreviosButton.hide()
        self.hireEmpLine.hide()
        self.empTel.hide()
        self.hireEmpButton.hide()
        self.empTable.hide()
        self.empCommute.hide()
        self.empLeave.hide()
        self.empRemove.hide()
        
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작9
        self.clickSalesInfoButton()
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝9
        
    def clickAdminInventoryButton(self):
        self.salesInfoButton.hide()
        self.salesRecordButton.hide()
        self.daySalesInfoButton.hide()
        self.monthSalesInfoButton.hide()
        self.daySalesInfoTable.hide()
        self.refundButton.hide()
        self.salesRecordTable.hide()
        self.inventoryTable.show()
        self.inventoryEnterName.show()
        self.inventoryEnterPrice.show()
        self.inventoryEnterNum.show()
        self.inventoryEnterButton.show()
        self.inventoryDiscardNum.show()
        self.inventoryDiscardButton.show()
        self.searchProductCode.hide()
        self.searchProductButton.hide()
        self.calcuTable.hide()
        self.cardCalcuButton.hide()
        self.cashCalcuButton.hide()
        self.refundRightPreviosButton.hide()
        self.hireEmpLine.hide()
        self.empTel.hide()
        self.hireEmpButton.hide()
        self.empTable.hide()
        self.empCommute.hide()
        self.empLeave.hide()
        self.empRemove.hide()

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작10
        self.printInventoryInfo()
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝10

        
    def clickCalcuButton(self):
        self.salesInfoButton.hide()
        self.salesRecordButton.hide()
        self.daySalesInfoButton.hide()
        self.monthSalesInfoButton.hide()
        self.daySalesInfoTable.hide()
        self.refundButton.hide()
        self.salesRecordTable.hide()
        self.inventoryTable.hide()
        self.inventoryEnterName.hide()
        self.inventoryEnterPrice.hide()
        self.inventoryEnterNum.hide()
        self.inventoryEnterButton.hide()
        self.inventoryDiscardNum.hide()
        self.inventoryDiscardButton.hide()
        self.searchProductCode.show()
        self.searchProductButton.show()
        self.calcuTable.show()
        self.cardCalcuButton.show()
        self.cashCalcuButton.show()
        self.refundRightPreviosButton.show()
        self.hireEmpLine.hide()
        self.empTel.hide()
        self.hireEmpButton.hide()
        self.empTable.hide()
        self.empCommute.hide()
        self.empLeave.hide()
        self.empRemove.hide()

    def clickAdminEmpButton(self):
        self.salesInfoButton.hide()
        self.salesRecordButton.hide()
        self.daySalesInfoButton.hide()
        self.monthSalesInfoButton.hide()
        self.daySalesInfoTable.hide()
        self.refundButton.hide()
        self.salesRecordTable.hide()
        self.inventoryTable.hide()
        self.inventoryEnterName.hide()
        self.inventoryEnterPrice.hide()
        self.inventoryEnterNum.hide()
        self.inventoryEnterButton.hide()
        self.inventoryDiscardNum.hide()
        self.inventoryDiscardButton.hide()
        self.searchProductCode.hide()
        self.searchProductButton.hide()
        self.calcuTable.hide()
        self.cardCalcuButton.hide()
        self.cashCalcuButton.hide()
        self.refundRightPreviosButton.hide()
        self.hireEmpLine.show()
        self.empTel.show()
        self.hireEmpButton.show()
        self.empTable.show()
        self.empCommute.show()
        self.empLeave.show()
        self.empRemove.show()

    #매출관리 메뉴 버튼 클릭
    def clickSalesInfoButton(self):
        self.daySalesInfoButton.show()
        self.monthSalesInfoButton.show()
        self.daySalesInfoTable.show()
        self.refundButton.hide()
        self.salesRecordTable.hide()
        
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작11
        self.clickDaySalesInfoButton()
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝11

    def clickSalesRecordButton(self):
        self.daySalesInfoButton.hide()
        self.monthSalesInfoButton.hide()
        self.daySalesInfoTable.hide()
        self.refundButton.show()
        self.salesRecordTable.show()

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작12
        self.printSalesRecord()
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝12
        

        #매출 정보 메뉴 버튼 클릭(일일 매출 정보, 월별 매출 정보)
    def clickDaySalesInfoButton(self):
        self.daySalesInfoTable.show()
        self.monthSalesInfoTable.hide()

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작13
        self.printDaySalesInfo()
        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝13

    def clcikMonthSalesInfoButton(self):
        self.daySalesInfoTable.hide()
        self.monthSalesInfoTable.show()

        #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트시작14
        self.printMonthSalesInfo()
        

    def clickRefundButton(self):
        global rowNum
        if rowNum == 0:
            print("환불처리 할 판매기록을 선택하지 않았습니다.")
        else:
            conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
            curs = conn.cursor(pymysql.cursors.DictCursor)
            sql = "delete from sale where sno = "+repr(rowNum)+";"
            curs.execute(sql)
            conn.commit()       
            sql = "update sale set sno = sno-1 where sno > "+repr(rowNum)+";"
            curs.execute(sql)
            conn.commit()
            conn.close()
            self.printSalesRecord()
        rowNum = 0
        

    def clickInventoryDiscardButton(self):
        global rowNum
        if rowNum == 0:
            print("폐기할 품목을 선택하지 않았습니다.")
        else:
            tmp = self.inventoryDiscardNum.text()
            if tmp == "":
                print("폐기할 품목의 갯수를 입력하지 않았습니다.")
            else:
                discardNum = int(tmp)
                conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
                curs = conn.cursor(pymysql.cursors.DictCursor)
                sql = "select Pcount, enter_date from inventory where pno = "+repr(rowNum)+";"
                curs.execute(sql)
                rows = curs.fetchall()
                countList = []
                for i in range(len(rows)):
                    countList.append(rows[i].get('Pcount'))
                    if countList[i] >= discardNum:
                        countList[i] -= discardNum
                        discardNum = 0
                    else:
                        discardNum -= countList[i]
                        countList[i] = 0
                    #업데이트해주기
                    sql = "select MIN(ino) from inventory where Pcount > 0 and pno = "+repr(rowNum)+";"
                    curs.execute(sql)
                    irows = curs.fetchall()
                    ino = irows[0].get('MIN(ino)')
                    sql = "update inventory set Pcount = "+repr(countList[i])+" where pno = "+repr(rowNum)+" and ino = "+repr(ino)+";"
                    
                    curs.execute(sql)
                    conn.commit()
                    if discardNum == 0:
                        break
                
                conn.close()
                self.printInventoryInfo()
        rowNum = 0
    
    def getDataFromCell(self,row,column):
        global rowNum
        rowNum = row+1

    def printInventoryInfo(self):
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select count(pno) as pcount from product;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = rows[0].get('pcount')
        #inventory table에서 pno별로 Pcount의 합산을 p_count라는 새로운 attribute에 저장하여 해당 값들을 받아옴
        sql = "select p.pno, p.pname, p.pprice, sum(i.Pcount) as p_count from product p, inventory i where i.pno = p.pno group by pno;"
        curs.execute(sql)
        prows = curs.fetchall()
        self.inventoryTable.setRowCount(rowCount)
        for i in range (rowCount):#product table에 저장되어있는 product의 각 정보들을 table에 넣어줌
            self.inventoryTable.setItem(i,0,QTableWidgetItem(str(prows[i].get('pno'))))
            self.inventoryTable.setItem(i,1,QTableWidgetItem(prows[i].get('pname')))
            self.inventoryTable.setItem(i,2,QTableWidgetItem(str(prows[i].get('pprice'))))
            self.inventoryTable.setItem(i,3,QTableWidgetItem(str(prows[i].get('p_count'))))
        
        conn.close()

    def printSalesRecord(self):
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select count(sno) as scount from sale;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = int(rows[0].get('scount'))#sno에 따라 판매기록이 나오도록 정렬하여 튜플을 받아옴
        self.salesRecordTable.setRowCount(rowCount)
        sql = "select s.sno, s.sdate, p.pname, s.total_price, sd.scount from sale s, product p, sale_detail sd where s.sno = sd.sno and p.pno = sd.pno order by sno asc;"
        curs.execute(sql)
        srows = curs.fetchall()
        sql2 = "select sdate, total_price from sale;"
        curs.execute(sql2)
        srows2 = curs.fetchall()
        sno = 0
        plist = ""
        for i in range(len(srows)):#sno에 따라서 판매물품의 이름이 달라지므로 그것을 따로 저장해주기위함.
            if sno != srows[i].get('sno'):
                sno = srows[i].get('sno')
                plist = ""
            plist += srows[i].get('pname')+" "+repr(srows[i].get('scount'))
            if i != len(srows)-1:
                if sno == srows[i+1].get('sno'):
                    plist += ", "
                else:
                    self.salesRecordTable.setItem(sno-1,1,QTableWidgetItem(plist))
            else:
                self.salesRecordTable.setItem(sno-1,1,QTableWidgetItem(plist))
                
        for i in range(rowCount):#사용자가 보기 쉽도록 시간을 재배치함(사실 sdate를 바로 str로 변형 못해서...)
            dtime = srows2[i].get('sdate')
            saleTime = repr(dtime.year)+"년 "+repr(dtime.month)+"월 "+repr(dtime.day)+"일 "+repr(dtime.hour)+"시 "+repr(dtime.minute)+"분 "+repr(dtime.second)+"초"
            self.salesRecordTable.setItem(i,0,QTableWidgetItem(saleTime))
            self.salesRecordTable.setItem(i,2,QTableWidgetItem(repr(srows2[i].get('total_price'))))
                    
        conn.close()


    def printDaySalesInfo(self):
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select sdate, total_price from sale order by sdate asc;"
        curs.execute(sql)
        rows= curs.fetchall()
        rowCount = 0
        dtimeArr = ["1999년 1월 1일"]
        tpriceArr = []
        newTprice = 0
        for i in range(len(rows)):
            tmpDtime = rows[i].get('sdate')
            tmpTprice = rows[i].get('total_price')
            newDtime = repr(tmpDtime.year)+"년 "+repr(tmpDtime.month)+"월 "+repr(tmpDtime.day)+"일"
            if dtimeArr[len(dtimeArr)-1] != newDtime:#DB에서 가져온 데이터의 년월일의 정보가 dtimeArr에 저장되지 않았다면
                dtimeArr.append(newDtime)#년월일의 정보를 dtimeArr에 저장하고
                tpriceArr.append(newTprice)#년월일의 매출액의 총합을 tpriceArr에 저장한다
                rowCount += 1
                newTprice = 0
                newTprice += tmpTprice#이 tmpTprice는 방금 새로 dtimeArr에 저장된 년월일의 첫번째 매출액이다
                if i == len(rows)-1:#이 해당 년월일의 정보가 가장 최근의 기록이라면
                    tpriceArr.append(newTprice)#tpriceArr에 그냥 저장한다
            else:#DB에서 가져온 데이터의 년월일의 정보가 dtimeArr에 저장되어 있다면
                newTprice += tmpTprice#해당 년월일의 매출액에 더해준다음
                if i == len(rows)-1:#이 해당 년월일의 정보가 가장 최근의 기록이라면
                    tpriceArr.append(newTprice)#tpriceArr에 그냥 저장한다
        
        for i in range(rowCount):
            self.daySalesInfoTable.setItem(i,0,QTableWidgetItem(dtimeArr[i+1]))
            self.daySalesInfoTable.setItem(i,1,QTableWidgetItem(repr(tpriceArr[i+1])))

        conn.close()
        

    def printMonthSalesInfo(self):
        conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "select sdate, total_price from sale order by sdate asc;"
        curs.execute(sql)
        rows = curs.fetchall()
        rowCount = 0
        dtimeArr = ["1999년 1월"]
        tpriceArr = []
        newTprice = 0
        for i in range(len(rows)):
            tmpDtime = rows[i].get('sdate')
            tmpTprice = rows[i].get('total_price')
            newDtime = repr(tmpDtime.year)+"년 "+repr(tmpDtime.month)+"월"
            if dtimeArr[len(dtimeArr)-1] != newDtime:#DB에서 가져온 데이터의 년월의 정보가 dtimeArr에 저장되지 않았다면
                dtimeArr.append(newDtime)#년월의 정보를 dtimeArr에 저장하고
                tpriceArr.append(newTprice)#년월의 매출액의 총합을 tpriceArr에 저장한다
                rowCount += 1
                newTprice = 0
                newTprice += tmpTprice#이 tmpTprice는 방금 새로 dtimeArr에 저장된 년월의 첫번째 매출액이다
            else:#DB에서 가져온 데이터의 년월의 정보가 dtimeArr에 저장되어 있다면
                newTprice += tmpTprice#해당 년월의 매출액에 더해준다음
                if i == len(rows)-1:#이 해당 년월의 정보가 가장 최근의 기록이라면
                    tpriceArr.append(newTprice)#tpriceArr에 그냥 저장한다
                    
        for i in range(rowCount):
            self.monthSalesInfoTable.setItem(i,0,QTableWidgetItem(dtimeArr[i+1]))
            self.monthSalesInfoTable.setItem(i,1,QTableWidgetItem(repr(tpriceArr[i+1])))

        conn.close()


    def inventoryEnter(self):
        productName = self.inventoryEnterName.text()
        productPrice = self.inventoryEnterPrice.text()
        productNum = self.inventoryEnterNum.text()

        if productName == "" or productPrice == "" or productNum == "":
            print("재고 등록에 실패하였습니다.")

        else:
            conn = pymysql.connect(host = 'localhost', user = 'conceo', password = 'conceo15', db = 'conpos')
            curs = conn.cursor(pymysql.cursors.DictCursor)
            sql = "select pno from product where pname = '"+productName+"' and pprice = "+str(productPrice)+";"
            
            try:#execute하여 pno가 존재한다면 해당 pno의 정보를 저장함
                curs.execute(sql)
                rows = curs.fetchall()
                pno = rows[0].get('pno')
            except:#execute하여 pno가 존재하지 않아서 오류가 발생한다면 pno를 최대값보다 1 더 추가하여 product table에 새롭게 저장함
                sql = "select MAX(pno) from product"
                curs.execute(sql)
                rows = curs.fetchall()
                pno = rows[0].get('MAX(pno)')
                pno += 1
                sql = "insert into product(pno, pname, pprice)\
                    values("+str(pno)+",'"+productName+"',"+str(productPrice)+");"
                curs.execute(sql)
                
            sql = "select MAX(ino) from inventory"
            curs.execute(sql)
            rows = curs.fetchall()
            ino = rows[0].get('MAX(ino)')
            ino += 1
            sql = "insert into inventory(ino, pno, Pcount)\
                values("+str(ino)+","+str(pno)+","+str(productNum)+");"
            curs.execute(sql)

            conn.commit()
            conn.close()
            #입고한 상품의 정보를 최신화 하기 위하여 click함수를 다시 호출함.
            self.clickAdminInventoryButton()
            #성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트#성찬파트끝14
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = POS()
    sys.exit(app.exec_())
