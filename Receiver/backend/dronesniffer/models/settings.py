from typing import Optional

from pydantic import BaseModel, validator


class Settings(BaseModel):
    """
    Represents the settings to be stored in a file and/or transmitted via HTTP.

    Attributes:
        google_maps_api_key (str, optional): Google Maps API key.
        activity_offset_in_m (int): Number of minutes after last received package a drone is considered active.
        drone_size_in_rem (int): Drone size in UI in rem.
        interfaces (list[str]): Name of all interfaces that are sniffed.
        performance_mode (bool): Repress animations and simplify UI when performance mode is on.
    """
    google_maps_api_key: Optional[str]
    activity_offset_in_m: int = 10
    drone_size_in_rem: int = 5
    interfaces: list[str] = []
    performance_mode: bool = False

    @validator("google_maps_api_key")
    def gmaps_api_key_must_not_be_blank(cls, value: Optional[str]) -> None:
        if value is not None and not value.strip():
            raise ValueError("must not be blank")
        return value

    @validator("activity_offset_in_m")
    def activity_offset_must_be_in_range(cls, value: int) -> None:
        if not 1 <= value <= 60:
            raise ValueError("must be between 1 and 60")
        return value

    @validator("drone_size_in_rem")
    def drone_size_must_be_in_range(cls, value: int) -> None:
        if not 1 <= value <= 10:
            raise ValueError("must be between 1 and 10")
        return value
