# Define constants
MOD = 1000000007  # Modulo value
MAXN = 1000  # Maximum value for the range of indices

# Initialize arrays
T = [[0] * (MAXN + 1) for _ in range(MAXN + 1)]  # 2D array
B = [0] * (MAXN + 1)  # 1D array
G = [0] * (MAXN + 1)  # 1D array

def init():
    """
    Initializes the 2D array 'T' based on specific recurrence relations.
    """
    T[1][0] = 1
    for j in range(1, MAXN + 1):
        T[1][j] = T[1][j - 1]
        if j >= 2:
            T[1][j] = (T[1][j] + T[1][j - 2]) % MOD
        if j >= 3:
            T[1][j] = (T[1][j] + T[1][j - 3]) % MOD
        if j >= 4:
            T[1][j] = (T[1][j] + T[1][j - 4]) % MOD
    for i in range(2, MAXN + 1):
        for j in range(1, MAXN + 1):
            T[i][j] = (T[i - 1][j] * T[1][j]) % MOD

# Initialize 'T' array
init()

# Take input for 'n' and 'm'
n = int(input())
m = int(input())

# Initialize arrays 'B' and 'G'
B[1] = 0
G[1] = 1

# Compute values for 'B' and 'G' using dynamic programming
for j in range(2, m + 1):
    B[j] = 0
    for k in range(1, j):
        B[j] = (B[j] + (T[n][j - k] * G[k]) % MOD) % MOD
    G[j] = (T[n][j] + MOD - B[j]) % MOD

# Print the result
print(G[m])
                                                                                                                            