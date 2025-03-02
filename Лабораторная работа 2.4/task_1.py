if __name__ == "__main__":
    class VrHeadseth:
        """
        Базовый класс вр гарнитур

        fov : float
        color : str
        strap_type : str
        price : float
        headset_type : str
        """

        def __init__(self, fov: float, color: str, strap_type: str, price: float, headset_type: str):
            """
            Конструктор класса WristWatch
            """
            if not isinstance(fov, (int, float)) or fov <= 0:
                raise TypeError('FOV (угол обзора) должен быть положительным числом')
            if not isinstance(color, str):
                raise TypeError('Цвет корпуса должен быть строкой')
            if not isinstance(strap_type, str):
                raise TypeError('Тип крепления должен быть строкой')
            if not isinstance(price, (int, float)) or price <= 0:
                raise TypeError('Цена должна быть положительным числом')
            if not isinstance(headset_type, str) or headset_type not in ['проводной', 'беспроводной']:
                raise TypeError('Тип гарнитуры должен быть строкой: "проводная" или "непроводная"')

            self.fov = fov
            self.color = color
            self.strap_type = strap_type
            self.price = price
            self.headset_type = headset_type

        def __str__(self) -> str:
            return (f"VR гарнитура: тип={self.headset_type}, угол обзора VOF={self.fov} мм, "
                    f"цвет корпуса={self.color}, тип крепления к голове={self.strap_type}, цена={self.price} руб.")

        def __repr__(self) -> str:
            return (f"VrHeadseth(FOV={self.fov}, color='{self.color}', "
                    f"strap_type='{self.strap_type}', price={self.price}, headset_type='{self.headset_type}')")

        def get_description(self) -> str:
            return self.__str__()


    class MetaQuest(VrHeadseth):
        """
        Дочерний класс для VR гарнитуры MetaQuest

        face_tracking : bool
        hand_tracking : bool
        """

        def __init__(self, fov: float, color: str, strap_type: str, price: float, headset_type: str,
                     face_tracking: bool, hand_tracking: bool):
            """
            Конструктор класса MetaQuest
            """
            super().__init__(fov, color, strap_type, price, headset_type)

            if not isinstance(face_tracking, bool):
                raise TypeError('Отслеживание лица должно быть значением True или False')
            if not isinstance(hand_tracking, bool):
                raise TypeError('Отслеживание рук должно быть значением True или False')

            self.face_tracking = face_tracking
            self.hand_tracking = hand_tracking

        def __str__(self) -> str:
            return (f"MetaQuest: тип={self.headset_type}, угол обзора VOF={self.fov} мм, "
                    f"цвет корпуса={self.color}, тип крепления к голове={self.strap_type}, цена={self.price} руб."
                    f"Отслеживание лица={self.face_tracking}, Отслеживание рук={self.hand_tracking}")

        def __repr__(self) -> str:
            return (f"MetaQuest(FOV={self.fov}, color='{self.color}', "
                    f"strap_type='{self.strap_type}', price={self.price}, headset_type='{self.headset_type}')"
                    f"face_tracking={self.face_tracking}, hand_tracking={self.hand_tracking})")

        def is_affordable(self, budget: float) -> bool:
            """
            Проверяет, доступна ли гарнитура для заданного бюджета
            """
            return self.price <= budget

    class Pico(VrHeadseth):
        """
        Дочерний класс для гарнитуры Pico

        maintainability : bool
        convenience_sleep : bool
        """

        def __init__(self, fov: float, color: str, strap_type: str, price: float, headset_type: str,
                     maintainability: bool, convenience_sleep: bool):
            """
            Конструктор класса Aviator
            """
            super().__init__(fov, color, strap_type, price, headset_type)

            if not isinstance(maintainability, bool):
                raise TypeError('Наличие хорошей ремонтопригодности должно быть True или False')
            if not isinstance(convenience_sleep, bool):
                raise TypeError('Наличие удобства пользования для сна должно быть True или False')

            self.maintainability = maintainability
            self.convenience_sleep = convenience_sleep

        def __str__(self) -> str:
            return (f"Pico: тип={self.headset_type}, угол обзора VOF={self.fov} мм, "
                    f"цвет корпуса={self.color}, тип крепления к голове={self.strap_type}, цена={self.price} руб."
                    f"ремонтопригодность={self.maintainability}, удобный сон={self.convenience_sleep}")

        def __repr__(self) -> str:
            return (f"Pico(FOV={self.fov}, color='{self.color}', "
                    f"strap_type='{self.strap_type}', price={self.price}, headset_type='{self.headset_type}')"
                    f"maintainability={self.maintainability}, convenience_sleep={self.convenience_sleep})")


        def is_luxury(self) -> bool:
            """
            Проверяет, стоит ли гарнитура больше 35 000 руб.
            """
            return self.price > 35000