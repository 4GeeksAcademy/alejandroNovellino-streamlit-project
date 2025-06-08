class OnePredictionInputDto:
    """
    Input DTO features to make a prediction.
    """

    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

    def __init__(self, n: float, p: float, k: float, temperature: float, humidity: float, ph: float, rainfall: float):
        # call pydantic basemodel constructor
        self.N=n
        self.P=p
        self.K=k
        self.temperature=temperature
        self.humidity=humidity
        self.ph=ph
        self.rainfall=rainfall


class OnePredictionOutputDto:
    """
    Output DTO for one prediction.
    """

    prediction: str

    def __init__(self, prediction: str):
        # call pydantic basemodel constructor
        self.prediction=prediction
