import pandas as pd
import json
import sys


def list_check(ipath, opath):
    data = pd.read_csv(ipath)
    unique_op = []
    with pd.ExcelWriter(opath) as xlw:
        for op in data.iterrows():
            op_row = op[1]['Operations']
            if op_row in unique_op:
                continue
            else:
                unique_op.append(op_row)
        for op_cat in unique_op:
            new_op = data.loc[data['Operations'] == op_cat]
            new_op = pd.DataFrame(new_op)
            for row in new_op.iterrows():
                load_ad = json.loads(row[1]['AuditData'])
                for a in load_ad:
                    b = load_ad[a]
                    if type(b) == list and len(b) >= 1:
                        main_list = expand_list(a, b)
                        for c in main_list:
                            new_op.loc[row[0], c] = main_list[c]
                    elif type(b) == int or type(b) == bool:
                        new_op.loc[row[0], a] = b
                    elif type(b) == dict:
                        for d in b:
                            collumn_name = f'{a}-{d}'
                            main_dict = expand_dict(collumn_name, b)
                            for e in main_dict:
                                new_op.loc[row[0], e] = main_dict[e]
                    elif len(b) >= 1:
                        new_op.loc[row[0], a] = b
                    else:
                        continue
            new_op.pop('AuditData')
            if len(op_cat) > 31:
                op_cat = op_cat[:30]
            new_op.to_excel(xlw, sheet_name=op_cat, index=False)


def expand_dict(a, b):
    collection = {}
    for c in b:
        dict_value = b[c]
        column_name = f'{a}-{c}'
        if type(dict_value) == list:
            el = expand_list(column_name, dict_value)
            collection.update(el)
        elif type(dict_value) == dict:
            ed = expand_dict(column_name, dict_value)
            collection.update(ed)
        else:
            collection.update({column_name: dict_value})
    return collection


def expand_list(a, b):
    collection = {}
    for c in b:
        if type(c) == str:
            out = ''
            for string in b:
                out += f'     {string}'
            out = out[(-len(out) + 5):]
            out = out.replace('     ', ', ')
            return {a: out}
        for d in c:
            e = c[d]
            column_name = f'{a}-{d}'
            if type(e) == list:
                el = expand_list(column_name, e)
                collection.update(el)
            elif type(e) == dict:
                ed = expand_dict(column_name, e)
                collection.update(ed)
            else:
                collection.update({column_name: e})
    return collection


if __name__ == '__main__':
    if '-h' in sys.argv:
        print('use: script.py input.csv output.xlsx')
    else:
        try:
            inp = sys.argv[1]
        except IndexError:
            print('Input needed EG: script.py input.csv output.xlsx')
            exit(0)
        try:
            output = sys.argv[2]
        except IndexError:
            output = 'default.xlsx'
        list_check(inp, output)
