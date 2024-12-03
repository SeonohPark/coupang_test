# import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
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


# 테스트 전 과정에 걸쳐 에러발생 시 에러를 기록하는 try, except문 
try:
  print('##################테스트 시작###################')
  # f = open(f'test_result/{now}_test_result.txt', 'w')
  # f.write(f'테스트 수행 일자 - {now}\n')

  driver = webdriver.Chrome()

  options = webdriver.ChromeOptions()
  options.add_argument("--disable-blink-features=AutomationControlled")
  options.add_argument("authority=" + "www.coupang.com")
  options.add_argument("method=" + "GET")
  options.add_argument("accept=" + "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
  options.add_argument("accept-encoding=" + "gzip, deflate, br")
  options.add_argument("user-agent=" + "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.104 Whale/3.13.131.36 Safari/537.36")
  options.add_argument("sec-ch-ua-platform=" + "macOS")
  options.add_argument("cookie=" + "PCID=31489593180081104183684; _fbp=fb.1.1644931520418.1544640325; gd1=Y; X-CP-PT-locale=ko_KR; MARKETID=31489593180081104183684; sid=03ae1c0ed61946c19e760cf1a3d9317d808aca8b; x-coupang-origin-region=KOREA; x-coupang-target-market=KR; x-coupang-accept-language=ko_KR;")

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  driver.get('https://www.coupang.com/')

  driver.implicitly_wait(10)
  driver.maximize_window()

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

  # #coupang_03 로그인 방법 확인
  # try:
  #   tc_progress = 'COUPANG_03'

  #   email_singnin = WebDriverWait(driver, 10).until(
  #     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/a[1]'))
  #   )
  #   phone_signin = WebDriverWait(driver, 10).until(
  #     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/a[2]'))
  #   )
  #   qr_signin = WebDriverWait(driver, 10).until(
  #     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/a[3]'))
  #   )

  #   if email_singnin.is_displayed():
  #     print('COUPANG_03 이메일 로그인 노출')
  #   else:
  #     print('COUPANG_03 이메일 로그인 미노출')

  #   if phone_signin.is_displayed():
  #     print('COUPANG_03 휴대폰번호 로그인 노출')
  #   else:
  #     print('COUPANG_03 휴대폰번호 로그인 미노출')

  #   if qr_signin.is_displayed():
  #     print('COUPANG_03 QR로그인 노출')
  #   else:
  #     print('COUPANG_03 QR로그인 미노출')

  #   result_pass_list.append(tc_progress)
  #   print('COUPANG_03 로그인 방법 확인')

  # except Exception as e:
  #   print(f'예외 발생 : {e}')
  #   fail_reason = '로그인방법 확인 실패'
  #   result_fail_list.append(tc_progress)
  #   fail_reason_list.append(fail_reason)

  #coupang_04 [이메일 로그인]클릭
  try:
    tc_progress = 'COUPANG_04'

    id_input = driver.find_element(By.ID, 'login-email-input')
    pw_input = driver.find_element(By.ID, 'login-password-input')

    email_singnin.click()

    if id_input.is_displayed() and pw_input.is_displayed():
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

  # #coupang_05 [휴대폰번호 로그인]클릭
  # try:
  #     tc_progress = 'COUPANG_05'
  #     phone_input = driver.find_element(By.XPATH, '//*[@id="phone-field-wrap"]/div[1]/label/input')
  #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((phone_signin))).click()

  #     if phone_input.is_displayed():
  #       result_pass_list.append(tc_progress)
  #       print('COUPANG_05 [휴대폰번호 로그인]버튼 클릭')
  #     else:
  #       print('휴대폰번호 입력란 확인 불가')

  # except Exception:
  #   fail_reason = '휴대폰번호 로그인 컴포넌트 확인 실패'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   fail_reason_list.append(fail_reason)
  #   print('COUPANG_05 [휴대폰번호 로그인] 확인 실패')
  
  # #coupang_06 [QR코드 로그인]클릭
  # time.sleep(2)
  # try:
  #     tc_progress = 'COUPANG_06'
  #     qr_signin.click()

  #     if qr_signin.is_displayed():
  #       result_pass_list.append(tc_progress)
  #       print('COUPANG_06 [QR코드 로그인]버튼 클릭')
  #     else:
  #       print('QR코드 확인 불가')

  # except Exception:
  #   fail_reason = 'QR코드 로그인 컴포넌트 확인 실패'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   fail_reason_list.append(fail_reason)
  #   print('COUPANG_06 [QR코드 로그인] 확인 실패')

  # #coupang_07 유효하지 않은 형식 이메일 입력
  # try:
  #   tc_progress = 'COUPANG_07'
  #   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((email_singnin))).click()
  #   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((id_input))).click()
  #   id_input.send_keys('pso0244')

  #   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((pw_input))).click()
  #   pw_input.send_keys('aaaaaaa')

  #   wrong_email = driver.find_element(By.CSS_SELECTOR, '#memberLogin > div.tab-item.member-login._loginRoot.sms-login-target.style-v2 > form > div.login__content.login__content--input > div:nth-child(1) > div.member__expand-field > div')
    
  #   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="memberLogin"]/div[1]/form/div[5]/button'))).click()

  #   if wrong_email.is_displayed():
  #     result_pass_list.append(tc_progress)
  #     print('COUPANG_07 유효하지 않은 계정 입력 성공')
  #   else:
  #     print('유효하지 않은 게정 확인 불가')

  # except Exception:
  #   fail_reason = '유효하지 않은 계정 확인 실패'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   fail_reason_list.append(fail_reason)
  #   print('COUPANG_07 유효하지 않은 계정 확인 실패')

  #coupang_08 로그인 성공
  try:
    time.sleep(3)
    tc_progress = 'COUPANG_08'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((id_input))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((id_input))).click()

    my_id = input('아이디를 입력해 주세요: ')
    id_input.send_keys(my_id)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((pw_input))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((pw_input))).click()
    
    my_pw = input('비밀번호를 입력해 주세요: ')
    pw_input.send_keys(my_pw)
    driver.find_element(By.XPATH, '//*[@id="memberLogin"]/div[1]/form/div[5]/button').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="memberLogin"]/div[1]/form/div[5]/button'))).click()
    time.sleep(2)
    
    signout_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout"]/a')))

    if signout_btn.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_08 로그인 성공')
    else:
      print('로그인 성공 확인 불가')

  except Exception as e:
    print(f'coupang_08 예외 발생 : {e}')
    fail_reason = '로그인 성공 확인 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  #coupang_9 메인화면 로고 옆 검색창 노출 확인
  time.sleep(2)
  try:
    tc_progress = 'COUPANG_09'
    search_form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'header-searchForm')))

    if search_form.is_displayed():
      result_pass_list.append(tc_progress)
      print('coupang_9 검색창 노출 확인')
    else:
      print('검색창 확인 불가')

  except Exception as e:
    print(f'coupang_9 예외 발생 : {e}')
    fail_reason = '검색창 확인 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  #coupang_10 검색어 입력란에 '칫솔' 입력 후 [돋보기]버튼 클릭
  try:
    tc_progress = 'COUPANG_10'
    search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerSearchKeyword"]')))
    search_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerSearchBtn"]')))
    # search_input.click()
    search_input.send_keys('칫솔')
    search_btn.click()

    if driver.current_url == 'https://www.coupang.com/np/search?component=&q=%EC%B9%AB%EC%86%94&channel=user':
      result_pass_list.append(tc_progress)
      print('coupang_10 칫솔 검색 확인')
    else:
      print('coupang_10 칫솔 검색 확인 불가')

  except Exception:
    fail_reason = '칫솔 검색 확인 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_10 칫솔 검색 확인 실패')

  # #coupang_11 필터 - 좌측 필터에서 '로켓직구만 보기' 클릭
  # # 1페이지에 노출되는 상품 목록에서 [로켓직구]라벨이 포함되어 있는지 체크
  # try:
  #   tc_progress = 'COUPANG_11'
  #   driver.find_element(By.XPATH, '//*[@id="searchServiceFilter"]/ul/li[1]/div/ul/li[3]/label').click()

  #   # 상품 목록 가져오기
  #   product_ids = driver.find_elements(By.XPATH, "//div[@class='id']")

  #   # 각 상품 검사
  #   all_abroad_delivery = True
  #   for product in product_ids:
  #     product_id = product.get_attribute('id')
  #     try:
  #       # 로켓직구 라벨 요소 찾기
  #       abroad_img = product.find_element(By.XPATH, f"//*[@id='{product_id}']/a/dl/dd/div/div[3]/div/div[1]/em/span/img")
  #       # 로켓직구 라벨 src 속성 확인
  #       if 'global_b.png' not in abroad_img.get_attribute('src'):
  #         all_abroad_delivery = False
  #         print(f"상품 ID {product_id} 로켓직구 해당 상품이 아님.")
  #         break
  #     except NoSuchElementException:
  #       all_abroad_delivery = False
  #       print(f"상품 ID {product_id} 로켓직구 해당 상품이 아님.")

  #   if all_abroad_delivery:
  #     print('coupang_11 모든 상품이 로켓직구 상품임.')
  #   else:
  #     print('coupang_11 로켓직구가 아닌 일부 상품이 포함되어 있음')

  # except Exception:
  #   fail_reason = '로켓직구 필터 오류'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   fail_reason_list.append(fail_reason)
  #   print('COUPANG_11 로켓직구 필터 확인 실패')

  # #coupang_12 필터 - 좌측 필터에서 '로켓와우만 보기' 클릭
  # # 1페이지에 노출되는 상품 목록에서 [로켓직구]이미지가 포함되어 있는지 체크
  # try:
  #   tc_progress = 'COUPANG_12'
  #   driver.find_element(By.XPATH, '//*[@id="searchServiceFilter"]/ul/li[1]/div/ul/li[2]/label').click()
  #   # 상품 목록 가져오기
  #   product_ids = driver.find_elements(By.XPATH, "//div[@class='id']")
  #   # 각 상품 검사
  #   all_rocket_delivery = True
  #   for product in product_ids:
  #     product_id = product.get_attribute('id')
  #     try:
  #       # 로켓직구 이미지 요소 찾기
  #       rocket_img = product.find_element(By.XPATH, f"//*[@id='{product_id}']/a/dl/dd/div/div[3]/div/div[1]/em/span/img")
  #       # 로켓직구 이미지의 src 속성 확인
  #       if 'rocket.png' not in rocket_img.get_attribute('src'):
  #         all_rocket_delivery = False
  #         print(f"상품 ID {product_id} 로켓배송 해당 상품이 아님.")
  #         break
  #     except NoSuchElementException:
  #       all_rocket_delivery = False
  #       print(f"상품 ID {product_id} 로켓배송 해당 상품이 아님.")

  #   if all_rocket_delivery:
  #     print('COUPANG_12 모든 상품이 로켓배송 상품임.')
  #   else:
  #     print('COUPANG_12 로켓배송이 아닌 일부 상품이 포함되어 있음')

  # except Exception:
  #   fail_reason = '로켓배송 필터 오류'
  #   print(fail_reason)
  #   result_fail_list.append(tc_progress)
  #   fail_reason_list.append(fail_reason)
  #   print('COUPANG_12 로켓 필터 확인 실패')

  try:
    #coupang_13 필터 - 상품목록 상단에서 [낮은가격순] 클릭
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchSortingOrder"]/ul/li[2]/label'))).click()
    prices = []
    time.sleep(3)

    product_ids = driver.find_elements(By.XPATH, "//div[@class='id']")

    #각 상품의 가격 정보 추출
    for product in product_ids:
      product_id = product.get_attribute(By.CLASS_NAME, 'price-value')
      try:
        # 가격 정보 요소 찾기
        price_element = product.find_element(By.XPATH, f"//*[@id='{product_id}']/a/dl/dd/div/div[3]/div[1]/div[1]/em/strong")
        # 가격 정보 추출 및 정수 변환
        price_text = price_element.text.replace(",", "").strip()
        price = int(price_text)

        try:
            prices.append(price)
            print(product_id)
        except ValueError:
            print(f"가격 정보를 정수로 변환할 수 없음: {price_text} (ID {product_id})")
      except NoSuchElementException:
        print(f"가격 정보 요소를 찾을 수 없음 ID {product_id}")
        continue

    #가격 비교 로직
    is_sorted = all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
    
    if is_sorted:
      print('COUPANG_13 낮은 가격순 정렬 확인')
      result_pass_list.append('COUPANG_13')
    else:
      print('COUPANG_13 낮은 가격순 정렬 확인 실패')
      fail_reason = '가격이 낮은 순으로 정렬되지 않음'
      fail_reason_list.append('COUPANG_13')


  except Exception as e:
    print(f'COPUPANG_13 예외 발생 : {e}')
    fail_reason = '낮은 가격순 필터 오류'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  #coupang_14 닞은가격순 1번 상품 클릭
  try:
    tc_progress = 'COUPANG_14'

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="734755"]/a/dl/dt/img'))).click()

    time.sleep(3)
    all_tabs = driver.window_handles
    if len(all_tabs) > 1:
      driver.switch_to.window(all_tabs[1])
    else:
      raise Exception('새 탭이 열리지 않았습니다.')

    product_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[2]/div[1]/div[3]/div[3]/h1')))
    
    if product_name.is_displayed():
      result_pass_list.append(tc_progress)
      print(product_name.text)
      print('COUPANG_14 상품 상세페이지 진입 성공')
    else:
      print('COUPANG_14 상품 상세페이지 진입 실패')

  except Exception as e:
    print(f'COUPANG_14 예외 발생 : {e}')
    fail_reason = '상품 상세페이지 확인 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  # #coupang_15 [장바구니 담기]버튼 클릭
  try:
      tc_progress = 'COUPANG_15'
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'prod-cart-btn'))).click()
      cart_cnt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'headerCartCount')))

      time.sleep(2)

      if cart_cnt.text != '0':
        result_pass_list.append(tc_progress)
        print('COUPANG_15 장바구니 담기 성공')
      else:
        print('COUPANG_15 장바구니 담기 실패')

  except Exception as e:
    print(f'COUPANG_15 예외 발생 : {e}')
    fail_reason = '장바구니 담기 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  # #coupang_16 [장바구니]버튼 및 숫자 1노출 확인
  try:
    tc_progress = 'COUPANG_16'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/section/div[1]/ul/li[2]/a/span[1]/img'))).click()

    if driver.current_url == 'https://cart.coupang.com/cartView.pang':
      result_pass_list.append(tc_progress)
      print('COUPANG_16 장바구니 페이지 이동 성공')
    else:
      print('COUPANG_16 장바구니 페이지 이동 실패')

  except Exception as e:
    print(f'COUPANF_16 예외 발생 : {e}')
    fail_reason = '장바구니 페이지 이동 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  #coupang_17 [장바구니] 버튼 클릭
  try:
    tc_progress = 'COUPANG_17'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnPay"]'))).click()
    pay_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[1]/div[1]/h3')))

    if pay_page.text == '주문/결제':
      result_pass_list.append(tc_progress)
      print('COUPANG_17 주문/결제 페이지 이동 성공')
    else:
      print('COUPANG_17 주문/결제 페이지 이동 실패')

  except Exception:
    fail_reason = '주문/결제 페이지 이동 실패'
    print(fail_reason)
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
    print('COUPANG_17 주문/결제 페이지 이동 실패')

  # #coupang_18 주문/결제 페이지 노출항목 확인
  try:
    tc_progress = 'COUPANG_18'
    buyer_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[1]/div[3]/div/h2')))
    receiver_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[1]/div[4]/h2')))
    delivery_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[1]/div[6]/div[1]/div/div[2]')))
    pay_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pay-price-section"]/h2')))
    card_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[1]/div[8]/div/h2')))

    if buyer_info.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_18_1 구매자정보 노출 확인')
    else:
      print('COUPANG_18_1 구매자정보 노출 실패')

    if receiver_info.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_18_2 받는사람정보 노출 확인')
    else:
      print('COUPANG_18_2 받는사람정보 노출 실패')
    
    if delivery_info.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_18_3 배송방법 노출 확인')
    else:
      print('COUPANG_18_3 배송방법 노출 실패')

    if pay_info.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_18_4 결제정보 노출 확인')
    else:
      print('COUPANG_18_4 결제정보 노출 실패')

    if card_info.is_displayed():
      result_pass_list.append(tc_progress)
      print('COUPANG_18_5 결제수단 노출 확인')
    else:
      print('COUPANG_18_5 결제수단 노출 실패')

  except Exception as e:
    print(f'COUPANG_18 예외 발생 : {e}')
    fail_reason = '주문/결제 페이지 노출항목 확인 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  # #coupang_19 [결제하기]버튼 클릭
  try:
      tc_progress = 'COUPANG_19'
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'paymentBtn-v2-style'))).click()

      # 기본 콘텐츠(메인 윈도우)로 전환
      driver.switch_to.default_content()

  except Exception as e:
    print(f'COUPANG_19 예외 발생 : {e}')
    fail_reason = '결제 비밀번호 입력창 노출 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  #coupang_20 결제 비밀번호 입력
  try: 
    input('결제 비밀번호 6자리를 입력해주세요. :')
    buyComplete = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/span')))

    if buyComplete.text == '주문완료':
      result_pass_list.append(tc_progress)
      print('COUPANG_20 주문완료 페이지 노출')
    else:
      print('COUPANG_20 주문완료 페이지 노출 실패')

  except Exception as e: 
    print(f'COUPANG_20 예외 발생 : {e}')
    fail_reason = '결제 비밀번호 입력 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)

  
  time.sleep(10)

  #coupang_21 우상단 장바구니 숫자 0확인
  # 기본 콘텐츠(메인 윈도우)로 전환
  driver.switch_to.default_content()
  try:
    tc_progress = 'COUPANG_21'
    time.sleep(2)

    if cart_cnt.text == '0':
      result_pass_list.append(tc_progress)
      print('COUPANG_21 장바구니 담기 성공')
    else:
      print('COUPANG_21 장바구니 담기 실패')

  except Exception as e:
    print(f'COUPANG_21 예외 발생 : {e}')
    fail_reason = '장바구니 담기 실패'
    result_fail_list.append(tc_progress)
    fail_reason_list.append(fail_reason)
  
  #coupang_22 [주문 상세보기]버튼 클릭
  #coupang_23_1 [배송조회]버튼 클릭 
  #coupang_23_2 이전 페이지로 이동
  #coupang_24_1 [주문취소]버튼 클릭
  #coupang_24_2 [단순변심]버튼 클릭
  #coupang_24_3 [다음단계]버튼 클릭
  #coupang_25 [신청하기]버튼 클릭
  #coupang_26 [확인]버튼 클릭
  #coupang_27 [쇼핑 계속하기]버튼 클릭
  #coupang_28 우상단 [로그아웃]버튼 클릭
  
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

