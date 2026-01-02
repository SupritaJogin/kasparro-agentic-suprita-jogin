from logic_blocks.output_writer import write_output
from agents.product_parser_agent import ProductParserAgent
from agents.content_generation_agent import ContentGenerationAgent

class Orchestrator:
    def __init__(self):
        self.agents = [
            ProductParserAgent(name="product_parser"),
            ContentGenerationAgent(name="content_generator")
        ]

    def dispatch(self, task: dict):
        """
        Send a task to all agents.
        The first agent that can handle it returns a response.
        """
        for agent in self.agents:
            response = agent.handle(task)
            if response is not None:
                return response

        raise ValueError(f"No agent could handle task: {task['type']}")
if __name__ == "__main__":
    orchestrator = Orchestrator()

    task = {
        "type": "PARSE_PRODUCT",
        "payload": {
            "name": "Wireless Mouse",
            "price": "999",
            "category": "Electronics"
        }
    }

    # Agent chain
    task = orchestrator.dispatch(task)
    task = orchestrator.dispatch(task)

    # Structured output
    output_path = write_output("product_page.json", task["payload"])
    print(f"Output written to {output_path}")
