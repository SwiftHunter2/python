class Television:
    """A class representing a Television with volume, channel, and power functionalities."""

    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize the Television with default values.
        The TV starts off, unmuted, with the minimum volume and channel.
        """
        self.__status: bool = False  # TV is off
        self.__muted: bool = False  # Not muted
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status of the television if it is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel value, cycling back to the minimum if at the maximum.
        """
        if self.__status:
            self.__channel = (
                Television.MIN_CHANNEL
                if self.__channel == Television.MAX_CHANNEL
                else self.__channel + 1
            )

    def channel_down(self) -> None:
        """
        Decrease the channel value, cycling back to the maximum if at the minimum.
        """
        if self.__status:
            self.__channel = (
                Television.MAX_CHANNEL
                if self.__channel == Television.MIN_CHANNEL
                else self.__channel - 1
            )

    def volume_up(self) -> None:
        """
        Increase the volume, but remain at maximum if already at maximum.
        If the TV is muted, unmute it first.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume, but remain at minimum if already at minimum.
        If the TV is muted, unmute it first.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return the string representation of the television's state.
        :return: A string in the format "Power = [status], Channel = [channel], Volume = [volume]"
        """
        status = "True" if self.__status else "False"
        volume = self.__volume if not self.__muted else "0"
        return f"Power = {status}, Channel = {self.__channel}, Volume = {volume}"