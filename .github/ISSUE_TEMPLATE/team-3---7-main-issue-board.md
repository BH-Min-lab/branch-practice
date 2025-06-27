---
name: Team 3 + 7 Main issue board
about: 100 prisoners problem
title: ''
labels: ''
assignees: ''

---

## 📌 업무 요약

100인의 죄수문제를 풀어봅시다. :)

---

## 📂 세부 내용

- **100인의 죄수는 페이크, 우리는 git과 github 업무흐름을 파악하는데 주력합니다.**
- **코드작성은 최소화 하되, 풀&리퀘스트시 1번의 리젝트가 있을 예정입니다.(시간이 허락한다면..)**
- **문제가 발생시 즉시 공유해주세요. 집단지성의 힘을 발휘해봅시다.**

---

## 👥 담당자
- [ ] **민병호** : 팀장
- [ ] **A: 김동준**:  첫번째 함수 작성
- [ ] **B: 김명철**:  두번째 함수 작성
- [ ] **C: 김상윤**:  두번째 함수 작성
- [ ] **D: 박재홍**:  두번째 함수 작성
- [ ] **E: 정민지**:  main 구동부 작성

prisoners/
├─ drawer.py            ← a
├─ random_strategy.py   ← b
├─ optimal_core.py      ← c
├─ optimal_runner.py    ← d
└─ main.py              ← e

---

## 📅 마감일
`성공 확률이 나올때까지 퇴근 없음'


---
A

# drawer.py  – 담당: a
import random
from typing import List

DRAWER_COUNT = 100          # 서랍/죄수 수
OPEN_LIMIT   = DRAWER_COUNT // 2  # 50

def shuffled_drawers() -> List[int]:
    """0‥99 숫자를 무작위로 섞은 서랍 상태를 반환."""
    lst = list(range(DRAWER_COUNT))
    random.shuffle(lst)
    return lst

def prisoners() -> range:
    """죄수 번호(0‥99)를 순회하는 range 객체."""
    return range(DRAWER_COUNT)


---
B

# random_strategy.py  – 담당: b
import random
from prisoners.drawer import shuffled_drawers, prisoners, OPEN_LIMIT, DRAWER_COUNT

def random_success(drawers: list[int], prisoner: int) -> bool:
    """해당 죄수가 무작위 전략으로 성공했는지 반환."""
    picks = random.sample(range(DRAWER_COUNT), OPEN_LIMIT)
    return any(drawers[idx] == prisoner for idx in picks)

def play_random(trials: int = 100_000) -> float:
    """무작위 전략의 생존 확률(%)"""
    wins = 0
    for _ in range(trials):
        drawers = shuffled_drawers()
        if all(random_success(drawers, p) for p in prisoners()):
            wins += 1
    return wins / trials * 100.0


---
C

# optimal_core.py  – 담당: c
from prisoners.drawer import OPEN_LIMIT, DRAWER_COUNT

def cycle_success(drawers: list[int], prisoner: int) -> bool:
    """
    최적 전략: 자기 번호 → 카드 → 인덱스 … 사이클을 따라가며
    50번 안에 자기 번호 카드를 찾으면 True.
    """
    idx = prisoner
    for _ in range(OPEN_LIMIT):
        card = drawers[idx]
        if card == prisoner:
            return True
        idx = card
    return False


---
D

# optimal_runner.py  – 담당: d
from prisoners.drawer import shuffled_drawers, prisoners
from prisoners.optimal_core import cycle_success

def play_optimal(trials: int = 100_000) -> float:
    """최적(사이클) 전략의 생존 확률(%)"""
    wins = 0
    for _ in range(trials):
        drawers = shuffled_drawers()
        if all(cycle_success(drawers, p) for p in prisoners()):
            wins += 1
    return wins / trials * 100.0


---
E

# main.py  – 담당: e
import argparse, time
from prisoners.random_strategy import play_random
from prisoners.optimal_runner  import play_optimal

def main() -> None:
    ap = argparse.ArgumentParser(description="100 Prisoners simulation")
    ap.add_argument("-n", "--trials", type=int, default=100_000,
                    help="시뮬레이션 반복 횟수 (default: 100 000)")
    args = ap.parse_args()

    for label, fn in [("Random", play_random), ("Optimal", play_optimal)]:
        t0 = time.perf_counter()
        pct = fn(args.trials)
        dt  = time.perf_counter() - t0
        print(f"{label:7}: {pct:5.2f}%  (elapsed {dt:.2f}s)")

if __name__ == "__main__":
    main()
