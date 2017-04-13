import datetime
import sys

import vim

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def get_timestamp(inp, time=''):
    """
    generate a timestamp from a string like 3wed
    which is the 3rd. wedesday from now on. Omitting
    a count means it is the next one.
    """
    # initial values and args
    repeat = 1
    day = inp
    if inp[0] in "123456789":
        repeat = int(inp[0])
        day = inp[1:].lower()
    if day not in days:
        print "Invalid day given! Possible values: 'mon', 'tue', 'wed'..."
        return

    today = datetime.date.today()
    # today's weekday
    current_weekday = today.weekday()
    # weekday of target
    target_weekday = days.index(day)

    # find the next day that matches the name given
    if current_weekday < target_weekday:
        delta1 = target_weekday - current_weekday
    else:
        delta1 = 7 - (current_weekday - target_weekday)

    # get the date
    target = today + datetime.timedelta(
        days=(repeat-1)*7 + delta1)
    ts = target.strftime("[%Y-%m-%d]")

    # handle optional time
    if time:
        ts = ts[:-1] + ":" + time + "]"

    # return our results
    return ts


def insert(index):
    prefix = vim.eval("a:mode")
    if prefix not in ["T", "S", "D"]:
        prefix = "T"
    if sys.argv != ["exact"]:
        ts = get_timestamp(vim.eval("a:desc"))
    else:
        ts = get_timestamp(vim.eval("a:desc"), vim.eval("a:time"))
    vim.current.line = l[:index] + " " + \
        prefix + ts + l[index:]

if __name__ == '__main__':
    l = vim.current.line
    padd = 3
    index = l.find("[ ]")
    if index == -1:
        index = l.find("[x]")
    if index == -1:
        padd = 1
        index = l.find("*")
    if index == -1:
        index = l.find("+")
    if index == -1:
        index = l.find("-")
    if index == -1:
        index = l.find(".")
    if index >= 0:
        insert(index + padd)
