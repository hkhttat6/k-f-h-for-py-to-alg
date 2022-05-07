from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
app = QApplication([])
fen = loadUi ("u2.ui")
fen.show()
def calcul_DR(mot1,mot2):
    nc=0
    for i in range(len(mot1)):
        if list(mot1)[i]==list(mot2)[i]:
            nc+=1

    return int((nc/len(mot1))*100)
def message(mot1,mot2):
    if not (mot1.isalpha() and mot2.isalpha() and len(mot1)==len(mot2)):
        msg='verifer votres mots'
    else :
        msg=str(calcul_DR(mot1,mot2))
    fen.l1.setText(msg)
    return msg
print(message('ertiu','efthu'))
def DR():
    mot1=fen.t1.text()
    mot2=fen.t2.text()
    message(mot1,mot2)
fen.b1.clicked.connect(DR)
def efface():
    fen.t1.setText('')
    fen.t2.setText('')
fen.b2.clicked.connect(efface)
def end():
    app.exit()
fen.b3.clicked.connect(end)
app.exec() 
    
        
    
        
    