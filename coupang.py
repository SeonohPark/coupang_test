import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


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

driver = webdriver.Chrome()

# 테스트 전 과정에 걸쳐 에러발생 시 에러를 기록하는 try, except문 
try:
  print('##################테스트 시작###################')
  # f = open(f'test_result/{now}_test_result.txt', 'w')
  # f.write(f'테스트 수행 일자 - {now}\n')

  driver.implicitly_wait(10)

  #coupang_01 쿠팡 홈페이지 접속
  try:
    tc_progress = 'COUPANG_01'
    driver.get('https://www.coupang.com')
    driver.maximize_window()
    
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
    qr_signin = driver.find_element(By.CSS_SELECTOR, 'body > div.member-wrapper.member-wrapper--flex.pc-otp-login-v4 > div.member-main > div.tab-item-header.tab-item-header-otp > a.qrcode')

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
  #coupang_05 [휴대폰번호 로그인]클릭
  #coupang_06 [QR코드 로그인]클릭
  #coupang_07 이메일 입력란에 유효하지 않은 형식 이메일 입력
  #coupang_08 암호 입력란에 암호 입력
  #coupang_09 [로그인]버튼 클릭
  #coupang_10 이메일 입력란에 유효한 아이디 입력
  #coupang_11 암호 입력란에 암호 입력
  #coupang_12 로그인 성공
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

  time.sleep(10)

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

