class BaseAgent:
    """
    Base class for all agents in the system.
    Every agent must implement the handle() method.
    """

    def __init__(self, name):
        self.name = name

    def handle(self, task: dict):
        """
        Process a task message.
        Return a response dict if the agent can handle the task,
        otherwise return None.
        """
        raise NotImplementedError("Agents must implement handle()")
