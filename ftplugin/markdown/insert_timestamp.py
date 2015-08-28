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
    repeat = 1
    day = inp
    if inp[0] in "123456789":
        repeat = int(inp[0])
        day = inp[1:].lower()
    if day not in days:
        print "Invalid day given! Possible values: 'mon', 'tue', 'wed'..."
        return
    today = datetime.date.today()
    current_day = today.weekday()
    target = today + datetime.timedelta(
        days=(repeat-1)*7 + days.index(day) + (7 - current_day))
    ts = target.strftime("[%d.%m.%Y]")
    if time:
        ts = ts[:-1] + ":" + time + "]"
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
