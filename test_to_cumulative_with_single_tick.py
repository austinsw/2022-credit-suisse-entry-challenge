def test_to_cumulative_with_single_tick(self):
  self.assertEqual([
      '00:00,A,5,27.5',
  ], to_cumulative([
      '00:00,A,5,5.5',
  ]))
