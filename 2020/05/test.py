#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest
import code

class TestDay05(unittest.TestCase):
    # Part 01
    def test_example01(self):
        bp = ["FBFBBFFRLR",
              "BFFFBBFRRR",
              "FFFBBBFRRR",
              "BBFFBBFRLL"]
        cr = [(44, 5),
              (70, 7),
              (14, 7),
              (102, 4)]
        seat_id =  [357, 567, 119, 820]

        for i in range(len(bp)):
            with self.subTest(bp[i]):
                r = code.get_seat(bp[i])
                s = code.get_seat_id(r)

                self.assertEqual(r, cr[i])
                self.assertEqual(s, seat_id[i])

        result = code.part01(bp)
        self.assertEqual(result, max(seat_id))

    # Part 02
    pass

if __name__ == '__main__':
    unittest.main()
