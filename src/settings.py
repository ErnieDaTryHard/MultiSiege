import json
from constants import *
from models import *
import os
from typing import Any, Optional
import logger
from abc import ABC, abstractmethod


#test change
class Settings(ABC):
    """
    Abstract class defining what methods a settings object needs to have.
    """
    @abstractmethod
    def __init__(self, settings_path: str) -> None:
        pass

    @abstractmethod
    def create_settings(self) -> None:
        pass

    @abstractmethod
    def load_from_file(self) -> None:
        pass

    @abstractmethod
    def get_setting(self, field_name: str) -> Any:
        pass

    @abstractmethod
    def set_setting(self, field_name: str, value: Any) -> None:
        pass

    @abstractmethod
    def dump_settings(self) -> None:
        pass

class GlobalSettings(Settings):
    def __init__(self, settings_path: str = GLOBAL_SETTINGS):
        self.SETTINGS_PATH = settings_path

        if not os.path.isfile(self.SETTINGS_PATH): self.create_settings()
        else: self.load_from_file()
    
    def create_settings(self) -> None:
        """
        Creates default settings.
        """
        self.settings = GlobalSettingsModel()
        self.dump_settings()

    def load_from_file(self) -> None:
        """
        Attempts to load global settings from the settings path provided.
        """
        with open(self.SETTINGS_PATH, "r+") as f:
            try:
                data = json.load(f)
                self.settings = GlobalSettingsModel(**data)
            except:
                logger.log("Could not load settings (corrupt file)", LogLevel.WARNING)

                self.settings = GlobalSettingsModel()
                self.dump_settings()

                logger.log("Replaced corrupt global settings file.", LogLevel.INFO)

    def get_setting(self, field_name: str) -> Any:
        """
        Attempts to get a global setting from the pydantic model.
        """
        try:
            return self.settings.__getattribute__(field_name)
        except:
            logger.log("Could not get global setting (incorrect field name)", LogLevel.ERROR)
            
    def set_setting(self, field_name: str, value: Any) -> None:
        """
        Attempts to set a setting in the pydantic model and JSON file.
        """
        try:
            self.settings.__setattr__(name=field_name, value=value)
            self.settings = GlobalSettingsModel(**self.settings.model_dump_json()) #needs to remake the model to go through the field validators
            self.dump_settings()
        except:
            logger.log("Could not update setting (invalid field)", LogLevel.ERROR)

    def dump_settings(self) -> None:
        """
        Dumps the settings into the global settings JSON file.
        """
        with open(self.SETTINGS_PATH, "w") as f:
            try:   
                f.write(self.settings.model_dump_json())
            except:
                logger.log("Unable to write to global settings file.", LogLevel.ERROR)

class InstanceSettings(Settings):
    def __init__(self, settings_path: str, *, name: Optional[str] = None, username: Optional[str] = None, version: Optional[SiegeVersions] = None, instance_directory: Optional[str] = None, siege_directory: Optional[str] = None):
        self.SETTINGS_PATH = settings_path

        if not os.path.isfile(self.SETTINGS_PATH): #if the file doesn't exist, it should mean that we have a new instance that we want to initialise with settings.
            self.create_settings(
                name=name,
                username=username,
                version=version,
                instance_directory=instance_directory,
                siege_directory=siege_directory
            )
        else:#the file exists, so we should load data from the file
            self.load_from_file()

    def create_settings(self, *, name: str, username: str, version: str , instance_directory: str, siege_directory: str) -> None:
        try:
            self.settings = InstanceSettingsModel(
                name=name,
                username=username,
                version=version,
                instance_directory=instance_directory,
                siege_directory=siege_directory
            )
        except:
            logger.log("Invalid instance settings data.", LogLevel.ERROR)
            raise ValueError('Could not parse instance settings data into pydantic object.') # if any of the data is corrupt, we want to start the recovery process and if that doesn't work delete the instance altogether

        self.dump_settings()

    def load_from_file(self) -> None:
        """
        Attempts to load the instance settings from the file.

        If it is corrupt or does not exist, raise an error and try to recover settings.
        """
        with open(self.SETTINGS_PATH, "r+") as f:
            try:
                data = json.load(f)
                self.settings = InstanceSettingsModel(**data)
            except:
                logger.log("Could not load instance settings (corrupt file)", LogLevel.WARNING)
                raise ValueError('Could not load instance settings (corrupt file)') # in case the file is tampered with we want to raise an error so we know to handle getting all of the data we need.

    def get_setting(self, field_name: str) -> Any:
        """
        Attempts to get a setting from the field name provided.
        """
        try:
            return self.settings.__getattribute__(field_name)
        except:
            logger.log("Could not get instance setting (incorrect field name)", LogLevel.ERROR)
            
    def set_setting(self, field_name: str, value: Any) -> None:
        """
        Attempts to set a setting in the pydantic model and JSON file.
        """
        try:
            self.settings.__setattr__(name=field_name, value=value)
            self.settings = InstanceSettingsModel(**self.settings.model_dump_json()) #need to remake the model to go through the field validators 
            self.dump_settings()
        except:
            logger.log("Could not update setting (invalid field)", LogLevel.ERROR)

    def dump_settings(self) -> None:
        """
        Dumps the settings into the instance settings file.
        """
        with open(self.SETTINGS_PATH, "w") as f:
            try:   
                f.write(self.settings.model_dump_json())
            except:
                logger.log(f"Unable to write to instance {self.settings.name} settings file.", LogLevel.ERROR)