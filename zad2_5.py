#Lista par (x,y), gdzie x jest liczbą całkowitą
# z przedziału [4,7], a y jednym znapisów
# 'jabłko', 'gruszka' lub 'komputer'

print([(x,y) for x in range(4,8,1) for y in ["jablko", "gruszka", "komputer"]])