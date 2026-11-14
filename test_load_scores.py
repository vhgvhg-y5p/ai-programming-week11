import pytest
from load_scores import load_scores

def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []

def 쓰기(path, 점수):
    with open(path, "w", encoding="utf-8") as f:
        f.write("이름,점수\n")
        f.write(f"테스트,{점수}\n")


@pytest.mark.parametrize("점수, 유효한가", [
    (-1,  False),
    (0,   True),
    (1,   True),
    (99,  True),
    (100, True),
    (101, False),
])
def test_점수_경계값(점수, 유효한가):
    쓰기("임시.csv", 점수)
    kept, skipped = load_scores("임시.csv")
    assert (len(kept) == 1) == 유효한가

def test_이름이_비어_있으면_건너뛴다():
    kept, skipped = load_scores("weird.csv")
    assert (2, ",90", "이름이 비어 있음") in skipped

def test_빈_줄은_건너뛴다():
    kept, skipped = load_scores("scores.csv")
    assert all(원본 != "" for _, 원본, _ in skipped)


def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert ("최,네번", 77) in kept    