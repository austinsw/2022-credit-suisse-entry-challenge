def test_to_cumulative_with_multiple_ticks_for_different_tickers(self):
  self.assertEqual([
      '00:00,A,5,27.5,B,4,17.6',
  ], to_cumulative([
      '00:00,B,4,4.4',
      '00:00,A,5,5.5',
  ]))
  