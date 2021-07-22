import enum


class ProductStatusEnum(enum.Enum):
    OUT_OF_STOCK = 0
    AVAILABLE = 1

    def status_name(self):
        return self.name.title().replace("_", " ")
