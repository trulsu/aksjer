/***
 * Get chart by ID
 */
(function (H) {
    H.getChartById = function (id) {
        return H.charts[document.getElementById(id).getAttribute('data-highcharts-chart')];
    };
}(Highcharts));

/***
 * MAIN DEMO
 */
window.onload = function () {

    function isNavigatorAxis(axis) {
        return axis.userOptions.className === 'highcharts-navigator-yaxis';
    }

    function getLastAxis(chart) {
        var axes = chart.yAxis,
            len = axes.length - 1;

        // If last yAxis is from navigator, return the previous one:
        return isNavigatorAxis(axes[len]) ? axes[len - 1] : axes[len];
    }

    function getHeight() {
        return Math.max(400,Math.min(1000, Math.round(window.innerHeight - Highcharts.offset(document.getElementById('demo')).top - 16)));
    }

    document.getElementById('container-inner').style.height = getHeight() + 'px';

    var indicatorsList = ['rsi', 'sma'],
        indicatorContainer = document.getElementById('indicators-container'),
        indicatorsButton = document.getElementById('indicators-dropdown'),
        advOptions = {
            chart: {
                type: 'candlestick',
                panning: false,
                spacingLeft: 50,
                alignTicks: false,
                // Keep events for cursor change:
                plotBackgroundColor: 'transparent'
            },
            plotOptions: {
                series: {
                    marker: {
                        enabled: false
                    },
                    dataGrouping: {
                        enabled: false
                    },
                    point: {
                        events: {
                            click: function () {
                                var annotation = Highcharts.Annotation[this.series.chart.annotating];

                                if (annotation && annotation.onPointClick) {
                                    annotation.onPointClick(this);
                                }
                            }
                        }
                    }
                }
            },
            rangeSelector: {
                buttonPosition: {
                    align: 'center',
                    x: 0,
                    y: 0
                },
                inputPosition: {
                    y: 0,
                    align: 'right',
                    x: -90
                },
                buttonTheme: {
                    fill: '#ffffff',
                    stroke: '#cccccc',
                    'stroke-width': 0,
                    width: '10px',
                    style: {
                        color: '#707070'
                    },
                    states: {
                        hover: {
                            fill: '#fff',
                            style: {
                                fontWeight: 'normal',
                                color: '#333333'
                            }
                        },
                        select: {
                            fill: '#fff',
                            style: {
                                fontWeight: 'normal',
                                color: '#29ABE2'
                            }
                        }
                    }
                },
                selected: 3,
                buttons: [{
                    type: 'day',
                    count: 7,
                    text: '1W'
                }, {
                    type: 'month',
                    count: 1,
                    text: '1M'
                }, {
                    type: 'month',
                    count: 3,
                    text: '3M'
                }, {
                    type: 'month',
                    count: 6,
                    text: '6M'
                }, {
                    type: 'all',
                    text: 'All'
                }]
            },
            responsive: {
                rules: [{
                    chartOptions: {
                        rangeSelector: {
                            buttonPosition: {
                                align: 'left',
                                x: 130
                            }
                        }
                    },
                    condition: {
                        maxWidth: 1250
                    }
                }, {
                    chartOptions: {
                        rangeSelector: {
                            buttonPosition: {
                                align: 'left',
                                x: 120
                            },
                            inputPosition: {
                                x: -75
                            }
                        }
                    },
                    condition: {
                        maxWidth: 950
                    }
                }, {
                    chartOptions: {
                        rangeSelector: {
                            buttonPosition: {
                                align: 'left',
                                x: 0,
                                y: 40
                            },
                            inputPosition: {
                                align: 'right',
                                x: 0,
                                y: 40
                            }
                        }
                    },
                    condition: {
                        maxWidth: 900
                    }
                }]
            },
            yAxis: [{
                height: '50%',
                resize: {
                    enabled: true,
                    controlledAxis: {
                        next: [1]
                    },
                    lineWidth: 4
                }
            }, {
                top: '50%',
                height: '50%',
                id: 'rsi'
            }],
            navigator: {
                yAxis: {
                    lineWidth: 0
                },
                xAxis: {
                    plotBands: [{
                        color: '#fff',
                        from: -Infinity,
                        to: Infinity
                    }]
                }
            },
            series: [{
                cropThreshold: 0,
                id: 'main',
                name: 'AAPL',
                data: [],
                tooltip: {
                    valueDecimals: 2
                },
                allowPointSelect: true
            }, {
                linkedTo: 'main',
                type: 'sma',
                id: 's-sma',
                params: {
                    period: 14
                },
                styles: {
                    'stroke-width': 1,
                    stroke: '#8ddd54',
                    dashstyle: 'solid'
                }
            }, {
                linkedTo: 'main',
                type: 'rsi',
                id: 's-rsi',
                params: {
                    period: 14
                },
                yAxis: 1,
                styles: {
                    'stroke-width': 1,
                    stroke: '#6ba583',
                    dashstyle: 'solid'
                }
            }]
        },
        defaultData = false;


    function attachEvents() {
        var selectDropdowns;
        function manageIndicators(value, adder, useAxis) {
            var index = -1,
                chart = Highcharts.getChartById('container-inner'),
                lastYAxis = getLastAxis(chart),
                lastYAxisIndex,
                previousYAxis,
                newHeight,
                nextAxis;

            chart.series.forEach(function (e, i) {
                if (e.options.type === value) {
                    index = i;
                }
            });

            if (adder) {
                if (useAxis) {
                    chart.addAxis({
                        top: lastYAxis.top + lastYAxis.height / 2,
                        height: lastYAxis.height / 2,
                        opposite: true,
                        minLength: 50,
                        id: value,
                        title: {
                            text: ''
                        }
                    }, false);
                    lastYAxis.update({
                        height: lastYAxis.height / 2,
                        resize: {
                            enabled: true,
                            controlledAxis: {
                                next: [value]
                            },
                            lineWidth: 4
                        }
                    }, false);
                }

                var lastIndicator = chart.addSeries({
                    linkedTo: 'main',
                    id: 's-' + value,
                    type: value,
                    yAxis: useAxis ? chart.yAxis.length - 1 : 0,
                    styles: {
                        'stroke-width': 1,
                        dashstyle: 'solid'
                    }
                });

                // set extremes i.e for Ichimoku
                chart.xAxis[0].setExtremes(chart.xAxis[0].min, lastIndicator.xData[lastIndicator.xData.length - 1]);

            } else {
                if (useAxis) {
                    // Remove last Axis
                    lastYAxis = chart.series[index].yAxis;
                    lastYAxisIndex = chart.yAxis.indexOf(lastYAxis);
                    newHeight = lastYAxis.height;
                    lastYAxis.remove(false);
                    // Now update previous Axis to fill the new space:
                    previousYAxis = isNavigatorAxis(chart.yAxis[lastYAxisIndex - 1]) ?
                        chart.yAxis[lastYAxisIndex - 2] : chart.yAxis[lastYAxisIndex - 1];

                    // If we removed last axis, go back by one:
                    if (!chart.yAxis[lastYAxisIndex]) {
                        lastYAxisIndex -= 1;
                    }

                    nextAxis = !isNavigatorAxis(chart.yAxis[lastYAxisIndex]) ?
                        chart.yAxis[lastYAxisIndex] : Highcharts.pick(
                            chart.yAxis[lastYAxisIndex + 1], // next if exists
                            chart.yAxis[lastYAxisIndex - 1] // previous otherwise
                        );

                    previousYAxis.update(
                        Highcharts.merge(
                            {
                                height: previousYAxis.height + newHeight
                            },
                            // If first yAxis on chart, and the only one, or
                            // it is last yAxis on the chart or
                            // it is a predefined axis on chart init
                            // then disable resizer:
                            previousYAxis === chart.yAxis[0] && chart.yAxis.length === 2 ||
                            previousYAxis === chart.yAxis[chart.yAxis.length - 1] ||
                            (
                                previousYAxis === chart.yAxis[chart.yAxis.length - 2] &&
                                chart.navigator.yAxis === chart.yAxis[chart.yAxis.length - 1]
                            ) ? // navigator jump
                            {
                                resize: {
                                    enabled: false
                                }
                            } :
                            // Otherwise set new reference for the next axis:
                            {
                                resize: {
                                    controlledAxis: {
                                        next: [nextAxis.options.id]
                                    }
                                }
                            }
                        )
                    );
                } else {
                    chart.series[index].remove();
                }
            }
        }

        selectDropdowns = document.querySelectorAll('#menu-nav .select-dropdown');

        selectDropdowns.forEach(function (dropdown) {
            dropdown.addEventListener('click', function (e) {
                var button = e.target, dropdownMenu = button.nextElementSibling;

                if (dropdownMenu.style.display === 'block') {
                    button.classList.remove('dropdown-active');
                    dropdownMenu.style.display = 'none';
                } else {
                    button.classList.add('dropdown-active');
                    dropdownMenu.style.display = 'block';
                }
            });
        });

        document.addEventListener('click', function (e) {
            var target = e.target,
                isIndica = target.getAttribute('id') === 'indicators-dropdown',
                hiders = [],
                removers = [];

            if (!isIndica) {
                if (indicatorsButton) {
                    indicatorsButton.classList.remove('dropdown-active');
                }
                document.querySelectorAll('#indicators-container .dropdown-menu').forEach(function (dropdown) {
                    dropdown.style.display = 'none';
                });
            }
        });

        document.querySelectorAll('#indicators-container .dropdown-menu a').forEach(function (link) {
            link.addEventListener('click', function (e) {
                var target = e.currentTarget,
                    val = target.getAttribute('data-value'),
                    useAxis = target.getAttribute('data-axis'),
                    inp = target.querySelectorAll('input')[0],
                    idx;

                if ((idx = indicatorsList.indexOf(val)) > -1) {
                    indicatorsList.splice(idx, 1);
                    setTimeout(function () {
                        inp.checked = false;
                    }, 0);
                    manageIndicators(val, false, useAxis);
                } else {
                    indicatorsList.push(val);
                    setTimeout(function () {
                        inp.checked = true;
                    }, 0);
                    manageIndicators(val, true, useAxis);
                }

                e.target.blur();

                return false;
            });
        });
    }

    /* Load data for charts */
    Highcharts.ajax({
        url: 'https://www.highcharts.com/samples/data/aapl-ohlc.json',
        dataType: 'text',
        success: function (data) {
            data = data.replace(/\/\*.*\*\//g, '');
            data = JSON.parse(data);
            advOptions.series[0].data = data;
            attachEvents(Highcharts.stockChart('container-inner', Highcharts.extend({}, advOptions)));
        }
    });

    // Initial select:
    indicatorsList.forEach(function (ind) {
        indicatorContainer.querySelectorAll('a[data-value="' + ind + '"] input')[0].checked = true;
    });

    // Adapt height on resize
    window.addEventListener('resize', function () {
        var height = getHeight();
        document.getElementById('container-inner').style.height = height + 'px';
        Highcharts.getChartById('container-inner').setSize(undefined,height,false);
    });
};
