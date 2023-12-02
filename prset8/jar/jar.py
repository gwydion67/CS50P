

class Jar:
    def __init__(self,capacity = 12):
        self.capacity = capacity
        self.size = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError('Invalid Capacity')
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        self._size = size

    def deposit(self,n):
        if self.size + n > self.capacity:
            raise ValueError('jar overflow')
        self.size = self.size + n

    def withdraw(self,n):
        if self.size - n < 0:
            raise ValueError('Not enough size')
        self.size = self.size - n

    def __str__(self):
        s = ''
        for _ in range(self._size):
            s = s + '🍪'
        return(s)

def main():
    myJar = Jar(30)
    myJar.deposit(10)
    print(myJar)
    myJar.withdraw(3)
    print(myJar)


if __name__ == "__main__":
    main()
