
import pandas as pd


def 정제(df):
    print("시작:", len(df))
    df = df.dropna(subset=["점수"]).copy()
    print("빈 칸 제거:", len(df))

    df = df.drop_duplicates()
    print("중복 제거:", len(df))

    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거:", len(df))

    return df

def 반별평균(df):
    return df.groupby("반")["점수"].mean()

if __name__ == "__main__":
    df = pd.read_csv("scores_2026.csv")
    df = 정제(df)

    print("반:", sorted(df["반"].unique()))
    print("과목:", sorted(df["과목"].unique()))

    math_df = df[df["과목"] == "수학"]
    print("수학 데이터 행 수:", len(math_df))


    print("\n[반별 통계]")
    print(df.groupby("반")["점수"].agg(
        ["count", "mean", "median", "max"]
    ))

    print("\n[과목별·반별 통계]")
    print(df.groupby(["과목", "반"])["점수"].agg(
        ["count", "mean", "median", "max"]
    ))


    print("\n[합계 검증]")
    print("그룹별 합계:", df.groupby("반")["점수"].sum().sum())
    print("전체 합계:", df["점수"].sum())
    print("그룹별 개수:", df.groupby("반")["점수"].count().sum())
    print("전체 행 수:", len(df))

    print("\n[스팟 체크: 1반 수학]")
    scores = df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"]
    print(scores.to_list())
    print("평균:", scores.mean())


    print("\n[mini.csv 검증]")
    mini = pd.read_csv("mini.csv")
    mini = 정제(mini)

    print("정제 후 행 수:", len(mini))
    print("반별 평균:")
    print(mini.groupby("반")["점수"].mean())

