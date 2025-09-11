s = input().split()
n = int(s[0])
m = int(s[1])

n_even = n - (n % 2)
m_remainder = m % 2
m_even = m - (m % 2)

t1 = n * (m_even / 2)
t2 = (m_remainder * (n_even / 2))

print(round(t1 + t2))
