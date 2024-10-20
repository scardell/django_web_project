from django.shortcuts import render

# Create your views here.
""" 
def chart_view(request):
    data = {
        'categories': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'data': [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
    }
    return render(request, 'charts/chart.html', data) """

def chart_view(request):
    data = {
        'series': [
            {
                'name': 'Browsers',
                'colorByPoint': True,
                'data': [
                    {
                        'name': 'Chrome',
                        'y': 61.41,
                        'drilldown': 'Chrome'
                    },
                    {
                        'name': 'Edge',
                        'y': 11.84,
                        'drilldown': 'Edge'
                    },
                    {
                        'name': 'Firefox',
                        'y': 10.85,
                        'drilldown': 'Firefox'
                    },
                    {
                        'name': 'Safari',
                        'y': 4.67,
                        'drilldown': 'Safari'
                    },
                    {
                        'name': 'Other',
                        'y': 2.61,
                        'drilldown': None  # No drilldown para esta sección
                    }
                ]
            }
        ],
        'drilldown_series': [
            {
                'name': 'Chrome',
                'id': 'Chrome',  # El ID debe coincidir con el drilldown de 'Chrome'
                'data': [
                    ['v95.0', 24.13],
                    ['v96.0', 17.2],
                    ['v97.0', 8.11]
                ]
            },
            {
                'name': 'Edge',
                'id': 'Edge',  # El ID debe coincidir con el drilldown de 'Edge'
                'data': [
                    ['v95.0', 10.5],
                    ['v96.0', 5.34]
                ]
            },
            {
                'name': 'Firefox',
                'id': 'Firefox',  # El ID debe coincidir con el drilldown de 'Firefox'
                'data': [
                    ['v92.0', 6.2],
                    ['v93.0', 3.1]
                ]
            },
            {
                'name': 'Safari',
                'id': 'Safari',  # El ID debe coincidir con el drilldown de 'Safari'
                'data': [
                    ['v14.1', 2.5],
                    ['v15.0', 1.7]
                ]
            }
        ]
    }
    return render(request, 'charts/chart.html', data)
