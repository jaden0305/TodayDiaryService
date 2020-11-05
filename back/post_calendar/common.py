import calendar
import datetime
from dateutil.relativedelta import relativedelta


def date_to_dict(year, month):
    year, month = int(year), int(month)

    before_month = []
    this_month = []
    after_month = []
    
    this_month_starts, day_count = calendar.monthrange(year, month)
    start_date = datetime.datetime(year, month, 1)
    total_day = 0

    # week = 0
    for count in range(day_count):
        # if len(this_month) <= week:
        #     this_month.append(list())
        result = start_date + datetime.timedelta(days=count)
        result_day = result.day
        result_week = (result.weekday() + 1) % 7
        # this_month[week].append({
        #     "week": result_week,
        #     "day": result_day})
        this_month.append({
            "year": result.year,
            "week": result_week,
            "day": result_day,
            "month": month})

        # if result_week == 6:
        #     week += 1
    for w in this_month:
        total_day += len(w)

    # week = 0
    flag = False
    for count in range(1, 14):
        # if len(before_month) <= week:
        #     before_month.append(list())
        result = start_date - datetime.timedelta(days=count)
        result_day = result.day
        result_week = (result.weekday() + 1) % 7 
        if result_week == 6:
            break
        else:
            flag = True
        # before_month[week].append({
        #     "week": result_week,
        #     "day": result_day})
        before_month.append({
            "year": result.year,
            "week": result_week,
            "day": result_day,
            "month": result.month})
        
    before_month = list(reversed(before_month))
    for w in before_month:
        total_day += len(w)

    # week = 0
    flag = False
    end_date = datetime.datetime(year, month, day_count)
    for count in range(1, 14):
        # if len(after_month) <= week:
        #     after_month.append(list())
        result = end_date + datetime.timedelta(days=count)
        result_day = result.day
        result_week = (result.weekday() + 1) % 7
        if result_week == 0:
            if flag and total_day // 7 >= 6:
                break
            # else:
            #     week += 1
            #     if len(after_month[week-1]) == 0:
            #         week -= 1
        else:
            flag = True
        # if len(after_month) <= week:
        #     after_month.append(list())
        # after_month[week].append({
        #     "week": result_week,
        #     "day": result_day})
        after_month.append({
            "year": result.year,
            "week": result_week,
            "day": result_day,
            "month": result.month})
        total_day += 1
    
    before = (start_date - relativedelta(months=1)).month
    after = (start_date + relativedelta(months=1)).month
    return {
        before: before_month,
        month: this_month,
        after: after_month,
    }

    
if __name__ == "__main__":
    from pprint import pprint
    pprint(date_to_dict(2020, 1))