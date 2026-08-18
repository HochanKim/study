import datetime  # noqa: I001

LOAN_DAYS = 14        # 기본 대출 기간
FEE_PER_DAY = 100     # 연체료 (하루당)
MAX_BOOKS = 5         # 1인당 최대 대출 권수

# 2주 계산하는 함수
def get_due_date(days=LOAN_DAYS) :
    today = datetime.date.today()  # noqa: DTZ011
    after_two_weeks = today + datetime.timedelta(days)
    return after_two_weeks

# 연체료 정산하는 함수
def get_late_fee(late_days, per_day=FEE_PER_DAY):
    late_fee = late_days * per_day
    return late_fee

# 파일 테스트
if __name__ == "__main__" :
    print("library_tools 자체 테스트")