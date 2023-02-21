n_side = int(input('Enter the row number: '))
m_side = int(input('Enter the column number: '))
k_countBar = int(input('Enter the num of bars you want: '))
if (k_countBar % n_side == 0 or k_countBar % m_side == 0) and k_countBar <= n_side * m_side:
    print(k_countBar, 'yes')
else:
    print(k_countBar, 'no')