from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @staticmethod
    @abstractmethod
    def get_all_instances():
        pass

    @staticmethod
    @abstractmethod
    def create_instance(**validated_data):
        pass

    @staticmethod
    @abstractmethod
    def get_instance_by_id(instance_id):
        pass

    @staticmethod
    @abstractmethod
    def update_instance(instance_id, **validated_data):
        pass

    @staticmethod
    @abstractmethod
    def delete_instance(instance_id):
        pass
