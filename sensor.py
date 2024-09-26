import logging
import actual
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Actual Budget sensor."""
    sensors = [ActualBudgetSensor("Budget Balance")]
    async_add_entities(sensors, True)

class ActualBudgetSensor(Entity):
    """Representation of an Actual Budget Sensor."""

    def __init__(self, name):
        """Initialize the sensor."""
        self._name = name
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            self._state = await self.get_budget_balance()
        except Exception as e:
            _LOGGER.error(f"Error fetching data: {e}")

    async def get_budget_balance(self):
        """Fetch budget balance from Actual Budget API."""
        try:
            # Connect to your Actual server
            client = actual.connect("http://localhost:5006", password="your-password")

            # Fetch budget data
            budget_data = await client.budget.budget()
            balance = budget_data["balance"]  # Adjust based on the API structure

            return balance
        except Exception as e:
            _LOGGER.error(f"Failed to fetch Actual Budget data: {e}")
            return None
