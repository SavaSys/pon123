from  PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QApplication, QWidget,QTableWidget , QListWidget, QListWidgetItem, QLineEdit, QFormLayout, QHBoxLayout,QVBoxLayout,QGroupBox,QButtonGroup,QRadioButton,QPushButton,QLabel,QSpinBox)
app = QApplication([]) 
btn_menu=QPushButton('Меню')
btn_sleep=QPushButton('відаочити')
Box_minutes= QSpinBox()
Box_minutes.setValue(30)
btn_Ok=QPushButton('Відповісти')
lb_Question= QLabel('')

RadioGroupBox= QGroupBox("варіанти відповідей")
RadioGroup=QButtonGroup()
rbtn_1=QRadioButton('1')
rbtn_2=QRadioButton('2')
rbtn_3=QRadioButton('3')
rbtn_4=QRadioButton('4')
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_ans1= QHBoxLayout()
layout_ans2= QVBoxLayout()
layout_ans3= QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result,alignment=(Qt.AlignLeft |Qt.AlignTop))
layout_res.addWidget(lb_Correct,alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()