import pytest
from television import Television

def test_init():
    """Test the initialization of the Television class."""
    tv = Television()
    assert not tv._status  # TV should be off
    assert not tv._muted  # TV should not be muted
    assert tv._volume == Television.MIN_VOLUME  # Volume should be at minimum
    assert tv._channel == Television.MIN_CHANNEL  # Channel should be at minimum

def test_power():
    """Test toggling the power status."""
    tv = Television()
    tv.power()
    assert tv._status  # TV should be on
    tv.power()
    assert not tv._status  # TV should be off

def test_mute():
    """Test toggling the mute status."""
    tv = Television()
    tv.power()  # Turn on the TV to test mute
    tv.mute()
    assert tv._muted  # TV should be muted
    tv.mute()
    assert not tv._muted  # TV should be unmuted

def test_channel_up():
    """Test increasing the channel value."""
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL + 1
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should cycle back to MIN_CHANNEL
    assert tv._channel == Television.MIN_CHANNEL

def test_channel_down():
    """Test decreasing the channel value."""
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL  # Should cycle to MAX_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL - 1

def test_volume_up():
    """Test increasing the volume."""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._volume == Television.MIN_VOLUME + 1
    tv.volume_up()
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME  # Should remain at MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME  # No change beyond max

def test_volume_down():
    """Test decreasing the volume."""
    tv = Television()
    tv.power()
    tv.volume_down()  # Should remain at MIN_VOLUME
    assert tv._volume == Television.MIN_VOLUME
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME + 1

def test_mute_volume_interaction():
    """Test that volume adjustments unmute the TV."""
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert not tv._muted  # Adjusting volume unmutes
    assert tv._volume == Television.MIN_VOLUME + 1
    tv.mute()
    tv.volume_down()
    assert not tv._muted  # Adjusting volume unmutes
    assert tv._volume == Television.MIN_VOLUME
