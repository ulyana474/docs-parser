from abc import abstractmethod


class BaseRepository:
    @abstractmethod
    async def get(self):
        raise NotImplemented("not implemented")

    @abstractmethod
    async def create(self):
        raise NotImplemented("not implemented")

    @abstractmethod
    async def update(self):
        raise NotImplemented("not implemented")

    @abstractmethod
    async def delete(self):
        raise NotImplemented("not implemented")
