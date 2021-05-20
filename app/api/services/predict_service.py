import os

import gdown
import joblib
import numpy as np
import pandas as pd

from app.logger.logger import configure_logging

logger = configure_logging(__name__)



class Predict:
    def __init__(self) -> None:
        pass