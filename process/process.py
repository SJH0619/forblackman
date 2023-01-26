from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from datetime import datetime

class Process():
    def start_process(self):
        # 크롬 드라이버를 하드코딩을 통해 selenium과 연결합니다
        service = Service(executable_path='./chromedriver.exe')
        # selenium에 등록된 크롬 드라이버를 통해서 옵션을 설정해줍니다
        options = webdriver.ChromeOptions()
        # USB연결 같은 경고문구를 제거하기위한 설정을 해주는 코드입니다
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # 아래는 파일이 다운로드 경로를 설정해주는 코드입니다
        # options.add_experimental_option("prefs", {
        #     "download.default_directory": "다운로드~~~",
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True,
        #     "safebrowsing.enabled": True
        # })
        # 드라이버가 실행시키기위해 세팅한 드라이버와 옵션을 적용합니다
        driver = webdriver.Chrome(service=service, options=options)

        # 사용자의 RCMS아이디를 받습니다
        client_id = self.rcms_id_input.text()
        # 사용자의 RCMS비밀번호를 받습니다
        client_pwd = self.rcms_pwd_input.text()
        # 브라우저에서 페이지를 렌더링하는데 걸리는 시간을 지정하기위한 변수입니다
        page_rendering_time = self.render_delay.value()
        # 로봇 감지나, 웹사이트의 애니메이션 효과로 인한 렌더링 시간을 고려한 동작 간의 딜레이를 지정하기위한 변수입니다
        set_delay = self.anti_auto.value()

        # 브라우저창을 전체화면으로 바꿉니다
        driver.maximize_window()
        # 특정 URL로 진입합니다
        driver.get('https://www.rcms.go.kr/index.do')

        # 추후 팝업이나 새 탭이 뜰 때를 대비한 현재 켜진 탭의 수를 받습니다
        first_handles = len(driver.window_handles)
        # 딜레이를 줍니다 // 자주 반복되므로 앞으로는 주석 생략합니다. 또한 다른 코드도 여러번 반복되는 경우에는 주석 생략합니다
        time.sleep(page_rendering_time)

        # 로그인 페이지로 넘어가는 버튼을 찾습니다
        login_page_btn = driver.find_element(By.XPATH, '//*[@id="wfm_header_btn_logInOut"]')
        # 찾아낸 버튼을 클릭합니다
        login_page_btn.click()

        time.sleep(page_rendering_time)

        # 아이디 입력 칸을 찾습니다
        input_id = driver.find_element(By.XPATH, '//*[@id="loginId"]')
        # 클릭합니다
        input_id.click()
        # 아이디를 입력하기위해 클립보드에 저장합니다 => 클립보드에 저장하고 끌어다 쓰는 이유는 로봇 감지 회피를 위해서
        pyperclip.copy(client_id)
        # 붙여넣기합니다
        input_id.send_keys(Keys.CONTROL, 'v')

        time.sleep(set_delay)

        # 비밀번호 입력 칸을 찾습니다
        input_pwd = driver.find_element(By.XPATH, '//*[@id="loginPasswd"]')
        input_pwd.click()
        pyperclip.copy(client_pwd)
        input_pwd.send_keys(Keys.CONTROL, 'v')

        time.sleep(set_delay)

        # 로그인요청 버튼을 찾습니다
        login_btn = driver.find_element(By.XPATH, '//*[@id="btn_login"]')
        login_btn.click()

        time.sleep(page_rendering_time)

        # 비밀번호 변경 팝업이 뜨면 자동으로 닫아줍니다. 로그인 후 기존 메인화면이 출력되는데, 처음에 접속에 있던 메인화면보다 탭이 많은지 체크합니다
        if (first_handles < len(driver.window_handles)):
            # 맨 마지막으로 생성된 탭을 '-1'로 접근할 수 있습니다. 활성 탭을 맨 마지막으로 생성된 탭으로 바꾸는 코드입니다
            driver.switch_to.window(driver.window_handles[-1])
            # 해당 탭을 닫습니다
            driver.close()
            # 다시 기존 탭을 활성 탭으로 지정합니다
            driver.switch_to.window(driver.window_handles[0])

        time.sleep(set_delay)

        # 업무를 보기위한 메인 페이지로 이동합니다
        main_page_btn = driver.find_element(By.XPATH, '//*[@id="wfm_main_btn_banner01"]')
        main_page_btn.click()

        time.sleep(page_rendering_time)

        # 업무용 메인 페이지를 접속할 경우 새로운 탭으로 접속됩니다. 탭을 이동합니다
        driver.switch_to.window(driver.window_handles[-1])
        # 연구비 관련 메뉴 버튼을 찾습니다
        rf_list_menu_btn = driver.find_element(By.XPATH, '//*[@id="wfm_header_gen_menuLvl1_1_btn_menuLvl1"]')
        rf_list_menu_btn.click()

        time.sleep(set_delay)

        # 연구비 이체 내역 버튼을 찾습니다
        rf_transfer_details_link_btn = driver.find_element(By.XPATH, '//*[@id="wfm_header_gen_menuLvl1_1_gen_menuLvl2_2_btn_menuLvl2"]')
        rf_transfer_details_link_btn.click()

        time.sleep(page_rendering_time)

        # 연구비 과제 선택 버튼을 찾습니다
        rp_select_on_btn = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_wframe_sbjtSelectMain_report_btn"]')
        rp_select_on_btn.click()

        time.sleep(set_delay)

        # 연구비 과제 선택으로 생긴 모달에서 진행 과제 버튼을 찾습니다
        rp_set_condition_btn = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_wframe_sbjtSelectMain_wframe_sbjtSelect_btnRcmsStt01"]')
        rp_set_condition_btn.click()

        time.sleep(set_delay)

        # 모든 항목을 체크하는 전체 항목 체크 버튼을 찾습니다
        rp_select_all_checkbox = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_wframe_sbjtSelectMain_wframe_sbjtSelect_gridView_column1"]/label')
        rp_select_all_checkbox.click()

        time.sleep(set_delay)

        # 연구비 과제 선택을 마치기위한 버튼을 찾습니다
        rp_select_finish_btn = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_wframe_sbjtSelectMain_wframe_sbjtSelect_btnClose"]')
        rp_select_finish_btn.click()

        time.sleep(set_delay)

        # 조회 기간을 선택하기위한 버튼입니다. 이 경우 전체 기간 버튼을 찾습니다
        rp_search_all_day_btn = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_anc_allDay"]')
        rp_search_all_day_btn.click()

        time.sleep(set_delay)

        # 연구비 구분을 전체로 바꾸기 위한 리스트창을 찾습니다
        rf_classification_select_list_el = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_sel_searchBudSe"]')
        rf_classification_select_list_el.click()

        time.sleep(set_delay)

        # 연구비 구분을 전체로 바꾸기 위해 '전체' 항목을 찾습니다
        rf_classification_select_all_el = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_sel_searchBudSe_itemTable_0"]')
        rf_classification_select_all_el.click()

        time.sleep(set_delay)

        # 조회 버튼을 찾습니다
        rf_transfer_details_search_btn = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_btn_srch"]')
        rf_transfer_details_search_btn.click()

        time.sleep(page_rendering_time)

        # 엑셀 파일로 받기 위한 모달을 생성하는 버튼을 찾습니다
        excel_file_download_btn = driver.find_element(By.XPATH, '//*[@id="tac_layout_contents_21230_body_btn_excelDown"]')
        excel_file_download_btn.click()

        time.sleep(page_rendering_time)

        # 엑셀 파일을 받기 전 세팅을 하는 모달에서 다운로드를 실행하기위한 버튼을 찾습니다
        excel_file_download_start_btn = driver.find_element(By.LINK_TEXT, '엑셀다운로드')
        excel_file_download_start_btn.click()

        # 다운로드 되는 시간을 고려한 5초의 딜레이를 둡니다
        time.sleep(5)

        # 완전히 드라이버의 실행을 종료합니다
        driver.quit()

        # 차후에 엑셀 변경 및 이동 등등을 위한 다운로드된 파일의 이름을 변수에 저장합니다. 다운로드된 모든 엑셀파일들은 '년월일_연구비이체결과내역.xlsx'의 형식으로 저장됩니다 
        today_file_name = datetime.today().strftime('%Y%m%d') + "_연구비이체결과내역.xlsx"

        # 아래 코드는 다운로드된 파일을 목적 경로를 향해 이동시킵니다. 이때 기존 파일은 새로 이동된 파일에 의해 덮여 쓰여집니다
        # os.replace("C:/Users/idiot/DownLoads/" + today_file_name, "목적폴더~~")

        # 이후 여타 추가할 작업은 반드시!!!!!!! 이 아래에 작성 부탁드립니다
