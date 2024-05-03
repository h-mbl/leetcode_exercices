def compareVersions(a, b):
    a = a.strip()
    b = b.strip()
    if len(a) >= 1 and len(b) >= 1 :
        version1 = a.split(".")
        version2 = b.split(".")
        # egaliser les lens
        if len(version1) < len(version2):
            version1 = version1 + ["0"] * (len(version2) - len(version1))
        elif len(version1) > len(version2):
            version2 = version2 + ["0"] * (len(version1) - len(version2))
        for i in range(len(version1)) :
            if int(version1[i]) != int(version2[i]) :
                if int(version1[i]) < int(version2[i]) :
                    print("-1")
                    return -1
                elif int(version1[i]) > int(version2[i]) :
                    print("1")
                    return 1
            else :
                continue
        print("0")
        return 0

compareVersions("0.1", "1.0")