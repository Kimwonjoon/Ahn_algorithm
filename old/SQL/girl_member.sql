-- https://school.programmers.co.kr/learn/courses/30/lessons/131120
-- 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일인데 전화번호가 NOT NULL이고 회원 ID를 기준으로 ASC 정렬
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = "W" AND month(DATE_OF_BIRTH) = "3" AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;