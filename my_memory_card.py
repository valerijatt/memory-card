from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QHBoxLayout, QVBoxLayout, QButtonGroup
from random import shuffle
def show_result():
    RadioGroupBox.hide()
    Group.show()
    button.setText('Следующий вопрос')
def show_question():
    Group.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def ask(q):
    shuffle(answers)
    question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    rightq.setText(q.right_answer)
def check_answer():
    if answers[0].isChecked():
        right.setText('Правильно')
        main_win.count += 1
    else:
        right.setText('Неправильно')
    
    main_win.count_q += 1
    tresult.setText(str(main_win.count) + ' из ' + str(main_win.count_q))
    show_result()

class Question():
    def __init__(self, question,right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 
    
def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
    ask(questions_list[main_win.cur_question])

    show_question()





app = QApplication([])
main_win = QWidget()
question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
button.clicked.connect(start_test)
RadioGroupBox = QGroupBox('Варианты ответов')
Group = QGroupBox('Результат теста')
main_win.count = 0
main_win.count_q = 0
tresult = QLabel(str(main_win.count) + ' из ' + str(main_win.count_q))
right = QLabel('Правильно/Неправильно')
rightq = QLabel('Правильный ответ')
layout_m = QVBoxLayout()
layout_m.addWidget(right)
layout_m.addWidget(rightq)
Group.setLayout(layout_m)
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH1.addWidget(rbtn_1)
layoutH1.addWidget(rbtn_3)
layoutH2.addWidget(rbtn_2)
layoutH2.addWidget(rbtn_4)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
RadioGroupBox.setLayout(layout_main)
answer = QVBoxLayout()
answer.addWidget(question)
answer.addWidget(Group)
answer.addWidget(RadioGroupBox)
answer.addWidget(button)
answer.addWidget(tresult)
main_win.cur_question = -1
main_win.setLayout(answer)
questions_list = [Question('Какая самая большая страна мира?', 'Россия', 'Финляндия', 'Франция', 'Польша'),Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французкий'),Question('Столица Франции', 'Париж', 'Тирана', 'Брюссель', 'Афины'),Question('В какой стране находится гора Эверест?', 'Непал', 'Тайланд', 'Египет', 'Сингапур'), Question('Какой штат США самый большой по площади?','Аляска','Колифорния','Аризона', 'Монтана'),Question('В какой стране самые естествинные озера?','Канада','Индия','Чехия','Мексика'),Question('Какую страну также называют Нидерландами?', 'Голландия','Австрия','Израиль','Иран'), Question('Из скольких штатов состоят Соедененные Штаты?','50','41','60','35'), Question('Через сколько штатов протекает река Миссисипи?', '31', '29', '25', '40'), Question('Сколько стран все еще используют шиллинг в качестве валюты?', '4', '1', '0', '10'), Question('Какой стране пренадлежат Канарские острова?', 'Испания', 'Канада','Филиппины', 'Венесуэла'), Question('Какая страна имеет самое большое население в мире?', 'Китай', 'Россия','CША','Швеция'), Question('Какая самая большая пустыня в мире?', 'Антарктическая пустыня','Сахара', 'Арктическая пустыня', 'Пустыня Аравийского полуострова'),Question('Вкакой стране вы бы нашли город Дрезден?', 'Германия', 'Австрия','Чехия','Финляндия'), Question('В каом городе Бунд является достопримечательностью?', 'Шанхай', 'Рим', 'Самара','Винница')]
next_question()
Group.hide()
main_win.show()
app.exec_()