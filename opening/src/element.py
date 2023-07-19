import numpy as np


class StructuringElement:
    def __init__(self, length, alpha, d_type=np.double):
        self.length = length
        self.alpha = alpha
        self.d_type = d_type
        self.__element = None

    @property
    def element(self):
        return self.__element

    @element.getter
    def element(self):
        if self.__element is not None:
            return self.__element

        element = np.zeros((self.length, self.length), dtype=self.d_type)
        center = (self.length - 1) / 2
        radians = np.radians(self.alpha)

        for i in range(self.length):
            x = i - center
            y = round(x * np.tan(radians))
            y_idx = int(center - y)
            if 0 <= y_idx < self.length:
                if self.d_type == bool:
                    element[y_idx, i] = True
                else:
                    element[y_idx, i] = 1.0

        self.__element = element

        return self.__element
