import pygal

# bar = pygal.Bar()
# bar.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
# bar.render_to_file('bar_chart.svg')

# bar_chart = pygal.StackedBar()
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
# bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
# bar_chart.render_to_file('prac.svg')

# bar_chart = pygal.StackedBar()
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
# bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
# bar_chart.render_to_file('n.svg')

# bar_chart = pygal.HorizontalStackedBar()
# bar_chart.title = "Remarquable sequences"
# bar_chart.x_labels = map(str, range(11))
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
# bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
# bar_chart.render_to_file('t.svg')

# line_chart = pygal.HorizontalLine()
# line_chart.title = 'Browser usage evolution (in %)'
# line_chart.x_labels = map(str, range(2002, 2013))
# line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
# line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
# line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
# line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# line_chart.range = [0, 100]
# line_chart.render_to_file('ev.svg')

# from datetime import datetime, timedelta
# date_chart = pygal.Line(x_label_rotation=20)
# date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
#  datetime(2013, 1, 2),
#  datetime(2013, 1, 12),
#  datetime(2013, 2, 2),
#  datetime(2013, 2, 22)])
# date_chart.add("Visits", [300, 412, 823, 672])
# date_chart.render_to_file('h.svg')

# hist = pygal.Histogram()
# hist.add('Wide bars', [(5, 0, 10), (4, 5, 13), (2, 0, 15)])
# hist.add('Narrow bars',  [(10, 1, 2), (12, 4, 4.5), (8, 11, 13)])
# hist.render_to_file('t.svg')

radar_chart = pygal.Radar()
radar_chart.title = 'V8 benchmark results'
radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
radar_chart.render_to_file('r.svg')