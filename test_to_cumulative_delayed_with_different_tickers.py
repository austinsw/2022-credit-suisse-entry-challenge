def test_to_cumulative_delayed_with_different_tickers(self):
  self.assertEqual([
      '00:00,B,5,27.5',
      '00:01,A,5,27.9',
  ], to_cumulative_delayed([
      '00:01,A,5,5.5',
      '00:00,A,4,5.6',
      '00:00,B,5,5.5',
      '00:02,B,4,5.6',
  ], 5))
