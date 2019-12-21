from abc import abstractmethod, ABC


class Card(ABC):

    @property
    @abstractmethod
    def type(self):
        pass

    # @property
    # @abstractmethod
    # def cost(self):
    #     pass


class AttackUnit(Card):
    type = 'attacker'

    @property
    @abstractmethod
    def atk(self):
        pass

    @property
    @abstractmethod
    def hp(self):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass


class DefendUnit(Card):
    type = 'defender'

    @property
    @abstractmethod
    def atk(self):
        pass

    @property
    @abstractmethod
    def hp(self):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass


class BuffUnit(Card):
    type = 'buff'

    @property
    @abstractmethod
    def atkChange(self):
        pass

    @property
    @abstractmethod
    def hpChange(self):
        pass

    @property
    @abstractmethod
    def costChange(self):
        pass


class Pawn(AttackUnit):
    hp = 5
    atk = 1
    cost = 1


class Impulsion(BuffUnit):
    hpChange = -1
    atkChange = 1
    costChange = 0


class WoodWall(DefendUnit):
    hp = 10
    atk = 0
    cost = 1
