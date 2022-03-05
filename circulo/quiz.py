class Sample:
    # Encapsulación
    __attr = "Random String"  # Atributo privado

    def get_attr(self):
        return self.__attr


sample = Sample()
print(sample.get_attr())
