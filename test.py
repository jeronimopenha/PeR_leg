from src.util.util import Util


annotation={'a b':[['c',0],],
            'b c': [['a',1],],
            'c d ': [['a',2],['b',1],['e',2]]
            }
print(Util.clear_invalid_annotations(annotation))