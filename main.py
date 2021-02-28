import csv, operator, itertools

with open('ledgers.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # filters the list to keep only the deposits
    deposits = [d for d in csv_reader if d['type']=='deposit']
    
    # removes duplicates (for some reason each deposit appears twice in the file)
    ref_ids = []
    deposits_no_duplicates = []
    for dep in deposits:
        if dep['refid'] not in ref_ids:
            ref_ids.append(dep['refid'])
            deposits_no_duplicates.append(dep)
    
    # sorts the list of deposits by asset
    deposits_no_duplicates.sort(key=operator.itemgetter('asset'))
    
    # groups deposits by assets for each asset
    for asset, deposits_of_asset in itertools.groupby(deposits_no_duplicates, key=operator.itemgetter('asset')):
        total_amount = 0.0
        for deposit in deposits_of_asset:
            total_amount = total_amount + float(deposit['amount'])
        
        print(f"You have invested {total_amount} {asset} since the start.")
