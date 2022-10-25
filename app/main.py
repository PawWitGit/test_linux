class CreateJob:
    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    def get_summary(self) -> int:

        a = self.var_1
        b = self.var_2

        return a + b


obj_1 = CreateJob(1, 2)
print(obj_1.get_summary())
