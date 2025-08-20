# test_emotion_app.py
import unittest
from emotion_app.emotion_detector import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_emotion_predictor(self):
        result = emotion_predictor('I am so happy today!')
        self.assertIn('emotion', result)
        self.assertIn('score', result)
        self.assertIsInstance(result['emotion'], str)
        self.assertIsInstance(result['score'], float)

if __name__ == '__main__':
    unittest.main()
