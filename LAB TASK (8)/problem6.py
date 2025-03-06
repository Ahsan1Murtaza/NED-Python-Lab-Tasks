def month(n):
    name="JanFebMarAprMayJunJulAugSepOctNovDec"

    return name[(n-1)*3:n*3]

print(month(1))
print(month(8))