latencies = [
    120,
    95,
    140,
    110,
    88,
    205,
    130,
    99,
    160,
    150,
    102,
    118,
    190,
    91,
    175,
    133,
    108,
    96,
    185,
    145,
]

p50 = 0

if len(latencies) % 2 == 0:
    latencies.sort()
    p50 = (
        latencies[int((len(latencies) / 2) - 1)] + latencies[int(len(latencies) / 2)]
    ) / 2
else:
    latencies.sort()
    p50 = latencies[int(((len(latencies) + 1) / 2) - 1)]

print(p50)

p95 = 0

if len(latencies) % 2 == 0:
    latencies.sort()
    p95 = latencies[int(len(latencies) * 0.95 - 1)]
else:
    latencies.sort()
    p95 = latencies[round(len(latencies) * 0.95)]

print(p95)

if p95 > 300:
    print("SLO 위반")
elif p95 > 200:
    print("주의")
else:
    print("정상")
