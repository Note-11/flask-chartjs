# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)
global table, flag

flag = 1
table = None

@app.route('/', methods=['GET'])
def dashboard():
    global table
    # Load Excel data
    import_excel()

    # Get selected transaction from dropdown
    selected_num = request.args.get('transaction_id')
    # if selected_num is not None:
    #     selected_num = int(selected_num)
    # else:
    #     selected_num = None

    # Labels and chart data
    labels = table['TransactionID'].tolist()
    amount_values = [float(x) for x in table['Amount'].tolist()]
    risk_values = [float(x) for x in table['RiskScore'].tolist()]
    flagged_count = [
        int(table['Flagged'].value_counts().get(0, 0)),
        int(table['Flagged'].value_counts().get(1, 0))
    ]

    # Highlight selected transaction
    highlight_index = labels.index(selected_num) if selected_num in labels else None

    info = {
        'total_transactions': int(len(table)),
        'total_flagged': int(table['Flagged'].sum()),
        'total_not_flagged': int(len(table) - table['Flagged'].sum()),
        'selected_transaction': selected_num
    }

    return render_template('graph.html',
                           labels=labels,
                           amount_values=amount_values,
                           risk_values=risk_values,
                           flagged_count=flagged_count,
                           info=info,
                           highlight_index=highlight_index)

def import_excel():
    global table, flag
    if flag:
        print("Loading Table.xlsx ...")
        table = pd.read_excel(io="Table.xlsx", sheet_name='I', header=0)
        table.fillna(0, inplace=True)
        flag = 0
    else:
        print("Excel already loaded, skipping reload.")

if __name__ == '__main__':
    app.secret_key = 'mykey'
    app.run(port=5000, debug=True)
