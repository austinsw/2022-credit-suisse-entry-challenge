def test_to_cumulative_delayed(self):
  self.assertEqual([
      '00:05,A,5,28.0',
  ], to_cumulative_delayed([
      '00:05,A,1,5.6',
      '00:00,A,1,5.6',
      '00:02,A,1,5.6',
      '00:03,A,1,5.6',
      '00:04,A,1,5.6',
  ], 5))
