import re


def get_warm_durations(file_path):
    durations = []
    with open(file_path, "r") as f:
        content = f.read()
    reports = [r for r in content.split("REPORT RequestId:") if r.strip()]
    for report in [r for r in reports if "Init Duration:" not in r]:
        match = re.search(r"Duration:\s+([\d.]+)\s+ms", report)
        if match:
            durations.append(float(match.group(1)))
    return durations


zip_warm = get_warm_durations("results/cloudwatch-zip-reports.txt")
cont_warm = get_warm_durations("results/cloudwatch-container-reports.txt")

zip_init = 571.53
zip_cold_h = 37.64
zip_cold_client = 1.4463 * 1000
zip_warm_client = 0.0965 * 1000

cont_init = 560.87
cont_cold_h = 85.12
cont_cold_client = 1.3657 * 1000
cont_warm_client = 0.0977 * 1000


def analyze(name, warm_handlers, init, cold_h, cold_c, warm_c):
    avg_warm_h = sum(warm_handlers) / len(warm_handlers) if warm_handlers else 0
    cold_rtt = cold_c - init - cold_h
    warm_rtt = warm_c - avg_warm_h

    print(f"--- {name} Results ---")
    print(f"Init Duration: {init} ms")
    print(f"Average Warm Handler: {avg_warm_h:.2f} ms")
    print(f"Cold RTT: {cold_rtt:.2f} ms")
    print(f"Warm RTT: {warm_rtt:.2f} ms")
    print()
    return avg_warm_h, cold_rtt, warm_rtt


zip_res = analyze(
    "ZIP", zip_warm, zip_init, zip_cold_h, zip_cold_client, zip_warm_client
)
cont_res = analyze(
    "CONTAINER", cont_warm, cont_init, cont_cold_h, cont_cold_client, cont_warm_client
)
