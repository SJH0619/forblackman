import shutil
import pytz
import sys
import os
from apscheduler.schedulers.qt import QtScheduler
from PySide6.QtCore import Slot, QTime
from PySide6.QtWidgets import QMainWindow, QApplication
from main_layout import Ui_MainWindow
from process.process import Process as p


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        # 매개변수가 들어오면 처리하는 코드입니다
        super(MyWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # 스케쥴러를 위해 스케쥴러를 초기화 생성합니다
        self.scheduler = QtScheduler()
        # 타임존을 우리나라로 설정합니다
        self.scheduler.timezone = pytz.timezone("Asia/Seoul")
        # UI의 스케쥴 추가 버튼을 누르면 add_schedule함수가 실행됩니다
        self.add_schedule_time_btn.clicked.connect(self.add_schedule)
        # UI의 시작 버튼을 누르면 start_process함수가 실행됩니다
        self.start_btn.clicked.connect(self.start_process)

    # 위 코드의 UI 버튼에 함수를 적용하려면 Slot 어노테이션을 붙여줘야합니다
    @Slot()
    # 스케쥴을 추가하는 함수입니다
    def add_schedule(self):
        # 일단 스케쥴러가 실행중에 있다면 멈춰줍니다. 멈추기 전까진 스케쥴 추가가 불가능합니다
        if self.scheduler.running:
            self.scheduler.pause()

        # 텍스트 브라우저에 글자를 입력하여 가시화시키기 위한 코드입니다
        tb_content = "%d:%d"%(self.schedule_time.time().hour(), self.schedule_time.time().minute())
        self.added_schedule_list.append(tb_content)

        # 스케쥴러에 추가 작업 시간을 설정합니다
        # 이때 제일 앞에 있는 매개변수는 동작할 함수를 지정하는 것이고(여기서는 start_process)
        # 두 번째 매개변수는 동작을 지정하기위한 방식을 지정하는 것이고
        # 세 번째 매개변수는 시간을
        # 네 번째 매개변수는 분을 설정합니다
        # 다섯 번째 매개변수는 해당 작업의 아이디를 지정합니다. 우리는 이 아이디를 통해 작업을 선택하여 수정 혹은 삭제할 수 있습니다
        # 특히 cron에 대한 개념은 인터넷에서 검색하여 찾아보시길 추천합니다
        self.scheduler.add_job(self.start_process,
            "cron",
            hour=self.schedule_time.time().hour(),
            minute=self.schedule_time.time().minute(),
            id="%d:%d"%(self.schedule_time.time().hour(), self.schedule_time.time().minute()))

        # 스케쥴이 추가된후에는 스케쥴 작업 시작을 적어주는 입력창의 값을 초기화 해줍니다
        self.schedule_time.setTime(QTime(0, 0, 0))

        # 스케쥴 작업을 단 한번도 실행하지 않았다면 스케쥴을 동작시켜줍니다. 이미 돌아가고 있다면 위에서 pause했었던 상태이므로 다시 resume으로 켜줍니다
        if not self.scheduler.running:
            self.scheduler.start()
        else:
            self.scheduler.resume()

    # start_process는 process패키지에서 process모듈을 실행합니다. process모듈을 따로 분리한 이유는 코드가 매우 길기 때문입니다
    @Slot()
    def start_process(self):
        p.start_process(self)

# 자동 시작이 되기위한 batch 파일을 만드는 함수입니다
def make_batch_n_reg():
    # 현재 프로젝트가 어떤 경로에서 실행중인지 확인합니다
    now_abs_path = os.path.dirname(os.path.abspath(__file__))

    # 파일 작성을 시작합니다
    f = open("./spreg.bat", "w")
    # start명령어는 해당 프로그램을 실행하는 명령어로써 어떤 경로에서 어떤 파일을 실행할지 지정하는 명령어입니다
    f.write('start /d ' + now_abs_path + '\\ /b AutoRCMS.exe\n')
    # 명령어가 다 입력되면 파일 작성을 종료합니다
    f.close()

    # 시작프로그램에 해당 batch파일을 옮겨줍니다
    shutil.copyfile(".\\spreg.bat", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\spreg.bat")

# 실행시 메인일 경우에는 아래 코드를 실행합니다. 다만 메인 실행 프로그램은 이 main.py이므로 반드시 실행됩니다
if __name__ == "__main__":
    # Qt앱을 실행하기위해 생성자 초기화 선언을 해줍니다
    app = QApplication([])

    # 위젯레이아웃을 생성자 초기화 선언을 해줍니다
    widget = MyWidget()
    # 해당 위젯을 출력합니다
    widget.show()

    # 만약 시작프로그램에 batch파일이 없다면 make_batch_n_reg 함수를 실행합니다
    if not os.path.isfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\spreg.bat"):
        make_batch_n_reg()

    # 종료를 하면 메모리상에서 해당프로그램에 대한 데이터를 모두 휘발시킵니다 => 즉 깔끔한 종료가 됩니다
    sys.exit(app.exec())
