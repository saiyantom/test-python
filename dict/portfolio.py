portfolio ={'accounts': ['SBI', 'IOB'],
            'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
            'ornaments': ['10 gm gold', '1 kg silver']
           }

print(f'Original: {portfolio}')

new_pair = {'MF': ['Relaince', 'ABSL']}
portfolio.update(new_pair)
portfolio['accounts'] = ['Axis', 'BOB']

share_values = portfolio['shares']
share_values.sort()

print(f'Sorted shares: {share_values}')
portfolio['ornaments']=''

print(f'Final: {portfolio}')
