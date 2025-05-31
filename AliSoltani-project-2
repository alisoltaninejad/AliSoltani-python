#محاسبه تغداد روز های زندگی کرده
print("تاریخ تولد را وارد کن:")
birth_year = int(input("سال تولد: "))
birth_month = int(input("ماه تولد: "))
birth_day = int(input("روز تولد: "))

print("\nتاریخ امروز را وارد کن:")
today_year = int(input("سال امروز: "))
today_month = int(input("ماه امروز: "))
today_day = int(input("روز امروز: "))

birth_total_days = birth_year * 365 + birth_month * 30 + birth_day
today_total_days = today_year * 365 + today_month * 30 + today_day

days_lived = today_total_days - birth_total_days

if days_lived < 0:
    print("\nتاریخ تولد از امروز جلوتره!")
else:
    print("\nشما حدوداً", days_lived, "روز زندگی کرده‌اید.")
