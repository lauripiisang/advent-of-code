import re


for file in [
    # 'day3-1-sample.txt',
    'day3.txt'
]:
    print(f"file - {file}")
    sumtotal = 0
    with open(file) as f:
        stopProcessing = False
        for line in f:
            m = re.finditer(r"(mul\((?P<firstnum>\d+),(?P<secondnum>\d+)\))|(?P<onoff>(?:don't\(\))|(?:do\(\)))", line)
            if not m:
                print(f"no match in {line}")
                continue
            sum = 0

            for (onoff, first, second) in [x.group('onoff', 'firstnum','secondnum') for x in m]:
                if onoff:
                    stopProcessing = True if onoff == "don't()" else False
                if stopProcessing:
                    if first and second:
                        print(f"Processing stopped, skipping {first} * {second}")
                    continue
                if onoff == 'do()':
                    print("Resuming processing")
                    continue
                print(f"doing {first} * {second}")
                sum += int(first) * int(second)
                print(f"sum - {sum}")
            sumtotal += sum
        print(f"sum total - {sumtotal}")