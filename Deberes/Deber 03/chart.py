import xlsxwriter
import pandas as pd


path_guardado = "../py-jaramillo-rojas-ronny-xavier/Deberes/Deber 03/artwork_data.pickle"
df = pd.read_pickle(path_guardado)
sub_df = df.iloc[49980:50519, :].copy()
num_artistas = sub_df['artist'].value_counts()
rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)


workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})


headings = ['Artist', 'Occurrences']
data = [
    num_artistas.index,
    num_artistas.values,
]


worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

######Gráfico de barras############
chart1 = workbook.add_chart({'type': 'bar'})

chart1.add_series({		#A2 hasta AN
    'categories': '=Sheet1!$A$2:$A${}'.format(len(num_artistas.index)+1),
    				#B2 hasta BN
    'values':     '=Sheet1!$B$2:$B${}'.format(len(num_artistas.index)+1),
})

chart1.set_title ({'name': 'Artists occurrences'})
chart1.set_x_axis({'name': 'Occurrences'})
chart1.set_y_axis({'name': 'Artist'})

chart1.set_style(11)

worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

######Gráfico de pastel############
chart2 = workbook.add_chart({'type': 'pie'})

chart2.add_series({
	'name': 'Artist',
    'categories': '=Sheet1!$A$2:$A${}'.format(len(num_artistas.index)+1),
    'values':     '=Sheet1!$B$2:$B${}'.format(len(num_artistas.index)+1),
})

chart2.set_title({'name': 'Popular Artists'})

chart2.set_style(10)

worksheet.insert_chart('D18', chart2, {'x_offset': 25, 'y_offset': 10})

workbook.close()

