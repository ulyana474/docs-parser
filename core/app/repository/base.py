from abc import abstractmethod

class BaseRepository:
    @abstractmethod
    async def get(self):
        raise NotImplemented

    @abstractmethod
    async def create(self):
        raise NotImplemented

    @abstractmethod
    async def update(self):
        raise NotImplemented

    @abstractmethod
    async def delete(self):
        raise NotImplemented