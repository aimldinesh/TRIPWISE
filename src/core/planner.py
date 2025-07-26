from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

# Initialize logger
logger = get_logger(__name__)


class TravelPlanner:
    """
    TravelPlanner manages user inputs (city and interests),
    tracks message history, and generates a day itinerary using an LLM.
    """

    def __init__(self):
        # Message history for potential future context use
        self.messages = []

        # User input fields
        self.city = ""
        self.interests = []

        # LLM-generated itinerary
        self.itinerary = ""

        logger.info("Initialized TravelPlanner instance.")

    def set_city(self, city: str):
        """
        Sets the city for the itinerary and logs the input.

        Args:
            city (str): Name of the destination city.
        """
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set successfully.")
        except Exception as e:
            logger.error(f"Error while setting city: {e}")
            raise CustomException("Failed to set city", e)

    def set_interests(self, interests_str: str):
        """
        Parses and sets user interests from a comma-separated string.

        Args:
            interests_str (str): Comma-separated string of interests (e.g., "museums, parks").
        """
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]

            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interests set successfully.")
        except Exception as e:
            logger.error(f"Error while setting interests: {e}")
            raise CustomException("Failed to set interests", e)

    def create_itinerary(self) -> str:
        """
        Generates a day itinerary using city and interests via the LLM.

        Returns:
            str: The generated itinerary.
        """
        try:
            logger.info(
                f"Generating itinerary for city: {self.city} with interests: {self.interests}"
            )
            itinerary = generate_itinerary(self.city, self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("Itinerary generated successfully.")
            return itinerary
        except Exception as e:
            logger.error(f"Error while creating itinerary: {e}")
            raise CustomException("Failed to create itinerary", e)
