import os
from pathlib import Path
from datetime import date
import pandas as pd



async def create_excel_report(
    data_list: list,
    output_dir: str = 'excel_files'
) -> Path:

    # 1. Создать папку, если её нет
    out_path = Path(output_dir)
    if not out_path.exists():
        out_path.mkdir(parents=True)
    
    # 2. Сформировать имя файла
    today = date.today().isoformat()  # 'YYYY-MM-DD'
    filename = today + '_report.xlsx'
    file_path = out_path / filename
    
    # 3. Подготовить Лист1
    columns1 = ['id', 'Номер машины', 'Марка', 'Год', 'Цвет', 'Из', 'Куда', 'Цена']
    df1 = pd.DataFrame(data_list, columns=columns1)
    
    total_price = df1['Цена'].sum()

    # 5. Добавляем пустую строку и проставляем только в колонке 'Год'
    #    df.loc[next_index, col] использован, чтобы не применять append/concat.
    next_index = len(df1)
    df1.loc[next_index, :] = ''         # сначала заполняем всю строку пустыми строками
    df1.loc[next_index, 'Цена'] = total_price  # а в 'Год' — сумму

    # 4. Записать в Excel — только Лист1
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        df1.to_excel(writer, sheet_name='Лист1', index=False)
        for column in df1:
            
            column_width = max(df1[column].astype(str).map(len).max(), len(column))+5
            col_idx = df1.columns.get_loc(column)
            writer.sheets['Лист1'].set_column(col_idx, col_idx, column_width)

        

    return file_path
