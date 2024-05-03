def compareVersions(version1, version2):
    version1 = list(map(int, version1.split('.')))
    version2 = list(map(int, version2.split('.')))
    max_length = max(len(version1), len(version2))
    min_length = min(len(version1), len(version2))
    version1.extend([0] * (max_length - len(version1)))
    version2.extend([0] * (max_length - len(version2)))
    if min_length >= 1:
        for i in range(max_length):
            tmp1 = version1[i]
            tmp2 = version2[i]
            if tmp1 != tmp2:
                if tmp1 < tmp2:
                    return -1
                elif tmp1 > tmp2:
                    return 1
        return 0

compareVersions("0.1", "1.0")