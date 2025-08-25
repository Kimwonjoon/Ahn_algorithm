-- https://school.programmers.co.kr/learn/courses/30/lessons/132203
-- CS or GS 의사여야하는데 고용일을 내림차순으로, 같을 경우에는 이름 기준 오름차순
-- 출력 시 날짜 포멧이 2025-03-17 이런 식이여야 한다.
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD, "%Y-%m-%d") as HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = "CS" or MCDP_CD = "GS"
ORDER BY HIRE_YMD DESC ,DR_NAME