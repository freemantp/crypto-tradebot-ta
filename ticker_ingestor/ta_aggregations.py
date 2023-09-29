macd_pipeline = [
                    {
                        "$group": {
                            "_id": {
                                "symbol": "$symbol",
                                "time": {
                                    "$dateTrunc": {
                                        "date": "$time",
                                        "unit": "minute",
                                        "binSize": 15,
                                    }
                                },
                            },
                            "price": {"$last": "$bid"},
                        }
                    },
                    {"$sort": {"_id.time": 1}},
                    {
                        "$setWindowFields": {
                            "partitionBy": "_id.symbol",
                            "sortBy": {"_id.time": 1},
                            "output": {
                                "ema_12": {
                                    "$expMovingAvg": {"input": "$price", "N": 12}
                                },
                                "ema_26": {
                                    "$expMovingAvg": {"input": "$price", "N": 26}
                                },
                            },
                        }
                    },
                    {"$addFields": {"macdLine": {"$subtract": ["$ema_12", "$ema_26"]}}},
                    {"$project": {"macdLine": 1}},
                    {
                        "$setWindowFields": {
                            "partitionBy": "_id.symbol",
                            "sortBy": {"_id.time": 1},
                            "output": {
                                "macdSignal": {
                                    "$expMovingAvg": {"input": "$macdLine", "N": 9}
                                }
                            },
                        }
                    },
                    {"$sort": {"_id.time": -1}},
                    {"$limit": 2}
                ]
rsi_pipeline = [
    {
        '$setWindowFields': {
            'partitionBy': '$_id.symbol', 
            'sortBy': {
                '_id.time': 1
            }, 
            'output': {
                'previousAskPrice': {
                    '$shift': {
                        'by': -1, 
                        'output': '$ask'
                    }
                }
            }
        }
    }, {
        '$addFields': {
            'diff': {
                '$subtract': [
                    '$ask', {
                        '$ifNull': [
                            '$previousAskPrice', '$ask'
                        ]
                    }
                ]
            }
        }
    }, {
        '$addFields': {
            'gain': {
                '$cond': {
                    'if': {
                        '$gte': [
                            '$diff', 0
                        ]
                    }, 
                    'then': '$diff', 
                    'else': 0
                }
            }, 
            'loss': {
                '$cond': {
                    'if': {
                        '$lte': [
                            '$diff', 0
                        ]
                    }, 
                    'then': {
                        '$abs': '$diff'
                    }, 
                    'else': 0
                }
            }
        }
    }, {
        '$setWindowFields': {
            'partitionBy': '$_id.symbol', 
            'sortBy': {
                '_id.time': 1
            }, 
            'output': {
                'avgGain': {
                    '$avg': '$gain', 
                    'window': {
                        'documents': [
                            -14, 0
                        ]
                    }
                }, 
                'avgLoss': {
                    '$avg': '$loss', 
                    'window': {
                        'documents': [
                            -14, 0
                        ]
                    }
                }, 
                'documentNumber': {
                    '$documentNumber': {}
                }
            }
        }
    }, {
        '$addFields': {
            'relativeStrength': {
                '$cond': {
                    'if': {
                        '$gt': [
                            '$avgLoss', 0
                        ]
                    }, 
                    'then': {
                        '$divide': [
                            '$avgGain', '$avgLoss'
                        ]
                    }, 
                    'else': '$avgGain'
                }
            }
        }
    }, {
        '$addFields': {
            'rsi': {
                '$cond': {
                    'if': {
                        '$gt': [
                            '$documentNumber', 14
                        ]
                    }, 
                    'then': {
                        '$subtract': [
                            100, {
                                '$divide': [
                                    100, {
                                        '$add': [
                                            1, '$relativeStrength'
                                        ]
                                    }
                                ]
                            }
                        ]
                    }, 
                    'else': None
                }
            }
        }
    },
    {"$sort": {"time": -1}},
    {"$limit": 2}
]