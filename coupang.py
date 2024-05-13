import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

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
  f = open(f'test_result/{now}_test_result.txt', 'w')
  f.write(f'테스트 수행 일자 - {now}\n')




except Exception as e:
  print(f'에러가 발생하여 테스트 종료: {tc_progress} >>> {e}')

#PASS 테스트 결과 기록
f.write('\n[RESULT - PASS]\n')
for pass_cnt in range(len(result_pass_list)):
  f.write(f'{result_pass_list[pass_cnt]} : PASS\n')

#FAIL 테스트 결과 기록
f.write('\n[RESULT - FAIL]\n')
for fail_cnt in range(len(result_fail_list)):
  f.write(f'{result_fail_list[fail_cnt]} : FAIL\n')
  f.write(f'\tFAIL REASON : {fail_reason_list[fail_cnt]}\n')

# f.write('\n') 
# f.write(f'PASS TC COUNT : {len(result_pass_list)}\n')#패스 TC 개수  
# f.write(f'FAIL TC COUNT : {len(result_fail_list)}\n')#실패 TC 개수
# f.write(f'COMPLETED TEST COUNT : {len(result_pass_list) + len(result_fail_list)}\n')#수행 완료한 TC 개수
# f.write(f'PROGRESS OF TEST : {(len(result_pass_list) + len(result_fail_list))/tc_count}\n') #TC 진척률
# f.write(f'PASS RATE : {(len(result_pass_list)/tc_count)*100}%\n')#패스 TC 비율

print('##########테스트 스크립트 종료##########')
driver.quit()

