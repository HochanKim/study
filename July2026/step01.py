# pwd → 현재 위치의 전체 경로
# ls → 현 위치에 있는 파일
# cd 00 → '00' 폴더로 이동
# cd .. → 한단계 위로 이동
# cd ../.. → 두단계 위로 이동
import math

numer = 8
denom = 12
gcd_val = math.gcd(numer, denom)

simple_numer = numer // gcd_val
simple_denom = denom // gcd_val
print(f"{simple_numer}/{simple_denom}")
