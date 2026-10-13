from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    id: int
    name: str
    rarity: int


@dataclass(frozen=True, slots=True)
class Report(Item):
    exp: int


# アイテムマスター
# IDは説明用の仮ID
ITEM_MASTER: dict[int, Item] = {
    1001: Report(1001, "NoviceActivityReport", 0, 50),
    1002: Report(1002, "NormalActivityReport", 1, 500),
    1003: Report(1003, "AdvancedActivityReport", 2, 2000),
    1004: Report(1004, "SuperiorActivityReport", 3, 10000),
}


# Lv1からの累計必要経験値
STUDENT_REQUIRED_EXP = {
    80: 613830,
    90: 1249185,
}


def calculate_total_report_exp(
    inventory: dict[int, int],
) -> int:
    total_exp = 0

    for item_id, count in inventory.items():
        item = ITEM_MASTER[item_id]

        if isinstance(item, Report):
            total_exp += item.exp * count

    return total_exp


def calculate_student_count(
    inventory: dict[int, int],
    target_level: int,
) -> int:
    """そのLvにできる生徒数"""
    required_exp = STUDENT_REQUIRED_EXP[target_level]
    total_exp = calculate_total_report_exp(inventory)

    return f"{total_exp / required_exp:.2f}"


def example1():
    # 所持レポート数から
    # 所持アイテム (アイテムID: 個数)
    inventory: dict[int, int] = {
        1001: 10788,  # 初級レポート
        1002: 1109,  # 中上級レポート
        1003: 141,  # 上級レポート
        1004: 53,  # 最上級レポート
    }

    total_exp = calculate_total_report_exp(inventory)

    print(f"合計経験値: {total_exp:,}")

    for level in (80, 90):
        count = calculate_student_count(inventory, level)
        print(f"Lv{level}: {count}人")

    # ->
    # 合計経験値: 1,905,900
    # Lv80: 3.10人
    # Lv90: 1.53人
    # 特別依頼1週間回って最上級・上級レポートそれぞれ300個以上手に入れたはずなのに今これ
