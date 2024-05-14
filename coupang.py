import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 현재 날짜, 시간 구하기
now = time.strftime('%Y-%m_%d_%H_%M')
today = time.strftime('%Y%m%d')

# Test Report 데이터
result_pass_list = [] #pass한 TC ID를 가지고 있는 리스트
result_fail_list = [] #fail한 TC ID를 가지고 있는 리스트
fail_reason_list = [] #fail한 원인을 가지고 있는 리스트
tc_count = 36 #전체 TC 개수 

# 리포트 파일 폴더 만들기
# if not os.path.exists('test_result'):
#   os.makedirs('test_result')

#   f = open('test_result.txt', 'a')
#   f.write('\n 내용을 추가로 작성합니다.')
#   f.close()

# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# user_ag = UserAgent().random
# options.add_argument('user-agent=%s'%user_ag)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# options = webdriver.ChromeOptions()
# options.add_argument("authority=" + "www.coupang.com")
# options.add_argument("method=" + "GET")
# options.add_argument("accept=" + "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
# options.add_argument("accept-encoding=" + "gzip, deflate, br")
# options.add_argument("user-agent=" + "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36")
# options.add_argument("sec-ch-ua-platform=" + "macOS")
# options.add_argument("cookie=" + "PCID=31489593180081104183684; _fbp=fb.1.1644931520418.1544640325; gd1=Y; X-CP-PT-locale=ko_KR; MARKETID=31489593180081104183684; sid=03ae1c0ed61946c19e760cf1a3d9317d808aca8b; x-coupang-origin-region=KOREA; x-coupang-target-market=KR; x-coupang-accept-language=ko_KR;")

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.coupang.com/'
driver.get(url=url)
driver.maximize_window()

# 테스트 전 과정에 걸쳐 에러발생 시 에러를 기록하는 try, except문 
try:
  print('##################테스트 시작###################')
  # f = open(f'test_result/{now}_test_result.txt', 'w')
  # f.write(f'테스트 수행 일자 - {now}\n')

  driver.implicitly_wait(10)

  #coupang_01 쿠팡 홈페이지 접속
  try:
    tc_progress = 'COUPANG_01'
    
    if driver.current_url == 'https://www.coupang.com/':
      print(driver.title)
      print(driver.current_url)
      result_pass_list.append(tc_progress)
      print('COUPANG_01 쿠팡 메인화면 진입 성공')
    else:
      print('쿠팡 메인화면 로고 확인 불가')

  except TimeoutException:
    print('로딩시간 초과 에러 발생')
  except NoSuchElementException:
    print('페이지 내 해당 엘리먼트 미노출')

  #coupang_02 로그인
  try:
    signin_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/a')))

    if signin_btn.is_displayed():
      tc_progress = 'COUPANG_02_1'
       #coupang_02_1 우상단 [로그인]버튼 확인
      result_pass_list.append(tc_progress)
      print('COUPANG_02_1 우상단 [로그인]버튼 확인')

      #coupang_02_2 [로그인]버튼 클릭
      try:
        signin_btn.click()
        tc_progress = 'COUPANG_02_2'
        result_pass_list.append(tc_progress)
        print('COUPANG_02_2 [로그인]버튼 클릭')
      except Exception as e:
        print(f'로그인 버튼 클릭 오류 : {e}')

    else:
      print('[로그인]버튼 확인 불가')

  except Exception:
    fail_reason = '로그인 버튼 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_02 로그인 버튼 확인 실패')

  #coupang_03 로그인 방법 확인
  try:
    tc_progress = 'COUPANG_03'

    email_singnin = driver.find_element(By.CSS_SELECTOR, 'body > div.member-wrapper.member-wrapper--flex.pc-otp-login-v4 > div.member-main > div.tab-item-header.tab-item-header-otp > a.password.active')
    phone_signin = driver.find_element(By.CSS_SELECTOR, 'body > div.member-wrapper.member-wrapper--flex.pc-otp-login-v4 > div.member-main > div.tab-item-header.tab-item-header-otp > a.pc-otp-login-v4')
    qr_signin = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[3]')

    if email_singnin.is_displayed():
      print('COUPANG_03 이메일 로그인 노출')
    else:
      print('COUPANG_03 이메일 로그인 미노출')

    if phone_signin.is_displayed():
      print('COUPANG_03 휴대폰번호 로그인 노출')
    else:
      print('COUPANG_03 휴대폰번호 로그인 미노출')
    
    if qr_signin.is_displayed():
      print('COUPANG_03 QR로그인 노출')
    else:
      print('COUPANG_03 QR로그인 미노출')

    result_pass_list.append(tc_progress)
    print('COUPANG_03 로그인 방법 확인')

  except Exception:
    fail_reason = '로그인방법 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_03 로그인방법 확인 실패')

  #coupang_04 [이메일 로그인]클릭
  try:
    tc_progress = 'COUPANG_04'

    id_input = driver.find_element(By.ID, 'login-email-input')
    pw_input = driver.find_element(By.ID, 'login-password-input')

    if id_input.is_displayed() & pw_input.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_04 [이메일 로그인]버튼 클릭')
    else:
      print('ID, PW 입력란 확인 불가')

  except Exception:
    fail_reason = '이메일 로그인 컴포넌트 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_04 [이메일 로그인] 확인 실패')

  #coupang_05 [휴대폰번호 로그인]클릭
  try:
      tc_progress = 'COUPANG_05'
      phone_input = driver.find_element(By.XPATH, '//*[@id="phone-field-wrap"]/div[1]/label/input')
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((phone_signin))).click()

      if phone_input.is_displayed():
        result_pass_list.append(tc_progress)
        print('COUPANG_05 [휴대폰번호 로그인]버튼 클릭')
      else:
        print('휴대폰번호 입력란 확인 불가')

  except Exception:
    fail_reason = '휴대폰번호 로그인 컴포넌트 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_05 [휴대폰번호 로그인] 확인 실패')
  
  #coupang_06 [QR코드 로그인]클릭
  try:
      tc_progress = 'COUPANG_06'
      qr_code = driver.find_element(By.CSS_SELECTOR, '#memberLogin > div.tab-item.qr-login > div.qr-login__content > div.right > div.qr-login__image > canvas')
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((qr_signin))).click()

      if qr_code.is_displayed():
        result_pass_list.append(tc_progress)
        print('COUPANG_06 [QR코드 로그인]버튼 클릭')
      else:
        print('QR코드 확인 불가')

  except Exception:
    fail_reason = 'QR코드 로그인 컴포넌트 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_06 [QR코드 로그인] 확인 실패')

  #coupang_07 유효하지 않은 형식 이메일 입력
  try:
    tc_progress = 'COUPANG_07'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((email_singnin))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((id_input))).click()
    id_input.send_keys('pso0244')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((pw_input))).click()
    pw_input.send_keys('aaaaaaa')

    wrong_email = driver.find_element(By.CSS_SELECTOR, '#memberLogin > div.tab-item.member-login._loginRoot.sms-login-target.style-v2 > form > div.login__content.login__content--input > div:nth-child(1) > div.member__expand-field > div')
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="memberLogin"]/div[1]/form/div[5]/button'))).click()

    if wrong_email.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_07 유효하지 않은 계정 입력 성공')
    else:
      print('유효하지 않은 게정 확인 불가')

  except Exception:
    fail_reason = '유효하지 않은 계정 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_07 유효하지 않은 계정 확인 실패')

  #coupang_08 로그인 성공
  try:
      tc_progress = 'COUPANG_08'
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((id_input))).clear()
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((id_input))).click()

      my_id = input('아이디를 입력해 주세요: ')
      id_input.send_keys(my_id)

      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((pw_input))).clear()
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((pw_input))).click()
      
      my_pw = input('비밀번호를 입력해 주세요: ')
      pw_input.send_keys(my_pw)
      
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="memberLogin"]/div[1]/form/div[5]/button'))).click()

      time.sleep(3)
      signout_btn = driver.find_element(By.XPATH, '//*[@id="logout"]/a')

      if signout_btn.is_displayed():
        result_pass_list.append(tc_progress)
        print('COUPANG_08 로그인 성공')
      else:
        print('로그인 성공 확인 불가')

  except Exception:
    fail_reason = '로그인 성공 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_08 로그인 성공 확인 실패')

  #coupang_12_1 [로그인]버튼 클릭
  #coupang_12_2 우상단 [로그아웃]버튼 확인
  #coupang_13 메인화면 로고 옆 검색창 노출 확인
  #coupang_14 검색어 입력란에 '칫솔' 입력 후 [돋보기]버튼 클릭
  #coupang_15 필터 - 좌측 필터에서 '로켓직구만 보기' 클릭
  #coupang_16 필터 - 좌측 필터에서 '로켓와우만 보기' 클릭
  #coupang_17 필터 - 상품목록 상단에서 [낮은가격순] 클릭
  #coupang_18 닞은가격순 1번 상품 클릭
  #coupang_19 [장바구니 담기]버튼 클릭
  #coupang_20 홈으로 이동 후 우상단 [장바구니]버튼 및 숫자 1 노출 확인
  #coupang_21 [장바구니]버튼 클릭
  #coupang_22 [구매하기]버튼 클릭
  #coupang_23 주문/결제 페이지 노출항목 확인
  #coupang_24 [결제하기]버튼 클릭
  #coupang_25 결제 비밀번호 입력
  #coupang_26 우상단 장바구니 숫자 0확인
  #coupang_27 [주문 상세보기]버튼 클릭
  #coupang_28_1 [배송조회]버튼 클릭 
  #coupang_28_2 이전 페이지로 이동
  #coupang_29_1 [주문취소]버튼 클릭
  #coupang_29_2 [단순변심]버튼 클릭
  #coupang_29_3 [다음단계]버튼 클릭
  #coupang_30 [신청하기]버튼 클릭
  #coupang_31 [확인]버튼 클릭
  #coupang_32 [쇼핑 계속하기]버튼 클릭
  #coupang_33 우상단 [로그아웃]버튼 클릭
  
  time.sleep(5)
  
except Exception as e:
  print(f'에러가 발생하여 테스트 종료: {tc_progress} >>> {e}')

# #PASS 테스트 결과 기록
# f.write('\n[RESULT - PASS]\n')
# for pass_cnt in range(len(result_pass_list)):
#   f.write(f'{result_pass_list[pass_cnt]} : PASS\n')

# #FAIL 테스트 결과 기록
# f.write('\n[RESULT - FAIL]\n')
# for fail_cnt in range(len(result_fail_list)):
#   f.write(f'{result_fail_list[fail_cnt]} : FAIL\n')
#   f.write(f'\tFAIL REASON : {fail_reason_list[fail_cnt]}\n')

# f.write('\n') 
# f.write(f'PASS TC COUNT : {len(result_pass_list)}\n')#패스 TC 개수  
# f.write(f'FAIL TC COUNT : {len(result_fail_list)}\n')#실패 TC 개수
# f.write(f'COMPLETED TEST COUNT : {len(result_pass_list) + len(result_fail_list)}\n')#수행 완료한 TC 개수
# f.write(f'PROGRESS OF TEST : {(len(result_pass_list) + len(result_fail_list))/tc_count}\n') #TC 진척률
# f.write(f'PASS RATE : {(len(result_pass_list)/tc_count)*100}%\n')#패스 TC 비율

print('##########테스트 스크립트 종료##########')
driver.quit()

