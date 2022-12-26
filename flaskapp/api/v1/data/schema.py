from flask import request
from functools import wraps
from helper.formatter import ResponseModel
import json
from jsonschema import validate,Draft4Validator

SCHEMA = {
    "type": "array",
    "items": {
        "properties": {
            "PositionType": {"pattern": "^(?i)(sell|buy)$"},
            "Lots": {"type": "integer"},
            "LegStopLoss": {
                "properties": {
                    "Type": {
                        "pattern": "^(?i)(percentage|points|underlyingpercentage|underlyingpoints)$"
                    },
                    "Value": {"type": "number"},
                },
                "required": ["Value", "Type"],
            },
            "LegTarget": {
                "properties": {
                    "Type": {
                        "pattern": "^(?i)(percentage|points|underlyingpercentage|underlyingpoints)$"
                    },
                    "Value": {"type": "number"},
                },
                "required": ["Value", "Type"],
            },
            "LegTrailSL": {
                "properties": {
                    "Type": {"pattern": "^(?i)(percentage|points|none)$"},
                    "Value": {
                        "properties": {
                            "InstrumentMove": {"type": "number"},
                            "StopLossMove": {"type": "number"},
                        },
                        "required": ["StopLossMove", "InstrumentMove"],
                    },
                },
                "required": ["Value", "Type"],
            },
            "LegMomentum": {
                "properties": {
                    "Type": {
                        "pattern": "^(?i)(None|pointsup|pointsdown|underlyingpointsup|underlyingpointsdown|percentagedown|percentageup|underlyingpercentagedown|underlyingpercentageup)$"
                    },
                    "Value": {"type": "number"},
                },
                "required": ["Value", "Type"],
            },
            "ExpiryKind": {"pattern": "^(?i)(weekly|monthly)$"},
            "StrikeParameter": {"pattern": "^(?i)(atm|(OTM|ITM)([1-9]|(1[0-9])|20))$"},
            "Premium": {"type": "number"},
            "Lower": {"type": "number"},
            "Upper": {"type": "number"},
            "Adjustment": {"pattern": "^(?i)(plus|minus)$"},
            "Multiplier": {"type": "number"},
        },
        "required": [
            "PositionType",
            "Lots",
            "LegStopLoss",
            "LegTarget",
            "LegTrailSL",
            "LegMomentum",
            "ExpiryKind",
        ],
        "oneOf": [
            {
                "properties": {"EntryType": {"pattern": "^(?i)(entrybystriketype)$"}},
                "reqired": ["EntryType", "StrikeParameter"],
            },
            {
                "properties": {"EntryType": {"pattern": "^(?i)(entrybypremiumrange)$"}},
                "reqired": ["EntryType", "Upper", "Lower"],
            },
            {
                "properties": {"EntryType": {"pattern": "^(?i)(entrybypremium)$"}},
                "reqired": ["EntryType", "Premium"],
            },
            {
                "properties": {
                    "EntryType": {"pattern": "^(?i)(entrybystraddlewidth)$"}
                },
                "reqired": ["EntryType", "Adjustment", "Multiplier"],
            },
        ],
    },
}



def expects_json(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            data = request.form.get("data")
            if not data:
                return ResponseModel(message="Invalid Data!",code=400),400
            if type(data) is str:
                data = json.loads(data)
            result = validate(instance=data, schema=SCHEMA)
            
        except Exception as e:
            print("Error",e,flush=True)
            return ResponseModel(message="Invalid Data2!",code=400),400
        return f(data=data,*args, **kwargs)
    return decorator
