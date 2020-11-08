from typing import List


class Solution:
    def maxArea(self, height: List[int])-> int:
        # f(x) = min(ai, aj) * |i - j|
        # To maximize this function, we check from two farthest points
        # And shift the x-axis accordingly.
        # If we shift the x-axis, the deciding factor becomes an
        start = 0
        end = len(height) - 1
        max_area = None
        while start < end:
            area = min(height[start], height[end]) * abs(end - start)
            if max_area is None or area > max_area:
                max_area = area

            # shift the lower guy towards the inner side of the axis
            # In case of equals, shift start/end, doesnt matter. But choose only 1 pointer to shift
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1

        return max_area

