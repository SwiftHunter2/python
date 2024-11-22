class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the television with default values."""
        self._status = False  # TV is off
        self._muted = False  # Not muted
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        """Toggle the power status of the television."""
        self._status = not self._status

    def mute(self):
        """Toggle the mute status of the television."""
        if self._status:  # Only toggle if the TV is on
            self._muted = not self._muted

    def channel_up(self):
        """Increase the channel value, cycling back to the minimum if at the maximum."""
        if self._status:
            self._channel = (
                Television.MIN_CHANNEL
                if self._channel == Television.MAX_CHANNEL
                else self._channel + 1
            )

    def channel_down(self):
        """Decrease the channel value, cycling back to the maximum if at the minimum."""
        if self._status:
            self._channel = (
                Television.MAX_CHANNEL
                if self._channel == Television.MIN_CHANNEL
                else self._channel - 1
            )

    def volume_up(self):
        """Increase the volume, but remain at maximum if already at maximum."""
        if self._status:
            if self._muted:
                self._muted = False  # Unmute when volume is adjusted
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the volume, but remain at minimum if already at minimum."""
        if self._status:
            if self._muted:
                self._muted = False  # Unmute when volume is adjusted
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        """Return the string representation of the television's state."""
        status = "True" if self._status else "False"
        volume = self._volume if not self._muted else "0"
        return f"Power = {status}, Channel = {self._channel}, Volume = {volume}"