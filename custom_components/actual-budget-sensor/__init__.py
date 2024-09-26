"""Actual Budget Sensor integration."""
import logging
from homeassistant.helpers.discovery import async_load_platform

_LOGGER = logging.getLogger(__name__)

DOMAIN = "actual_budget_sensor"

async def async_setup(hass, config):
    """Set up the Actual Budget Sensor component."""
    # Perform any initial setup tasks
    _LOGGER.info("Setting up Actual Budget Sensor")
    
    # Load the sensor platform
    hass.async_create_task(
        async_load_platform(hass, "sensor", DOMAIN, {}, config)
    )

    return True
