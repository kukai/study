# 指定した月の日本の祝日一覧を出力するコマンドラインスクリプト
import jpholiday
import datetime
import sys

def print_japanese_holidays_of_specific_month(year=None, month=None):
    # 引数がなければ現在の年と月を取得
    if year is None:
        specific_year = datetime.datetime.now().year
    else:
        specific_year = year
    if month is None:
        specific_month = datetime.datetime.now().month
    else:
        specific_month = month
    
    # 今月の祝日一覧を取得
    holidays = [holiday for holiday in jpholiday.month_holidays(specific_year, specific_month)]

    # 祝日があるかどうか確認し、あれば出力
    if holidays:
        for date, name in holidays:
            print(f"{date.strftime('%Y-%m-%d')} {name}")
    else:
        print("この月には祝日がありません。")

if __name__ == "__main__":
    # コマンドライン引数から年月を読み取り
    if len(sys.argv) > 1:
        try:
            year_month_str = sys.argv[1]
            year, month = map(int, year_month_str.split('-'))
            print_japanese_holidays_of_specific_month(year, month)
        except ValueError:
            print("引数の形式が正しくありません。YYYY-MM形式で入力してください。")
    else:
        print_japanese_holidays_of_specific_month()

