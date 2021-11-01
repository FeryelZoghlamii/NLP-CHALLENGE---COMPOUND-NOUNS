import  unittest
from    predict_icd    import predict_icd 


class TestCalc(unittest.TestCase):

    def test_predict_icd(self):
        self.assertEqual(predict_icd('Infektion der Harnblase'), 'N30.9')
        self.assertEqual(predict_icd('Harnblaseninfektion'), 'N30.9')
        self.assertEqual(predict_icd('Schenkelhalsfraktur'), 'S72.00')
        self.assertEqual(predict_icd('Fraktur des Schenkelhalses'), 'S72.00')



if __name__ == "__main__":
    unittest.main()