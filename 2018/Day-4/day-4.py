import datetime
import fileinput

lines = list(fileinput.input('4.txt'))
entries = [[datetime.datetime.strptime(line[1:17], '%Y-%m-%d %H:%M'), line[19:-1]] for line in lines]
entries.sort()
guard_sleep_timers = dict()
minutes_asleep = dict()


def part1():
    index = 0
    while index < len(entries):
        guard_id = entries[index][1].split()[1]
        total_sleep = guard_sleep_timers.setdefault(guard_id, 0)
        index += 1
        while index < len(entries) and entries[index][1].split()[0] != 'Guard':
            total_sleep += ((entries[index+1][0] - entries[index][0]).total_seconds()) / 60
            times_slept = minutes_asleep.setdefault(guard_id, dict())
            for minute in range((entries[index][0]).minute, (entries[index+1][0]).minute):
                count = times_slept.setdefault(minute, 0)
                count += 1
                times_slept.update({minute: count})
            minutes_asleep.update({guard_id: times_slept})
            index += 2
        guard_sleep_timers.update({guard_id: total_sleep})

    candidate = max(guard_sleep_timers, key=guard_sleep_timers.get)
    return max(minutes_asleep[candidate], key=minutes_asleep[candidate].get) * int(candidate[1:])


def part2():
    candidate = ""
    high_frequency = 0
    minute = 0
    for guard in minutes_asleep.keys():
        max_guard_freq_min, max_guard_freq = max(minutes_asleep[guard], key=minutes_asleep[guard].get), \
                                             max(minutes_asleep[guard].values())
        if max_guard_freq > high_frequency:
            candidate = guard
            high_frequency = max_guard_freq
            minute = max_guard_freq_min

    return minute * int(candidate[1:])


print(part1())
# 30630

print(part2())
# 136571
