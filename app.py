import sys
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QMessageBox
from main_ui import Ui_widget as Ui_Main
from check_ui import Ui_Form as Ui_Check
from going_ui import Ui_Form as Ui_Going
from register_ui import Ui_Form as Ui_Register

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 스택 생성
        self.stack = QStackedWidget()

        # main 화면
        self.main_page = QWidget()
        self.main_ui = Ui_Main()
        self.main_ui.setupUi(self.main_page)

        # check 화면
        self.check_page = QWidget()
        self.check_ui = Ui_Check()
        self.check_ui.setupUi(self.check_page)

        # going 화면
        self.going_page = QWidget()
        self.going_ui = Ui_Going()
        self.going_ui.setupUi(self.going_page)

        # register 화면
        self.register_page = QWidget()
        self.register_ui = Ui_Register()
        self.register_ui.setupUi(self.register_page)
        
        # 학번 입력 저장용
        self.student_number = ""

        # 숫자 버튼 연결
        self.register_ui.btn_0.clicked.connect(lambda: self.append_number("0"))
        self.register_ui.btn_1.clicked.connect(lambda: self.append_number("1"))
        self.register_ui.btn_2.clicked.connect(lambda: self.append_number("2"))
        self.register_ui.btn_3.clicked.connect(lambda: self.append_number("3"))
        self.register_ui.btn_4.clicked.connect(lambda: self.append_number("4"))
        self.register_ui.btn_5.clicked.connect(lambda: self.append_number("5"))
        self.register_ui.btn_6.clicked.connect(lambda: self.append_number("6"))
        self.register_ui.btn_7.clicked.connect(lambda: self.append_number("7"))
        self.register_ui.btn_8.clicked.connect(lambda: self.append_number("8"))
        self.register_ui.btn_9.clicked.connect(lambda: self.append_number("9"))

        # 지우기 버튼 연결
        self.register_ui.btn_del.clicked.connect(self.delete_last_digit)

        # 확인 버튼 연결
        self.register_ui.btn_ok.clicked.connect(self.handle_ok_clicked)

        # 스택에 위젯 추가
        self.stack.addWidget(self.main_page)      # index 0
        self.stack.addWidget(self.check_page)     # index 1
        self.stack.addWidget(self.going_page)     # index 2
        self.stack.addWidget(self.register_page)  # index 3

        self.stack.setCurrentIndex(0)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.setGeometry(100, 100, 800, 480)

        # 시간 자동 업데이트 타이머
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # 메인 화면 → 다른 화면 전환
        self.main_ui.btn_check_in_out.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.main_ui.btn_going_out.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.main_ui.btn_fingerprint.clicked.connect(lambda: self.stack.setCurrentIndex(3))

        # 다른 화면 → 메인 화면으로 (뒤로가기 시 학번 초기화)
        self.check_ui.btn_previous_page.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.going_ui.btn_previous_page.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.register_ui.btn_previous_page.clicked.connect(self.back_to_main)

        # 도움말 버튼 연결
        self.main_ui.btn_help.clicked.connect(self.show_help)
        self.check_ui.btn_help.clicked.connect(self.show_help)
        self.going_ui.btn_help.clicked.connect(self.show_help)
        self.register_ui.btn_help.clicked.connect(self.show_help)

    # 숫자 입력
    def append_number(self, num):
        self.student_number += num
        self.register_ui.label_message.setText(f"< {self.student_number} >")

    # 숫자 지우기
    def delete_last_digit(self):
        self.student_number = self.student_number[:-1]
        self.register_ui.label_message.setText(f"< {self.student_number} >")

    # 확인 버튼 눌렀을 때
    def handle_ok_clicked(self):
        if self.student_number:
            self.register_ui.label_message.setText(f"<  지문을 등록해주세요  >")
            QTimer.singleShot(2000, self.fingerprint_registered)

    # 등록 완료 메시지
    def fingerprint_registered(self):
        self.register_ui.label_message.setText(f"<  지문이 등록되었습니다  >")
        self.student_number = ""

    # 뒤로가기 → 메인 + 학번 초기화
    def back_to_main(self):
        self.student_number = ""
        self.register_ui.label_message.setText("<                            >")
        self.stack.setCurrentIndex(0)

    # 시간 갱신
    def update_time(self):
        current = QDateTime.currentDateTime()
        text = current.toString("yyyy년 MM월 dd일 / hh:mm분")
        self.main_ui.label_date_time.setText(text)
        self.check_ui.label_date_time.setText(text)
        self.going_ui.label_date_time.setText(text)
        self.register_ui.label_date_time.setText(text)

    # 도움말 팝업
    def show_help(self):
        QMessageBox.information(self, "도움말", "1. 먼저 지문 등록을 진행해 주세요.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
