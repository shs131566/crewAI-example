#!/usr/bin/env python
"""여행 플래너 CrewAI - 메인 실행 파일"""

import sys
from trip_planner.main import run, train, replay, test


def main():
    """CLI 진입점"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "run":
            run()
        elif command == "train":
            train()
        elif command == "replay":
            replay()
        elif command == "test":
            test()
        else:
            print("사용법: python main.py [run|train|replay|test]")
            sys.exit(1)
    else:
        # 기본적으로 run 실행
        run()


if __name__ == "__main__":
    main()
