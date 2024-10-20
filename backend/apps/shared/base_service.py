from abc import ABC, abstractmethod


class BaseService(ABC):

    @staticmethod
    @abstractmethod
    def list_all_instances():
        pass

    @staticmethod
    @abstractmethod
    def create_instance(**validated_data):
        pass

    @staticmethod
    @abstractmethod
    def retrieve_instance(instance_id):
        pass

    @staticmethod
    @abstractmethod
    def update_instance_and_partial_update(instance_id, **validated_data):
        pass

    @staticmethod
    @abstractmethod
    def destroy_instance(instance_id):
        pass
